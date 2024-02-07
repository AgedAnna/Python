'''
try/except

try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero = input('Digite um número: ')

try:
    numero_int = float(numero)
    print(f"o dobro do valor é {numero_int * 2}")
except:
    print("Não é um número")

