from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "vinayaka-stone-crusher-secret-key"


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# ABOUT
# =========================================================

@app.route("/about")
def about():
    return render_template("about.html")


# =========================================================
# MATERIALS
# =========================================================

@app.route("/materials")
def materials():
    return render_template("materials.html")


# =========================================================
# GALLERY
# =========================================================

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


# =========================================================
# CONTACT
# =========================================================

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        material = request.form.get("material", "").strip()
        quantity = request.form.get("quantity", "").strip()
        location = request.form.get("location", "").strip()
        message = request.form.get("message", "").strip()

        # -------------------------------
        # VALIDATION
        # -------------------------------

        if not name:
            flash("Please enter your name.", "error")
            return redirect(url_for("contact"))

        if not phone:
            flash("Please enter your phone number.", "error")
            return redirect(url_for("contact"))

        if not phone.isdigit() or len(phone) != 10:
            flash("Please enter a valid 10-digit phone number.", "error")
            return redirect(url_for("contact"))

        if not material:
            flash("Please select a material.", "error")
            return redirect(url_for("contact"))

        if not quantity:
            flash("Please enter the required quantity.", "error")
            return redirect(url_for("contact"))

        if not location:
            flash("Please enter the delivery location.", "error")
            return redirect(url_for("contact"))

        # -------------------------------
        # DISPLAY REQUEST IN TERMINAL
        # -------------------------------

        print()
        print("=" * 70)
        print("        NEW VINAYAKA STONE CRUSHER MATERIAL REQUEST")
        print("=" * 70)

        print(f"Name       : {name}")
        print(f"Phone      : {phone}")
        print(f"Material   : {material}")
        print(f"Quantity   : {quantity}")
        print(f"Location   : {location}")
        print(f"Message    : {message}")

        print("=" * 70)
        print()

        # -------------------------------
        # SUCCESS
        # -------------------------------

        flash(
            "Your material request has been submitted successfully. "
            "We will contact you soon.",
            "success"
        )

        return redirect(url_for("contact"))

    return render_template("contact.html")


# =========================================================
# MATERIAL REQUEST
# =========================================================

@app.route("/material-request", methods=["POST"])
def material_request():

    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    material = request.form.get("material", "").strip()
    quantity = request.form.get("quantity", "").strip()
    location = request.form.get("location", "").strip()
    message = request.form.get("message", "").strip()

    # -------------------------------
    # VALIDATION
    # -------------------------------

    if not name:
        flash("Please enter your name.", "error")
        return redirect(url_for("materials"))

    if not phone or not phone.isdigit() or len(phone) != 10:
        flash("Please enter a valid 10-digit phone number.", "error")
        return redirect(url_for("materials"))

    if not material:
        flash("Please select a material.", "error")
        return redirect(url_for("materials"))

    if not quantity:
        flash("Please enter the required quantity.", "error")
        return redirect(url_for("materials"))

    if not location:
        flash("Please enter the delivery location.", "error")
        return redirect(url_for("materials"))

    # -------------------------------
    # DISPLAY IN TERMINAL
    # -------------------------------

    print()
    print("=" * 70)
    print("             NEW MATERIAL REQUEST")
    print("=" * 70)

    print(f"Name       : {name}")
    print(f"Phone      : {phone}")
    print(f"Material   : {material}")
    print(f"Quantity   : {quantity}")
    print(f"Location   : {location}")
    print(f"Message    : {message}")

    print("=" * 70)
    print()

    flash(
        "Thank you! Your material request has been received.",
        "success"
    )

    return redirect(url_for("materials"))


# =========================================================
# 404 ERROR
# =========================================================

@app.errorhandler(404)
def page_not_found(error):

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>404 - Page Not Found</title>
    </head>

    <body style="
        font-family: Arial;
        text-align: center;
        padding: 80px;
    ">

        <h1>404 - Page Not Found</h1>

        <p>The requested page could not be found.</p>

        <a href="/">
            Return to Vinayaka Stone Crusher
        </a>

    </body>
    </html>
    """, 404


# =========================================================
# 500 ERROR
# =========================================================

@app.errorhandler(500)
def internal_server_error(error):

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>500 - Server Error</title>
    </head>

    <body style="
        font-family: Arial;
        text-align: center;
        padding: 80px;
    ">

        <h1>500 - Internal Server Error</h1>

        <p>Something went wrong.</p>

        <a href="/">
            Return to Vinayaka Stone Crusher
        </a>

    </body>
    </html>
    """, 500


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )