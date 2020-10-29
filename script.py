from time import sleep as delay

i = 1
while 1:
    delay(0.2)
    
    print(f'\rLoading' + '.' * i + '   ', end='')
    i = i + 1 if i < 3 else 1



