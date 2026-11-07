from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/health")
def health():
    return {"status": "ok", "channel": "SMPTV"}

@app.get("/video")
def video():
    return send_from_directory(os.path.join(app.static_folder), "smptv.mp4")

if __name__ == "__main__":
    # Local development only. For production use gunicorn (see Procfile).
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
