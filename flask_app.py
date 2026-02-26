from flask import Flask, render_template, request
from gemini_connect import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        income = request.form.get("income")
        rent = request.form.get("rent")
        travel = request.form.get("travel")
        food = request.form.get("food")
        shopping = request.form.get("shopping")

        prompt = f"""
        Create a monthly savings & budgeting plan.

        Monthly Income: {income}
        Rent: {rent}
        Travel: {travel}
        Food: {food}
        Shopping: {shopping}

        Provide:
        1. Total expenses
        2. Remaining savings
        3. Where the user is overspending
        4. Suggestions to reduce costs
        5. Final savings advice
        """

        result = get_response(prompt)

        return render_template("prediction.html", result=result)

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)