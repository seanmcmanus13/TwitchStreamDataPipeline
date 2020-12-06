import requests
import schedule
import time
import subprocess


##scrape_amazon_rank should be ran once a night. scrape_stock_price needs to be developed
##subprocess.call("scrape_stock_price.py", shell=True)
schedule.every().day.at("00.00").do(subprocess.call("scrape_amazon_rank.py", shell=True)) 
##schedule.every().day.at("00.01").do(subprocess.call("calc_minutes_viewed.py", shell=True)) 
##need to write 'sync_game_names.py' to sync the names from the scrape_amazon_rank script, the scrape_games_views script and the games/publisher table
##schedule.every().day.at("00.02").do(subprocess.call("sync_game_names.py", shell=True)) 
while True:
    schedule.run_pending()
    time_sleep(1)