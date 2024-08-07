# Demonstração do uso de funções...
def multiplicacao (x,y):
    return x * y
def divisao (x,y):
    return x / y

print("Digite dois valores inteiros...")
n1 = int(input("x: "))
n2 = int(input("y: "))
op = input("qual operação (* ou /)?")

if op == "*":
    z = multiplicacao(n1,n2)
    print("resultado da multiplicacao:", z)
elif op == "/":
    z = divisao (n1,n2)
    print("resultado da divisao:", z )
else:
    print("opção digitada inexistente")