import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

url="http://www.cedars.hku.hk/careers/latest-announcement"
resp=requests.get(url)
if resp.status_code==200:
    print('HTTP requested successfully')
else:
    print('Something wrong happened, the HTTP Status Code is: ',resp.status_code)

soup=BeautifulSoup(resp.text,'html.parser')

dates=[]
names=[]
links=[]

check=False

for index in soup.findAll('tr'):
    for link in index.findAll('a', {'style': 'font-family: Verdana; font-size: 12px; letter-spacing: normal;'}):
        names.append(link.get_text())
        links.append(link.get('href'))
        dates.append(" ")
        check=True
    for date in index.findAll('i'):
        dates.append(date.get_text())
        check=False
    if check==True:
        dates.pop()

raw={'Names':names,'Links':links}
df=pd.DataFrame(raw,columns=['Names','Links'],index=dates)
df.to_csv('d:\output.csv',encoding='utf_8_sig')
print ('CSV file generated successfully')
