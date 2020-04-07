import requests
from bs4 import BeautifulSoup
import time
from playsound import playsound
import os.path
import random
while True:
    url ="https://www.espncricinfo.com/series/19312/game/1187014/india-vs-bangladesh-2nd-t20i-bangladesh-in-india-2019-20"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    divi = soup.findAll('div',{'class':'recent-overs-wrapper'})
    # print(len(divi))
    totaldata=divi[0]
    # print(divi.text)
    totalovers = totaldata.text
    print(totalovers)
    overs = []
    overs = totalovers.split('|')
    #sz = len(overs)
    for i in overs:
        print(i)
    l_s = overs[0][6]
    print("this is latest score",l_s)
    #ans = imp[6]
    #print("this is score",ans)
    random_file = random.choice([1, 2, 3])
    print("random number is " ,random_file)
    #time.sleep(10)
    if l_s =="4":
        if(random_file == 1):
            music_path = os.path.abspath('four1.mp3')
            playsound(music_path)
        if(random_file == 2):
            music_path = os.path.abspath('four2.mp3')
            playsound(music_path)
        if(random_file == 3):
            music_path = os.path.abspath('four3.mp3')
            playsound(music_path)
    elif l_s == "6":
        if(random_file == 1):
            music_path = os.path.abspath('six1.mp3')
            playsound(music_path)
        if(random_file == 2):
            music_path = os.path.abspath('six2.mp3')
            playsound(music_path)
        if(random_file == 3):
            music_path = os.path.abspath('six3.mp3')
            playsound(music_path)
    elif l_s == "W":
       if(random_file == 1):
           music_path = os.path.abspath('wicket1.mp3')
           playsound(music_path)
       if(random_file == 2):
           music_path = os.path.abspath('wicket2.mp3')
           playsound(music_path)
       if(random_file == 3):
           music_path = os.path.abspath('wicket3.mp3')
           playsound(music_path)
    time.sleep(10)
