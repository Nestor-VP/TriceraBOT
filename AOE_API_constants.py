# Aoe2.net API Constants
# some useful constants to retrieve the desired data from the Aoe2.net API

## Aoe2:DE leaderboard URL on Ao2.net API
AOE2 = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id="

## RELIC LINK community API - personal stats endpoint
AOE_API = "https://aoe-api.reliclink.com/community/leaderboard/GetPersonalStat?title=age2&profile_ids=["


## Leaderboard Constants
### aoe2 unranked leaderboard id
URK = "0"
### aoe2 RM 1v1 leaderboard id
RM1 = "3"
### aoe2 RM TEAM leaderboard id
RMT = "4"

## Start and Count string constant 
##( useless for us , because we want to search data for only 1 player ) - but required for using the aoe2 API
## That's why we define Start and count as constant
START= "&start=1&count=1"

## Search Type Constants

ID_SEARCH = "&profile_id="

XBOX = "&profile_id="
STEAM = "&steam_id="

#.......................................................................
##  Bot-users list file path

# users_file = "./nicknames.json"
users_file = "./users_list.json"




