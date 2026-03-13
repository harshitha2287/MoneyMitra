from flask import Flask, render_template, request
import sqlite3
from loan_model import calculate_emi, evaluate_loan

app = Flask(__name__)


def save_history(name, amount, status):

    conn = sqlite3.connect("loan_history.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        amount INTEGER,
        status TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO history(name, amount, status) VALUES(?,?,?)",
        (name, amount, status)
    )

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    reasons = []

    if request.method == "POST":

        name = request.form["name"]
        age = int(request.form["age"])
        employment = request.form["employment"]
        income = int(request.form["income"])

        existing_emi = request.form.get("existing_emi", 0)
        existing_emi = int(existing_emi) if existing_emi else 0

        credit = request.form.get("credit", 700)
        credit = int(credit)

        amount = int(request.form["amount"])
        term = int(request.form["term"])

        emi = calculate_emi(amount, 10, term)

        status, reasons = evaluate_loan(
            age,
            income,
            credit,
            existing_emi,
            emi,
            employment
        )

        save_history(name, amount, status)

        result = status

    return render_template("index.html", result=result, reasons=reasons)


@app.route("/history")
def history():

    conn = sqlite3.connect("loan_history.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, amount, status FROM history")
    data = cursor.fetchall()

    conn.close()

    return render_template("history.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)