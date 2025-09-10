def busca_linear(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i
    return -1

qtd = int(input("Quantos números você quer no vetor? "))
vetor = []

for i in range(qtd):
    num = int(input(f"Digite o número na posição {i+1}: "))
    vetor.append(num)

print("\nVetor:", vetor)

busca = int(input("Digite o número que deseja buscar: "))

pos = busca_linear(vetor, busca)
if pos != -1:
    print(f"O número {busca} foi encontrado na posição {pos}.")
else:
    print(f"O número {busca} não está no vetor.")