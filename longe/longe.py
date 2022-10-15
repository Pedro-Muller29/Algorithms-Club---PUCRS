entrada = open("inputlonge.txt", "r")
coordenadas1 = [[int(z.strip()) for z in x.strip().split(",")] for x in entrada]
coordenadas = [(x,y) for x,y in coordenadas1]


maiory = 0
menory = 300
maiorx = 0
menorx = 300
for y,x in coordenadas:
    if y > maiory:
        maiory = y
    if y < menory:
        menory = y
    if x > maiorx:
        maiorx = x
    if x < menorx:
        menorx = x
maiory += 1
menory -= 1
maiorx += 1
menorx -=1

#Função que calcula a menor distância de manhattan:
def manhattan(posi,coord):
    ans = [(),()]
    tmp = 1000
    for y,x in coord:
        if abs(y-posi[0]) + abs(x - posi[1]) < tmp:
            ans = [posi,(y,x)]
            tmp = abs(y-posi[0]) + abs(x - posi[1])
        elif abs(y-posi[0]) + abs(x - posi[1]) == tmp:
            ans = [posi,(0,0)]
    return ans

"""
A ideia seria criar uma lista de listas de tamanho 2 com posição 0 = (y,x) e posição 1 = (estrela com menor distancia de manhattan)
"""

a = menory
estrelas = []
bordas = []
while a <= maiory:
    b = menorx
    while b <= maiorx:
        tmp_cord = manhattan((a,b),coordenadas)
        estrelas.append(tmp_cord)
        if b == menorx or b == maiorx or a==maiory or a==menory:
            if tmp_cord[1] not in bordas:
                bordas.append(tmp_cord[1])
        b += 1
    a += 1

"""
Agora criamos uma lista para contar quantas estrelas pertencem a cada sol
"""
for b in bordas:
    if b == (0,0):
        continue
    coordenadas.remove(b)
pontuacao = [[x,0] for x in coordenadas]

"""
E por fim fazemos a contagem
"""

maiorcoord = (0,0)
maior = 0
for p in pontuacao:
    for star in estrelas:
        if star[1] == p[0]:
            p[1] += 1
    tmp = p[1]
    if tmp > maior:
        maior = tmp
        maiorcoord = p[0]

print(maior)
