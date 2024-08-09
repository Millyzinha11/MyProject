# Revisão geral de algoritmos & lógica de programação...
nome = input()
idade = int(input("Digite a idade:"))
altura = float(input("Digite a altura:"))

print(f"Meu nome é {nome},")
print(f"A minha idade é {idade},")
print(f"e a minha altura é {altura}")

if idade < 18:
    print("Você é menor de idade!")
elif idade >= 18 and idade <65:
    print("Você é maior de idade!")
else:
    print("Você já pode se aposentar!")
