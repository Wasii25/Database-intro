from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
app = Flask(__name__)

all_books = []


@app.route('/')
def home(): 
    text = "Library is empty"
    n=0
    if len(all_books) == 0:
        n=1
        return render_template("index.html", paragraph=text, n=n)
    else:
        return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)

        # NOTE: You can use the redirect method from flask to redirect to another route
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))

    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
