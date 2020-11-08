from twitchAPI.twitch import Twitch
import pandas as pd
import sched, time
import json

##twitch api input variables
client_ID = ''
secret = ''

#create instance of twitch API
twitch = Twitch(client_ID, secret)
twitch.authenticate_app([])

##sql
##engine = create_engine('postgresql://postgres:FwwBFmleh65qYxKxDVb9@twitchdata.chd4n5ul8muk.us-east-2.rds.amazonaws.com:5432/twitchdata')


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



