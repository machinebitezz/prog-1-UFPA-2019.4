temp = input()
temp = temp.split(' ')

pi = 3.14159

a = float(temp[0])
b = float(temp[1])
c = float(temp[2])

triangulo = (a*c) / 2.0
circulo = pi * (c**2)
trapezio = ((a+b) * c) / 2.0
quadrado = b ** 2
retangulo = a * b

print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))
