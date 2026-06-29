from app import db
from datetime import datetime


class ScanHistory(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    url = db.Column(
        db.String(500)
    )

    risk = db.Column(
        db.String(50)
    )

    score = db.Column(
        db.Integer
    )

    date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )