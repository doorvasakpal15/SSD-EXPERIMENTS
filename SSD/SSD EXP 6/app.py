from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# -----------------------------
# CREATE DATABASE
# -----------------------------

def init_db():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    """)

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        ("admin",)
    )

    if cursor.fetchone() is None:

        cursor.execute(
            "INSERT INTO users VALUES (?, ?)",
            ("admin", "admin123")
        )

    conn.commit()
    conn.close()


# -----------------------------
# LOGIN PAGE
# -----------------------------

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""
    alert = ""

    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # -----------------------------
        # SQL INJECTION DETECTION
        # -----------------------------

        suspicious_patterns = [
            "' or ",
            "'or'",
            " or ",
            "1=1",
            "'='",
            "--",
            "/*",
            "*/"
        ]

        test_input = (username + " " + password).lower()

        if any(pattern in test_input for pattern in suspicious_patterns):

            alert = "SQL INJECTION ATTEMPT DETECTED!"
            message = "Malicious input detected and blocked."

        else:

            # -----------------------------
            # SECURE PARAMETERIZED QUERY
            # -----------------------------

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM users
                WHERE username = ? AND password = ?
                """,
                (username, password)
            )

            user = cursor.fetchone()

            conn.close()

            if user:
                message = "Login successful."

            else:
                message = "Invalid username or password."

    return render_template(
        "login.html",
        message=message,
        alert=alert
    )


# -----------------------------
# START APPLICATION
# -----------------------------

if __name__ == "__main__":

    init_db()

    print("Starting Secure Coding Application...")

    app.run(
        debug=True,
        port=5003
    )