import requests
import json
import sched, time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import subprocess


##function to check if it's midnight, used for daily offloading of data/scheduling of tasks
def checkIfMidnight():
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return seconds_since_midnight == 0

##scrape_game_views should be ran, then scrape_amazon_rank.py and minutes_viewed.py should be ran once a night.