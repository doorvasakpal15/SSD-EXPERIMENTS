from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin123"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        with open("security.log", "a") as log:
            log.write(f"SUCCESSFUL LOGIN: {username}\n")

        return redirect(url_for("dashboard"))

    else:
        with open("security.log", "a") as log:
            log.write(f"FAILED LOGIN ATTEMPT: {username}\n")

        return render_template(
            "login.html",
            error="Invalid username or password"
        )


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    print("Starting Secure Web Application...")
    app.run(host="127.0.0.1", port=5001, debug=True)