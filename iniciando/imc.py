nome = input(str('Digite seu nome: '))
altura = input(float('Digite sua altura: '))
peso =  input(float('Digite seu peso: '))

def calImc(altura: float, peso: float):
    imc = peso/ (altura*altura)
    return imc

calImc(altura, peso)

print(nome    ,altura,'de altura')
print('pesa' ,peso)
print('Seu imc é:' ,calImc(altura, peso))