chave = "amgozmfv"
chaves = []
for i in range(128):
    chaves.append(chave + "-" + str(i))
lista = []
def acahrhex(f):
    data = [int(ord(y)) for y in f]
    data = data + [17, 31, 73, 47, 23]

    global lista
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
        
        aux = sub_fim + sub_inicio
        aux.reverse()
        novo_subFim = aux[:len(sub_fim)]
        novo_subinicio = aux[len(sub_fim):]
        lista = novo_subinicio + lista[idx_inicio: idx]+ novo_subFim + lista[idx_fim:]
            
    idx = 0
    salto = 0
    for l in range(64):
        for i in data:
            inverter_Sublista(idx, i)
            if i+salto == len(lista):
                pass
            else:
                idx = (idx+i+salto) % len(lista)
            salto += 1

    def xor(listaa):
        tmp = 0
        for i in listaa:
            tmp = tmp ^ i
        return tmp
    hash = []
    for t in range(16):
        hash.append(xor(lista[t*16:(t+1)*16]))

    resposta = ""
    for ha in hash:
        if ha < 16:
            tmpha = "0" + hex(ha)[2:]
        else:
            tmpha = hex(ha)[2:]
        resposta = resposta + tmpha
    return resposta

def hexbin(hexx):
    binv = ""
    for h in hexx:
        binv = binv + bin(int(h,16))[2:].zfill(4)
    return binv

cont = 0
HDantigo = []
for c in chaves:
    tmp = (hexbin(acahrhex(c)))
    HDantigo.append(tmp)
    for t in tmp:
        if t == "1":
            cont += 1


def checaradj(tuplaidx):
    HD[tuplaidx[0]][tuplaidx[1]] = 0
    idx_checar = []
    if tuplaidx[0] > 0:
        idx_checar.append((tuplaidx[0]-1,tuplaidx[1]))
    if tuplaidx[0] < len(HD)-1:
        idx_checar.append((tuplaidx[0]+1,tuplaidx[1]))
    if tuplaidx[1] < len(HD[tuplaidx[0]])-1:
        idx_checar.append((tuplaidx[0],tuplaidx[1]+1))
    if tuplaidx[1] > 0:
        idx_checar.append((tuplaidx[0],tuplaidx[1]-1))
    for i in idx_checar:
        if HD[i[0]][i[1]] == 1:
            checaradj(i)

HD = [[int(l) for l in d] for d in HDantigo]
contnovo = 0
for y in range(len(HD)):
    for x in range(len(HD[y])):
        if HD[y][x] == 1:
            checaradj((y,x))
            contnovo += 1
print(contnovo)


1,2,3,4,5,6,7,8

