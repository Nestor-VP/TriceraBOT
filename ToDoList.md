# TriceraBOT ToDo List

## First Steps 
1. [x] Install Discord API for python
2. [x] set Aoe2.net API for Ladder Data
3. [x] Basic BOT commands

## Next Steps
1. [x] Retrieve Data from Aoe2 API
2. [x] Merge AOE2 API - DISCORD py
3. [ ] Send Embeds with Discord BOT
   - [x] basic embeds
   - [ ] Formatting and labeling text for embeds
   - [x] add tumbnail
   - [x] add image
   - [ ] Create Player Card with embeds
4. [x] Make BOT commands case unsensitive
5. [ ] Make Bot Set Roles
6. [ ] Work with JSON files
    - [x] Read Data from JSON
    - [x] Edit JSON file
    - [x] Sort Data from a JSON file
7. [ ] Optimize Code
   - [x] functions
   - [x] Classes
   - [x] Define Constants
   - [x] Create Modules
8. [ ] Show Table on Discord
9. [ ] Set User and Admin Commands
10. [ ] Bot Data self-update function

## BOT Commands List
1. [x] !bind platform UserID  
   > Binds Discord account with Xbox/Steam account  
   > Parameters:  
   > - platform = xbox or steam  
   > - UserID = PlayerID or SteamID
   > New player will start with a defaul-role (villager)

2. [ ] !unbind
   > Unbinds Discord account with associated platform-account
   > User aoe2-role will be deleted and set to channel-default-role

3. [ ] !rebind platform UserID
   > Rebinds Discord account with a new Xbox/Steam account
   > Users aoe2-role will be set to default-player-role ( villager)

4. [ ] !info *Discord.User
   > Retrieves Desired user Player Card  
   > if empty retrieves command.author Player Card

5. [ ] !update
   > Updates Command.author Player Card

6. [ ] !verify Discord.User
   > Admins command to verify Player Identity

7. [ ] !rebind platform UserID
   > Command to rebind Discord Account with xbox/steam account  
   > WARNING: You will lose your verification

8. [ ] !RemoveBind
    > Unlinks Discord.Account with Platform Account  
    > User is removed from Local Ladder  
    > All User Stored Data is deleted  
    > User will Lose his "Ladder Role"

9.  [ ] !AdminRemove Discord.member
    > Admin Command to manually remove a Discord.member from local ladder.  
    > All User Stored Data is deleted  
    > User will Lose his "Ladder Role"


## Player Card 
 - [x] Discord.name
 - [x] Discord avatar - thumbnail
 - [ ] AoE2 nickname
 - [ ] RM 1v1 ELO
 - [ ] RM TG ELO
 - [ ] Unranked ELO
 - [ ] Ladder Role
 - [x] Ladder Role Avatar
    
   



  

