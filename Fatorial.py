def fatorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * fatorial(n-1)

n = int(input("Digite o número que vc deseja o fatorial: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}.")