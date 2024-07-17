# Desenvolvendo... Atividade 2...
# Construa um programa onde o usuário digitará quatro notas trimestrais e o programa irá calcular a média (lembrem-se do tipo da variável). 
# Caso ela seja menor que 6, exibirá na tela: "Aluno Reprovado". Caso seja maior ou igual a 6 exibirá na tela: "Aluno Aprovado".

numero = float(input("Digite um número:"))
print("Digite a sua idade:")
idade = int(input())

if idade < 18:
    print("Você não é maior de idade!")
    print("Não poderá realizar a operação!")
elif idade >= 65:
    print("Você já está pronto para se aposentar?")
    print("Poderemos oferecer suporte técnico...")
else:
    print("Você é maior de idade.")
    print("Portanto, poderá realizar a operação.")
    
print("Obrigado por optar pelos nossos serviços!")
####################################################################
nota1 = float(input("Digite a nota do primeiro trimestre: "))
nota2 = float(input("Digite a nota do segundo trimestre: "))
nota3 = float(input("Digite a nota do terceiro trimestre: "))
nota4 = float(input("Digite a nota do quarto trimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")

