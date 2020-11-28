import requests
import schedule
import time
import subprocess


##scrape_game_views should be ran, then scrape_amazon_rank.py and minutes_viewed.py should be ran once a night.
subprocess.call("best_sellers.py", shell=True)
schedule.every().day.at("00.00").do(subprocess.call("scrape_amazon_rank.py", shell=True)) 
schedule.every().day.at("00.01").do(subprocess.call("calc_minutes_viewed.py", shell=True)) 
##need to write 'sync_game_names.py' to sync the names from the scrape_amazon_rank script, the scrape_games_views script and the games/publisher table
schedule.every().day.at("00.02").do(subprocess.call("sync_game_names.py", shell=True)) 

while True:
    schedule.run_pending()
    time_sleep(1)