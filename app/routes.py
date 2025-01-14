from flask import Blueprint, render_template, request
from app.models import Roll
from app import db
import random

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        dice_type = request.form.get("dice_type", "D6")
        dice_count = int(request.form.get("dice_count", 1))
        rolls = [random.randint(1, int(dice_type[1:])) for _ in range(dice_count)]
        total = sum(rolls)

        new_roll = Roll(dice_type=dice_type, rolls=",".join(map(str, rolls)), total=total)
        db.session.add(new_roll)
        db.session.commit()

        return render_template("result.html", rolls=rolls, total=total, dice_type=dice_type)

    return render_template("index.html")
