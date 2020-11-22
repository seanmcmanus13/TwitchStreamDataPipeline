import requests
import pandas as pd
import json
import sched, time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

##psycopg2 connection
connection = psycopg2.connect(user="postgres",
                                  password="PASSWORD",
                                  host="localhost",
                                  port="?",
                                  database="twitch_project")
#styleguide - field name should be all lowercase. Space between words should contain a _ always.
#you can probably integrate all the game metadata to sit in one table. no need to overcomplicate this right now
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Games (game_id integer PRIMARY KEY, game_name varchar);")
cursor.execute("CREATE TABLE IF NOT EXISTS Views (id serial PRIMARY KEY,game_id integer, game_name varchar, viewers integer,time timestamp);")
cursor.execute("CREATE TABLE IF NOT EXISTS Minutes_Viewed (id serial PRIMARY KEY,game_id integer, game_name varchar, minutes_viewed integer,date date);")
cursor.execute("CREATE TABLE IF NOT EXISTS Publishers (publisher_id serial PRIMARY KEY, game_name varchar,publisher varchar);")
cursor.execute("CREATE TABLE IF NOT EXISTS Amazon_Best_Sellers (id serial PRIMARY KEY, game_id integer,console varchar, game_name varchar, rank int, time timestamp);")
connection.commit()
cursor.close()
connection.close()