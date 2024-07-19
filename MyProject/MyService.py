# Escreva um algoritmo para criar um sistema de avaliação de serviços prestados, para 5 notas diferentes e informar os seus respectivos valores: 
# "1) péssimo", "2) ruim", "3) razoável", "4) bom" e "5) ótimo". Porém, estas avaliações só poderão ser feitas se o serviço em questão ter sido realmente prestado, 
# atendendo a todos os requisitos. Caso contrário, o usuário deverá digitar "O) não executado", para que o sistema lhe possibilite descrever as suas reclamações.

serviço = input ("O serviço foi executado (sim/não?")
avaliacao = int (input ("Qual a nota da avaliação (1/5)?"))

if serviço == "sim" and avaliacao == 1:
    print("O serviço foi péssimo!")
elif serviço == "sim" and avaliacao == 2:
    print("O serviço foi ruim!")
elif serviço == "sim" and avaliacao == 3:
    print("O serviço foi razoável!")
elif serviço == "sim" and avaliacao == 4:
    print("O serviço foi bom!")
elif serviço == "sim" and avaliacao == 5:
    print("O serviço foi excelente!")
else: 
    if serviço == "não" and avaliacao == 0:
        reclamação = input("Digite a sua reclamação: ")
    else:
        print("AS suas avaliações não fazem sentido!")
