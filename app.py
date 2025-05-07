
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

festivals = [
    {
        "title": "서울장미축제",
        "location": "서울 중랑천",
        "month": 5,
        "date": "2025-05-17 ~ 2025-05-26",
        "description": "수천 송이 장미가 흐드러진 서울의 봄",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/93/Seoul_Rose.jpg"
    },
    {
        "title": "전주한지문화축제",
        "location": "전주한옥마을",
        "month": 5,
        "date": "2025-05-03 ~ 2025-05-06",
        "description": "전통 한지의 멋을 체험할 수 있는 전주 대표 축제",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Jeonju_Hanji.jpg"
    },
    {
        "title": "진주남강유등축제",
        "location": "진주 남강",
        "month": 10,
        "date": "2025-10-01 ~ 2025-10-14",
        "description": "형형색색 유등이 수놓는 진주의 밤",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Jinju_Lantern.jpg"
    }
]

@app.route("/api/festival")
def get_festivals():
    month = request.args.get("month", type=int)
    if month:
        return jsonify([f for f in festivals if f["month"] == month])
    return jsonify(festivals)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
