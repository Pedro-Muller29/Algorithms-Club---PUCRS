def check_landing(x,y):
    distancia = 0
    altura = 0
    while True:
        distancia += x
        altura += y
        if x > 0:  
            x -= 1
        y -= 1
        if 50 >= distancia >= 14:
            if -225 >= altura >= -267:
                return True
        if altura < -267 or distancia > 50:
            return False

contador = 0
for i in range(51):
    for j in range(-267, 268):
        if check_landing(i,j):
            contador += 1

print(contador)