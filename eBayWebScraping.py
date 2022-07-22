import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=men+underwear&_sacat=0&LH_TitleDesc=0&_dmd=1&rt=nc&_odkw=men+boxers&_osacat=0'

def get_data(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  return soup

def parse(soup):
  results = soup.find_all('div',{'class':'s-item__info clearfix'})
  for item in results:
    product = {
        'Title': item.find('h3',{'class':'s-item__title'}).text,
        'SoldPrice': item.find('span',{'class':'s-item__price'}).text,
        'ShippingElement': item.find('span',{'class':'s-item__shipping s-item__logisticsCost'}),
        #'Shipping': 'ShippingElement'.get_text() if 'ShippingElement' else "No details",
        'Location': item.find('span',{'class':'s-item__location s-item__itemLocation'}),
        'sold_watchers': item.find('span',{'class':'BOLD'}),
        'link': item.find('a',{'class':'s-item__link'})['href'] 
    } 
  print(product)
  return

soup = get_data(url)
parse(soup)
