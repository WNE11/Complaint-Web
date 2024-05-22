from web_config import db
from sqlalchemy.sql import func

class Complaintone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_phone = db.Column(db.String(15), nullable=False)
    user_selector = db.Column(db.String(100), nullable=False)
    user_mail_one = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f'<Complaintone {self.id}>'
