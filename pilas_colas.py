# Pilas - LIFO "Ultimo en Entrar Primero en Salir"

pila = [1,2,3,4,5,6,7,8]

# Añadir elemento
pila.append(9)
pila.append(10)
pila.append(11)
pila.append(12)
print(pila)

# Eliminar elemento 
elemento_eliminado = pila.pop() # Se elimina ultimo elemento
print(elemento_eliminado)
print(pila)

# Colas - FIFO "Primero en Entrar, Primero en Salir"
# Se debe importar
from  collections import deque

cola = deque
print(cola)

cola = deque(['Joshua', 'Jayden', 'Karly', 'Meredyth'])

# Podemos añadir elementos a una cola como una lista
cola.append('Thiryon')
cola.append('Dracko')
cola.append('Dobby')

print(cola)

# Eliminamos elementos de una cola, recordamos primero en entrar, primero en salir

elemento_cola_eliminado = cola.popleft() # cola.popleft() - Solo funciona en deque(colas)
print(elemento_cola_eliminado)
print(cola)

