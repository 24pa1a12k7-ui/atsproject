from flask import Flask, request, jsonify, render_template
import PyPDF2
from google import genai  

app=Flask(__name__)

client = genai.Client(api_key="AIzaSyBi4c8_8yRrHlcwi-6TZiGfmIAdWMTru70")

def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text
    return extracted_text 

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["message"]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"reply": response.text})

app.run(port=8080)