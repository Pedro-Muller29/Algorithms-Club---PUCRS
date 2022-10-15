"""
Trabalhando o input
"""

entrada = open("inputjorge.txt", "r")
linhas_tmp = [x.split(" (contains ") for x in entrada]
alergias = []
linhas = []
for row in linhas_tmp:
    tmp = (row[1].strip()[:-1])
    alergias.append(tmp.split(", "))
    linhas.append(row[0].split(" "))

"""
Criação do dicionário que dará as respostas através de intersecções de sets
"""

alergias_dict = {}
for a in alergias:
    for d in a:
        if d not in alergias_dict:
            alergias_dict[d] = 0

for i in range(len(alergias)):
    for alerg in alergias[i]:
        if alergias_dict[alerg] == 0:
            alergias_dict[alerg] = set(linhas[i])
        else:
            alergias_dict[alerg] = alergias_dict[alerg].intersection(set(linhas[i]))

for i in range(5):
    for ale in alergias_dict:
        if len(alergias_dict[ale]) == 1:
            for al in alergias_dict:
                if al != ale:
                    alergias_dict[al] = alergias_dict[al] - alergias_dict[ale]

"""
alergias_dict agora é o "gabarito" de qual coisa é oq
"""
#print(alergias_dict)

"""
Agora nos resta contar os pontos para a parte 1:
"""

itens_venenosos = []
for a in alergias_dict:
    for item in alergias_dict[a]:
        itens_venenosos.append(item)

contador = 0

for l in linhas:
    for item in l:
        if item not in itens_venenosos:
            contador += 1

print("PARTE 1:")
print(contador)
print("/////////////////////////////////////////////////////////////////////////////\nPARTE 2:")
print(alergias_dict)