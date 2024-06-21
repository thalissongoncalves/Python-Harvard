# Ask user for their name / Remove whitespace from str / Capitalize user's name
# Pergunte ao usuário o nome dele / Remova espaços em branco da string / Capitaliza o nome de usuário
name = input("What's your name? ").strip().title()

# Separando dentro de 1 string, palavras, por exemplo "palavra1 palavra2" se eu printar first irá aparecer "palavra1"
first, last = name.split(" ")

# Say hello to user
# Diz olá para o usuário
print(f"hello, {first}")

def main():
    name = input("What's your name?")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()