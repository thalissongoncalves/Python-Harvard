# Exemplo do uso de int()
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

# Exemplo do uso de float()
a = float(input("What's a? "))
b = float(input("What's b? "))

print(a + b)

# Exemplo do uso de round()
# Serve para arredondar para o número mais próximo
c = float(input("What's c? "))
d = float(input("What's d? "))

print(round(c + d))

# Para adicionar "," entre as casas de milhares
e = float(input("What's e? "))
f = float(input("What's f? "))

g = round(e + f)

print(f"{g:,}")

# Para arredondar em duas casas decimais
# Exemplo 01
h = float(input("What's h? "))
i = float(input("What's i? "))

j = round(h / i, 2)

print(j)

#Exemplo 02
k = float(input("What's k? "))
l = float(input("What's l? "))

m = k / l

print(f"{m:.2f}")

# Exemplo de exponenciação
def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)
    # or
    # return n * n
    # or
    # return n ** n

main()