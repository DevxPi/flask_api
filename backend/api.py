from flask import Blueprint, jsonify

# register api as blueprint
api_bp = Blueprint("api", __name__)


@api_bp.route("/")
def index():
    website_info = {
        'ip': 'localhost',
        'framework': 'flask'
    }

    return jsonify(website_info), 200