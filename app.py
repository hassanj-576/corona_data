import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify

from models import db
from utils.hourly_task import hourly_task
from utils.parse_requests import get_latest_data_for_count, get_country_data_for_time

app = Flask(__name__)
app.config.from_object('config.config')

db.init_app(app)
db.app = app


def job_function():
    hourly_task()


scheduler = BackgroundScheduler()
scheduler.add_job(func=job_function, trigger="interval", hours=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route('/')
def hello_world():
    # hourly_task()
    return 'Hello World!'


@app.route('/country/<country_name>', methods=['GET'])
def get_country_data(country_name: str):
    return jsonify(get_latest_data_for_count(country_name))


@app.route('/country/<country_name>/<time>', methods=['GET'])
def get_country_for_time_frame(country_name: str, time: str):
    data = get_country_data_for_time(country_name, time)
    return jsonify(data)


if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=5000))
