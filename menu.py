
import OS
def Numeros():
    print ("*********opcion de numeros*******")

    #ingresar n numeros donde n es un numero ingresado por teclado, calcular y mostrar:
    #cantidad de numeros poitivos cantidad de numeros negativos 

    veces= int(input("Cuantos números desea ingresar?: "))
    pos=0
    neg=0
    cero=0
        for x in range(veces): 
            nume=int(input("Ingrese un número: "))
            if (nume>0):
                pos=pos+1
            elif(nume<0):
                neg=neg+1
            else:
                cero=cero+1
    print("Cantidad de un numeros positivos :"+ str(pos)+
          "\nCantidad de numeros negativos :" + str (neg)+
          "\nCantidad de numeros iguales a cero : " + str(cero))

    pausa = input ("Presione una tecla para continuar")

def Numeros():
    print ("*********opcion de datos de personas*******")

    pausa = input ("Presione una tecla para continuar")

seguirb = True
while (seguir):
    os.system('cls')
    print("1. Opción Numeros ")
    print("2. Opción Datos de Personas ")
    print("3. Finalizar")
    op=int(input("Ingrese opción 1,2,3: "))
    if (op==1):
        Numeros() #invocamos una opcion def
    if (op==2):
        Datos()   #invocamos una opcion def
    if (op==3):
        seguir=False
        break