# --- DATOS ENTRANTE ---
# Lista de tuplas simulando el flujo de la torre
flujo_telemetria = [
    ("S-NORTE", 28.5),
    ("S-SUR", 30.1),
    ("S-ESTE", 45.0), # Error: temperatura imposible
    ("S-OESTE", 29.8),
    ("APAGADO", 0.0), # Señal para detener el sistema
    ("S-FANTASMA", 25.0) # Este dato nunca debería procesarse
]

# Copiamos la lista para poder extraer elementos sin perder la original
datos_pendientes = flujo_telemetria.copy()
temperaturas_registradas = []

print(datos_pendientes)
print("Iniciando procesamiento de telemetría...\n")

# --- TU MISIÓN EMPIEZA AQUÍ ---

# 1. Crea un bucle 'while True:' (nuestra simulación de do-while).

# 2. Dentro del bucle, usa el método .pop(0) en la lista 'datos_pendientes' 
#    para extraer la primera tupla de la lista y guárdala en una variable.
while True:
    tupla = datos_pendientes.pop(0)
# 3. Aplica el DESEMPAQUETADO para separar esa tupla en dos variables: 'sensor' y 'temp'.
    sensor, temp = tupla
# 4. Usa un 'if' para verificar si el 'sensor' es igual a "APAGADO".
#    Si lo es, imprime un mensaje de apagado y usa 'break' para romper el bucle.
    if sensor == "APAGADO":
        print(f'Sensor - {sensor}')
        break
# 5. Usa un 'elif' para verificar si la temperatura es mayor a 40.0.
#    Si es mayor, imprime un mensaje de alerta indicando qué sensor falló.
    elif temp > 40.0:
        print(f'El Sensor Fallo: {temp} - Temperatura Invalida')
# 6. Usa un 'else' (si todo está normal) para agregar la temperatura a la lista 'temperaturas_registradas'.
    else:
        temperaturas_registradas.append(temp)
# 7. Fuera del bucle, imprime la lista final de 'temperaturas_registradas'.
print(f'Temperaturas Registradas: {temperaturas_registradas}')