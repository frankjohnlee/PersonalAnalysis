from Website import db


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


class SleepMeasurement(db.Model):
    __tablename__ = 'Sleep'
    __database__ = 'Health_Information'
    Date = db.Column(db.Date, primary_key=True)
    Sleep = db.Column(db.Float)

    def __init__(self, Date, Sleep):
        self.Date = Date
        self.Sleep = Sleep

    def __repr__(self):
        return "<User(date=%s, weight=%s)>" % (self.Date, self.Sleep)
