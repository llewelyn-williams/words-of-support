"""
Words of Support App
"""

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/topics")
def topics():
    """
    Display home page.
    """

    my_topics = mongo.db.topics.find()
    return render_template("topics.html", topics=my_topics)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the supplied username or email is already in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("The supplied username is already in use. Please try another.")
            return redirect(url_for("register"))

        if existing_email:
            flash("The supplied email is already in use. Please try another.")
            return redirect(url_for("register"))

        # entry for use in the database
        register = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        #TO-DO password confirmation field.

        mongo.db.users.insert_one(register)

        # put the new user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have been Signed Up Successfully.")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
