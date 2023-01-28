import hashlib
from os import getenv
from dotenv import load_dotenv

load_dotenv()
secret_key = getenv("KEY")
 
from Crypto.Cipher import AES
import base64

msg_text = "ww.gogole.lk"

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = base64.b64encode(cipher.encrypt(msg_text))
# ...
decoded = cipher.decrypt(baes64.b64decode(msg_text))