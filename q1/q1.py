#!/usr/bin/python3
import random
from random import choice

f=open("dataset.txt","r")
data=f.readlines()
li=[]
for i in data:
    #print(i)
    li.append(i.split(':'))

bats={}
bowl={}
allr={}
wick={}
for i in li:
    if(i[2]=='Batsman'):
        bats[i[0]]=[i[1],i[2],i[3].rstrip('\n')]
    if(i[2]=='Bowler'):
        bowl[i[0]]=[i[1],i[2],i[3].rstrip('\n')]
    if(i[2]=='All-Rounder'):
        allr[i[0]]=[i[1],i[2],i[3].rstrip('\n')]
    if(i[2]=='Wicket Keeper'):
        wick[i[0]]=[i[1],i[2],i[3].rstrip('\n')]
    #print(i)

# print(bats)
# print(bowl)
# print(allr)
# print(wick)

f1=open("config.txt","r")
data1=f1.readlines()
li=[]
flag=0
teams={}
count1=0
count=0
for i in data1:
    #print(type(i))
    #print(i,"flag: ",flag)
    if(count1<5):
        li.append(i.split(':'))
    if(flag==1):
        teams[i.rstrip('\n')]=[0,0,0,0,0,0]
        count+=1
    if(i[5:7]=="na"):
        count=0
        flag=1
    count1=count1+1
#print(teams)
#print(li)
constraints={}
for i in li:
    constraints[i[0]]=[int(i[1]),int(i[2].rstrip('\n'))]

#print(constraints)


c=0
f2=[]
for i in teams:
    str1=i+".txt"
    f2.append(open(str1,"w"))
    c=c+1

c=0
for i in teams:
    str1=i+".txt"
    f2[c].close()
    c=c+1

c=0
f1=[]
for i in teams:
    str1=i+".txt"
    f1.append(open(str1,"a+"))
    c=c+1

selected={}
c=0
count=1
for t,v in teams.items():
    f1[c].write('Team: '+t+'\n\n')
    randconst=int(constraints['overseas'][1])
    print(randconst)
    while(v[5]<randconst):
        for loop in range(0,10):
            batlist=[]
            batlist.append(random.choice(list(bats.items())))
            # print(batlist)
            if(batlist[0][1][0]!='India' and batlist[0][0] not in selected and v[5]<randconst):
                print(batlist[0][1])
                f1[c].write('Player'+str(v[5]+1)+'\n')
                f1[c].write('Name: '+batlist[0][0]+'\n')
                f1[c].write('Country: '+batlist[0][1][0]+'\n')
                f1[c].write('Ability: Batsman'+'\n')
                f1[c].write('Fees: '+batlist[0][1][2]+'\n\n')
                #count+=1
                selected[batlist[0][0]]=True
                v[0]+=1
                v[4]+=1
                v[5]+=1
                break
        
        for loop in range(0,10):
            batlist=[]
            batlist.append(random.choice(list(bowl.items())))
            #print(batlist)
            if(batlist[0][1][0]!='India' and batlist[0][0] not in selected and v[5]<randconst):
                print(batlist[0][1])
                f1[c].write('Player'+str(v[5]+1)+'\n')
                f1[c].write('Name: '+batlist[0][0]+'\n')
                f1[c].write('Country: '+batlist[0][1][0]+'\n')
                f1[c].write('Ability: Bowler'+'\n')
                f1[c].write('Fees: '+batlist[0][1][2]+'\n\n')
                #count+=1
                selected[batlist[0][0]]=True
                v[1]+=1
                v[4]+=1
                v[5]+=1
                break
        
        for loop in range(0,10):
            batlist=[]
            batlist.append(random.choice(list(allr.items())))
            #print(batlist)
            if(batlist[0][1][0]!='India' and batlist[0][0] not in selected and v[5]<randconst):
                print(batlist[0][1])
                f1[c].write('Player'+str(v[5]+1)+'\n')
                f1[c].write('Name: '+batlist[0][0]+'\n')
                f1[c].write('Country: '+batlist[0][1][0]+'\n')
                f1[c].write('Ability: All-Rounder'+'\n')
                f1[c].write('Fees: '+batlist[0][1][2]+'\n\n')
                #count+=1
                selected[batlist[0][0]]=True
                v[2]+=1
                v[4]+=1
                v[5]+=1
                break

        for loop in range(0,10):
            batlist=[]
            batlist.append(random.choice(list(wick.items())))
            #print(batlist)
            if(batlist[0][1][0]!='India' and batlist[0][0] not in selected and v[5]<randconst):
                print(batlist[0][1])
                f1[c].write('Player'+str(v[5]+1)+'\n')
                f1[c].write('Name: '+batlist[0][0]+'\n')
                f1[c].write('Country: '+batlist[0][1][0]+'\n')
                f1[c].write('Ability: Wicket Keeper'+'\n')
                f1[c].write('Fees: '+batlist[0][1][2]+'\n\n')
                #count+=1
                selected[batlist[0][0]]=True
                v[3]+=1
                v[4]+=1
                v[5]+=1
                break
        
        #count+=1

    c+=1

