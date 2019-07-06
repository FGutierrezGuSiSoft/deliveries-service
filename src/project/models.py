from project import db
from sqlalchemy.sql import func


class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    creation = db.Column(db.DateTime, default=func.now(), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
