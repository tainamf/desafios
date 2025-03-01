from random import randint  

sort = randint(1, 20)  #randit: sortear de 1 a 20
vidas = 5

while True:
    palpite = int(input('DIGITE UM NÚMERO DE 1 A 20: '))

    if palpite == sort:
        print('VOCÊ GANHOU!!!')
        break

    elif palpite < sort:
        print('TENTE NOVAMENTE! (DICA: O NÚMERO É MAIOR)')

    elif palpite > sort:
        print('TENTE NOVAMENTE! (DICA: O NÚMERO É MENOR)')

    vidas -= 1

    if vidas == 0:
        print('VOCÊ PERDEU KKKKKKKKKKKKKKKK')
        break