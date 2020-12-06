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
session.execute('INSERT INTO games(game_id, game_name) SELECT DISTINCT game_id, game_name FROM views WHERE views.game_id NOT IN (SELECT game_id FROM games) AND views.game_name IS NOT NULL')
session.connection().connection.set_isolation_level(1)  
