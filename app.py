from flask import Flask, render_template, request
from search import search_director, search_title, search_actor

app = Flask(__name__)


@app.route("/")
@app.route("/home/")
def home():
    return render_template("index.html")


@app.route("/director/", methods=["GET", "POST"])
def director():
    if request.method == "POST":
        director = request.form.get("name")
        result = search_director(director)
        return render_template("director.html", result=result, director=director)
    else:
        return render_template("director.html", result="")


@app.route("/title/", methods=["GET", "POST"])
def title():
    if request.method == "POST":
        title = request.form.get("name")
        result = search_title(title)
        return render_template("title.html", result=result, title=title)
    else:
        return render_template("title.html", result="")


@app.route("/actor/", methods=["GET", "POST"])
def actor():
    if request.method == "POST":
        actor = request.form.get("name")
        result = search_actor(actor)
        return render_template("actor.html", result=result, actor=actor)
    else:
        return render_template("actor.html", result="")


if __name__ == "__main__":
    app.run(debug=True, port=8050, host="0.0.0.0")
