from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os


app = Flask(__name__)

# ==========================================================
# FLASK SETTINGS
# ==========================================================

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "vinayaka-stone-crusher-2026"
)


# ==========================================================
# GMAIL SETTINGS
# ==========================================================

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

# Gmail address
app.config["MAIL_USERNAME"] = os.environ.get(
    "MAIL_USERNAME",
    "preethigowda507@gmail.com"
)

# IMPORTANT:
# Never put your Gmail password/app-password directly in this file.
app.config["MAIL_PASSWORD"] = os.environ.get(
    "MAIL_PASSWORD",
    "uqmh ucop rhhr edik"
)

app.config["MAIL_DEFAULT_SENDER"] = (
    app.config["MAIL_USERNAME"]
)

mail = Mail(app)


# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================================
# ABOUT
# ==========================================================

@app.route("/about")
def about():
    return render_template("about.html")


# ==========================================================
# MATERIALS
# ==========================================================

@app.route("/materials")
def materials():

    materials_list = [

        {
            "name": "M-Sand",
            "image": "msand.jpg",
            "description":
                "Manufactured sand suitable for construction."
        },

        {
            "name": "Stone Dust",
            "image": "dust.jpg",
            "description":
                "Fine stone material suitable for filling and levelling."
        },

        {
            "name": "C-Sand",
            "image": "csand.jpg",
            "description":
                "Quality sand for suitable construction requirements."
        },

        {
            "name": "P-Sand",
            "image": "psand.jpg",
            "description":
                "Sand suitable for plastering and finishing."
        },

        {
            "name": "6mm Aggregate",
            "image": "6mm.jpg",
            "description":
                "6mm aggregate for selected construction applications."
        },

        {
            "name": "12mm Aggregate",
            "image": "12mm.jpg",
            "description":
                "12mm aggregate for concrete and construction."
        },

        {
            "name": "20mm Aggregate",
            "image": "20mm.jpg",
            "description":
                "20mm aggregate for concrete and structural work."
        },

        {
            "name": "40mm Aggregate",
            "image": "40mm.jpg",
            "description":
                "40mm aggregate for construction applications."
        },

        {
            "name": "GSB",
            "image": "GSB.jpg",
            "description":
                "Granular Sub-Base material for road and foundation work."
        }

    ]

    return render_template(
        "materials.html",
        materials=materials_list
    )


# ==========================================================
# TRUCKS
# ==========================================================

@app.route("/trucks")
def trucks():

    trucks_list = [

        {
            "name": "10 Wheel Lorry",
            "capacity": "28 Tons",
            "image": "10wheel.jpg",
            "description":
                "Heavy-duty transportation for construction materials."
        },

        {
            "name": "12 Wheel Lorry",
            "capacity": "Heavy Load",
            "image": "12wheel.jpg",
            "description":
                "Large-capacity transportation for bigger requirements."
        },

        {
            "name": "6 Wheel Lorry - LP",
            "capacity": "18 Tons",
            "image": "6wheel18.jpg",
            "description":
                "Reliable transportation for medium and large loads."
        },

        {
            "name": "709 Lorry",
            "capacity": "8 Tons",
            "image": "709.jpg",
            "description":
                "Compact transportation for smaller requirements."
        }

    ]

    return render_template(
        "trucks.html",
        trucks=trucks_list
    )


# ==========================================================
# CONTACT PAGE
# GET  = SHOW PAGE
# POST = ACCEPT FORM
# ==========================================================

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        return process_enquiry()

    selected_material = request.args.get(
        "material",
        ""
    )

    selected_truck = request.args.get(
        "truck",
        ""
    )

    return render_template(
        "contact.html",
        selected_material=selected_material,
        selected_truck=selected_truck
    )


# ==========================================================
# SEND MESSAGE
# ==========================================================

@app.route("/send-message", methods=["POST"])
def send_message():
    return process_enquiry()


# ==========================================================
# PROCESS CUSTOMER ENQUIRY
# ==========================================================

