# Coleccion de elementos unicos y desordenados
conjunto = set() #Conjunto vacio

conjunto = {1,2,3}

# Añadir un elemento al conjunto
conjunto.add(4)
print(conjunto)

grupo = {'Joshua', 'Karly', 'Mer', 'Jayden'}

print('Joshua' in grupo) #Busca un elemento en el conjunto, si esta dara True

test = {1,1,1} # No hay elmentos duplicados 
print(test)

# Nos ayuda por ejemplo para eliminar elementos duplicados de una lista, haciendo uso de casting

l = [1,2,3,4,4,5,5,6,7,8,9,9,10,10]

l = list( set(l) ) # Convertimos l a conjunto para eliminar elementos duplicados y luego nuevamente a lista
print(l)

