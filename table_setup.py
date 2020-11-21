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
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Games (game_id integer PRIMARY KEY, game_name varchar);")
cursor.execute("CREATE TABLE IF NOT EXISTS Views (id serial PRIMARY KEY,game_id integer, game_name varchar, viewers integer,time timestamp);")
cursor.execute("CREATE TABLE IF NOT EXISTS Publishers (publisher_id serial PRIMARY KEY, game_name varchar,publisher varchar);")
cursor.execute("CREATE TABLE IF NOT EXISTS Sales (id serial PRIMARY KEY, game_id integer, sales int, time timestamp);")
connection.commit()
cursor.close()
connection.close()