def passarsegundo(y):
    altura = 0
    max_altura = 0
    while True:
        altura += y
        if altura > max_altura:
            max_altura = altura
        y -=1
        if -267 <= altura <= -255:
            return max_altura
        elif altura < -267:
            return False


for i in range(268, 0, -1):
    tmp = passarsegundo(i)
    if tmp:
        print(tmp)
        break


        
    
        

