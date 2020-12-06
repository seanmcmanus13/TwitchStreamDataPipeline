from bs4 import BeautifulSoup
import requests
import json
import sched, time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

ps4_url = "https://www.amazon.com/Best-Sellers-Video-Games-PlayStation/zgbs/videogames/6427831011/ref=zg_bs_nav_vg_2_6427814011"
switch_url = "https://www.amazon.com/Best-Sellers-Video-Games-Nintendo-Switch/zgbs/videogames/16227133011/ref=zg_bs_nav_vg_2_16227128011"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
response=requests.get(ps4_url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')

db_string = "postgres://postgres:PW@localhost:5432/twitch_project"
db = create_engine(db_string, pool_pre_ping=True)
session = sessionmaker(bind=db)()

##this isn't finished, check and test this
sales_query = []
i=1
for item in soup_ps4.select('.zg-item-immersion'):
            sales_query = 'INSERT INTO amazon_best_sellers (console, game_name, price, rank, time) VALUES (' + '\'' + 'Playstation 4' + '\'' + ',' + '\'' + str(item.select('.p13n-sc-truncate')[0].get_text().strip()).replace('\'','') + '\'' + ',' + '\'' + str(item.select('.p13n-sc-price')[0].get_text().strip()).replace('\'','') + '\'' + ',' + str(i) + ',' + 'NOW()' + ')'
            ##print(sales_query)
            session.connection().connection.set_isolation_level(0)
            session.execute(sales_query)
            session.connection().connection.set_isolation_level(1)  
            i+=1
