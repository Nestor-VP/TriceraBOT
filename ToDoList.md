# TriceraBOT ToDo List

## First Steps 
1. [x] Install Discord API for python
2. [x] set Aoe2.net API for Ladder Data
3. [x] Basic BOT commands

## Next Steps
1. [x] Retrieve Data from Aoe2 API
2. [x] Merge AOE2 API - DISCORD py
3. [x] Send Embeds with Discord BOT
   - [x] basic embeds
   - [x] Formatting and labeling text for embeds
   - [x] add tumbnail
   - [x] add image
   - [x] Create Player Card with embeds
4. [x] Make BOT commands case unsensitive
5. [x] Make Bot Set Roles
6. [x] Work with JSON files
    - [x] Read Data from JSON
    - [x] Edit JSON file
    - [x] Sort Data from a JSON file
7. [x] Optimize Code
   - [x] functions
   - [x] Classes
   - [x] Define Constants
   - [x] Create Modules (Cogs)
8. [x] Show Table on Discord
9. [x] Set User and Admin Commands
10. [ ] Bot Data self-update function

## BOT Commands List
1. [x] !bind AOE_ID  
   > Binds Discord account with AOE account  
   > Parameters:  
   > - AOE_ID = AOE player-ID-number
   > New player will start with a defaul-role (villager)

2. [x] !unbind (Admin command)
   > Unbinds Discord account with associated AOE-account
   > User aoe2-role will be deleted and set to channel-default-role

3. [x] !rebind  UserID
   > Rebinds Discord account with a new AOE account
   > Users aoe2-role will be set to default-player-role ( villager)

4. [x] !info *Discord.User
   > Retrieves Desired user Player Card  
   > if empty retrieves command.author Player Card

5. [x] !update
   > Updates Command.author Player Card

6. [x] !verify Discord.User
   > Admins command to verify Player Identity

7. [x] !rebind UserID
   > Command to rebind Discord Account with new AOE account  
   > WARNING: You will lose your verification


8.  [x] !AdminRemove Discord.member  ( same as !unbind)
    > Admin Command to manually remove a Discord.member from local ladder.  
    > All User Stored Data is deleted  
    > User will Lose his "Ladder Role"


## Player Card 
 - [x] Discord.name
 - [x] Discord avatar - thumbnail
 - [x] AoE2 nickname
 - [x] RM 1v1 ELO
 - [x] RM TG ELO
 - [ ] Unranked ELO ( cant fetch data from AOE - API)
 - [x] Ladder Role
 - [x] Ladder Role Avatar
    
   



  

