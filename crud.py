"""CRUD operations for Melon Tasting Reservation Scheduler."""

import datetime
from model import User, Appointment, connect_to_db, db

def create_user(username):
    """Create and return a new user."""
   
    user = User(username=username)

    return user

def get_user_by_username(username):
    """Get a user by their username."""

    return User.query.filter(User.username == username).first()

def get_user_appointments(username):
    """Get all of a user's scheduled appointments."""

    user = get_user_by_username(username)

    return Appointment.query.filter(user.user_id == Appointment.user_id).all()

def create_appointment(appt_datetime, user_id):
    """Create an appointment."""
    
    appointment = Appointment(appt_datetime=appt_datetime, user_id=user_id)

    return appointment

def appt_date_check(username, appt_datetime):
    """Check to see if user already has an appointment on a given date."""

    appts = get_user_appointments(username)

    for appt in appts:
        if appt.appt_datetime.date() == appt_datetime:
            return True


def create_time_slots(cal_date, start_time, end_time):
    """Given a time range, create available time slots."""

    datetime.datetime.strptime(start_time,"%H:%M").time()
    cal_date = datetime.datetime.strptime(cal_date,"%Y-%m-%d").date()

    appt = datetime.datetime.combine(cal_date, datetime.datetime.strptime(start_time,"%H:%M").time())
    slots = [appt]

    while appt.time() < datetime.datetime.strptime(end_time,"%H:%M").time():
        appt = appt + datetime.timedelta(minutes=30)
        if not Appointment.query.filter(Appointment.appt_datetime == appt).first():
            slots.append(appt)
    return slots

def format_date():
    """Take in a datetime.now and format it into YYYY-DD-MM to use in HTML."""

    return datetime.datetime.now().strftime("%Y-%m-%d")
    

if __name__ == "__main__":
    from server import app
    connect_to_db(app)