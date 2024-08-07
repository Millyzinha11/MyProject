# Demonstração...
def menor():
    print("Eis, os programas ideias para você:")
    print("Teletubies, Tom & Jerri, Xou de Xuxa...")
    print("Se passar das 10h, vai dormir!!!")
    return
def maior():
    print("Eis, boas opções de carro para comprar:")
    print("Fiat 147, vw fusca, chevette...")
    print("Se beber, não dirija...")
    return

print("Digite a sua idade;")
idade = int(input())

    
if idade < 18:
    menor()
else:
    maior()