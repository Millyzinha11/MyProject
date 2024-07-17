# Desenvolvendo... Atividade 3
# Constua um programa onde o usuário digitará o seu peso e a sua altura e o programa irá calcular o IMC (peso/altura).
# Caso o IMC seja maior que 25 exibirá, na tela, "Acima do peso ideal"
# Caso seja menor que 18, "Abaixo do peso ideal". Por fim, se o resultado do cálculo entregar um valor entre 18 e 25, informar que " O seu peso eestá OK".

peso = int(input("Digite o seu peso:"))
altura = float(input("Digite sua altura:"))

imc = peso / altura ** 2

print(f"O seu imc é {imc}.")
if imc > 25 :
    print("Acima do peso ideal")
elif imc < 18:
    print("Abaixo do peso ideal")
else:
    print("O seu peso eestá OK")
