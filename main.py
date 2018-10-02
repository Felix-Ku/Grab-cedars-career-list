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
        
# Loop to assign every record a date  
for i in range((len(dates)-1)):
    if dates[i+1]==" ":
        dates[i+1]==dates[i]
        

# Main selection process
for i in range((len(dates)-1)):
    next=input('Show the next & following record(s)? [Y/N] ')
    if next=='N' or next=='n':
        break
    else:
        print ('Record.',i+1)
        print ('Posted date: ',dates[i])
        print ('Name of career/event: ',names[i])
        print ('Interested? ')
        choice=input('[Y/N]')
        if choice=='Y' or choice=='y':
           # Save the interested data to files
           localpath="D:\saved_career_data\%s"%(links[i].split('/')[-1])
           urllib.request.urlretrieve(links[i],localpath)
           print('File has been saved successfully!')                           

print ('This is the end of records')

# Create CSV file for all records
create_csv=input('Create a CSV file to store all records? [Y/N] ')
if create_csv=='Y' or create_csv=='y':                                    
    raw={'Names':names,'Links':links}
    df=pd.DataFrame(raw,columns=['Names','Links'],index=dates)
    df.to_csv('d:\saved_career_data\%s_updated.csv'%(dates[i]),encoding='utf_8_sig')
    print ('CSV file generated successfully')

print ('Good luck!')
