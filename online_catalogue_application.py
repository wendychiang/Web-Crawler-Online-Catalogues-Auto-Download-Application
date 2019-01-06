import requests
import bs4
import os
import sys
import urllib.request
import time
import shutil

# Create the file of today's day in the current path
form="%Y-%m-%d"
a = time.strftime(form,time.localtime())
if os.path.exists(a):
    shutil.rmtree(a)
os.mkdir(a)
os.chdir(a)

# The online catalogue url
originurl='http://www.pxmart.com.tw/px/edm.px'

response = requests.get(originurl)
soup = bs4.BeautifulSoup(response.text,'html.parser')

w1 = soup.find('button')
w2 = soup.button['onclick']

# w3 is the monthly url info for the catalogue
w3 = w2.split("'")[1]


pxurl = 'http://www.pxmart.com.tw/px/www.pxmart.com.tw/px/edm/edm/'

# final online catalogue url
finurl = pxurl+w3

response = requests.get(finurl)
soup2 = bs4.BeautifulSoup(response.text,'html.parser')

# find the image of the online catalogue
p3 = soup2.select("div[data-double='false']")
final = ''
n = len(p3)
count = 1
pxmpic = 'http://www.pxmart.com.tw/'
for i in range(0,n-1):
    final = p3[i]
    final_string = str(final)
    if i == 0:
        finalword = final_string.split('"')[5]
    else:
        finalword = final_string.split('"')[3]
    finalpath = pxmpic+finalword
    f = open(str(count)+'.png','wb')
    
    with urllib.request.urlopen(finalpath) as response2:
        html = response2.read()
        f.write(html)
    count +=1
