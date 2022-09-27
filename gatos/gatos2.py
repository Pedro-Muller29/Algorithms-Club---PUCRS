entrada = open("gatosinput.txt", "r")
x = 0
baralho1 = []
baralho2 = []
for row in entrada:
    if row == "\n":
        x=1
    if x == 0:
        try:
            baralho1.append(int(row))
        except:
            continue
    if x == 1:
        try:
            baralho2.append(int(row))
        except:
            continue

def jogo(bar1,bar2):
    jogospassados = []
    while len(bar1) != 0 and len(bar2) != 0:
        if (tuple(bar1),tuple(bar2)) in jogospassados:
            return 1
        tmp = (tuple(bar1),tuple(bar2))
        jogospassados.append(tmp)
        if bar1[0] < len(bar1) and bar2[0] < len(bar2):
            minibar1 = bar1[1:bar1[0]+1]
            minibar2 = bar2[1:bar2[0]+1]  
            winner = jogo(minibar1,minibar2)
        elif bar1[0] > bar2[0]:
            winner = 1
        else:      
            winner = 2
        if winner == 1:
            bar1.append(bar1[0])
            bar1.append(bar2[0])
            bar1.pop(0)
            bar2.pop(0)
        else:
            bar2.append(bar2[0])
            bar2.append(bar1[0])
            bar2.pop(0)
            bar1.pop(0)
    if len(bar1) == 0:
        return 2
    else:
        return 1
jogo(baralho1,baralho2)
contador = 50
somatorio = 0
for carta in baralho2:
    somatorio += contador * carta
    contador -= 1
print(somatorio)
