from collections import deque

# --- DATOS CRUDOS DE ENTRADA ---
# Una cola FIFO donde cada elemento es una tupla: (ID_Formulario, Diccionario_Mediciones)
cola_formularios = deque([
    ("F-001", {"temp": 26.5, "humedad": 60}),
    ("F-002", {"temp": 30.0, "humedad": 45}),
    ("F-003", {"temp": 45.1, "humedad": 15}),    # Anomalía: Valores extremos
    ("F-004", {"temp": 28.0, "humedad": "N/A"}), # Anomalía: Dato corrupto (texto en vez de número)
    ("F-005", {"temp": 27.2, "humedad": 55})
])

# --- TU MISIÓN EMPIEZA AQUÍ ---

# 1. Crea una función llamada 'auditar_formularios' que reciba una cola (deque) como parámetro.
def auditar_formularios(cola):
# 2. Dentro de la función, crea una copia de la cola para no destruir la original:
#    cola_trabajo = cola.copy()
    cola_trabajo = cola.copy()
# 3. Crea un diccionario vacío llamado 'resultado_auditoria' con dos llaves:
#    - 'aprobados': inicializada con una lista vacía []
#    - 'rechazados': inicializada con una lista vacía []
    resultado_auditoria = {
        'aprobrados': [],
        'rechazados': []
    }
# 4. Crea un bucle 'while' que se ejecute mientras la 'cola_trabajo' tenga elementos.
#    Pista: puedes usar 'while len(cola_trabajo) > 0:'
    while len(cola_trabajo) > 0: 
# 5. Dentro del bucle, extrae el primer elemento usando .popleft() y aplica
#    desempaquetado para guardarlo en las variables 'id_form' y 'mediciones'.
        id_form, mediciones = cola_trabajo.popleft()
# 6. Extrae los valores del diccionario 'mediciones' en variables locales:
#    t = mediciones["temp"]
#    h = mediciones["humedad"]
        t = mediciones["temp"]
        h = mediciones["humedad"]
# 7. Aplica la lógica de validación (if / elif / else):
#    - Si 'h' es exactamente igual a "N/A", agrega el 'id_form' a la lista de 'rechazados'.
#    - Si 't' es mayor a 40.0 O 'h' es menor a 20, agrega el 'id_form' a 'rechazados'.
#    - Si todo está normal (else), agrega el 'id_form' a la lista de 'aprobados'.
        if h == "N/A":
            resultado_auditoria["rechazados"].append(id_form)
        elif t > 40.0 or h < 20:
            resultado_auditoria["rechazados"].append(id_form)
        else:
            resultado_auditoria["aprobrados"].append(id_form)
# 8. Fuera del bucle, retorna (return) el diccionario 'resultado_auditoria' completo.
    return resultado_auditoria
# --- ZONA DE PRUEBAS ---
# Llama a tu función pasándole la 'cola_formularios' y guarda el resultado en una variable.
# Imprime el resultado final. Debería verse similar a esto:
# {'aprobados': ['F-001', 'F-002', 'F-005'], 'rechazados': ['F-003', 'F-004']}
cola_auditar = auditar_formularios(cola_formularios)
print(cola_auditar)