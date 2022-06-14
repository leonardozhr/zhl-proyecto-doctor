import usuarios.usuario as modelo
import consultas.acciones 

class Acciones:

    def registro(self):
        print("Se realizara tu registro en el sistema...")

        nombre = input("¿Cual es tu nombre? ")
        apellidos = input("¿Cuales son tus apellidos? ")
        puesto = input("¿Que tipo de doctor eres? ")
        consultorio = input("¿Cual es tu numero de consultorio? ")
        piso = input("¿En que piso se encuentra tu consultorio? ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, puesto, consultorio, piso, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto Doctpr {registro[1].nombre}, te haz registrado con el email {registro[1].email}")
        else:
            print("\nNo te haz registrado correctamnete !!!")


    def login(self):
        print("Identificate en el sistema")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            usuario = modelo.Usuario('', '', '', '', '', email, password)
            login = usuario.identificar()

            if email == login[6]:
                print(f"Bienvenido doctor: {login[1]}, te has registrado {login[8]} en el sistema")
                self.proximasAcciones(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("\n Login incorrecto intentalo mas tarde ")
        
    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles
            -Crear consulta (crear)
            -Mostrar consultas (mostrar)
            -Eliminar consulta (eliminar)
            -Editar cita (editar)
            -Salir (salir)
        """)
        
        accion = input("¿Que quieres hacer? ")
        hasEl = consultas.acciones.Acciones()

        if accion == "crear":
            #print("vamos a crear nota")
            hasEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            #print("vamos a mostrar")
            hasEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "eliminar":
            #print("vamos a eliminar")
            hasEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "editar":
            #print("vamos a eliminar")
            hasEl.editar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            exit()    
