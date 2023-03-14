from bs4 import BeautifulSoup
import requests
import pandas

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
            'Accept-Language':'en-US, en;q=0.5'})
#URL temporaria pra eu poder substituir o search method, assim mostrando o que o user quer ver

TEMP_URL = 'https://www.amazon.com/s?k=cat+toys&crid=9UO84T9OISOI&sprefix=cat+toy%2Caps%2C191&ref=nb_sb_noss_1'
search_method = input('What do you want to see?: ')
search_method.replace(' ', '+')
URL = "https://www.amazon.com/s?k={}&crid=9UO84T9OISOI&sprefix=cat+toy%2Caps%2C191&ref=nb_sb_noss_1".format(search_method)
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")
title = soup.findAll("span", attrs={"class":'a-size-base-plus a-color-base a-text-normal'})


#Pegando os nomes dos 5 primeiros produtos

data = []
for i in title[:4]:
    for _ in i:
        _ = _.text
        data.append(_)
for i in data:
    print(i)

#Criando o arquivo .csv

"""
Product_name | Price | 
"""