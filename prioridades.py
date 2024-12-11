import heapq
from datetime import datetime

class eduardomanejatareas:
    def __init__(self):
        self.heap = []

    def agregar_tarea(self, tarea, prioridad, fecha_vencimiento):
        # Usar una tupla (prioridad, fecha_vencimiento, tarea) para mantener el heap ordenado por prioridad
        fecha_vencimiento_dt = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        heapq.heappush(self.heap, (prioridad, fecha_vencimiento_dt, tarea))
        print(f"Tarea '{tarea}' con prioridad {prioridad} y fecha de vencimiento {fecha_vencimiento} añadida.")

    def obtener_tarea(self):
        if self.heap:
            prioridad, fecha_vencimiento, tarea = heapq.heappop(self.heap)
            print(f"Tarea '{tarea}' con prioridad {prioridad} y fecha de vencimiento {fecha_vencimiento.date()} extraída.")
            return tarea
        else:
            print("No hay tareas en la cola.")
            return None

    def mostrar_tareas(self):
        if self.heap:
            print("Tareas en la cola (ordenadas por prioridad):")
            # La lista heap ya está ordenada por prioridad
            tareas_ordenadas = sorted(self.heap)
            for idx, (prioridad, fecha_vencimiento, tarea) in enumerate(tareas_ordenadas):
                print(f"{idx + 1}. Prioridad: {prioridad}, Fecha de vencimiento: {fecha_vencimiento.date()}, Tarea: {tarea}")
        else:
            print("No hay tareas en la cola.")

    def mostrar_tareas_urgentes(self):
        if self.heap:
            fecha_actual = datetime.now()
            tareas_ordenadas = sorted(self.heap, key=lambda x: (x[1] - fecha_actual).days)
            print("Tareas en la cola (ordenadas por urgencia de vencimiento):")
            for prioridad, fecha_vencimiento, tarea in tareas_ordenadas:
                dias_para_vencer = (fecha_vencimiento - fecha_actual).days
                print(f"Fecha de vencimiento: {fecha_vencimiento.date()}, Prioridad: {prioridad}, Tarea: {tarea}, Días para vencer: {dias_para_vencer + 1}")
        else:
            print("No hay tareas en la cola.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.heap):
            tarea_eliminada = self.heap.pop(indice)
            heapq.heapify(self.heap)  # Volver a crear el heap para mantener la estructura de prioridad
            print(f"Tarea '{tarea_eliminada[2]}' eliminada con éxito.")
        else:
            print("Índice no válido. No se pudo eliminar la tarea.")

def solicitar_fecha_vencimiento():
    while True:
        fecha_vencimiento = input("Indique la fecha de vencimiento (formato YYYY-MM-DD): ")
        try:
            fecha_vencimiento_dt = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
            fecha_actual = datetime.now()
            if fecha_vencimiento_dt < fecha_actual:
                print("La tarea ya ha vencido. Por favor, introduzca una fecha futura.")
                continue
            return fecha_vencimiento
        except ValueError:
            print("Formato de fecha no válido. Por favor, intente de nuevo.")

def solicitar_prioridad():
    while True:
        prioridad = input("Indique la prioridad (número entero, donde menor número indica mayor prioridad): ")
        if prioridad.isdigit():
            return int(prioridad)
        else:
            print("Prioridad no válida. Debe ser un número entero. Por favor, intente de nuevo.")

def solicitar_tarea():
    while True:
        tarea = input("Escriba la tarea: ")
        if tarea.strip():
            return tarea
        else:
            print("El nombre de la tarea no puede estar vacío. Por favor, intente de nuevo.")

def solicitar_indice():
    while True:
        indice = input("Indique el índice de la tarea que desea eliminar: ")
        if indice.isdigit():
            return int(indice) - 1  # Convertir a índice de lista (0 basado)
        else:
            print("Índice no válido. Debe ser un número entero. Por favor, intente de nuevo.")

def mainmenu():
    gestor_tareas = eduardomanejatareas()
    while True:
        print("\n1: Agregar tarea")
        print("2: Tarea de mayor prioridad completada (extrae la tarea de la lista)")
        print("3: Mostrar todas las tareas")
        print("4: Mostrar tareas urgentes (por fecha actual)")
        print("5: Eliminar una tarea")
        print("6: Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tarea = solicitar_tarea()
            prioridad = solicitar_prioridad()
            fecha_vencimiento = solicitar_fecha_vencimiento()
            gestor_tareas.agregar_tarea(tarea, prioridad, fecha_vencimiento)
        elif opcion == "2":
            gestor_tareas.obtener_tarea()
        elif opcion == "3":
            gestor_tareas.mostrar_tareas()
        elif opcion == "4":
            gestor_tareas.mostrar_tareas_urgentes()
        elif opcion == "5":
            gestor_tareas.mostrar_tareas()
            indice = solicitar_indice()
            gestor_tareas.eliminar_tarea(indice)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 6.")

mainmenu()

