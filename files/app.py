"""Serveur web de production pour le site vitrine AURUM."""
from pathlib import Path
import os

from flask import Flask, abort, send_from_directory

ROOT = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)

# Seuls les fichiers du site peuvent être servis, pas le code serveur ni les
# fichiers du dépôt. La démo reste entièrement exécutée dans le navigateur.
PUBLIC_FILES = {
    "index.html",
    "styles.css",
    "app.js",
    "config.js",
    "architecture.jpg",
    "assets/logo-simple.svg",
    "assets/capture-tableau.jpg",
}


@app.route("/")
def index():
    return send_from_directory(ROOT, "index.html", max_age=0)


@app.route("/<path:filename>")
def public_file(filename):
    if filename not in PUBLIC_FILES:
        abort(404)
    return send_from_directory(ROOT, filename, max_age=0)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")), debug=False)
