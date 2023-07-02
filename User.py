# Defining the BotUser Class:
# Attribute: A dictionary containing User-AOE-Info ( Aoe-id , Aoe-name , ELOs , etc)
# Methods : Getters and Setters and Fetch-Methods( to retrive data from the AOE-API)
# 


import json
import AOE_API_constants as aoe_cts
from urllib.request import urlopen

class BotUser:
    def __init__(self, discord_id, aoe_id ):

        self.api_lista = self.fetch_data(aoe_id)
        self._user_dictionary = {
            discord_id: {
                
                "aoe_id": aoe_id,
                "aoe_name": self.api_lista[0],
                "country": self.api_lista[1],
                "elo_single": self.api_lista[2],
                "elo_team": self.api_lista[3],
                "ladder_role": self.calc_role(self.api_lista[2]),
                "rank_single": 0,
                "rank_team": 0,
                "verified" : "\u274C"
            }}
        

        

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
    def country(self):
        return self._user_dictionary[self.key_id]["country"]
    
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

    # Fetch_data: Retrieve (aoe_name, country, elo_single, elo_team) from AOE API
    def fetch_data(self,aoe_id):
        user_info = ["no-data","🇪🇺",0,0]

        try:
            api_data = urlopen(aoe_cts.AOE_API+f"{aoe_id}]")
            dictionary1 = api_data.read()
            my_dict = json.loads(dictionary1.decode('utf-8'))

            # Fetch User profile data
            user_data= my_dict["statGroups"]
            user_stats = my_dict["leaderboardStats"]
            alias = user_data[0]['members'][0]['alias']
            country = user_data[0]['members'][0]['country']

            # Code to get user_data country flag emoji - This could be a function
            country_code = country.upper()
            filename = "./flag.json"
            flag = "🇪🇺"
            with open(filename, mode='r',encoding='utf-8') as file:
                flag_list = json.load(file)
    
            for key in flag_list.keys():
                if key == country_code:
                    flag = flag_list[key]
                    break
                else:
                    flag = "🇪🇺"   

            
            user_info[0]= alias
            user_info[1]= flag   

            try:
                for game_type_info in user_stats:
                    if game_type_info["leaderboard_id"] == 3:
                        user_info[2] = game_type_info["rating"]
                    elif game_type_info["leaderboard_id"] == 4:
                        user_info[3] = game_type_info["rating"]
                    else:
                        pass
            except:
                pass
        
        except:
            pass

        return user_info
    

    #Working Fine until line 157

    def calc_role(self,elo):

        intervals = [(800 + i * 200, 800 + (i + 1) * 200) for i in range(5)]
        values = ['Aldeano', 'Milicia', 'Hombre de Armas', 'Espadachín', 'Espada Mandoble', 'Campeón', 'Legionario']
    
        for i in range(len(intervals)):
            interval = intervals[i]
            value = values[i+1]
        
            if elo >= interval[0] and elo < interval[1]:
                return value
    
        if elo < 800:
            return values[0]
        elif elo >= 1800:
            return values[6]















