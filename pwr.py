#WEB SCRAPING FROM WEB WIKIPEDIA POWER RANGERS

import requests
from bs4 import BeautifulSoup
import csv

link=requests.get('https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes')
soup=BeautifulSoup(link.content,'html.parser')      

# PRINT LIST FILM POWER RANGERS
k=1
alldata=""
for a in soup.find_all('table',class_='wikitable'):
    for b in a.find_all('tr'):
        for c in b.find_all('td'):    
            dataperitem=''
            for d in c.find_all('i'):
                dataperitem=dataperitem+str(k)+','+d.text                               # d.text -> tittle
                k+=1
                for e in b.find_all('span',class_='bday dtstart published updated'):        
                    dataperitem=dataperitem+','+e.text                                  # e.text -> first aired
                    for f in b.find_all('span',class_='dtend'):
                        dataperitem=dataperitem+','+f.text                              # f.text -> last aired
                alldata=alldata+dataperitem+'\n'
print(alldata)

# saving output to csv file

datapwr=open('./file excel/powerrangers.csv','w',newline='',encoding='utf8')
#input header
writer=csv.DictWriter(datapwr,fieldnames=["no", "title", "first aired","last aired"])
writer.writeheader()
#import data
datapwr.write(alldata)