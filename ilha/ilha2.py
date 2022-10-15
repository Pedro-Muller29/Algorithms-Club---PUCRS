import re

entrada = open("inpute.txt", "r")
tmp = [re.split(r'(\d+)', x) for x in entrada] 
comandos = [[x,int(y)] for x,y,z in tmp]

direcoes = ["E","N","W","S"]
direcaoatual = 0
loc = [10,1]
locn = [0,0]

for c in comandos:
    if c[0] == "F":
        print(loc)
        print(locn)
        print(c[1])
        locn[0] += (loc[0]) * c[1]
        locn[1] += (loc[1]) * c[1]
        print(loc)
        print(locn)
        print("------------------------------------------------")

    if c[0] == "N":
        loc[1] += c[1]
    elif c[0] == "S":
        loc[1] -= c[1]
    elif c[0] == "E":
        loc[0] += c[1]
    elif c[0] == "W":
        loc[0] -= c[1]
    elif c[0] == "R":
        direcaoatual = int((4-(c[1]/90))%4)
#Leste = [LW,NS] Norte = [-NS,LW] Oeste = [-LW,-NS] Sul = [NS, -LW]
    elif c[0] == "L":
        direcaoatual = int((c[1]/90)%4)

    if c[0] == "R" or c[0] == "L":
        loctmp = []
        loctmp.append(loc[0])
        loctmp.append(loc[1])
        print(direcaoatual)
        print(loc)
        
        if direcaoatual == 0:
            None
        elif direcaoatual == 1:
            loc[0] = -loctmp[1]
            loc[1] = loctmp[0]
        elif direcaoatual == 2:
            
            loc[0] = -loctmp[0]
            
            loc[1] = -loctmp[1]
            
        elif direcaoatual == 3:
            loc[0] = loctmp[1]
            loc[1] = - loctmp[0]
        direcaoatual = 0
        print(loc)
print(abs(locn[0])+abs(locn[1]))
