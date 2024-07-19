# Construa uma página onde o usuário digitará duas notas escolares.
# Casoa média seja abaixo de 4, o programa escreverá: "Aluno reprovado".
# Caso a nota seja maior que 4 e menor que 6 escreverá: "Aluno em recuperação". 
# No úlimo caso, o programa deve solicitar anota de recuperação. 
# Caso ela seja menor que 5, escrever: "Reprovado na recuperação" ou, caso contrario, escrever "Aprovação na recuperação".

nota1 = float(input("Digite a prijmeira nota : "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 4:
    print("Aluno Reprovado")
elif media >= 4 and media < 6:
    print("Aluno em recuperação")
    nota_recuperacao = float(input("Digite a nota da recuperação: "))
    if nota_recuperacao < 5:
        print("Reprovado na recuperação")
    else:
        print("Aprovação na recuperação")
else:
    print("Aluno aprovado")