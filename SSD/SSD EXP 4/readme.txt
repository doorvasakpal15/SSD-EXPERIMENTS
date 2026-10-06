EXP 4 :

1. Create the project
In VS Code terminal:
--> mkdir secure_web_app
--> cd secure_web_app

Create a virtual environment:
--> python -m venv .venv

Activate it:
--> .venv\Scripts\Activate.ps1

Install Flask:
--> pip install flask

CODE:
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import logging

app = Flask(__name__)

# Secret key used to protect Flask sessions
app.secret_key = "change-this-secret-key"

# Logging configuration
logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Demo user
users = {
    "admin": generate_password_hash("Admin@123")
}


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Input validation
        if not username or not password:
            logging.warning("Login attempt with missing credentials")
            return render_template(
                "login.html",
                error="Username and password are required."
            )

        # Authentication
        if username in users and check_password_hash(
            users[username], password
        ):
            session["user"] = username

            logging.info(
                "Successful login for user: %s",
                username
            )

            return redirect(url_for("dashboard"))

        logging.warning(
            "Failed login attempt for username: %s",
            username
        )

        return render_template(
            "login.html",
            error="Invalid username or password."
        )

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    # Authorization check
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["user"]
    )


@app.route("/logout")
def logout():

    username = session.get("user")

    session.clear()

    logging.info(
        "User logged out: %s",
        username
    )

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=False)