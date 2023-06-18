import AOE_API_constants as ct
import Avatars as avt
import os
from dotenv import load_dotenv

root = ct.AOE2

#__________________________________________________

# get_token: function to retrieve the Discord-Bot-Token from a .env file

def get_token():
    load_dotenv()
    token = os.getenv('TOKEN1')
    return token

#_________________________________________________________


# function to Validate the Platform ( Xbox or Steam)
def eval_platform(platform):

    plt = platform.casefold()

    if (plt=='xbox')or(plt=='steam'):
        return plt
    else:
        return 'error'


# ________________________________________________________________

