# Escreva um algoritmo para cadastrar o time e a sua posição na tabela de classificação do campeonato brasileiro. 
# A partir da sua posição, ele deverá exibir as seguintes classificações: "Campeão!" (1º. Lugar), "Libertadores!" (entre 1° e 6°). "Sul-Americana!" (entre 7° e 12°). 
# E "rebaixado" (entre os 4 últimos). Para clubes que estão entre a 13a. e 16a. posição...

time = input(("Digite o nome time:"))
posição = int(input("Digite a posição do time na tabela de classificação: "))

if posição == 1 :
    print("Campeão!")
elif posição >1 and posição <= 6:
    print("Libertadores!")
elif posição >6 and posição <= 12:
    print("Sul-Americana!")
elif posição >= 12 and posição <= 16:
    print("Sem classificação")
elif posição >= 17 and posição <= 20:
   print("Rebaixado...")
else:
 print("Digite a posição correta!")