def mmc(a, b):
    maior = max(a, b)
    while True:
        if maior % a == 0 and maior % b == 0:
            return maior
        maior += 1

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

print(f"O MMC entre {x} e {y} é {mmc(x, y)}")