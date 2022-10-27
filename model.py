"""Model for for Melon Tasting Reservation Scheduler."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), nullable=False, unique=True)

    appointments = db.relationship('Appointment', back_populates='user')

    def __repr__(self):
        """Show info about a user."""

        return f'<User user_id={self.user_id} username={self.username}>'


class Appointment(db.Model):
    """An appointment."""

    __tablename__ = 'appointments'

    appt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appt_datetime = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship("User", back_populates="appointments")
    
    def __repr__(self):
        """Show info about an appointment."""

        return f'<Appointment appt_datetime={self.appt_datetime} user={self.user}>'


def connect_to_db(app, db_uri="postgresql:///melons"):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # db.app = app
    with app.app_context():
        db.init_app(app)
    

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to db.")