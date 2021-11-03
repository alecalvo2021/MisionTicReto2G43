# Este es un ejemplo de funciones matematicas en Python

# funcion sumar
def sumar(n1, n2):
    return n1 + n2

def resta (a, b):
    return print(a - b)

def producto (a, b):
    return print(a * b)

def division (a, b):
    return print(a / b)

n, o, m = input("Ingrese dos número junto con su operador separados por espacios: ").split()
n = float(n)
m = float(m)


if o == "+":
    suma(n, m)
elif o == "-":
    resta(n, m)
elif o == "*":
    producto(n, m)
elif o == "/":
    division(n, m)