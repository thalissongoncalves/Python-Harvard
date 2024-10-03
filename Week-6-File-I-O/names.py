# Adicionar valor no arquivo
# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# Ler o arquivo
# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())


# Ler o arquivo colocando os valores em ordem alfabética
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")