# Construa um programa onde o usuário irá digitar 3 números distintos, que por sua vez serão armazenados nas varíaveis "X", "Y" e "Z". 
# A partir daí, o programa informe se estes números estão em ordem crescente ou decrescente. 
# Se não, exibir "Eles estão misturados!"

X = float(input("Digite o primeiro número (X): "))
Y = float(input("Digite o segundo número (Y): "))
Z = float(input("Digite o terceiro número (Z): "))

if X < Y < Z:
    print("Os números estão em ordem crescente!")
elif X > Y > Z:
   print("Os números estão em ordem decrescente!")
else:
   print("Os números estão misturados!")