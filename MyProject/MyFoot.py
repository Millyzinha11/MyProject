# Construa um programa onde o usuário digitará as funções que ele pode exercer em um jogo de futebol. 
# Se a resposta for "goleiro", "zagueiro" ou "lateral", exibir "Defesa!", se a resposta for "volante" ou "meia", exibir "Meia-campo"; 
# se a resposta for "ponta", "atacante" ou "centroavante", exibir "ataque!". Para qualquer outra resposta, exibir "Teimoso!"

print("Digite o número referente a função :")
print("1. goleiro / zagueiro / lateral")
print("2 volante / meia")
print("3 ponta / atacante / centroavante")
print("4. Outra resposta")
funções = int(input())

match funções:
    case 1: 
        print("Defesa!")
    case 2:
         print("Meia-campo")
    case 3: 
        print("Ataque!")
    case 4:
        print("Teimoso!")
    case _: 
        print("Opção não reconhecida")
