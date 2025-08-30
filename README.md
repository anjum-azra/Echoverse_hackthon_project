🎧 EchoVerse – AI Text-to-Speech Generator

Hackathon Project for CognitiveX Hackathon 2025, Teegala Krishna Reddy Engineering College

🏆 Inspiration

In today’s digital era, storytelling, accessibility, and immersive learning are vital.
We built EchoVerse to help people transform written stories into expressive audio, making technology more engaging, inclusive, and impactful.

🚀 Features

📝 Convert written text into clear, natural-sounding speech

🎭 Choose different tones – Neutral, Excited, Calm, Inspiring, Suspenseful

🎙️ Select simulated voices – Allison, Michael, Lisa

🎧 Instant audio playback & download

🎨 Beautiful, colorful UI built with Bootstrap

🌐 Powered by Flask + Hugging Face / gTTS

🏗️ Project Architecture

Frontend: HTML, CSS, Bootstrap (responsive design)

Backend: Flask (Python)

AI/ML Engine: Hugging Face models / gTTS

File Storage: Static folder for generated .wav audio

📂 Project Structure
EchoVerse/
│── app.py               # Flask backend
│── requirements.txt     # Python dependencies
│── .env                 # Environment variables (HF_TOKEN if using Hugging Face)
│── templates/
│    └── index.html      # Web UI
│── static/
│    ├── style.css       # Styling
│    └── output.wav      # Generated audio

⚙️ Setup & Installation

1️⃣ Clone the repo

git clone (https://github.com/anjum-azra/Echoverse_hackthon_project)
cd echoverse


2️⃣ Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt


3️⃣ Add environment variables
Create a .env file and add:

HF_TOKEN=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 


4️⃣ Run the app

python app.py


Visit: http://127.0.0.1:5000/



🔮 Future Scope

🌍 Multi-language support (Telugu, Hindi, Spanish, etc.)

🧠 Smarter emotional tones (AI-driven sentiment-based speech)

📱 Mobile app for real-time voice streaming

♿ Accessibility features for visually impaired users

👥 Team – Teegala Krishna Reddy Engineering College

AlgoAI – CognitiveX Hackathon 2025

Team Members: P.Anjum Azra (Team Lead)
T.Lakshmi
S.Supriya


✨ Built with passion during CognitiveX Hackathon 2025 @ TKR Engineering College
