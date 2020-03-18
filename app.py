import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from utils.hourly_task import hourly_task

app = Flask(__name__)


def job_function():
    hourly_task()


scheduler = BackgroundScheduler()
scheduler.add_job(func=job_function, trigger="interval", hours=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route('/')
def hello_world():
    hourly_task()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
