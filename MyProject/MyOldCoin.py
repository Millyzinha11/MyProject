# Demonstração de uso da condicional match/case...
print("Digite o número referente ao estado da moeda:")
print("1. flor de cunho")
print("2. soberba")
print("3. muito bem conservado")
print("4. bem conservada")
print("5. outros estados")
estado= int(input())

match estado:
    case 1: 
        print("Perfeita! Vou pagar R$ 1.000.000,00!")
    case 2:
         print("Quase perfeita! Ofereço R$ 250.000,00!")
    case 3: 
        print("Que ótimo! Posso dar uns R$ 1.000.000,00!")
    case 4:
        print("Que bom! Aceitaria R$ 30.000,00?")
    case 5: 
        print("Desculpe, não aceito neste estado")
    case _: 
        print("Opção não reconhecida")