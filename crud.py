"""CRUD operations for Melon Tasting Reservation Scheduler."""

from model import db, User, Appointment, connect_to_db

def create_user(username):
    """Create and return a new user."""

    user = User(username=username)

    return user


def get_user_by_username(username):
    """Get a user by their username."""

    return User.query.filter(User.username == username).first()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)