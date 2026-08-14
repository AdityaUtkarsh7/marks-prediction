from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html", your_marks=None)


@app.route("/predict", methods=["POST"])
def predict():
    hours = float(request.form["hours"])

    prediction = model.predict([[hours]])
    marks = round(float(prediction[0]), 2)

    return render_template(
        "index.html",
        your_marks=marks
    )


if __name__ == "__main__":
    app.run(debug=True)