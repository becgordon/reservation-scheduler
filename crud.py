"""CRUD operations for Melon Tasting Reservation Scheduler."""

from model import db, User, Apointment, connect_to_db





if __name__ == "__main__":
    from server import app
    connect_to_db(app)