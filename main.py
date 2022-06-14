#DDI CLASS
print("Leonardo Zacateco Hernández")

#para importar de otra lases
from usuarios import acciones
#import usuarios.acciones

print("""
Acciones disponibles:
    -registro
    -login
""")

hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer? ")
if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
