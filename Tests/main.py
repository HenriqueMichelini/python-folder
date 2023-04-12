import numpy as np

##  PEGAR NUMERO DE LETRAS NA PALAVRA, DEFINIR A COMPLEXIDADE (QUE SERÁ DOIS POR EXEMPLO).

print("Escreva a palavra que desejar:")
palavra = str(input())

print("Defina o nível de complexidade (>1):")
complexidade = int(input())

quantidade_caracteres = len(palavra)
matriz_cifrada = np.zeros((quantidade_caracteres, complexidade), dtype='U1')
aux = 0
limite = False

##  CRIPTOGRAFANDO

for i in range(0, quantidade_caracteres):
    matriz_cifrada[i][aux] = palavra[i]
    if(limite == False):
        if(aux <= complexidade):
            aux = aux + 1
        if(aux >= 0):
            aux = aux - 1
        if(aux == complexidade):
            limite = True
        if(aux == 0):
            limite = False

## IMPRIMINDO MATRIZ DA CIFRA

for i in range(0, quantidade_caracteres):
    for j in range(0, complexidade):
        print(matriz_cifrada[i][j])

##  TRANSFORMANDO A MATRIZ EM VETOR

vetor_cifrado = np.zeros(quantidade_caracteres, dtype='U1')
for i in range(0, quantidade_caracteres):
    if(matriz_cifrada[i][j] == ''):
        vetor_cifrado[quantidade_caracteres] = matriz_cifrada[i][j]
    if(limite == False):
        if(aux <= complexidade):
            aux = aux + 1
        if(aux >= 0):
            aux = aux - 1
        if(aux == complexidade):
            limite = True
        if(aux == 0):
            limite = False

## IMPRIMINDO VETOR DA CIFRA

for i in range(0, quantidade_caracteres):
    print(vetor_cifrado[i])

print("FIM")