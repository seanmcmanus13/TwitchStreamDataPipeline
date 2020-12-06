from twitchAPI.twitch import Twitch
from twitch import TwitchClient
import requests
import pandas as pd
import json
import sched, time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

####establish connection
db_string = "postgres://postgres:PW@localhost:5432/twitch_project"
db = create_engine(db_string, pool_pre_ping=True)
session = sessionmaker(bind=db)()

##insert the following information into a minutes_viewed table daily.
session.connection().connection.set_isolation_level(0)
session.execute(query)
session.connection().connection.set_isolation_level(1)  
#minutes_viewed_table fields
id serial PRIMARY KEY,game_id integer, game_name varchar, minutes_viewed integer,date date
##this is all rough work - i can't write this until i have data in this db as i need to test it.
INSERT INTO minutes_viewed
(game_id,
 game_name,
 minutes_viewed,
 date)
SELECT
game_id,
game_name,
,viewers
NOW()
FROM views AS V1
INNER JOIN views AS V2
ON v1.game_id = V2.game_id
##pseudo code - only want to select the values for that game for that day
WHERE views.time BETWEEN 
##pseudo code
##all the viewers for a game in a day = x
##x*10 = total minutes viewed per day = y
##
##store game, y, date