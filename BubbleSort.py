def bubble_sort(lista):
    n = len(lista)
    for i in range(n):  
        for j in range(0, n-i-1):  
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

qtd = int(input("Quantos números você quer ordenar? "))
numeros = []

for i in range(qtd):
    num = int(input(f"Digite o número: "))
    numeros.append(num)

print("\nLista original:", numeros)
print("Lista ordenada:", bubble_sort(numeros))