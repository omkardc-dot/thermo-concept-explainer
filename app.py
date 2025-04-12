from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Hardcoded Gemini API Key
API_KEY = "AIzaSyDSvUs6NmXxJH3DGmH4R23mUvSCGq5n6kA"
genai.configure(api_key=API_KEY)

# Load Gemini 1.5 Flash model
model = genai.GenerativeModel("models/gemini-1.5-flash")

@app.route('/', methods=['GET', 'POST'])
def index():
    explanation = ""
    if request.method == 'POST':
        concept = request.form['concept']
        prompt = f"Explain the thermodynamics concept '{concept}' in simple terms suitable for a college student."
        try:
            response = model.generate_content(prompt)
            explanation = response.text
        except Exception as e:
            explanation = f"Error: {str(e)}"
    return render_template('index.html', explanation=explanation)

if __name__ == '__main__':
    app.run(debug=True)

