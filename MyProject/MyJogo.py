def par_ou_impár():
    print("Bem-vindo ao jogo de Par ou Ímpar!")
numero = (0,10)
print(f"Escolha um numero de o a 10, {numero}")
numero_1 =  int(input("Escolha um número entre o e 10:"))

if numero_1 < 0 or numero_1 > 10:
    print("Numero inexistente")

soma = numero + numero_1
if soma *2 == 0:
    print("a soma é par")
    print("Você acertou!")
else:
    print("A soma é impar")