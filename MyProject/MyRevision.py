# este é um comentário!

local = input("qual foi o local que você viajou?")
match local:
    case"disney":
        print("Local excelente para levar as crianças!")
    case "paris":
        print("Lugar perfeito para passeios românticos")
    case _:
        print("não conheço este lugar...")