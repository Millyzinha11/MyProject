# Demonstração de métodos em listas
inss = ["Maria", "Manoel", "José", "Isabela"]
print("Eis, a fila do inss:", inss)

novo = input("Insira mais uma pessoa:")
inss.append(novo)
print("conferindo a nova lista:", inss)

print("Vou tirar a última pessoa desta lista...")
especial = inss.pop()

print("Agora vou colocá-la na frente de todos!")
inss.insert(0, especial)
print("Conferindo a lista:", inss)

print("Maria não gostou e reclamou...")
inss.remove("Maria")
print("E agora, ela saiu 'pé da vida'", inss)

print("Para não ter mais reclamação, vamos atender...")
inss.sort()
print("... em ordem alfabética:", inss)

print("Onde está esta nova pessoa chamada", especial, "?")
print("Ela agora ficou na posição", inss.index(especial)+1, "!")