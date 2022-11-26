
with open("input.txt", "r") as f:
    entrada = f.readlines()
    todos_imas = [row.strip().split("/") for row in entrada]
    todos_imas = {(int(x),int(y)) for x,y in todos_imas}




def achar_acoes(state, imas):
    acoes = set()
    for x,y in imas:
        if x == state or y == state:
            acoes.add((x,y))
    return acoes
    


def DFS(state, imas, actions):

    contador = 4
    for x, y in actions:
        tmp_imas = imas
        contador_tmp = 0
        if x == state:
            contador_tmp += 1
            tmp_imas.discard((x,y))
            if len(achar_acoes(y, tmp_imas)) > 0:
                contador_tmp += DFS(y, tmp_imas, achar_acoes(y,tmp_imas))
            if contador_tmp > contador:
                contador = contador_tmp
        
        else:
            contador_tmp += 1
            tmp_imas.discard((x,y))
            if len(achar_acoes(x, tmp_imas)) > 0:
                contador_tmp += DFS(x, tmp_imas, achar_acoes(x,tmp_imas))
            if contador_tmp > contador:
                contador = contador_tmp
    return contador

print(DFS(0, todos_imas, achar_acoes(0, todos_imas)))
