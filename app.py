from flask import Flask, render_template, request, redirect, url_for, flash
import os
import requests
from dotenv import load_dotenv
from gtts import gTTS

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    print("⚠️ Hugging Face token missing! Will use gTTS fallback.")
else:
    print("✅ Hugging Face token loaded successfully!")

# Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    rewritten_text = None
    original_text = ""
    voice = ""
    tone = ""

    if request.method == "POST":
        original_text = request.form.get("text")
        voice = request.form.get("voice")
        tone = request.form.get("tone")

        if not original_text:
            flash("Please enter some text.", "error")
            return redirect(url_for("index"))

        # Default output path
        output_path = "static/output.wav"

        # --- Try Hugging Face TTS ---
        if HF_TOKEN:
            model_id = "suno/bark"   # You can try other HF TTS models
            API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            payload = {"inputs": original_text}

            response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code == 200 and response.content:
                with open(output_path, "wb") as f:
                    f.write(response.content)
                audio_file = "output.wav"
                flash("✅ Audio generated with Hugging Face!", "success")
            else:
                flash("⚠️ Hugging Face TTS failed. Falling back to gTTS.", "warning")
                tts = gTTS(text=original_text, lang="en")
                tts.save(output_path)
                audio_file = "output.wav"
        else:
            # --- Always fallback to gTTS if no token ---
            tts = gTTS(text=original_text, lang="en")
            tts.save(output_path)
            audio_file = "output.wav"
            flash("✅ Audio generated with gTTS fallback!", "success")

        return render_template(
            "index.html",
            audio_file=audio_file,
            rewritten_text=original_text,  # Here you could later add tone-based rewriting
            original_text=original_text,
            voice=voice,
            tone=tone,
        )

    return render_template("index.html", audio_file=None)


if __name__ == "__main__":
    app.run(debug=True)
