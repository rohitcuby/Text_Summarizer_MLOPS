from flask import Flask, request, jsonify, render_template
from TextSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
pipeline = PredictionPipeline()

@app.route('/')
async def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
async def predict():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'Text is required'}), 400
    summary = pipeline.predict(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)