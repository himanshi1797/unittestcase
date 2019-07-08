import uuid,base64
from datetime import datetime

def isBase64(s):
 """This module use to encode and decode """
 try:
  return base64.b64encode(base64.b64decode(s)).decode() == s
 except Exception:
  return False


def decode_records(data):
 """This module use to decode the data"""
 import base64

 for i in data.keys():
  if isBase64(data[i]):
   data[i] = base64.b64decode(data[i]).decode()
 return data

def generate_uuid():
 """Returns a random uuid"""
 eventId = str(uuid.uuid4()).replace('-', '')
 return eventId


def get_current_timestamp():
 """Returns a timestamp"""
 ts_ISO8601 = datetime.utcnow().isoformat() + 'Z'
 return str(ts_ISO8601)

# print(isBase64('aGVsbG8gd29ybGQ='));

#print(decode_records(6425))

#print( get_current_timestamp())
