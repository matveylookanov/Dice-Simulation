from flask import Blueprint, jsonify, request
from app.models import Roll
from app import db
import random

api_bp = Blueprint("api", __name__)

@api_bp.route("/roll", methods=["POST"])
def roll_dice():
    data = request.json
    dice_type = data.get("dice_type", "D6")
    dice_count = int(data.get("dice_count", 1))

    rolls = [random.randint(1, int(dice_type[1:])) for _ in range(dice_count)]
    total = sum(rolls)

    new_roll = Roll(dice_type=dice_type, rolls=",".join(map(str, rolls)), total=total)
    db.session.add(new_roll)
    db.session.commit()

    return jsonify(new_roll.to_dict()), 201

@api_bp.route("/history", methods=["GET"])
def get_history():
    rolls = Roll.query.all()
    return jsonify([roll.to_dict() for roll in rolls])
