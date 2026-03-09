from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import random

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)

    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()

    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=["GET"])
def search_cafe():
    location = request.args.get("loc")
    stmt = db.select(Cafe).where(Cafe.location.ilike(f"%{location}%"))
    results = db.session.execute(stmt).scalars().all()

    return jsonify(cafe=[cafe.to_dict() for cafe in results])


@app.route("/add", methods=["POST"])
def add_cafe():
    try:

        data = request.form

        new_cafe = Cafe(
            name=data.get("name"),
            map_url=data.get("map_url"),
            img_url=data.get("img_url"),
            location=data.get("location"),
            seats=data.get("seats"),
            has_toilet=(data.get("has_toilet", "false").lower() == "true"),
            has_wifi=(data.get("has_wifi", "false").lower() == "true"),
            has_sockets=(data.get("has_sockets", "false").lower() == "true"),
            can_take_calls=(data.get("can_take_calls", "false").lower() == "true"),
            coffee_price=data.get("coffee_price"),
        )

        db.session.add(new_cafe)
        db.session.commit()

        return jsonify({"success": True, "cafe": new_cafe.to_dict()}), 201

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/delete/<int:id>", methods=["POST"])
def delete_cafe(id):
    api_key = request.args.get("API_KEY", None)
    if api_key == "TOPSECRETKEY":
        try:

            cafe = Cafe.query.get(id)
            if not cafe:
                return jsonify({"success": False, "error": "Cafe not found"}), 404

            db.session.delete(cafe)
            db.session.commit()

            return (
                jsonify(
                    {"success": True, "message": f"Cafe with id {id} has been deleted"}
                ),
                200,
            )

        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400
    else:
        return (
            jsonify(
                {
                    "success": False,
                    "error": {"Forbidden": "Sorry, Not allowed with proper api key."},
                }
            ),
            404,
        )


@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new_price")
    try:
        cafe = Cafe.query.get(id)
        if not cafe:
            return jsonify({"success": False, "error": "Cafe not found"}), 404
        else:
            cafe.coffee_price = new_price
        db.session.commit()

        return (
            jsonify(
                {
                    "success": True,
                    "message": f"Cafe with id {id} has updated coffee price.",
                }
            ),
            200,
        )

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
