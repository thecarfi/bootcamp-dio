texto = input("Informe o texto: ")
VOGAIS = "AEIOU"


for letra in texto:   
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
        print()
        print("Fim da execução")    