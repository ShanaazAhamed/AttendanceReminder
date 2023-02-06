from os import getenv
from dotenv import load_dotenv
from datetime import datetime


def validate_time(time):
    AM_PM = ['AM', "PM"]
    try:
        h, r = time.split(':')
        mins = r[:2]
        am_pm = r[2:]
        if int(h) < 13 and int(mins) < 60:
            if am_pm.upper() in AM_PM:
                return True
        return False
    except:
        return False


def convert24(time):
    t = datetime.strptime(time, '%I:%M%p')
    return t.strftime('%H:%M')


def convert12(time):
    d = datetime.strptime(time, "%H:%M")
    return d.strftime("%I:%M%p")


def get_token():
    load_dotenv()
    API_TOKEN = getenv("TOKEN")
    return API_TOKEN


def get_key():
    load_dotenv()
    KEY = getenv("KEY")
    return bytes(KEY, "UTF-8")
