import sys

# Serve para no prompt já passar, capturar e retornar o valor digitado,
#  caso não passar vai retornar o erro de que está faltando argumentos

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])