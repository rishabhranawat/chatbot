from app import db

class Greeting(db.Model):
    __tablename__ = 'greeting'
    id = db.Column(db.Integer, primary_key=True)
    greeting = db.Column(db.String)

    def __init__(self, greeting):
        self.greeting = greeting

    def __str__(self):
        return repr(self.greeting)

class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    log = db.Column(db.String)

    def __init__(self, log):
        self.log = log

    def __str__(self):
        return repr(self.log)

    
