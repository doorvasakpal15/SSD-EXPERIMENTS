from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""
    encoded_message = ""

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        address = request.form.get("address", "").strip()

        # -------------------------
        # INPUT VALIDATION
        # -------------------------

        # Name validation
        if not name:
            message = "❌ Invalid Name: Name cannot be empty."

        elif not name.replace(" ", "").isalpha():
            message = "❌ Invalid Name: Name should contain only letters."

        # Email validation
        elif "@" not in email or "." not in email:
            message = "❌ Invalid Email Address."

        # Address validation
        elif not address:
            message = "❌ Invalid Address: Address cannot be empty."

        elif len(address) < 5:
            message = "❌ Invalid Address: Address is too short."

        # -------------------------
        # VALID INPUT
        # -------------------------

        else:
            message = "✅ All inputs are valid."

            # Output encoding
            encoded_message = escape(
                f"Name: {name} | Address: {address}"
            )

    return render_template(
        "form.html",
        message=message,
        encoded_message=encoded_message
    )


if __name__ == "__main__":
    print("Starting Experiment 5...")
    app.run(debug=True, port=5002)