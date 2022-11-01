x = 1321131112
def fazernum(num):
    """
    pega a sequência de numeros iguais
    """
    tmp = ""
    cont = 1
    ultnum = None
    for n in str(num):
        if n == ultnum:
            cont += 1
        else:
            if ultnum is not None:
                tmp += str(cont) + ultnum
            cont = 1
            ultnum = n
    fin_num = tmp + str(cont) + ultnum
    return fin_num

for i in range(50):
    x = fazernum(x)
    print(i)
    
print(len(x))