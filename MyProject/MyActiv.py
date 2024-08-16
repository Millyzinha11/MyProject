# Desenvolvendo atividade...
print("Vamons montar um cardápio personalizado?")
cafe_da_manha = []
almoço = []
jantar = []

print("Café da manhã:")
for x in range(0, 3):
    opção = input(f"Digite a {x+1} opção:")
    cafe_da_manha.append(opção) 
    if opção == "leite" or opção == "queijo" or opção == "pão":
           print("Alimento não recomendado")
print("Eis, as opções escolhidas:", cafe_da_manha)

print("Almoço:")
for x in range(0, 4):
    opção = input(f"Digite a {x+1} opção:")
    almoço.append(opção) 
    if opção == "camarão" or opção == "pimenta":
           print("Alimento não recomendado!")
print("Eis, as opções escolhidas:", almoço)

print("Jantar:")
for x in range(0, 4):
    opção = input(f"Digite a {x+1} opção:")
    jantar.append(opção) 
    if opção == "camarão" or opção == "pimenta":
           print("Alimento não recomendado!")
print("Eis, as opções escolhidas:", almoço)