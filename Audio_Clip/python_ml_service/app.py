from flask import Flask, request, jsonify
import io
import soundfile as sf

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    audio_bytes = request.data
    # Read WAV bytes
    try:
        audio, sr = sf.read(io.BytesIO(audio_bytes))
        # Here you would run your ML model
        # For demo, always return 'cry'
        result = "cry"  # or "noise"
        return jsonify({"label": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
