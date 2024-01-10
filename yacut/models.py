from datetime import datetime

from . import db
from settings import MAX_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(MAX_LENGTH), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Метод для сериализации данных."""
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp,
        )
