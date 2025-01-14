from app import db

class Roll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dice_type = db.Column(db.String(10), nullable=False)
    rolls = db.Column(db.String(255), nullable=False)  # Результаты бросков
    total = db.Column(db.Integer, nullable=False)  # Сумма бросков

    def to_dict(self):
        return {
            "id": self.id,
            "dice_type": self.dice_type,
            "rolls": self.rolls,
            "total": self.total
        }
