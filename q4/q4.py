#!/usr/bin/python3
import requests
import bs4
import pandas
from bs4 import BeautifulSoup

URL="https://www.gsmarena.com/"
r=requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')
list1=[]
for brands in soup.find_all('div',attrs={'class':'brandmenu-v2 light l-box clearfix'}):
    for links in brands.find_all('li'):
        for urls in links.find_all('a'):
            str1="https://www.gsmarena.com/"+urls.get('href')
            list1.append(str1)

phone_cam=[]
phone_dim=[]
phone_dis=[]
phone_cpu=[]
phone_dissize=[]
phone_os=[]
phone_net=[]
phone_name=[]
phone_sim=[]
phone_ram=[]

count=1
for i in list1:
    if(count>504):
        break
    r1=requests.get(i)
    soup=BeautifulSoup(r1.content,'html5lib')
    list2=[]
    for brands in soup.find_all('div',attrs={'class':'section-body'}):
        for links in brands.find_all('li'):
            for urls in links.find_all('a'):
                str1="https://www.gsmarena.com/"+urls.get('href')
                print(str1)
                if('watch' not in str1):
                    #continue
                    list2.append(str1)
    for k in list2:
        r2=requests.get(k)
        soup1=BeautifulSoup(r2.content,'html5lib')
        try:
            phone_name.append(soup1.find('h1',attrs={'data-spec':'modelname'}).text)
        except Exception:
            phone_name='NA'
        try:
            phone_net.append(soup1.find('a',attrs={'data-spec':'nettech'}).text)
        except Exception:
            phone_net.append('NA')
        try:
            phone_dim.append(soup1.find('td',attrs={'data-spec':'dimensions'}).text)
        except Exception:
            phone_dim.append('NA')
        try:
            phone_sim.append(soup1.find('td',attrs={'data-spec':'sim'}).text)
        except Exception:
            phone_sim.append('NA')
        try:
            phone_dis.append(soup1.find('td',attrs={'data-spec':'displaytype'}).text)
        except Exception:
            phone_dis.append('NA')
        try:
            phone_dissize.append(soup1.find('td',attrs={'data-spec':'displaysize'}).text)
        except Exception:
            phone_dissize.append('NA')
        try:
            phone_os.append(soup1.find('td',attrs={'data-spec':'os'}).text)
        except Exception:
            phone_os.append('NA')
        try:
            phone_ram.append(soup1.find('td',attrs={'data-spec':'internalmemory'}).text)
        except Exception:
            phone_ram.append('NA')
        try:
            phone_cpu.append(soup1.find('td',attrs={'data-spec':'cpu'}).text)
        except Exception:
            phone_cpu.append('NA')
        try:
            phone_cam.append(soup1.find('td',attrs={'data-spec':'cam1modules'}).text)
        except Exception:
            phone_cam.append('NA')
        #print(phone_cam)
        count+=1

dict={'Model Name':phone_name,'Network type':phone_net,'Dimensions':phone_dim,'Sim':phone_sim,'Display type':phone_dis,'Display size':phone_dissize,'OS':phone_os,'RAM':phone_ram,'CPU':phone_cpu,'Main Camera':phone_cam}
df=pandas.DataFrame(dict)
df.to_csv('Mobiles_Dataset.csv')
