from flask import Flask, render_template, request, jsonify
from scheduler import BatchScheduler

app = Flask(__name__)

scheduler = BatchScheduler()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/schedule", methods=["POST"])
def schedule():

    data = request.json

    year = int(data["year"])
    month = int(data["month"])

    absent = data.get("absent", [])

    result = scheduler.generate_schedule(
        year,
        month,
        absent
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False)