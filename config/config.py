import os

UPLOAD_FOLDER = os.path.join("app", "static", "uploads")  # Speichert in app/static/uploads/
ALLOWED_EXTENSIONS = {"pdf", "docx", "png", "jpg"}

SECRET_KEY = os.urandom(24)  # Sicheren Key generieren


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Sicherstellen, dass das Upload-Verzeichnis existiert
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
