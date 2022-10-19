with open('input.txt') as f:
    data = [[int(y) for y in x.split(",")] for x in f.readlines()]

data = data[0]


lista = [x for x in range(256)]


def inverter_Sublista(idx, comp):
    global lista
    sub_inicio = []
    sub_fim = []

    if idx+comp >= len(lista):
        if comp >= len(lista):
            idx_inicio = idx
            idx_fim = len(lista)
        else:
            idx_inicio = (idx + comp) % len(lista)
            idx_fim = len(lista)
    else:
        idx_fim = idx+comp
        idx_inicio = 0

    sub_fim = lista[idx:idx_fim]
    sub_inicio = lista[0:idx_inicio]
    print(idx, lista[idx])
    print("SUBFIM")
    print(sub_fim)
    print("SUBINICIO")
    print(sub_inicio)
    
    aux = sub_fim + sub_inicio
    aux.reverse()
    print('AUX: ',aux)
    novo_subFim = aux[:len(sub_fim)]
    novo_subinicio = aux[len(sub_fim):]
    print("NOVO SUBINICIO\n", novo_subinicio)
    print(novo_subFim)
    lista = novo_subinicio + lista[idx_inicio: idx]+ novo_subFim + lista[idx_fim:]
        

idx = 0
salto = 0

for i in data:
    inverter_Sublista(idx, i)
    if i+salto == len(lista):
        pass
    else:
        idx = (idx+i+salto) % len(lista)
    print(salto, i)
    salto += 1
    
print("////////////////////////////////")   
print(lista[0]*lista[1])

