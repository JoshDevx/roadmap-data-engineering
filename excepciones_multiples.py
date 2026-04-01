try:
    n = input('Ingrese un numero: ')
    5/n
except Exception as e: # le agregamos la excepcion a e
    print(type(e).__name__) #Imprimimos la excepcion

try:
    x = float(input('Ingrese un numero: '))
    5/x
except TypeError:
    print('No se puede divdir un numero por una cadena')
except ValueError:
    print('Debes introducir una cadena que sea un numero')
except ZeroDivisionError:
    print('No se puede dividir por cero, prueba otro numero')
except Exception as e:
    print(type(e).__name__)
    
    