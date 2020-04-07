#!/usr/bin/python3
import os
import time
import sys
import requests, json 

key="2e5cec2f5be67181fbc5c833498bbbb5"
city=input("Enter the name of the city: ")

URL="http://api.openweathermap.org/data/2.5/weather?appid="+key+"&q="+city
response=requests.get(URL)
r=response.json()

if(r['cod']=='404'):
    print("City not found")
    sys.exit()

wallpapers=['ash','clear','clouds','drizzle','dust','fog','haze','mist','rain','sand','smoke','snow','squall','thunderstorm','tornado']
weather=r["weather"]
weather1=weather[0]["description"]
print(weather1)
flag=0
space=0
li=[]
li=weather1.split(' ')
for walls in wallpapers:
    for i in li:
        if(i==walls):
            weather1=i
            flag=1
            break
    if(flag==1):
        break

if(flag==0):
    weather1='clear'
weather1='snow'
print(weather1)

y,m,d,h,mm=map(int,time.strftime("%Y %m %d %H %M").split())
print(y,m,d,h,mm)
if(h>=0 and h<=12):
    str1='gsettings set org.gnome.desktop.background picture-uri file:///home/sagnik/vscode/weather_wallpapers/'+weather1.capitalize()+'.jpg'
else:
    str1='gsettings set org.gnome.desktop.background picture-uri file:///home/sagnik/vscode/weather_wallpapers/'+weather1.capitalize()+'-night.jpg'
    os.system(str1)
