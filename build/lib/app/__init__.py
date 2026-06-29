from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )


    app.config["SECRET_KEY"] = "dev-key-12345"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cybershield.db"


    db.init_app(app)


    from app.routes import main
    app.register_blueprint(main)


    with app.app_context():
        db.create_all()


    return app