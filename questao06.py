n = int(input("Tabuada de: "))
inicio = int(input("Informe o inicio: "))
final = int(input("Informe o final: "))
x = inicio

while x <= final:
	resultado = n * x
	print('%d x %d = %d' %(n , x, resultado))
	x = x + 1
