# Demonstração... Atividade 4
# Construa um programa onde o usuário digitará o ano que nasceu e o programa irá escrever, n atela, quantos nos ele completará em 2040.

anodenascimento = int(input("Digite o ano em que você nasceu: "))
anodereferencia = 2040
idadeem2040 = anodereferencia - anodenascimento
print(f"Em {anodereferencia}, você terá {idadeem2040} anos.")