def process_enquiry():

    # ------------------------------------------------------
    # GET FORM DATA
    # ------------------------------------------------------

    name = request.form.get(
        "name",
        ""
    ).strip()

    phone = request.form.get(
        "phone",
        ""
    ).strip()

    location = request.form.get(
        "location",
        ""
    ).strip()

    material = request.form.get(
        "material",
        ""
    ).strip()

    truck = request.form.get(
        "truck",
        ""
    ).strip()

    quantity = request.form.get(
        "quantity",
        ""
    ).strip()

    message_text = request.form.get(
        "message",
        ""
    ).strip()


    # ------------------------------------------------------
    # VALIDATION
    # ------------------------------------------------------

    if not name:

        flash(
            "Please enter your name.",
            "error"
        )

        return redirect(
            url_for("contact")
        )


    if not phone:

        flash(
            "Please enter your phone number.",
            "error"
        )

        return redirect(
            url_for("contact")
        )


    if not phone.isdigit() or len(phone) != 10:

        flash(
            "Please enter a valid 10-digit phone number.",
            "error"
        )

        return redirect(
            url_for("contact")
        )


    if not location:

        flash(
            "Please enter the delivery address.",
            "error"
        )

        return redirect(
            url_for("contact")
        )


    # ------------------------------------------------------
    # CHECK GMAIL CONFIGURATION
    # ------------------------------------------------------

    mail_password = app.config.get(
        "MAIL_PASSWORD",
        ""
    )

    if not mail_password:

        print()
        print("=" * 70)
        print("GMAIL PASSWORD IS NOT CONFIGURED")
        print("=" * 70)
        print(
            "Set the MAIL_PASSWORD environment variable."
        )
        print("=" * 70)
        print()

        flash(
            "The enquiry form is available, but email service is not configured yet.",
            "error"
        )

        return redirect(
            url_for("contact")
        )


    # ------------------------------------------------------
    # CREATE EMAIL BODY
    # ------------------------------------------------------

    email_body = f"""
VINAYAKA STONE CRUSHER

NEW CUSTOMER ENQUIRY
========================================

Customer Name:
{name}

Phone Number:
{phone}

Delivery Address:
{location}

Material Required:
{material if material else "Not specified"}

Truck Required:
{truck if truck else "Not specified"}

Quantity:
{quantity if quantity else "Not specified"}

Additional Message:
{message_text if message_text else "No additional message"}

========================================
Submitted from Vinayaka Stone Crusher website.
"""


    # ------------------------------------------------------
    # SEND EMAIL
    # ------------------------------------------------------

    try:

        msg = Message(

            subject=f"New Enquiry - {name}",

            sender=app.config["MAIL_USERNAME"],

            recipients=[
                app.config["MAIL_USERNAME"]
            ],

            body=email_body
        )

        mail.send(msg)

        print()
        print("=" * 70)
        print("EMAIL SENT SUCCESSFULLY")
        print("=" * 70)
        print("Name     :", name)
        print("Phone    :", phone)
        print("Location :", location)
        print("Material :", material)
        print("Truck    :", truck)
        print("Quantity :", quantity)
        print("=" * 70)
        print()

        flash(
            "Your enquiry has been sent successfully.",
            "success"
        )

    except Exception as error:

        print()
        print("=" * 70)
        print("EMAIL ERROR")
        print("=" * 70)
        print(error)
        print("=" * 70)
        print()

        flash(
            "The enquiry could not be sent. Please try again.",
            "error"
        )


    return redirect(
        url_for("contact")
    )


# ==========================================================
# 404 ERROR
# ==========================================================

@app.errorhandler(404)
def page_not_found(error):

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>404 - Page Not Found</title>

        <style>

            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 80px 20px;
                background: #111;
                color: white;
            }

            h1 {
                color: #ff8c00;
                font-size: 50px;
            }

            a {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 24px;
                background: #ff8c00;
                color: #111;
                text-decoration: none;
                border-radius: 25px;
                font-weight: bold;
            }

        </style>

    </head>

    <body>

        <h1>404</h1>

        <h2>Page Not Found</h2>

        <p>
            The requested page could not be found.
        </p>

        <a href="/">
            Return Home
        </a>

    </body>

    </html>
    """, 404


# ==========================================================
# SERVER
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("          VINAYAKA STONE CRUSHER")
    print("=" * 60)
    print("Website   : http://127.0.0.1:5000/")
    print("About     : http://127.0.0.1:5000/about")
    print("Materials : http://127.0.0.1:5000/materials")
    print("Trucks    : http://127.0.0.1:5000/trucks")
    print("Contact   : http://127.0.0.1:5000/contact")
    print("Mail User :", app.config["MAIL_USERNAME"])
    print("=" * 60)
    print()

    # Local development only.
    # Production hosting should use Gunicorn:
    # gunicorn app:app

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )