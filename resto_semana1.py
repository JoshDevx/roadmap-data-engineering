# --- DATOS CRUDOS DE ENTRADA ---
sensor_id = "   TR-09-NORTE   " # Viene con espacios en blanco accidentales
humedad_actual = "68" # Viene como texto (string), pero debería ser un número entero (int)
temperaturas_semana = [28.5, 30.2, "ERROR_SENSOR", 29.1, 27.8] 

# --- TU MISIÓN EMPIEZA AQUÍ ---
# 1. Limpia el sensor_id (quita los espacios al inicio y al final).
sensor_id = sensor_id.strip()
print(sensor_id)
# 2. Convierte la humedad_actual de texto a número entero.
humedad_actual = int(humedad_actual)
print(humedad_actual)
# 3. De la lista de temperaturas, elimina el dato "ERROR_SENSOR".
temperaturas_semana.remove("ERROR_SENSOR")
#Aqui intente iterar, pero se me ocrurrio que esto es ya un valor predefinido para un tipo de error
#podria ser una lista de los errores y asi limpiar la data por ejemplo
print(temperaturas_semana)
#print(temperaturas_semana_limpia)
# 4. Calcula el promedio de las temperaturas válidas.
promedio_temperaturas = round(sum(temperaturas_semana)/len(temperaturas_semana),2)
print(promedio_temperaturas)
# 5. Crea un diccionario vacío llamado 'resumen_parcela' y agrégale 3 llaves:
#    - 'id': el sensor limpio
#    - 'humedad': la humedad en formato numérico
#    - 'temp_promedio': el promedio que calculaste (redondeado a 2 decimales)

# 6. Imprime un mensaje final usando un f-string utilizando los datos del diccionario.
#    Ejemplo esperado: "El sensor TR-09-NORTE reporta 68% de humedad y 28.9°C de temperatura promedio."
resumen_parcela = {
    'id': sensor_id,
    'humedad': humedad_actual,
    'temp_promedio': promedio_temperaturas
}

print(f"El sensor {resumen_parcela['id']} reporta {resumen_parcela['humedad']}% de humedad y {resumen_parcela['temp_promedio']}°C de temperatura promedio.")
