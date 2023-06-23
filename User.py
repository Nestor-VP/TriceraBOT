# Defining the BotUser Class:
# This class contains all the required user information
# 
import json
import AOE_API_constants as aoe_cts
from urllib.request import urlopen




class BotUser:
    def __init__(self, discord_id, platform , platform_id ):
        self._user_dictionary = {
            discord_id: {
                "user_platform": self.eval_platform(platform),
                "platform_id": platform_id,
                "aoe_name": self.fetch_aoe_name(platform,platform_id),
                "elo_single": self.fetch_elo_single(platform,platform_id),
                "elo_team": self.fetch_elo_team(platform,platform_id),
                "ladder_role": "villager",
                "rank_single": 0,
                "rank_team": 0
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
    def platform(self):
        return self._user_dictionary[self.key_id]["user_platform"]
    
    @property
    def platform_id(self):
        return self._user_dictionary[self.key_id]["platform_id"]
    
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
    

    # Key_id setter
    @key_id.setter
    def key_id(self, new_key):
        self._user_dictionary[new_key] = self._user_dictionary.pop(self.key_id)

    
    #Methods

    # Evaluates if platform input value is correct
    def eval_platform(self,platform):

        plt = platform.casefold()

        if (plt=='xbox')or(plt=='steam'):
            return plt
        else:
            return 'invalid'
    

    # 

    def fetch_aoe_name(self,platform,platform_id):

        plt = self.eval_platform(platform)

        root = aoe_cts.AOE2
        start = aoe_cts.START
        leaderboard_id = aoe_cts.RM1

        if plt =='xbox':
            
            platform_name = aoe_cts.XBOX
        
        elif plt =='steam':
            platform_name = aoe_cts.STEAM
        else:
            return 'no-data'
    

        try:
            api_data = urlopen( root + leaderboard_id+start+platform_name+f"{platform_id}")

            dictionary1 = api_data.read()
            
            my_dict = json.loads(dictionary1.decode('utf-8'))
            sub_dict = my_dict['leaderboard']
            dict2= sub_dict[0]
                    
            name = dict2['name']
            
            return name

        except:
            return 'no-data'

        
    

    
    def fetch_elo_single(self,platform,platform_id):

        plt = self.eval_platform(platform)

        root = aoe_cts.AOE2
        start = aoe_cts.START
        leaderboard_id = aoe_cts.RM1

        if plt =='xbox':
            
            platform_name = aoe_cts.XBOX
        
        elif plt =='steam':
            platform_name = aoe_cts.STEAM
        else:
            return 0
    

        try:
            api_data = urlopen( root + leaderboard_id+start+platform_name+f"{platform_id}")

            dictionary1 = api_data.read()
            
            my_dict = json.loads(dictionary1.decode('utf-8'))
            sub_dict = my_dict['leaderboard']
            dict2= sub_dict[0]
                    
            elo = dict2['rating']
            
            return elo

        except:
            return 0
        
    
    def fetch_elo_team(self,platform,platform_id):

        plt = self.eval_platform(platform)

        root = aoe_cts.AOE2
        start = aoe_cts.START
        leaderboard_id = aoe_cts.RMT

        if plt =='xbox':
            
            platform_name = aoe_cts.XBOX
        
        elif plt =='steam':
            platform_name = aoe_cts.STEAM
        else:
            return 0
    

        try:
            api_data = urlopen( root + leaderboard_id+start+platform_name+f"{platform_id}")

            dictionary1 = api_data.read()
           
            my_dict = json.loads(dictionary1.decode('utf-8'))
            sub_dict = my_dict['leaderboard']
            dict2= sub_dict[0]      
            elo = dict2['rating']
            return elo

        except:
            return 0



    

"""

# Create an instance of MyClass
my_instance = BotUser(231321,"xboxx", 321321)


# Access and print the dictionary

print(my_instance.dictionary)


#print attributes
print(my_instance.key_id)
print(my_instance.platform)
print(my_instance.platform_id)
print(my_instance.role)

"""

#my_instance = BotUser(2313,"STEAM", 76561198260505584)

#print(my_instance.dictionary)

# Access and print the dictionary






