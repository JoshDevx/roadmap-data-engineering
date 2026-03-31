def indeterminados_posicion(*args):
    for i in args:
        print(i)

indeterminados_posicion(5,1,2,[1,2,3],'Hola')

# Diccionarios

def indeterminados_nombres(**kwargs):
    for i, a in kwargs.items():
        print(f'{i} - {a}')

indeterminados_nombres(c=1, b=2, name='Joshua')

# Funciones recursivas

def bomba(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        bomba(numero)
    else:
        print("Booom!")

bomba(10)

def factorial(num):
    if num > 1:
        num = num * factorial(num - 1)
    return num

print(factorial(5))


# Funciones integradas
n = int("10") #float(), etc

f = float ("10.5")
print(f)

c = "Un texto y un numero " + str(10)
print(c)

x = bin(10) # Binario
print(x)

ab = abs(10) # Valor absoluto

ac = eval('2+5') 
print(ac)