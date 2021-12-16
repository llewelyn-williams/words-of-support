"""
Words of Support App
"""

import os
import datetime
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
@app.route("/home.html")
def home():
    """
    Display home page.
    """

    return render_template("home.html")


@app.route("/read")
def read():
    """
    Display read page.
    """

    return render_template("read.html")


@app.route("/search-results", methods=["GET", "POST"])
def search():
    """
    Display search results from read or write page.
    """

    if request.method == "POST":
        search_term = request.form.get("topic")
        topics_found = list(
            mongo.db.topics.find({"$text": {"$search": search_term}}))

        if request.form.get("page_source") == "read":

            return render_template(
                "read-search-results.html",
                topics=topics_found,
                search_term=search_term)

        else:

            return render_template(
                "write-search-results.html",
                topics=topics_found,
                search_term=search_term)


@app.route("/all-topics", methods=["GET", "POST"])
def search_all():
    """
    Display all results from read page.
    """

    if request.method == "POST":
        topics_found = list(mongo.db.topics.find())

    if request.form.get("page_source") == "read":
        return render_template(
            "read-search-results.html",
            topics=topics_found)
    else:
        return render_template(
            "write-search-results.html",
            topics=topics_found)


@app.route("/write")
def write():
    """
    Display write page.
    """

    # if check that there is a session user
    try:
        if session["user"]:
            return render_template("write.html")
    # if there is a KeyError because there is no session user
    except KeyError:
        flash("Please sign in to be able to submit content.")
        return redirect(url_for("login"))


@app.route("/add-words/<topic>", methods=["GET", "POST"])
def add_words(topic):
    """
    Display add words page.
    Handle submission to the supportive_words collection
    """

    if request.method == "POST":
        kind_words = {
            "words": request.form.get("words"),
            "words_creator": session["user"],
            "words_creation_date": datetime.datetime.utcnow(),
            "words_rating": 2.5,
            "topic_id": ObjectId(request.form.get("topic_id"))
        }
        mongo.db.supportive_words.insert_one(kind_words)
        flash("Thank you for your kind words.")

    topic_id = mongo.db.topics.find_one({"topic": topic})["_id"]

    return render_template("add-words.html", topic=topic, topic_id=topic_id)


@app.route("/add-topic", methods=["GET", "POST"])
def add_topic():
    """
    Display add topic page.
    Handle submission to the topics collection
    """

    if request.method == "POST":
        try:
            topic = {
                "topic": request.form.get("topic").lower(),
                "topic_creator": mongo.db.users.find_one(
                    {"email": session["user_email"]})["_id"],
                "topic_creation_date": datetime.datetime.utcnow(),
            }
            mongo.db.topics.insert_one(topic)
            flash("Thank you for your addition.")
        except KeyError:
            topic = {
                "topic": request.form.get("topic").lower(),
                "topic_creator": "anonymous",
                "topic_creation_date": datetime.datetime.utcnow(),
            }
            mongo.db.topics.insert_one(topic)
            flash("Thank you for your addition.")

    return render_template("add-topic.html", topic=topic)


@app.route("/struggling-with", methods=["GET", "POST"])
def struggling_with():
    """
    Display add topic page.
    Handle submission to the topics collection
    """

    if request.method == "POST":
        # check if it's already there and flash if so and reload page
        if mongo.db.topics.find_one(
                {"topic": request.form.get("topic").lower()}):
            flash(f"{request.form.get('topic')} has already been submitted.")
        else:
            # add it to the datbase if it's not there and flash that it's added
            try:
                topic = {
                    "topic": request.form.get("topic").lower(),
                    "topic_creator": mongo.db.users.find_one(
                        {"email": session["user_email"]})["_id"],
                    "topic_creation_date": datetime.datetime.utcnow(),
                }
                mongo.db.topics.insert_one(topic)
                flash("Thank you for your addition.")
            except KeyError:
                topic = {
                    "topic": request.form.get("topic").lower(),
                    "topic_creator": "anonymous",
                    "topic_creation_date": datetime.datetime.utcnow(),
                }
                mongo.db.topics.insert_one(topic)
                flash("Thank you for your addition.")

    return render_template("struggling-with.html")


@app.route("/words/<topic>", methods=["GET", "POST"])
def words(topic):
    """
    Display supportive words associated to a given topic
    """
    topic_id = mongo.db.topics.find_one({"topic": topic})["_id"]
    supportive_words = list(
        mongo.db.supportive_words.find({"topic_id": topic_id}))

    return render_template("words.html", supportive_words=supportive_words)


@app.route("/topics")
def topics():
    """
    Display topics page.
    """

    my_topics = list(mongo.db.topics.find())
    return render_template("topics.html", topics=my_topics)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handle Sign Up Page and Functionality.
    """

    if request.method == "POST":
        # check if the supplied username or email is already in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash(
                "The supplied username is already in use. Please try another.")
            return redirect(url_for("register"))

        if existing_email:
            flash("The supplied email is already in use. Please try another.")
            return redirect(url_for("register"))

        # entry for use in the database
        register_user = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        # TO-DO password confirmation field.

        mongo.db.users.insert_one(register_user)

        # put the new user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have been Signed Up Successfully.")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handle Sign In Page and Functionality.
    """

    if request.method == "POST":
        # check if email is in the database
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            # make sure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user_email"] = request.form.get("email").lower()
                session["user"] = existing_user["username"]
                flash("Signed in with the email: {}".format(
                    request.form.get("email")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # password doesn't match
                flash("Email and/or password incorrect.")
                return redirect(url_for("login"))

        else:
            # username not found
            flash("Email and/or password incorrect.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Handle Profile Page and Functionality.
    """

    # get the session user's usename fom the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # only go to the profile page if there is a session user
    if session["user"]:
        return render_template("profile.html", username=username)

    # otherwise redirect users to the login page
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Handle Logout Functionality.
    """

    # remove user and email from session cookies
    flash("You have been logged out.")
    session.pop("user_email")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
