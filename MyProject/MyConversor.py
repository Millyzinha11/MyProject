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

print("Digite a temperatura que você gostaria de converter...")
print("1. celsius")
print("2. kelvin")
print("3. fahrenheit")

        print(" ")
    case 3:
        print("")