f = open("fvttcopy.txt","r")
import  csv
import itertools
import sys
import re
from collections import defaultdict

out = open('output.csv','w') 
out = csv.writer(out, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
a = f.read()
b = a.split('---------------------------')
#print(len(b))
totalrolls = len(b)
# PC Entry Orders
# 1 Initiative
# 2 General Attack Rolls
# 3 Strength Saving Throw
# 4 Dex Save
# 5 Con Save 
# 6 Int Save
# 7 Wisdom Save
# 8 Charisma Save
#XDDDD
# 8 Acrobatics
# 9 Animal Handling
# 10 Arcana
# 11 Athletics
# 12 Deception
# 13 History
# 14 Insight
# 15 Intimidation
# 16 Investigation
# 17 Medicine
# 18 Nature
# 19 Perception
# 20 Performance
# 21 Persuasion
# 22 Religion
# 23 Sleight of Hand
# 24 Stealth
# 25 - > Different Weapon Stats
# Different Spells attacks with stats on spells

### MONSTER ENTRIES
# 1 Iniative
# 2 Attacks
# 3 Saving Throws 
# 4 Spells with stats

RollData = {
       
}
Abilities = ['Acrobatics',"Animal Handling",'Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuasion','Religion',"Sleight of Hand",'Stealth']
PCList = ["Zoz","Tilikuss","Mikael","Malus","Alchemical"] 
BadBoyList = ['Jack','Josh','Will','Zev','Gamemaster']
XD = ['Average Attack Roll','Initiative','Strength Saving Throw','Dexterity Saving Throw','Constitution Saving Throw','Intelligence Saving Throw','Wisdom Saving Throw','Charisma Saving Throw']

BIGLIST = Abilities + XD
#print(b[0])

#print(type(b[100]))
#ABILITY CHECK CASE
#b[0] = Date 
#b[1] = Time
#b[2] = AM/PM worthless
#b[3] = Character First Name 
#b[4] = Character Last Name
#b[5] = Ability Check(Perception) could be others
#b[6] = Roll 1 d20 for example
#b[7] = Formula (+) 
#b[8] = For ability check its modifier (+1)
#b[9] = Formula for Roll 1 d 20 for example
#b[10] = ACTUAL ROLL , in case 0 is 9 
#b[11] = ACTUAL ROLL AGAIN 
#b[12] = ADVANTEDGE ROLL FORMULA
#b[13] = ADVANTEDGE ROLL 
#b[14] = ADVANTEDCGE ROLL AGAIN
#b[15] = read as 109 means final roll 10 , natural roll 9 
def handleAbilityCheck(rolltype):
    name = rolltype[3]
    skill = rolltype[5]
    roll = rolltype[10]
    if '1d20' in roll:
        #print("CASE")
        roll = rolltype[11]
    #print(rolltype[5])
    #print(RollData.get('Zoz'))
    #print(RollData.get('Zoz').get('Stealth'))
    #print(type(RollData.get('Zoz').get('Stealth')))
    #RollData.get(rolltype[3]).get(rolltype[5][0]) += 1
    #print(RollData.get(rolltype[3]).get(rolltype[5]))

    #print(type(RollData.get(rolltype[3]).get(rolltype[5][0])))
    #print(RollData.get(rolltype[3]).get(rolltype[5][0]))
    #a = int(RollData.get(rolltype[3]).get(rolltype[5])[0])
    #b = int(RollData.get(rolltype[3]).get(rolltype[5])[1])
    #print(a)
    #print(b)
    if name in PCList:

        (RollData.get(name).get(skill)[0])+=1
        (RollData.get(name).get(skill)[1])+=int(roll)
    else:
        RollData.get(name).get('Skills')[0]+=1
        RollData.get(name).get('Skills')[1]+=int(roll)
    #print(a)
    #print(RollData.get(name).get(skill)[1])
def handleAttackRoll(roll):
    if('Alchemical' in roll): #DEBUG
        print(roll)
    d = roll.split()           
    name = d[3]
    weapon = d[5]
    try: # FIX THIS SHIT , IDK IM REALLY TIRED BUT I THINK its better to check legnth then disregard idk
        ind = [i for i,n in enumerate(d) if n == '1d20'][1] #second occurence of 1 d20 
        attackroll = d[ind+1]
        if name in PCList:
            RollData.get(name).get('Average Attack Roll')[0]+=1
            RollData.get(name).get('Average Attack Roll')[1]+=int(attackroll)
            if weapon not in RollData.get(name).keys():
                RollData.get(name).update({weapon :[1,int(attackroll)]})
            else:
                RollData.get(name).get(weapon)[0]+=1
                RollData.get(name).get(weapon)[1]+=int(attackroll)
    except
    else:
        RollData.get(name).get('Average Attack Roll')[0]+=1
        RollData.get(name).get('Average Attack Roll')[1]+=int(attackroll)
    except IndexError:

    
    #print(b)
    #print(d[b+1])
    #print(d[3])
def determineRollType(roll):
    d = roll.split()
    if('Alchemical' in roll): #DEBUG
        print(roll)
    #print(d[6])
    if d[3] in PCList and d[3] not in RollData:
        RollData.update({d[3]: { 'Initiative' : [0,0],'Average Attack Roll': [0,0],'Strength Saving Throw':[0,0],'Dexterity Saving Throw':[0,0],'Constitution Saving Throw':[0,0],'Intelligence Saving Throw':[0,0],'Wisdom Saving Throw':[0,0],'Charisma Saving Throw':[0,0],'Acrobatics':[0,0],'Animal Handling':[0,0],'Arcana':[0,0],'Athletics':[0,0],'Deception':[0,0],'History':[0,0],'Insight':[0,0],'Intimidation':[0,0],'Investigation':[0,0],'Medicine':[0,0],'Nature':[0,0],'Perception':[0,0],'Performance':[0,0],'Persuasion':[0,0],'Religion':[0,0],'Sleight of Hand':[0,0],'Stealth':[0,0] } })  
    if d[3] not in PCList and d[3] not in RollData:
        RollData.update({d[3]: { 'Initiative' : [0,0],'Average Attack Roll':[0,0],'Saving Throws':[0,0],'Skills':[0,0]}})
    if d[5] in Abilities:
        #print("IN Abilities")
        handleAbilityCheck(d)
        #print(d[3]+" " + d[4])
    if 'Attack' in roll:
        #print("attack")
        handleAttackRoll(roll)
    #if d[3]+" " + d[4] not in PCList: DEBUG EXAMPLE
        #print(d[3]+" "+d[4])
    #if d[3] in PCList:


if __name__ == '__main__':
    for i in range(0,55):
        #print(len(b[30].split()))
        #print((b[30].split()))
        #print(b[52].split())
        if len(b[i].split()) < 7 or b[i].split()[3] in BadBoyList or '/roll' in b[i]:
            continue
        
        print(i)
        determineRollType(b[i])
        #print(RollData)
    #print(len(b[1325].split()))
    #print(RollData)
    
    

