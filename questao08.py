
dividendo = float(input("Informe um número:"))
divisor = float(input("Informe outro número:"))


def divisao( dividendo , divisor ):
    quociente = 0
    resto = dividendo
    while ( resto - divisor >= 0):
        quociente += 1
        resto = resto - divisor

    return quociente, resto


print("Divisão e resto")
print( divisao(dividendo, divisor) )
