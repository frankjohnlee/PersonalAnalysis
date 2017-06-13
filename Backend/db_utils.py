from models import SleepMeasurement
from Website import db
import datetime as dt

def upload_fitbit_to_df(sleep_info):

    for rec in sleep_info:
        print(rec['dateTime'] + " " + rec['value'])

    '''
    try:
        new_entry = SleepMeasurement(dt.date(2014, 9, 16), 140)
        db.session.add(new_entry)
        print("Connected!\n")

        # Make the changes to the database persistent
        db.session.commit()

        # Close communication with the database
        db.session.close()
        print("Disconnected!\n")

    except Exception:
        print("error")
    '''