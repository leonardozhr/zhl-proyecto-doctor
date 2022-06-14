from pydoc import describe
import consultas.consulta as modelo


class Acciones:

    def crear(self, usuario):
        print(f"OK {usuario[1]}!! Vamos a crear una consulta")
        
        paciente = input("Introduce el nombre del paciente: ")
        enfermedad = input("Escribe la enfermedad que precenta: ")
        descripcion = input("Describe los sintomas: ")

        consulta = modelo.Consulta(usuario[0], paciente,enfermedad, descripcion)
        guardar = consulta.guardar()

        if guardar[0] >= 1:
            print(f"\n Perfecto! has guardado una consulta con: {consulta.paciente}")
        
        else:
            print(f"\nNo se guardo tu consulta: {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\n{usuario[1]} Estas son tus notas")
        consulta = modelo.Consulta(usuario[0])
        consultas = consulta.listar()
        #print(notas)
        for consulta in consultas:
            print("\n***********************")
            print("Folio de consulta: ",consulta[0])
            print("Nombre del paciente: ", consulta[2])
            print("Enfermedad que presenta: ",consulta[3])
            print("Descripción de los sintomas: ",consulta[4])
            print("\n***********************")
            
    def borrar(self, usuario):
        print(f"\n{usuario[1]} !!!ha continuacion borraras una consulta")
        paciente = input("Introduce el nombre de tu paciente con quien canselaras la consulta: ")
        consulta = modelo.Consulta(usuario[0], paciente)
        eliminar = consulta.eliminar()
        if eliminar[0]>= 1:
            print(f"Se borro la consulta exitosamente")
        else:
            print("No se borro la consulta, prueba mas tarde")



    def editar(self, usuario):
        id = input("\nIntroduce el folio de la consulta a modificar: ")
        paciente = input("Introduce nombre del paciente: ")
        enfermedad = input("Introdude el diagnostico: ")
        descripcion = input("Describa el diagnostico: ")
       

        consulta = modelo.Consulta(usuario[0])
        modificar = consulta.editar(paciente,enfermedad,descripcion,id)

        if modificar[0] >= 1:
            print(f"\nLa consulta se actualizo correctamente!!!")
        else:
            print("No se pudo actualizar, prueba más tarde...")