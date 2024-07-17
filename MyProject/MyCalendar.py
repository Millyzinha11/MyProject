# Demonstração... Atividade 1
# Construa um programa onde o usuário digitará o dia de semana. De acordo com a sua resposta, 
# o programa deverá exibir na tela uma recomendação do que ele poderia fazer neste dia.
# Se ele não digitar absolutamente, nada, o programa exibirá um alerta.

print("Digite o dia da semana")
print("1. Domingo")
print("2. Segunda-feira")
print("3. Terça-feira")
print("4. Quarta-feira")
print("5. Quinta-feira")
print("6. Sexta-feira")
print("7. Sabado")
semana = input()

match semana:
    case "Domingo":
        print("Dia perfeito para descansar e recarregar as energias para a próxima semana")
    case "Segunda-feira":
        print("Dia de luta e não de glória")
    case "Terça-feira":
        print("Vamos botar um cropped e ragir")
    case "Quarta-feira":
        print("Calma, falta pouco se esforce!")
    case "Quinta-feira":
        print("Aguenta só mais um pouco, estamos quase lá!")
    case "Sexta-feira": 
        print("Uhull! Sextouuuuuuuuuuu!!!")
    case "Sabado": 
        print("Relaxe e divirta-se, é final de semana!")
    case _:
        print("Dia da semana não reconhecido. Por favor, digite um dia válido.")
