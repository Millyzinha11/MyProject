# Revisão geral de algoritmos & lógica de programação...
print("Digite o seu nome:")
nome = input()
idade = int(input("Digite a idade:"))
altura = float(input("Digite a altura:"))

idade=input("Digite a idade:")
altura=input("Digite a altura:")

print(f"Meu nome é {nome},")
print(f"A minha idade é {idade},")
print(f"e a minha altura é {altura}")

print("Qual será a minha idade em 2036?")
tempo = 2036 - 2024
idade = idade + tempo
altura = altura / 2
print("A minha idade em 2036 será:", idade)
print("A minha altura em 2036 será:", altura)

print(type(nome))
print(type(idade))
print(type(altura))