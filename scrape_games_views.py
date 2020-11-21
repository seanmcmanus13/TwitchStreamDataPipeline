from twitchAPI.twitch import Twitch
from twitch import TwitchClient
import requests
import pandas as pd
import json
import sched, time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


##twitch api input variables

client_ID = ''
secret = ''

#create instance of twitch API
twitch = Twitch(client_ID, secret)
twitch.authenticate_app([])
client = TwitchClient(client_ID)

####establish connection
db_string = "postgres://postgres:PW@localhost:5432/twitch_project"
db = create_engine(db_string, pool_pre_ping=True)
session = sessionmaker(bind=db)()

##function to check if it's midnight, used for daily offloading of data/scheduling of tasks
def checkIfMidnight():
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return seconds_since_midnight == 0

##write to games tables, write to views table
while True:
    time.sleep(500)
    curr_time = []
    name = []
    game_viewers = []
    times = []
    query = []
    i = 0
    games = client.games.get_top(100)
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
    while i < 99:
        query = 'INSERT INTO views (game_id,viewers,game_name,time) VALUES (' + str(games[i]['game']['id']) + ',' + ((str([games[i]['viewers']])).replace('[','')).replace(']','') +',' + '\'' + str(games[i]['game']['name']).replace('\'','') + '\'' + ',' + 'NOW()' +')'
        #print(query)
        #send viewership information straight to views table
        session.connection().connection.set_isolation_level(0)
        session.execute(query)
        session.connection().connection.set_isolation_level(1)  
        #df_viewers = df_viewers.append(pd.DataFrame({"game_name":[games[i]['game']['name']],"viewers":[games[i]['viewers']],"time":[curr_time]}), ignore_index=True, sort=False)
        i+=1
        #if checkIfMidnight():
            #if gamename from the views table is not in the games table add it
            #session.connection().connection.set_isolation_level(0)
            #session.execute('INSERT INTO games (game_id, game_name)')
            #session.connection().connection.set_isolation_level(1) 
            