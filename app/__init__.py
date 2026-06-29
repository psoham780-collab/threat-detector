import os
import tempfile

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def _get_storage_dir():
    override = os.environ.get("CYBERSHIELD_STORAGE_DIR")
    if override:
        storage_dir = os.path.abspath(override)
    else:
        storage_dir = os.path.join(tempfile.gettempdir(), "cybershield-ai")

    os.makedirs(storage_dir, exist_ok=True)
    return storage_dir


def create_app():

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )


    app.config["SECRET_KEY"] = "dev-key-12345"

    storage_dir = _get_storage_dir()
    app.instance_path = storage_dir
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(storage_dir, 'cybershield.db')}"
    )


    db.init_app(app)


    from app.routes import main
    app.register_blueprint(main)


    with app.app_context():
        db.create_all()


    return app