# Desenvolvendo um conversor de temperatura!
# Preciso de um programa que faça a conversão da temperatura, em diferentes unidades de medida...
print("Converter de celsium para kelvin e fahrenheit...")
celsius = int(input("Digite a temperatura:"))

kelvin = celsius + 273
fahrenheit = ( 9 / 5 * celsius) - 32
print(f"A temperatura em kelvin será {kelvin}.")
print(f"A temperatura em fahrenheit será {fahrenheit}")

# Seria possível utilizar as estruturas condicionais if/elif/else ou match/case,
# Para personalizar este programa, de forma que ele ofereça as três conversões?
# Por exemplo, ele poderia perguntar ao usuário qual a unidade de medida e qual valor de temperatura ele quer converter e a partir daí, realizar os cálculos necessários.

print("Qual a conversão você deseja realizar?")
escolha = int(input("1. celsius/ 2. kelvin / 3. fahrenheit: "))
temperatura = int(input("Digite o valor da temperatura:"))

match escolha:
    case 1:
        kelvin = temperatura + 273
        fahreneheit = (9 / 5 * temperatura) - 32
        print(f"A conversão de celsius para kelvin será {kelvin}.")
        print(f"A convrsão de celsius para fahrenheit será {fahrenheit}")
    case 2:
        celsius = temperatura - 273
        fahrenheit = 1,8 * ( temperatura - 273) + 32
        print(f"A conversão de kelvin para celsius será {celsius}.")
        print(f"A convrsão de kelvin para fahrenheit será {fahrenheit}")
    case 3:
        celsius = 9 / 5 * (temperatura - 32)
        kelvin =  (temperatura - 32) / 1.8 + 273
        print(f"A conversão de fahrenheit para celsius será {celsius}.")
        print(f"A conversão de fahrenheit para kelvin será {kelvin}.")