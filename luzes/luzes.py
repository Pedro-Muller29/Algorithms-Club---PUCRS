entrada = open("inputee.txt", "r")
matriz = [[int(x) for x in row.strip()] for row in entrada]

def adj(y,x,coord):
    tmp = 1
    xis = [x-1, x, x+1]
    yps = [y-1, y, y+1]
    for f in yps:
        for t in xis:
            tmpc = (f,t)
            if tmpc == (y,x):
                continue
            try:
                if f >= 0 and t >= 0:
                    matriz[f][t] += 1
                    if matriz[f][t] == 10:
                        if tmpc not in coord:
                            tmp += adj(f,t,coord)
            except:
                None
    return tmp

def segundo():
    cont = 0
    coord = []
    for r in range(len(matriz)):
        for c in range(len(matriz[r])):
            matriz[r][c] += 1
            if matriz[r][c] == 10:
                coord.append((r,c))
    for par in coord:
        cont += adj(par[0], par[1],coord)
    for l in range(len(matriz)):
        for k in range(len(matriz[l])):
            if matriz[l][k] > 9:
                matriz[l][k] = 0
    return cont

def tempo(segundos):
    counter = 0
    for i in range(segundos):
        counter += segundo()
    return counter


i = 0
d = 0
cont = 0
while d != 1:
    d = 1
    i +=1 
    cont += tempo(1)
    if i == 100:
        print("PARTE 1:")
        print(cont)
    for p in matriz:
        for o in p:
            if o != 0:
                d = 0
print("////////////////////////")
print("PARTE 2:")
print(i)