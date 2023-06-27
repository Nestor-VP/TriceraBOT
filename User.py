# Defining the BotUser Class:
# Attribute: A dictionary containing User-AOE-Info ( Aoe-id , Aoe-name , ELOs , etc)
# Methods : Getters and Setters and Fetch-Methods( to retrive data from the AOE-API)
# 


import json
import AOE_API_constants as aoe_cts
from urllib.request import urlopen

class BotUser:
    def __init__(self, discord_id, aoe_id ):
        self._user_dictionary = {
            discord_id: {
                
                "aoe_id": aoe_id,
                "aoe_name": self.fetch_aoe_name(aoe_id),
                "elo_single": self.fetch_elo_single(aoe_id),
                "elo_team": self.fetch_elo_team(aoe_id),
                "ladder_role": "Aldeano",
                "rank_single": 0,
                "rank_team": 0,
                "verified" : "\u274C"
            }
        }

    def print_dictionary(self):
        print(self._user_dictionary)

    
    # Getters

    @property
    def dictionary(self):
        return self._user_dictionary
    
    
    @property
    def key_id(self):
        return list(self._user_dictionary.keys())[0]
    
    @property
    def value(self):
        return self._user_dictionary[self.key_id]
    
  
    @property
    def aoe_id(self):
        return self._user_dictionary[self.key_id]["aoe_id"]
    
    @property
    def aoe_name(self):
        return self._user_dictionary[self.key_id]["aoe_name"]
    
    @property
    def elo_single(self):
        return self._user_dictionary[self.key_id]["elo_single"]
    
    @property
    def elo_team(self):
        return self._user_dictionary[self.key_id]["elo_team"]
    
    @property
    def role(self):
        return self._user_dictionary[self.key_id]["ladder_role"]
    
    @property
    def rank_single(self):
        return self._user_dictionary[self.key_id]["rank_single"]
    
    @property
    def rank_team(self):
        return self._user_dictionary[self.key_id]["rank_team"]
    
    @property
    def verified(self):
        return self._user_dictionary[self.key_id]["verified"]
    

    # Key_id setter
    @key_id.setter
    def key_id(self, new_key):
        self._user_dictionary[new_key] = self._user_dictionary.pop(self.key_id)
    
    # role setter
    @role.setter
    def role(self,new_role):
        self._user_dictionary[self.key_id]["ladder_role"] = new_role

    @verified.setter
    def verified(self,new_value):
        self._user_dictionary[self.key_id]["verified"]= new_value

    
    #Methods 

    def fetch_aoe_name(self,aoe_id):

       

        root = aoe_cts.AOE2
        start = aoe_cts.START
        leaderboard_id = aoe_cts.RMT

        id_search = aoe_cts.ID_SEARCH
    

        try:
            api_data = urlopen( root + leaderboard_id+start+id_search+f"{aoe_id}")

            dictionary1 = api_data.read()
            
            my_dict = json.loads(dictionary1.decode('utf-8'))
            sub_dict = my_dict['leaderboard']
            dict2= sub_dict[0]
                    
            name = dict2['name']
            
            return name

        except:
            return 'no-data'

        
    

    
    def fetch_elo_single(self,aoe_id):

        root = aoe_cts.AOE2
        start = aoe_cts.START
        leaderboard_id = aoe_cts.RM1
        id_search = aoe_cts.ID_SEARCH

        

        try:
            api_data = urlopen( root + leaderboard_id+start+id_search+f"{aoe_id}")

            dictionary1 = api_data.read()
            
            my_dict = json.loads(dictionary1.decode('utf-8'))
            sub_dict = my_dict['leaderboard']
            dict2= sub_dict[0]
                    
            elo = dict2['rating']
            
            return elo

        except:
            return 0
        
    
    def fetch_elo_team(self,aoe_id):

        root = aoe_cts.AOE2
        start = aoe_cts.START
        leaderboard_id = aoe_cts.RMT
        id_search = aoe_cts.ID_SEARCH

    
        try:
            api_data = urlopen( root + leaderboard_id+start+id_search+f"{aoe_id}")

            dictionary1 = api_data.read()
           
            my_dict = json.loads(dictionary1.decode('utf-8'))
            sub_dict = my_dict['leaderboard']
            dict2= sub_dict[0]      
            elo = dict2['rating']
            return elo

        except:
            return 0








