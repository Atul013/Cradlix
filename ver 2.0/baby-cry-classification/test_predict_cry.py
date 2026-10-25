from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path
from unittest.mock import MagicMock, call

import pytest


@pytest.fixture
def predictor_module(monkeypatch):
    fake_joblib = types.ModuleType("joblib")
    fake_joblib.load = MagicMock()
    monkeypatch.setitem(sys.modules, "joblib", fake_joblib)
    monkeypatch.setitem(sys.modules, "librosa", types.ModuleType("librosa"))
    monkeypatch.setitem(sys.modules, "numpy", types.ModuleType("numpy"))

    module_path = Path(__file__).with_name("predict_cry.py")
    spec = importlib.util.spec_from_file_location("cradlix_predict_cry", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FakeFeatures:
    def reshape(self, *shape):
        assert shape == (1, -1)
        return self


class FakeModel:
    def predict(self, features):
        assert isinstance(features, FakeFeatures)
        return [2]


class FakeLabelEncoder:
    def inverse_transform(self, prediction):
        assert prediction == [2]
        return ["hunger"]


def configure_prediction(module):
    module.joblib.load.side_effect = [FakeModel(), FakeLabelEncoder()]
    module.extract_features = MagicMock(return_value=FakeFeatures())


def test_default_artifacts_resolve_beside_script(predictor_module, monkeypatch, tmp_path):
    module = predictor_module
    configure_prediction(module)
    monkeypatch.chdir(tmp_path)

    result = module.predict_cry("fixture.wav")

    expected_dir = Path(module.__file__).resolve().parent
    assert result == "hunger"
    assert module.joblib.load.call_args_list == [
        call(expected_dir / "model.joblib"),
        call(expected_dir / "label.joblib"),
    ]


def test_explicit_artifact_paths_override_defaults(predictor_module, tmp_path):
    module = predictor_module
    configure_prediction(module)
    model_path = tmp_path / "custom-model.joblib"
    label_path = tmp_path / "custom-label.joblib"

    result = module.predict_cry(
        "fixture.wav",
        model_path=str(model_path),
        label_path=str(label_path),
    )

    assert result == "hunger"
    assert module.joblib.load.call_args_list == [
        call(model_path),
        call(label_path),
    ]
