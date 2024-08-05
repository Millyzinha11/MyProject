# Demonstração do uso de estrutura repetitiva...
contador = 0; senha = ""
while senha != "s3nh4":
    print("digite a senha:")
    senha = input()

    if senha == "s3nh4":
        print ("senha correta!")
        break
    else:
        print("senha errada...")

    contador = contador +1
    if contador == 3:
        print("tentativas excedidas!")
        break