from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            message = "Login successful!"
        else:
            message = "Invalid username or password."

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Burp Suite Demo</title>
    </head>

    <body>

        <h1>Burp Suite Dynamic Analysis</h1>

        <form method="POST">

            <label>Username:</label>
            <input type="text" name="username">

            <br><br>

            <label>Password:</label>
            <input type="password" name="password">

            <br><br>

            <button type="submit">Login</button>

        </form>

        <h3>{message}</h3>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(port=5004)