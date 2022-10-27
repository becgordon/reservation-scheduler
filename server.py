"""Server for for Melon Tasting Reservation Scheduler."""

from flask import Flask, render_template, flash, session, redirect, request
import datetime
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
        session["user"] = user.username
        flash("Log in successful.")
        return redirect("/appointmentsearch")


@app.route("/appointmentsearch")
def appointment_search():
    """Page to search for appointments."""

    current = crud.format_date()

    return render_template("search.html", current=current) 


@app.route("/appointmentresults")
def appointment_results():
    """
    Page to view apointment search results. Allows user to book any of the 
    appointments and shows error if none are found.
    """

    date = request.args.get("res-date")
    print('\n'*5)
    print(date)
    print('\n'*5)

    print(crud.appt_date_check(session["user"], date))
    print('\n'*5)

    if crud.appt_date_check(session["user"], date):
        error = True
    else:
        error = False

    start_time = request.args.get("start-time")
    end_time = request.args.get("end-time")

    slots = crud.create_time_slots(date, start_time, end_time)

    return render_template("results.html", slots=slots, error=error)


@app.route("/scheduledappointments")
def scheduled_appointments():
    """
    Page to view all the scheduled appointments for the current user. 
    Optionally add cancelling or editing of appointments.
    """
    user = crud.get_user_by_username(session["user"])
    appt_time = request.args.get("slot")
    appt = crud.create_appointment(appt_time,user.user_id)
    db.session.add(appt)
    db.session.commit()

    appointments = crud.get_user_appointments(session["user"])
    
    return render_template("scheduled.html", appointments=appointments)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")



# Things To Do
"""
If time:
-Edit appts to be more readable

"""