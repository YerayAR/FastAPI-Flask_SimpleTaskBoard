"""Application factory for the Flask front-end."""

from flask import Flask


def create_app() -> Flask:
    """Create and configure the Flask application instance."""

    app = Flask(__name__)

    from .routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
