import json
from urllib.request import urlopen
from urllib.parse import urlencode

# Get a list [aoeid_1, aoeid_2, aoeid_3, ...] of aoe_ids of registered users
def update_all_elos(json_file):
        # Read Users-Database - 
        filename = json_file
        with open(filename, mode='r',encoding='utf-8') as file:
                data = json.load(file)
    

        user_list = []

        # From users database create a list will users-aoe_ids
        for key in data:
                user_list.append(int(data[key]["aoe_id"]))

        # Using users-aoe_ids list , proceed with the API-request
        #profile_ids = urlencode({'profile_ids': user_list}, doseq=True)
        url = f"https://aoe-api.reliclink.com/community/leaderboard/GetPersonalStat?title=age2&profile_ids="+ f"{user_list}"
        url = url.replace(" ", "%20")
        api_data = urlopen(url)
        dictionary1 = api_data.read()
        api_response = json.loads(dictionary1.decode('utf-8'))

        # Destructure API-data and retrieve desired data
        users_db = api_response["statGroups"]
        elo_db = api_response["leaderboardStats"]

        user_dictionary={}
        for user in users_db:

                user_dictionary.update(
                {user["members"][0]["profile_id"]:
                {"aoe_name":user["members"][0]["alias"],
                "country":user["members"][0]["country"],
                "stat_group":user["members"][0]["personal_statgroup_id"],
                "elo_single":0,
                "elo_team":0              
                 }} )   
   
        for key in user_dictionary:
        
                stat_group = user_dictionary[key]["stat_group"]
                for elo_data in elo_db:
                        statgroup_id = elo_data["statgroup_id"]
               
                        if stat_group==statgroup_id:
                                leaderboard_id = elo_data["leaderboard_id"]
                                elo = elo_data["rating"]
                                if leaderboard_id ==3:
                                        user_dictionary[key]["elo_single"]= elo
                                elif leaderboard_id ==4:
                                        user_dictionary[key]["elo_team"]= elo
                                else:
                                        pass


        # Save updated-API-data in users-list-info
        filename = json_file
        with open(filename, mode='r',encoding='utf-8') as file:
                data = json.load(file)

        for key in data:
                user_aoe_id = data[key]["aoe_id"]
                #print(type(user_aoe_id))

                for key2 in user_dictionary:
                
                        if str(key2) == user_aoe_id:
                                data[key]["aoe_name"]= user_dictionary[key2]["aoe_name"]
                                data[key]["elo_single"]= user_dictionary[key2]["elo_single"]
                                data[key]["elo_team"]= user_dictionary[key2]["elo_team"]


        filename = json_file
        with open(filename, mode='w',encoding='utf-8') as file:
                json.dump(data,file)