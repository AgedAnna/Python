"Operadores logicos: and, or, not | in e not in"

nome = 'anna'

if 't' in nome:
    print('existe')
else:
    print('nao existe')


usuario = str(input('digite nome: '))

def quant(name):
    qtd = len(name)
    return qtd

print(quant(usuario))