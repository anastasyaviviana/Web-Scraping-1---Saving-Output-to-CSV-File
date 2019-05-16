import requests
from bs4 import BeautifulSoup
import csv

link=requests.get('https://pokemondb.net/pokedex/national')
soup=BeautifulSoup(link.text,'html.parser')

alldata=""
for a in soup.findAll(class_='infocard'):
        for b in a.findAll('span',class_='infocard-lg-data text-muted'):
                dataperitem=""
                for c in b.findAll(class_='ent-name'):
                        for d in b.find('small'):
                                dataperitem=dataperitem+str(d)+','+c.text
                        alldata=alldata+dataperitem+'\n'
print(alldata)

#saving output to csv file

datapokemon=open('./file excel/pokemon.csv','w',newline='',encoding='utf8')
#input header
header=csv.DictWriter(datapokemon,fieldnames=["id_pokemon", "nama_pokemon"])
header.writeheader()
#input data
datapokemon.write(alldata)