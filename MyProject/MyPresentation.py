# Demonstração do uso de funções...
def apresentar():
    print("Meu nome é", MyName, ".")
    print("Minha altura é de", MyHeigh, "metros")
    print("Minha idade é", Myage, "anos.")
    return
def conferir(x):
    if x >= 18:
        print("Você é maior de idade")
    else:
        print("Ops, menor de idade não pode!")
    return

MyName = str(input("Digite o seu nome: "))
MyHeigh = float(input("Digite a sua altura: "))
Myage = int(input("Digite a sua idade: "))

apresentar()
conferir(Myage)