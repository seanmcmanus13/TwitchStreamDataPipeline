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

    ##add timestamp data to df
    
    ##push df data to sql





