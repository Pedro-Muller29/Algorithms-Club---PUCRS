with open('input.txt') as f:
    data = [[int(y) for y in x.split(",")] for x in f.readlines()]

data = data[0]
print(data)

lista = [x for x in range(5)]

def inverter_Sublista(idx, comp):
    global lista
    sub_inicio = []
    sub_fim = []

    if idx+comp >= len(lista):
        idx_inicio = (idx + comp + 1) % len(lista)
        idx_fim = len(lista)
    else:
        idx_fim = idx+comp
        idx_inicio = 0

    sub_fim = lista [idx:idx_fim]
    sub_inicio = lista[0:idx_inicio]

    aux = sub_fim + sub_inicio
    aux.reverse()
    novo_subFim = aux[:len(lista) - idx]
    novo_subinicio = aux[len(lista) - idx:]
    lista = novo_subinicio + lista[idx_inicio: idx]+ novo_subFim + lista[idx_fim:]
            

idx = 0

for i in data:
    salto = 0
    inverter_Sublista(idx, i)
    idx = (idx+i+salto) % len(lista)
    salto += 1
    print(lista,'idx ',idx)
# print(lista[0], lista[1])

    