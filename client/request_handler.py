from client.db import DB
from client.helper import validate_time,get_key
from client.encryption import encrypt_text,decrypt_text
from datetime import datetime

def _start(username):
    greenings = f"Hi {username}😎, welcome"
    prefix = "I will remind you to mark the attendance‼️"
    subscribe = "Please select /subscribe to subscribe yourself"
    _help = "Please select /help to get help"
    return f"{greenings}\n{prefix}\n{subscribe}\n{_help}"

def _subscribed(id):
    db = DB()
    IN_t = "8:30AM"
    OUT_t = "5:00PM"
    validate = db.check_id(id)
    note = "<i>default time is set as,</i>\n<code>IN : 8:30PM\nOUT : 5:00PM\nUTC+05:30 Colombo, Sri Lanka</code>"
    if not validate:
        data = {"id":id,"in_t":IN_t,"out_t":OUT_t,"url":""}
        res = db.insert_data(data)
        if res:
            return f"Successfully subscribed!\m\n{note}"
    return "Already subscribed!"
    

def _help():
    start = f"/start <i>to start conversation</i>\n"
    subscribe = "/subscribe <i>to subscribe yourself</i>\n"
    in_time = "/in <i>to set `IN` time</i>\n"
    out_time = "/out <i>to set `OUT` time</i>\n"
    url = "/url <i>to set url</i>\n"
    # remaning_time = "/r <i>to get remaining time</i>\n\n"
    # return f"{start}{subscribe}{in_time}{out_time}{remaning_time}"
    note = "<i>\nDefault time is set as,</i>\n<code>IN : 8:30PM\nOUT : 5:00PM\nUTC+05:30 Colombo, Sri Lanka</code>"
    return f"{start}{subscribe}{in_time}{out_time}{url}{note}"

def _changein(id):
    msg = "Please enter time as 12-hour AM/PM format\n<code>Eg: 8:30AM</code>"
    # note = "<i>Default time is set as,</i>\n<code>IN : 8:30PM\nOUT : 5:00PM\nUTC+05:30 Colombo, Sri Lanka</code>"
    db = DB()
    id_validate = db.check_id(id)
    if id_validate:
        data = db.get_detialsById(id)
        in_t = data['in_time'].strip()
        if in_t != '':
            msg += f"\n\nYour previous IN time: {in_t}"
    return f"{msg}"

def _setin(id,time):
    db = DB()
    id_validate = db.check_id(id)
    t_validate = validate_time(time)
    if id_validate and t_validate:
        res = db.update_intime(id, time)
        if res:
           return  "Sucessfully `IN` time updated",True
    return "Coudn't update the time",False

def _changeout(id):
    msg = "Please enter time as 12-hour AM/PM format\n<code>Eg: 5:00PM</code>"
    # note = "<i>Default time is set as,</i>\n<code>IN : 8:30PM\nOUT : 5:00PM\nUTC+05:30 Colombo, Sri Lanka</code>"
    db = DB()
    id_validate = db.check_id(id)
    if id_validate:
        data = db.get_detialsById(id)
        out_t = data['out_time'].strip()
        if out_t != '':
            msg += f"\n\nYour previous `OUT` time: {out_t}"
    return f"{msg}"

def _setout(id,time):
    db = DB()
    id_validate = db.check_id(id)
    t_validate = validate_time(time)
    if id_validate and t_validate:
        res = db.update_outtime(id, time)
        if res:
           return  "Sucessfully `OUT` time updated",True
    return "Coudn't update the time",False

def _addurl(id):
    msg = "Your data is encrypted\nPlease enter the url:"
    db = DB()
    id_validate = db.check_id(id)
    if id_validate:
        data = db.get_detialsById(id)
        url = data['url'].strip()
        if url != '':
            try:
                key = get_key()
                durl = decrypt_text(url, key)
            except:
                return "Error Occurs"
            msg += f"\n\nYour previous url: {durl}"
    
    return msg+'\n\n*<code>Privacy at your own risk</code>*'

def _seturl(id,url):
    db = DB()
    id_validate = db.check_id(id)
    if id_validate:
        try:
            key = get_key()
            encypted = encrypt_text(url, key)
        except:
            return "Coudn't add the url"
        
        res = db.update_url(id,encypted)
        if res:
           return  "Url is sucessfully added!"
    return "Coudn't add the url"

def _getr(id):
    msg = "## time remaining"
    return msg