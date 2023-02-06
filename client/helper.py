from os import getenv
from dotenv import load_dotenv

def validate_time(time):
    AM_PM = ['AM',"PM"]
    try:
        h,r = time.split(':')
        mins = r[:2] 
        am_pm = r[2:] 
        if int(h) < 13 and int(mins) < 60:
            if am_pm.upper() in AM_PM:
                return True
        return False
    except:
        return False


def get_token():
    load_dotenv()
    API_TOKEN = getenv("TOKEN")
    return API_TOKEN

def get_key():
    load_dotenv()
    KEY = getenv("KEY")
    return bytes(KEY,"UTF-8")