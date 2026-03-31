# Aprendiendo del error
# A programar se aprende programando y cometer errores es la prueba de que estas avanzando

# Bloque de codigo excepcional, que nos permitira continuar con la ejecucion asi ocurra un error


while(True):
    try:
        n = float(input('Introduce un número: '))
        m= 4
        print(f'{n}/{m} = {n/m}')
    except:
        print('Ha ocurrido un error, ingrese un numero correcto: ')
    else:
        print('Todo a funcionado correctamente.')
        break
    finally:
        print('Termino la iteración')