def numeros_primos(n):
    if n < 2:
        return "não primo"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "não é primo"
    return "é primo"

n = int(input("Digite o número para saber se ele é primo: "))
print(f"O número {n} {numeros_primos(n)}.")