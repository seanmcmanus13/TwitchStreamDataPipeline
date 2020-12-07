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

##The query below inserts yesterday's data since this script is ran after midnight
session.connection().connection.set_isolation_level(0)
session.execute('INSERT INTO minutes_viewed (game_id,game_name,minutes_viewed,date) SELECT game_id, game_name, SUM(viewers)*10, CURRENT_DATE FROM views WHERE time >= (CURRENT_DATE-1) AND time < (CURRENT_DATE) GROUP BY game_name,game_id ORDER BY sum(viewers) DESC')
session.connection().connection.set_isolation_level(1) 