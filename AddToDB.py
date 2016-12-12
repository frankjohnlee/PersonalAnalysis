import sys
from flask import Flask, ext
from flask_sqlalchemy import SQLAlchemy
import datetime as dt

CONNECTION_STRING = 'postgresql://postgres:postgres@localhost:5432/Health_Information'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
db = SQLAlchemy(app)

class WeightMeasurement(db.Model):
    __tablename__ = 'Weight'
    __database__ = 'Health_Information'
    Date = db.Column(db.DateTime, primary_key=True)
    Weight = db.Column(db.Float)

    def __init__(self, Date, Weight):
        self.Date = Date
        self.Weight = Weight

    def __repr__(self):
        return "<User(date=%s, weight=%s)>" % (self.Date, self.Weight)


def main():

    try:
        new_entry = WeightMeasurement(dt.datetime(2014, 9, 16, 0, 0), 140)
        db.session.add(new_entry)
        print("Connected!\n")

        # Make the changes to the database persistent
        db.session.commit()

        # Close communication with the database
        db.session.close()
        print("Disconnected!\n")

    except Exception:
        print("error")


if __name__ == "__main__":
    main()
