
from random import randint
from statistics import mean, geometric_mean
sueldos = []
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]



def asignar_sueldo_aleatorio():
    for trabajador in trabajadores:
        print(f"{trabajador.ljust(20)} {str(randint(300000,2500000)).ljust(10)}")
        sueldos.append({"nombre":trabajador,"sueldo":randint})

        


        

def clasificar_sueldo():
   print("Lo Sentimos, El Programa Aún No Está Terminado...")
        
        

        
    
      

def ver_estadistica():
    print("Lo Sentimos, El Programa Aún No Está Terminado...")


def reporte_sueldos():
    print("Lo Sentimos, El Programa Aún No Está Terminado...")
    

       
        
         




def menu():
    while True:
        print("1) Asignar Sueldos Aleatorios.")
        print("2) Clasificar Sueldos.")
        print("3) Ver Estadisticas.")
        print("4) Reporte De Sueldos.")
        print("5) Salir Del Programa.")
        opc=input("Ingrese Una Opcion: ")
        
        if opc == "1":
            asignar_sueldo_aleatorio()
            print("Sueldos Asignados Exitosamente...")
        elif opc == "2":
            clasificar_sueldo()
        elif opc == "3":
            ver_estadistica()
        elif opc == "4":
            reporte_sueldos()
        elif opc == "5":
            print("Saliendo Del Programa...")
            print("Desarrollado por Vicente East")
            print("RUT: 21.649.430-K")
            break
        else:
            print("Opción No Válida...")
            
menu()
            
            

