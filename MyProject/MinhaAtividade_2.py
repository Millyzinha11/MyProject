# Revisão geral de algoritmos & lógica de programação...

print("Olá seja bem-vindo ao banco inti")
print("Vamos iniciar seu cadastro?")

nome = input("Digite o seu nome completo:")
data_de_nascimento = input("Digite a data de nascimento:")
identidade = input("Digite a identidade:")
valor_abertura_de_conta = float(input("Digite o valor de abertura de conta:"))
saldo_de_conta= int(input("Digite o saldo da conta:"))

print(f"Meu nome é {nome},")
print(f"A minha data de nascimento é {data_de_nascimento},")
print(f"Meu CPF é {identidade},")
print(f"O valor de abertura de conta é {valor_abertura_de_conta}")
print(f"Meu saldo é {saldo_de_conta}")

print("Qual serviço você deseja realizar?")
print("1. Consulta de saldo, 2. Depósito, 3. Saque...")
serviços = int(input("Digite uma opção:"))

match serviços:
    case 1:
        print("Vamos iniciar sua consulta de saldo?")
        print(f"Você possui saldo de {saldo_de_conta}")
    case 2:
        deposito = float(input("Digite o valor de depósito:"))
        saldo = saldo_de_conta + deposito
        print("Vamos iniciar seu depósito?")
        print("")
    case 3:
        saque = int(input("Digite o valor a ser sacado:"))
        if saque > saldo_de_conta:
            print("Não poderá fazer saque maior que o saldo!")
        else:
            saldo = saldo_de_conta - saque
    case _ :
        print("Operação inexistente!")