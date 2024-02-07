n1 = float(input('Digite n1: '))
n2 = float(input('Digite n2:'))

def calclulaMaior(n1, n2):
    if (n1 == n2):
        print(f"{n1} é igual a {n2}")
    else:
        if (n1 > n2):
           return print(f"{n1} é maior que {n2}")
        else:
           return print(f"{n2} é maior que {n1}")

calclulaMaior(n1,n2)

if (n1 == n2):
    print(f"{n1} é igual a {n2}")
else:
    if (n1 > n2):
        print(f"{n1} é maior que {n2}")
    else:
        print(f"{n2} é maior que {n1}")