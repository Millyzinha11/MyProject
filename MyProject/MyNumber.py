#Demonstração do uso de estrutura repetitiva...
numero = 1
while numero >= 0 :
    print("digite um número negtivo para sair:")
    numero = int(input())
    continue 
    print ("este texto não será exibido! Mas...")
else:
    print("o número digitado foi:", numero)