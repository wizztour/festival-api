
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

festivals = [
    {
        "title": "서울국제불꽃축제",
        "location": "여의도 한강공원",
        "date": "2025-10-05",
        "description": "화려한 불꽃으로 가을 밤하늘을 수놓는 대표 행사",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Seoul_Fireworks.jpg"
    },
    {
        "title": "한강몽땅 여름축제",
        "location": "한강 전역",
        "date": "2025-07-15 ~ 2025-08-20",
        "description": "물놀이·영화·음악이 어우러지는 여름 대표 축제",
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Hangang_Festival.jpg"
    },
    {
        "title": "서울장미축제",
        "location": "서울 중랑천",
        "date": "2025-05-17 ~ 2025-05-26",
        "description": "수천 송이 장미가 흐드러진 서울의 봄",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/93/Seoul_Rose.jpg"
    }
]

@app.route("/api/festival")
def get_festivals():
    month = request.args.get("month")
    if month:
        filtered = [f for f in festivals if f["date"].startswith(f"2025-{month.zfill(2)}")]
        return jsonify(filtered)
    return jsonify(festivals)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
