import os
def limpiarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

class Carro:
#Función Constructora (__Init__())
#Las propiedades: modelo, color, motor, asientos, marca, puertas, combustible, placa.
    def __init__(self, modelo, color, motor, asientos, marca, puertas, combustible, placa):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.asientos  = int(asientos)
        self.marca = marca
        self.puertas = int(puertas)
        self.combustible = combustible
        self.placa = placa

    def __str__(self):
        return """Modelo: {}, Color: {}, Motor: {}, Asientos: {}, Marca: {}, Puertas: {}, Combustible: {}, Placa: {}
                """.format(self.modelo, self.color, self.motor, self.asientos, self.marca, self.puertas, self.combustible, self.placa)

    #Los métodos: acelerar, parquear, echar gasolina, info.
    velocidad = 0
    def acelerar(self):
        velocidad = int(input("¿A que velocidad viaja? "))
        self.velocidad += self.velocidad + velocidad
        print("Viaja a", self.velocidad, "KM/H")

    parqueado = False
    def parqueo(self):
        opcion = input("¿Desea parquear el vehículo? escriba si ó no: ")
        if(opcion=="si"):
            parqueado=True
            print("Vehículo parqueado")
        else:
            parqueado=False
            print("Vehículo NO parqueado")
    
    gasolina = False
    def gas(self):
        opcion = input("¿Desea echar gasolina? escriba si ó no: ")
        if(opcion=="si"):
            gasolina=True
            print("Tanque lleno")
        else:
            gasolina=False
            print("No se echó gasolina")

#Heredar de clase padre Carro a clases TransportePublico, Policial, Bomberos.
#Crear métodos y propiedades apropiadas para las clases hijas.
class TransportePublico(Carro):  
  ruta=""
  capacidad=0.0
  def bus(self):
      r = input("¿Cual es el número de ruta del bus? ")
      ruta = r
      toneladas = float(input("¿Capacidad en toneladas del bus? "))
      capacidad = toneladas
      print("Ruta: ", self.r, "Capacidad en Toneladas: ", self.toneladas)

class Policial(Carro):  
  ciudadAsignada=""
  def Police(self):
      ciudad = input("¿A qué ciudad se encuentra asignado el coche? ")
      ciudadAsignada = ciudad
      print("Asignado a la ciudad: ", self.ciudad)

class Bomberos(Carro):  
  CapacidadAgua=0.0
  def bombero(self):
      cisterna = float(input("¿Capacidad de la cisterna? "))
      CapacidadAgua = cisterna
      print("Capacidad de la cisterna: ", self.cisterna)

#Valores predeterminados

coche = Carro("Corolla", "Marrón", "E80", 5, "Toyota", 4, "Lleno", "474-157")
BusSM = Carro("Coaster", "Blanco", "3.7L", 30, "Toyota", 5, "Lleno", "777-999")
PoliciaSM = Carro("Frontier", "Blanco/Azul", "V6", 5, "Nissan", 4, "Lleno", "123-456")
BomberoSM = Carro("D14/280 CCF 4x4", "Rojo", "450L", 4, "RENAULT", 2, "Lleno", "654-321")


# coche.acelerar()
# coche.parqueo()
# coche.gas()
#print(coche)
try:
    while True:
        print("""Asignación 6 - Elija la opción que desee
        1- Carro Normal.
        2- Transporte Público.
        3- Policial.
        4- Bomberos.
        5- Salir
        """)
        menu = int(input("Escriba el número de la opción: "))

        #Menú de Carro Normal
        if (menu==1):
            limpiarPantalla()
            while True:
                limpiarPantalla()
                print("""Asignación 6 - Menú de Carro Normal
                1- Acelerar.
                2- Parquear.
                3- Echar Gasolina.
                4- Información.
                5- Ir al menú principal.
                """)
                opcion = int(input("Escriba el número de la opción: "))
                if (opcion==1):
                    limpiarPantalla()
                    coche.acelerar()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==2):
                    limpiarPantalla()
                    coche.parqueo()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==3):
                    limpiarPantalla()
                    coche.gas()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==4):
                    limpiarPantalla()
                    print(coche)
                    continuar = input("Pulse cualquier tecla para continuar.")
                else:
                    limpiarPantalla()
                    break
        #Menú de Transporte Público
        elif (menu==2):
            limpiarPantalla()
            while True:
                limpiarPantalla()
                print("""Asignación 6 - Menú de Transporte Público
                1- Acelerar.
                2- Parquear.
                3- Echar Gasolina.
                4- Información.
                5- Ir al menú principal.
                """)
                opcion = int(input("Escriba el número de la opción: "))
                if (opcion==1):
                    limpiarPantalla()
                    BusSM.acelerar()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==2):
                    limpiarPantalla()
                    BusSM.parqueo()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==3):
                    limpiarPantalla()
                    BusSM.gas()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==4):
                    limpiarPantalla()
                    print(BusSM)
                    continuar = input("Pulse cualquier tecla para continuar.")
                else:
                    limpiarPantalla()
                    break
        #Menú Policial
        elif (menu==3):
            limpiarPantalla()
            while True:
                limpiarPantalla()
                print("""Asignación 6 - Menú Policial
                1- Acelerar.
                2- Parquear.
                3- Echar Gasolina.
                4- Información.
                5- Ir al menú principal.
                """)
                opcion = int(input("Escriba el número de la opción: "))
                if (opcion==1):
                    limpiarPantalla()
                    PoliciaSM.acelerar()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==2):
                    limpiarPantalla()
                    PoliciaSM.parqueo()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==3):
                    limpiarPantalla()
                    PoliciaSM.gas()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==4):
                    limpiarPantalla()
                    print(PoliciaSM)
                    continuar = input("Pulse cualquier tecla para continuar.")
                else:
                    limpiarPantalla()
                    break

        #Menú de Bomberos
        elif (menu==4):
            limpiarPantalla()
            while True:
                limpiarPantalla()
                print("""Asignación 6 - Menú de Bomberos
                1- Acelerar.
                2- Parquear.
                3- Echar Gasolina.
                4- Información.
                5- Ir al menú principal.
                """)
                opcion = int(input("Escriba el número de la opción: "))
                if (opcion==1):
                    limpiarPantalla()
                    BomberoSM.acelerar()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==2):
                    limpiarPantalla()
                    BomberoSM.parqueo()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==3):
                    limpiarPantalla()
                    BomberoSM.gas()
                    continuar = input("Pulse cualquier tecla para continuar.")
                elif (opcion==4):
                    limpiarPantalla()
                    print(BomberoSM)
                    continuar = input("Pulse cualquier tecla para continuar.")
                else:
                    limpiarPantalla()
                    break
        else:
            print("Fin del programa")
            break

except (KeyboardInterrupt, ValueError):
    print("Opción no válida, adiós")