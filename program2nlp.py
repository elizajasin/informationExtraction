__author__ = 'elizajasin'

import re
import os
from pip._vendor.distlib.compat import raw_input

print("Statistik Pertandingan Chelsea vs Burnley")
print("-----------------------------------------")
ans=True
while ans:
    os.system('cls')
    print ("""
    1.Statistik Free Kick
    2.Statistik Yellow Card
    3.Exit/Quit
    """)
    ans = raw_input("Masukan Pilihan : ")
    if ans=="1":
        # Free Kick
        frekiChel = 0
        frekiBurn = 0
        with open('ChelseavsBurnley.txt','r') as ins:
            for line in ins:
                freki = re.search(r'([\d].+\')free kick[,!\w\s]+.([A-Z][\w\s]+) \(([\w]+)\)', line)
                if freki:
                    re.match(r'([\d].+\')free kick[,!\w\s]+.([A-Z][\w\s]+) \(([\w]+)\)', line)
                    print("Menit ke "+freki.groups()[0]+" oleh "+freki.groups()[1]+" dari tim "+freki.groups()[2])
                    if freki.groups()[2] == 'Chelsea':
                        frekiChel += 1
                    elif freki.groups()[2] == 'Burnley':
                        frekiBurn += 1
        print("Total Free Kick Chelsea : "+str(frekiChel))
        print("Total Free Kick Burnley : "+str(frekiBurn))
    elif ans=="2":
        # Yellow Cards
        yellChel = 0
        yellBurn = 0
        with open('ChelseavsBurnley.txt','r') as ins:
            for line in ins:
                yellow = re.search(r'([\d].+\')yellow[,!\w\s]+.([A-Z][\w\s]+) \(([\w]+)\)', line)
                if yellow:
                    re.match(r'([\d].+\')free kick[,!\w\s]+.([A-Z][\w\s]+) \(([\w]+)\)', line)
                    print("Menit ke "+yellow.groups()[0]+", "+yellow.groups()[1]+" dari tim "+yellow.groups()[2]+" mendapatkan yellow card")
                    if yellow.groups()[2] == 'Chelsea':
                        yellChel += 1
                    elif yellow.groups()[2] == 'Burnley':
                        yellBurn += 1
        print("Total Yellow Card Chelsea : "+str(yellChel))
        print("Total Yellow Card Burnley : "+str(yellBurn))
    elif ans=="3":
      quit()
    elif ans !="":
      print("\n Not Valid Choice Try again")