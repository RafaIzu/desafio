import sys
import os
sys.path.insert(0, './contador_de_notas.py')

from contador_de_notas import Contador_de_notas

flag1= True
while flag1 == True:
    flag2 = True
    while flag2 == True:
        try:
            valor = int(input('Digite um valor: '))
        except:
            raise ValueError('Valor incorreto!')
        else:
            flag2 = False

    print(Contador_de_notas(valor).mostrar_possibilidades())

    opcao = input('Deseja fazer mais alguma consulta?(s/n)')
    opcao = opcao.lower()
    if opcao != 's':
        flag1 = False
    else:
        os.system('cls')


