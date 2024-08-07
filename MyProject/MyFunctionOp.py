# Demonstração do uso de funções...
def adicao(x,y):
    return x + y
def subtracao (x,y):
    return x - y

print("Digite dois valores inteiros...")
n1 = int(input("x: "))
n2 = int(input("y: "))
op = input("qual operação (+ ou -)?")

if op == "+":
    z = adicao(n1,n2)
    print("resultado da soma:", z)
elif op == "-":
    z = subtracao (n1,n2)
    print("resultado da subtração:", z )
else:
    print("opção digitada inexistente")