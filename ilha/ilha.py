import re

entrada = open("inpute.txt", "r")
tmp = [re.split(r'(\d+)', x) for x in entrada] 
comandos = [[x,int(y)] for x,y,z in tmp]


direcoes = ["E","N","W","S"]
direcaoatual = 0
loc = [0,0]


for c in comandos:
    if c[0] == "F":
        c[0] = direcoes[(direcaoatual)]
    if c[0] == "N":
        loc[1] += c[1]
    elif c[0] == "S":
        loc[1] -= c[1]
    elif c[0] == "E":
        loc[0] += c[1]
    elif c[0] == "W":
        loc[0] -= c[1]
    elif c[0] == "R":
        direcaoatual = int((direcaoatual+4-(c[1]/90))%4)
    elif c[0] == "L":
        direcaoatual = int((direcaoatual+(c[1]/90))%4)
print(loc)

