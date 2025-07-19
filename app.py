from flask import Flask, render_template, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '')
        source_lang = data.get('source_lang', 'en')
        target_lang = data.get('target_lang', 'sw')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Create translation prompt
        if source_lang == 'en' and target_lang == 'sw':
            prompt = f"Translate the following English text to Swahili: {text}"
        elif source_lang == 'sw' and target_lang == 'en':
            prompt = f"Translate the following Swahili text to English: {text}"
        else:
            return jsonify({'error': 'Invalid language pair'}), 400
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional translator. Provide only the translation without any additional text or explanations."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.3
        )
        
        translation = response.choices[0].message.content.strip()
        
        return jsonify({
            'original': text,
            'translation': translation,
            'source_lang': source_lang,
            'target_lang': target_lang
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)