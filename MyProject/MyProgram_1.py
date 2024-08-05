#construa um programa que pergunte ao usuario, qual é o melhor clube de futebol do brasil 
# (o qual devra estar definifo no corpo do programa) 
# enquanto ele irá fazer uma advertencia e retornara para a pergunta somente apos o usario responder a pergunta corretamente, o programa ira paraneniza-lo

clube = "flamengo"
while clube:
    print("qual o melhor clube do brasil:")
    resposta = input()

    if resposta == clube :
        print ("Parabéns, você acertou!!")
        break
    else:
       if resposta :
        print(" Resposta incorreta!")
        break