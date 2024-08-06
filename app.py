from flask import Flask, request, jsonify, render_template
from TextSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
pipeline = PredictionPipeline()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'Text is required'}), 400
    summary = pipeline.predict(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True,port=8080)