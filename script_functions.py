
# Some useful functions 

import AOE_API_constants as ct
import Avatars as avt
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
import json
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError

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
    current_hour = current_time.strftime("%H:%M")
    # Print the current hour
    return current_hour

#______________________________________________________________________
# Check if aoe-id was input correctly
def request_code(aoe_id):
    url = f"https://aoe-api.reliclink.com/community/leaderboard/GetPersonalStat?title=age2&profile_ids=[{aoe_id}]"

    try:
        api_data = urlopen(url)
        dictionary1 = api_data.read()
        response = json.loads(dictionary1.decode('utf-8'))
        request_code = response["result"]["message"]
        if request_code == "SUCCESS":
            return True
        
    except HTTPError as http_error:

            return False
    except URLError as url_error:
            return False

#______________________________________________________________________
# Return number of registered users
def number_of_users():
     
    filename = "./channel_info.json"
    with open(filename,'r') as file:
        data = json.load(file)
    
    return data["registered_users"]


#______________________________________________________________________
# Add +1 on Number of registered users (used on a succesful bind)
def add_one_user():
     
    filename = "./channel_info.json"
    with open(filename,'r') as file:
        data = json.load(file)
    
    data["registered_users"] += 1

    with open(filename, mode='w') as file:
                json.dump(data, file)
    
#______________________________________________________________________



