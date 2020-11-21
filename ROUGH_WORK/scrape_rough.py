from twitchAPI.twitch import Twitch
import pandas as pd
import sched, time
import json
from datetime import datetime
import psycopg2


##twitch api input variables
client_ID = ''
secret = ''

#create instance of twitch API
twitch = Twitch(client_ID, secret)
twitch.authenticate_app([])

##sql
connection = psycopg2.connect(user="",
                                  password="",
                                  host="localhost",
                                  port="",
                                  database="twitch_project")

##check if it's midnight
def checkIfMidnight():
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return seconds_since_midnight == 0

#setup dataframe
game_data_df = pd.DataFrame(columns = ['',''])
##loop to push data every minute
while True:
    sleep(60 - time() % 60)
    ##get games data
    games = client.games.get_top(100)
    ##get time stamp
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
    ##parse json data into df
        ##need to figure out how to specifically remove the data I want from the json. Seems like it's indexable by index and tag, see below:
        ##games[0]['game']['name']
        ##add a new row of data based on the output of client.games.get_top(100)


    ##add timestamp data to df
        ##add time stamp to that row
    ##push df data to sql
        ##what is the most performant way of doing this? Write to the sql db how often? See below as a starting spot
=            ##df.to_sql('stream_data', engine, if_exists='append',index=False)
            ##engine.dispose()


##-------------------------------------------------------------------------------------------------------------------------------------------------

##rough work
##this code needs to be added to the while loop above so that these run at fixed intervals to pull new information
df1 = pd.DataFrame({"game_name":[]})
game_names = []
game_ids = []
game_viewers = []
time = []
##add game_name not in list to the list
i = 0
while i < 99 and games[i]['game']['name'] not in game_names:
    game_names.append(games[i]['game']['name'])
    game_ids.append(games[i]['game']['id'])
    i+=1
curr_time = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
##add the name to df where it's not in the list
##add the other items as appropriate to this table or another one
n=0
for name in game_names:
    if name not in list(df1["game_name"]):
        df1= df1.append({'game_name': name}, ignore_index=True)

df1 = df1.set_index("game_name")
##add game_id
for i in range(len(game_dict)):
    if list(game_dict)[i] in df1.index.tolist():
        df1.at[list(game_dict)[i],'game_id'] = list(game_dict.values())[i]
##make seperate df to store view information
##think about how best to store this data. the goal isnt to store it all in pandas. pandas df is just an intermediary before pushing to sql
##loop to pull game/viewer/time informatione very 60 seconds

#Loop will grab data every 5 minutes.
#After 24 hours, the loop will kick the data to a ____ and delete the pandas dataframe

while True:
    time.sleep(300)
    curr_time = []
    name = []
    game_viewers = []
    times = []
    i = 0
    games = client.games.get_top(100)
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
    while i < 99:
        df_viewers = df_viewers.append(pd.DataFrame({"game_name":[games[i]['game']['name']],"viewers":[games[i]['viewers']],"time":[curr_time]}), ignore_index=True, sort=False)
        i+=1
        if checkIfMidnight():
            ##kick the df to postgres

            ##reset the pandas df
            df_viewers = pd.DataFrame({"game_name":[],"viewers":[],"time":[]})
