def inverter(valor):
    texto = str(valor)
    invertido = texto[::-1]
    if texto.isdigit():
        return int(invertido)
    return invertido

entrada = input("Digite uma palavra ou número: ")
print(f"Invertido: {inverter(entrada)}")
