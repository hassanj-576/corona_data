from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Country_data(db.Model):
    def __init__(self, country, time, total_cases, total_deaths, total_recovered, active_cases, hourly_new_cases,
                 hourly_new_deaths, hourly_new_recovered, daily_new_cases, daily_new_deaths):
        self.country = country
        self.time = time
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.total_recovered = total_recovered
        self.active_cases = active_cases
        self.hourly_new_cases = hourly_new_cases
        self.hourly_new_deaths = hourly_new_deaths
        self.hourly_new_recovered = hourly_new_recovered
        self.daily_new_cases = daily_new_cases
        self.daily_new_deaths = daily_new_deaths
        pass

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    country = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    total_cases = db.Column(db.Integer, nullable=False)
    total_deaths = db.Column(db.Integer, nullable=False)
    total_recovered = db.Column(db.Integer, nullable=False)
    active_cases = db.Column(db.Integer, nullable=False)
    hourly_new_cases = db.Column(db.Integer, nullable=False)
    hourly_new_deaths = db.Column(db.Integer, nullable=False)
    hourly_new_recovered = db.Column(db.Integer, nullable=False)
    daily_new_cases = db.Column(db.Integer, nullable=False)
    daily_new_deaths = db.Column(db.Integer, nullable=False)


class Country_json_data(db.Model):
    def __init__(self, country, time, json_data):
        self.country = country
        self.time = time
        self.json_data = json_data

    country = db.Column(db.String, primary_key=True, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    json_data = db.Column(db.JSON, nullable=False)
