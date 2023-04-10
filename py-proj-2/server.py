from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, delete_cupcake_csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cupcakes")
def all_cupcakes():
    cupcakes = get_cupcakes("sample.csv")
    return render_template("cupcakes.html", cupcakes=cupcakes)


@app.route("/cupcake_individual/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("sample.csv", name)
    if cupcake:
        return render_template("individual-cupcake.html", cupcake=cupcake)
    else:
        return "Cupcake not found"


@app.route("/order")
def order():
    cupcakes = get_cupcakes("order.csv")
    return render_template("order.html", cupcakes=cupcakes)


@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("sample.csv", name)

    if cupcake:
        add_cupcake_dictionary("order.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Cupcake not found"


@app.route("/delete-order/<name>")
def delete_cupcake(name):
    delete_cupcake_csv("order.csv", name)
    return redirect(url_for("order"))


if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")
