from flask import (request, Blueprint, render_template)
from app.helpers.extract import extract_page
bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("main/index.html", title="Website-Extractor")

@bp.route("/extract", methods=["POST", "OPTIONS"])
def start_extract():
    import json
    if requests.method == "POST":
        data = json.loads(req.data)
        result = extract_page(data['url'], data['root'], data['target'])
        try:
            return json.dumps(result)
        except Exception:
            return { "message": "Cannot return object data" }

    return "200"
