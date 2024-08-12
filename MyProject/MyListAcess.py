# Demonstração de acesso a listas...

print("Vou montar uma marmita com 5 alimentos!")
marmita = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Eis, a nossa recomendação", marmita)

resposta = input("Você quer montar uma marmita diferente (s/n)?")
if resposta == "s":
    for x in range(0, 5):
        print(f'Digite o {x+1}o, item do cardápio:')
        marmita[x] = input()
    print("A marmita montada foi:", marmita) 
    print("Os três primeiros intes foram:", marmita[0:3])
    print("O último item da marmita foi:", marmita[-1])
else:
    print("Ok. Você decide...")