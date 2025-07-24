from flask import Flask, request, jsonify
import io
import soundfile as sf

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    audio_bytes = request.data
    audio, sr = sf.read(io.BytesIO(audio_bytes))
    # result = your_ml_inference(audio, sr)
    # For demo, random result:
    result = "cry"  # or "noise"
    return jsonify({"label": result})

# def your_ml_inference(audio, sr):
#     # Preprocess, run model, return "cry" or "noise"
#     pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
