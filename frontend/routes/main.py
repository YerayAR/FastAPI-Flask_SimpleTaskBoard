from flask import Blueprint, render_template
import os

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    """Render the main page with the base API URL."""
    api_url = os.environ.get('FASTAPI_URL', 'http://localhost:8000')
    return render_template('index.html', api_url=api_url)
