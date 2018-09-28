# Modules
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import urllib.request

# HTTP request
url="http://www.cedars.hku.hk/careers/latest-announcement"
resp=requests.get(url)
if resp.status_code==200:
    print('HTTP requested successfully')
else:
    print('Something wrong happened, the HTTP Status Code is: ',resp.status_code)

soup=BeautifulSoup(resp.text,'html.parser')

# Storing current data into seperate lists
dates=[]
names=[]
links=[]

check=True

for index in soup.findAll('tr'):
    for date in index.findAll('i'):
        dates.append(date.get_text())
        check=False
    for link in index.findAll('a', {'style': 'font-family: Verdana; font-size: 12px; letter-spacing: normal;'}):
        names.append(link.get_text())
        links.append(link.get('href'))
        dates.append(" ")
        check=True
    if check==True:
        dates.pop()
        
# Loop to assign every record a date  
for i in (range(dates)-1):
    if dates[i+1]==" ":
        dates[i+1]==dates[i]
        

# Main selection process
for i in range(dates):
    next=raw_input('Show the next & following record(s)? [Y/N]')
    if next=='N'
        break
    else:
        print ('Record.',i)
        print ('Posted date: ',dates[i])
        print ('Name of career/event: ',names[i])
        print ('Interested?')
        choice=raw_input('[Y/N]')
        if choice==Y
           # Save the interested data to files
           urllib.request.urlretrieve(links[i], 'D:\saved_career_data\'+dates[i]+'\'+links[i].split('/')[-1])
           print('File has been saved successfully!')                           

print ('This is the end of records')

# Create CSV file for all records
create_csv=raw_input('Create a CSV file to store all records? [Y/N]')
if create_csv=='Y'                                    
    raw={'Names':names,'Links':links}
    df=pd.DataFrame(raw,columns=['Names','Links'],index=dates)
    df.to_csv('d:\saved_career_data\'+dates[i]+'_updated.csv',encoding='utf_8_sig')
    print ('CSV file generated successfully')

print ('Good luck!')
