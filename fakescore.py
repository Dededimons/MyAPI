from main import db, Score

fake_scores = [
    {"player": "Dante", "score": 301},
    {"player": "Vergil", "score": 124},
    {"player": "Chala", "score": 200},
    {"player": "Goku", "score": 214},
    {"player": "Rob", "score": 220},
    {"player": "Rachet", "score": 91},
    {"player": "Clank", "score": 99},
    {"player": "Jak", "score": 175},
    {"player": "Dexter", "score": 95},
    {"player": "Vegeta", "score": 50},
    {"player": "John", "score": 28},
    {"player": "Jake", "score": 24},
]


with db.app.app_context():
    for score_data in fake_scores:
        score = Score(player=score_data["player"], score=score_data["score"])
        db.session.add(score)
    db.session.commit()
    print("Fake scores +")
