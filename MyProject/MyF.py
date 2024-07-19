# Escreva um algoritmo para cadastrar o time e a sua posição na tabela de classificação do campeonato brasileiro. 
# A partir da sua posição, ele deverá exibir as seguintes classificações: "Campeão!" (1º. Lugar), "Libertadores!" (entre 1° e 6°). "Sul-Americana!" (entre 7° e 12°). 
# E "rebaixado" (entre os 4 últimos). Para clubes que estão entre a 13a. e 16a. posição...

time = input(("Digite o nome time:"))
posição = int(input("Digite a posição do time na tabela de classificação: "))

if posição == 1 :
    print(f"{time} Campeão!")
elif posição <= 6:
    print(f"{time} Libertadores!")
elif posição <= 12:
    print(f"{time} Sul-Americana!")
elif posição >= 13:
    print(f"{time} Rebaixado!")
else:
 print(f"{time} está em {posição}º lugar.")
        
