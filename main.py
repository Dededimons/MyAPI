from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///baza.db"
db = SQLAlchemy(app)

class Score(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    player=db.Column(db.String(60),nullable=False)
    score=db.Column(db.Integer,nullable=False)

    def to_dict(self):
        return{"player":self.player,"score":self.score}

with app.app_context():
    db.create_all()


@app.route("/savescore", methods=["POST"])
def save_score():
    data=request.json
    new_score = Score(player=data["player"], score=data["score"])
    db.session.add(new_score)
    db.session.commit()
    return jsonify({"message": "Score pohranjen."}), 201

@app.route("/top10", methods=["GET"])
def top10():
    scores=Score.query.order_by(Score.score.deck()).limit(10).all()
    return jsonify([score.to_dict() for score in scores])

if __name__ == "__main__":
    app.run(debug=True)