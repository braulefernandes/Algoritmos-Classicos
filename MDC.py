def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

print(f"O MDC entre {x} e {y} é {mdc(x, y)}")