
from tkinter import DoubleVar
from Nodo import ListaEnlazada as ListaEN
from Grafica import graficar
Inicio = True
ListaOrdenes= ListaEN()
sumas = 0
def Menu_principal():
    print("====================================")
    print("||-----------Los shucos-----------||")
    print("====================================")
    print("         -Menú principal-")
    print("         1. Generar orden")
    print("         2. Control de ordenes")
    print("         3. Realizar entrega")
    print("         4. info. creador")
    print("         0. Salir")
    print("\nIngrese la opción a realizar")

def Info():
    print("     ====================================")
    print("     ||-----------Los shucos-----------||")
    print("     ====================================")
    print("           -Información del creador-")
    print(" Nombre: Christopher Iván Monterroso Alegria     ")
    print(" Estudiante de ingeniería en ciencias y sistemas ")
    print("\n 0. Regresar")
    print("Ingrese la opción a realizar")

def Menu_Ordenes():
    print(" -Ordenes pendientes-")
    print(" Abriendo gráfica ")

def Generar_orden(cliente):
    print("====================================")
    print("||-----------Los shucos-----------||")
    print("====================================")
    print("   -Generar orden para: ",cliente)
    print("Especialidades: ")
    print("           1.  Salchicha")
    print("           2.  Chorizo")
    print("           3.  Salami")
    print("           4.  Longaniza")
    print("           5.  Costilla")
    print("           0. Cancelar orden")
    print("Ingrese la especialidad a elegir")

def Enlistar(cliente,especialidad,tiempo):
    listaaux = ListaEN()
    listaaux.append(cliente)
    listaaux.append(especialidad)
    listaaux.append(float(tiempo))
    suma=0
    if len(ListaOrdenes)==0:
        listaaux.append(float(tiempo))
    else:
        for i in range(len(ListaOrdenes)):
            print(float(ListaOrdenes[i][3]))
            suma = float(ListaOrdenes[i][3])+float(tiempo)
        listaaux.append(suma)
    ListaOrdenes.append(listaaux)
while Inicio :
    Menu_principal()
    opcion=int(input())
    if ( opcion>4):
        print("Opción no valida")
    else:
        if (opcion==0):
            print("Cerrando programa...")
            Inicio=False
        elif opcion==1:
            print("Ingrese el nombre del cliente:")
            cliente = input()

            generar= True
            while generar:
                
                Generar_orden(cliente)
                opcion=int(input())
                if opcion==0:
                    generar= False
                elif opcion==1:
                    print("Generando orden - Tiempo estimado: 2 minutos")
                    Enlistar(cliente,"salchicha",2)
                    print("Orden generada, regresando...")
                    generar=False
                elif opcion==2:
                    print("Generando orden - Tiempo estimado: 3 minutos")
                    Enlistar(cliente,"Chorizo",3)
                    print("Orden generada, regresando...")
                    generar=False
                elif opcion==3:
                    print("Generando orden - Tiempo estimado: 1.5 minutos")
                    Enlistar(cliente,"Salami",1.5)
                    print("Orden generada, regresando...")
                    generar=False
                elif opcion==4:
                    print("Generando orden - Tiempo estimado: 4 minutos")
                    Enlistar(cliente,"Longaniza",4)
                    print("Orden generada, regresando...")
                    generar=False
                elif opcion==5:
                    print("Generando orden - Tiempo estimado: 6 minutos")
                    Enlistar(cliente,"Costilla",6)
                    print("Orden generada, regresando...")
                    generar=False
                
        elif opcion==2:
            if ListaOrdenes.Tamaño>0:

                Menu_Ordenes()
                graficar(ListaOrdenes)
                print("Presione enter para continuar")
                input()
            else:
                print("\n[Atención]: No hay ordenes pendientes\n")
                print("Presione enter para continuar")
                input()
        elif opcion==3:
            print("Orden para",ListaOrdenes[0][0],"\nEntregada.")
            ListaOrdenes.Remove(ListaOrdenes[0])
            if ListaOrdenes.Tamaño>0:
                print("\nMonstrando ordenes pendientes.")
                graficar(ListaOrdenes)
            else:
                print("\n0 ordenes pendientes")
        elif opcion==4:
            informacion=True
            while informacion:
                Info()
                opcion=int(input())
                if opcion==0:
                    informacion=False
        



