
list = [l for l in range(20)]
data = [2,6,18,14]

def inverter_Sublist(idx, comp):
    global list
    sub_inicio = []
    sub_fim = []

    if idx+comp >= len(list):
        if comp >= len(list):
            idx_inicio = idx
            idx_fim = len(list)
        else:
            idx_inicio = (idx + comp) - len(list)
            idx_fim = len(list)
    else:
        idx_fim = idx+comp
        idx_inicio = 0

    sub_fim = list[idx:idx_fim]
    sub_inicio = list[0:idx_inicio]
    print(idx, list[idx])
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
    list = novo_subinicio + list[idx_inicio: idx]+ novo_subFim + list[idx_fim:]



idx = 0
salto = 0

for i in data:
    inverter_Sublist(idx, i)
    if i+salto == len(list):
        pass
    else:
        idx = (idx+i+salto) % len(list)
    salto += 1
    print("SALTO ", salto-1)
    print(list)
    print("///////////////////////////////////////////////////////////////////////////")

