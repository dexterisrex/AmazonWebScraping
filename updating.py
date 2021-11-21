from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"E:\python\tmtconnekt\automationscrapping\chromedriver_win32\chromedriver.exe")

url = "https://www.amazon.ae/New-Apple-iPhone-FaceTime-256GB/dp/B09G9CD8PS/ref=sr_1_1?pf_rd_i=15415001031&pf_rd_m=A2KKU8J8O8784X&pf_rd_p=3ab8e537-f846-4593-99e4-dbcb0b161425&pf_rd_r=5GKQZE2AHGP6JJV0P8G0&pf_rd_s=merchandised-search-8&pf_rd_t=101&qid=1637344982&s=electronics&sr=1-1&srs=17025067031&th=1"

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

title = soup.find('span',{'id':'productTitle'})
title = title.text.strip()
#print(title)
info = soup.find('div', {'data-feature-name': 'productOverview'})
#print(info)
description = soup.find('div', {'data-feature-name':'featurebullets'})
#print(description)
specification = soup.find_all('table', {'class':'a-bordered'})
#print(specification[1])
price = soup.find('span', {'class':'a-price a-text-price a-size-medium apexPriceToPay'})
price = price.text.replace("AED","").split('.')
#print(price[0])

quantity = 100

sk = url.split('/')

for i in sk:
    if i.startswith("B"):
        if len(i)==10:
            sku = i

data = [[title,info,description,specification[1],price[0],quantity,sku]]

df = pd.DataFrame(data, columns=['title', 'Info', 'Description', 'Specification', 'Price', 'Quantity', 'SKU'])
df.to_csv('withsku.csv')