c=0
for t,v in teams.items():
    #print(v)
    #print(type(constraints['overseas'][0]))
    count=1
    print(randconst)
    while(v[5]<18):
        for loop in range(0,10):
            batlist=[]
            batlist.append(random.choice(list(bats.items())))
            # print(batlist)
            if(batlist[0][1][0]=='India' and v[0]<int(constraints['batsmen'][1]) and v[0]<int(constraints['batsmen'][1]) and batlist[0][0] not in selected and v[5]<18):
                print(batlist[0][1])
                f1[c].write('Player'+str(v[5]+1)+'\n')
                f1[c].write('Name: '+batlist[0][0]+'\n')
                f1[c].write('Country: '+batlist[0][1][0]+'\n')
                f1[c].write('Ability: Batsman'+'\n')
                f1[c].write('Fees: '+batlist[0][1][2]+'\n\n')
                count+=1
                selected[batlist[0][0]]=True
                v[0]+=1
                v[5]+=1
                break
        
        for loop in range(0,10):
            batlist=[]
            batlist.append(random.choice(list(bowl.items())))
            #print(batlist)
            if(batlist[0][1][0]=='India' and v[1]<int(constraints['bowlers'][1]) and v[1]<int(constraints['bowlers'][1]) and batlist[0][0] not in selected and v[5]<18):
                print(batlist[0][1])
                f1[c].write('Player'+str(v[5]+1)+'\n')
                f1[c].write('Name: '+batlist[0][0]+'\n')
                f1[c].write('Country: '+batlist[0][1][0]+'\n')
                f1[c].write('Ability: Bowler'+'\n')
                f1[c].write('Fees: '+batlist[0][1][2]+'\n\n')
                count+=1
                selected[batlist[0][0]]=True
                v[1]+=1
                v[5]+=1
                break
        
        for loop in range(0,10):
            batlist=[]
            batlist.append(random.choice(list(allr.items())))
            #print(batlist)
            if(batlist[0][1][0]=='India' and v[2]<int(constraints['allrounders'][1]) and v[2]<int(constraints['allrounders'][1]) and batlist[0][0] not in selected and v[5]<18):
                print(batlist[0][1])
                print("constraints['allrounders'][1]: ",constraints['allrounders'][1])
                f1[c].write('Player'+str(v[5]+1)+'\n')
                f1[c].write('Name: '+batlist[0][0]+'\n')
                f1[c].write('Country: '+batlist[0][1][0]+'\n')
                f1[c].write('Ability: All-Rounder'+'\n')
                f1[c].write('Fees: '+batlist[0][1][2]+'\n\n')
                count+=1
                selected[batlist[0][0]]=True
                v[2]+=1
                v[5]+=1
                break

        for loop in range(0,10):
            batlist=[]
            batlist.append(random.choice(list(wick.items())))
            #print(batlist)
            if(batlist[0][1][0]=='India' and v[3]<int(constraints['wicketkeepers'][1]) and v[3]<int(constraints['wicketkeepers'][1]) and batlist[0][0] not in selected and v[5]<18):
                print(batlist[0][1])
                f1[c].write('Player'+str(v[5]+1)+'\n')
                f1[c].write('Name: '+batlist[0][0]+'\n')
                f1[c].write('Country: '+batlist[0][1][0]+'\n')
                f1[c].write('Ability: Wicket Keeper'+'\n')
                f1[c].write('Fees: '+batlist[0][1][2]+'\n\n')
                count+=1
                selected[batlist[0][0]]=True
                v[3]+=1
                v[5]+=1
                break
        
        #count+=1

    c+=1



print(teams)
print(constraints)
