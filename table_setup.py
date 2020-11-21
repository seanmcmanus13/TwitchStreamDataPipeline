import requests
import pandas as pd
import json
import sched, time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

####establish connection
##db_string = "postgres://postgres:PW@localhost:5432/twitch_project"
##db = create_engine(db_string, pool_pre_ping=True)
##session = sessionmaker(bind=db)()
##
####build db
##session.connection().connection.set_isolation_level(0)
##session.execute('INSERT INTO GAME_NAMES (GAME_ID,GAME_NAME) VALUES (1,2)')
##session.connection().connection.set_isolation_level(1)

##psycopg2 connection
connection = psycopg2.connect(user="postgres",
                                  password="PASSWORD",
                                  host="localhost",
                                  port="?",
                                  database="twitch_project")
#styleguide - field name should be all lowercase. Space between words should contain a _ always.
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Games (id integer PRIMARY KEY, game_name varchar);")
cursor.execute("CREATE TABLE IF NOT EXISTS Views (id serial PRIMARY KEY,game_id integer, game_name varchar, viewers integer,time timestamp);")
cursor.execute("CREATE TABLE IF NOT EXISTS Publishers (id integer PRIMARY KEY, game_name varchar,publisher varchar);")
cursor.execute("CREATE TABLE IF NOT EXISTS Sales (id integer PRIMARY KEY, sales int, time timestamp);")
connection.commit()
cursor.close()
connection.close()