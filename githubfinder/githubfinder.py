from flask import Flask, request, render_template, redirect, url_for
import requests
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form.get("user")
        return redirect(url_for("search", user=user))
    return render_template("index.html")


@app.route("/user/<user>")
def search(user):
    resp = requests.get(f"https://api.github.com/users/{user}")
    data = resp.json()
    return render_template("index.html", data=data)


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("error"))


@app.route("/error")
def error():
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
