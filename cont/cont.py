x = 1321131112
def fazernum(num):
    list_num = [int(x) for x in str(num)]
    """
    pega a sequência de numeros iguais
    """
    fin_num = ""
    cont = 1
    ultnum = None
    for n in list_num:
        if n == ultnum:
            cont += 1
        else:
            if ultnum is not None:
                fin_num = fin_num + str(cont) + str(ultnum)
            cont = 1
            ultnum = n
    fin_num = fin_num + str(cont) + str(ultnum)
    return fin_num

for i in range(50):
    x = fazernum(x)
    print(i)
    
print(len(x))