"""Server for for Melon Tasting Reservation Scheduler."""

from flask import Flask, render_template, flash, session, redirect, request
from model import connect_to_db, db
import crud

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/", methods=["GET"])
def display_login():
    """Simple login screen. No authentication needed."""
    return render_template("login.html")


@app.route("/", methods=["POST"])
def process_login():
    """Log user into site."""

    username = request.form.get("username")

    user = crud.get_user_by_username(username)

    if not user:
        flash("Username not found.")
        return redirect("/")
    
    else:
        user = session["username"]
        flash("Log in successful.")
        return redirect("/appointmentsearch")


@app.route("/appointmentsearch")
def appointment_search():
    """Page to search for appointments."""
    return render_template("search.html")


@app.route("/appointmentresults")
def appointment_results():
    """
    Page to view apointment search results. Allows user to book any of the 
    appointments and shows error if none are found.
    """
    pass


@app.route("/scheduledappointments")
def scheduled_appointments():
    """
    Page to view all the scheduled appointments for the current user. 
    Optionally add cancelling or editing of appointments.
    """
    pass


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")