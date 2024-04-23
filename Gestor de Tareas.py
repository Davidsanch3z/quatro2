
class  task:
    def __init__(self, id, nombre, descripcion, completada=False):
        
      self.id = id
      self.nombre = nombre
      self.descripcion = descripcion
      self.completada = completada

def agregar_tarea( tarea, nombre, descripcion):
    
    nueva_tarea =task(len(tarea)+ 1, nombre,descripcion)
    tareas.append(nueva_tarea)
    print("tarea agregada con exito.")
    
def ver_tareas(tareas):
    if not tareas:
      print("no hay tareas disponibles.")
      return
    for tarea in tareas:
      print(f"[{tarea.id}]{tarea.nombre} - {tarea.descripcion} - completada: {tarea.completada}")
 
def marcar_completada(tareas, id, tarea):
    for tarea in tareas:
        if tarea.id == id_tarea:
           tareas.completada = True
           print(f"Tarea '{tarea.nombre}' marcada como completada.")
           return  
    print("Error: La tarea especificada no existe.")

def eliminar_tarea(tarea, id_tarea):
    
  for tarea in tarea:
    if tarea.id == id_tarea:
      tarea.remove(tarea)
      print("tarea eliminada con exito")
      return 
  print("error: la tarea especifica no existe.") 
       
tareas = []
while True:
    print("\n--- Menú ---")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
     
      
    if opcion == "1":
       id_tarea = int(input("Ingrese el ID de la tarea: "))
       nombre = input("Ingrese el nombre de la tarea: ")
       descripcion = input("Ingrese la descripción de la tarea: ")
       

    elif opcion == "2":
        ver_tareas(tareas)
    elif opcion == "3":
        id_tarea = int(input("Ingrese el ID de la tarea a marcar como completada: "))
        marcar_completada(tareas, id_tarea)
    elif opcion == "4":
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        eliminar_tarea(tareas, id_tarea)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
    else:
      
        print("Error: Opción no válida. Por favor, seleccione una opción válida.")    
