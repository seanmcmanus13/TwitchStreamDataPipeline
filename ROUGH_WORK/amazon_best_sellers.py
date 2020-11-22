from bs4 import BeautifulSoup
import requests

ps4_url = "https://www.amazon.com/Best-Sellers-Video-Games-PlayStation/zgbs/videogames/6427831011/ref=zg_bs_nav_vg_2_6427814011"
switch_url = "https://www.amazon.com/Best-Sellers-Video-Games-Nintendo-Switch/zgbs/videogames/16227133011/ref=zg_bs_nav_vg_2_16227128011"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
response=requests.get(ps4_url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')

##function to check if it's midnight, used for daily offloading of data/scheduling of tasks
def checkIfMidnight():
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return seconds_since_midnight == 0

#adapt this framework with scheduling to push this data to postgres once a day
i=1
for item in soup.select('.zg-item-immersion'):
    try:
        print('----------------------------------------')
        print(item.select('.p13n-sc-truncate')[0].get_text().strip())
        print(item.select('.p13n-sc-price')[0].get_text().strip())
        print(item.select('.a-icon-row i')[0].get_text().strip())
        print(item.select('.a-icon-row a')[1].get_text().strip())
        print('Rank: '+ str(i))
        i+=1
    except Exception as e:
        #raise e
        print('')