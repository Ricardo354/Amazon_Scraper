from bs4 import BeautifulSoup
import requests
import pandas
import re

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
price = soup.findAll('span', attrs={'class':'a-offscreen'})

#Pegando os nomes e preços dos 5 primeiros produtos


product_title = [_.text for i in title[:5] for _ in i]
product_price = [_ for i in price[:5] for _ in i]

for prod_name,prod_price in zip(product_title,product_price):
    print(f'PRODUCT NAME: {prod_name}\nPRODUCT PRICE: {prod_price}')
    print('\n')


"""
Product_name | Price | 
"""