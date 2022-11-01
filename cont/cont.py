x = 1
def fazernum(num):
    vencedores = []
    list_num = [int(x) for x in str(num)]
    """
    pega a sequência de numeros iguais
    """
    cont = 1
    ultnum = None
    for n in list_num:
        if n == ultnum:
            cont += 1
        else:
            if ultnum is not None:
                vencedores.append((cont,ultnum))
            cont = 1
            ultnum = n
    vencedores.append((cont,ultnum))
    
    fin_num = ""
    for v in vencedores:
        fin_num = fin_num + str(v[0]) + str(v[1])
    return fin_num

for _ in range(50):
    x = fazernum(x)
print(len(x))