
# Some useful functions 

import AOE_API_constants as ct
import Avatars as avt
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

root = ct.AOE2

#__________________________________________________

# get_token: function to retrieve the Discord-Bot-Token from a .env file

def get_token():
    load_dotenv()
    token = os.getenv('TOKEN1')
    return token

#_________________________________________________________

def get_current_hour(timezone_offset):
    # Calculate the current time with the specified timezone offset
    current_time = datetime.now(timezone.utc) + timedelta(hours=timezone_offset)

    # Extract the hour from the current time
    current_hour = current_time.strftime("%H:%M:%S")
    # Print the current hour
    return current_hour


