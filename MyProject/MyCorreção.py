#Correção... atividade 1
posicao = input ("Digite a posição que você joga: ")

if posicao == "goleiro" or posicao == "zagueiro" or posicao == "lateral":
    print("você joga na defesa!")
elif posicao == "volante" or posicao == "meia":
    print("você joga no meio-campo")
elif posicao == "ponta" or posicao == "atacante" or posicao == "centroavante":
    print("você joga no ataque")
else: 
    print("você joga de teimoso")