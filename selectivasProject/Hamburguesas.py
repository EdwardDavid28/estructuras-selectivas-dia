#Definir las Constantes
from pydoc import describe
PRECIO_SENCILLA=20000
PRECIO_DOBLE=25000
PRECIO_TRIPLE=28000
IMPUESTO_TARJETA=0.07

#Funcion para calcular el precio
def calcular_precio(tipo_hamburguesa,medio_pago,cantidad):
    #Definir los precios segun w ltipo de hamburguesa
    if tipo_hamburguesa==1:
        precio=PRECIO_SENCILLA
        descripcion="Sencilla"
    elif tipo_hamburguesa==2:
        precio=PRECIO_DOBLE
        descripcion="Doble"
    elif tipo_hamburguesa==3:
        precio=PRECIO_TRIPLE
        descripcion="Triple"
    else:
        return None #Tipo de hamburguesa

#Calcular el total sin cargos
    total_sin_cargo=precio*cantidad

#Aplicar impuestos si el medio de pago es tarjeta
    if medio_pago==1:
     impuesto=round(total_sin_cargo*IMPUESTO_TARJETA)
    else:
     impuesto=0

    total=round(total_sin_cargo+impuesto)

#Retornar datos revelantes
    return descripcion, precio,cantidad,impuesto,total

#Funcion para generar mensaje
def generar_mensaje(descripcion,precio,cantidad,impuesto,total):
        return (f"Tipo de hamburguesa:{descripcion}\n"
                f"precio: ${precio}\n"
                f"Cantidad: {cantidad}\n"
                f"Impuesto: ${impuesto}\n"
                f"Total: ${total}")
#Funcion para validar los datos
def validar_datos(tipo_hamburguesa,medio_pago,cantidad):
        if 1<=tipo_hamburguesa<=3 and 1<=medio_pago<=2 and cantidad>0:
            resultado=calcular_precio(tipo_hamburguesa,medio_pago,cantidad)
            #print("Resutlado:",resultado)
            descripcion,precio,cantidad,impuesto,total=resultado
            mensaje=generar_mensaje(descripcion,precio,cantidad,impuesto,total)
            print("--------------------\n"+mensaje)
        else:
            print("verifique")

#Entradas
tipo_hamburguesa=int(input("ingrese tipo de Hamburguesa\n1. Sencilla \n2 doble \n3 triple\n"))
medio_pago=int(input("ingrese el medio de pago \n1. tarjeta \n2. otro \n"))
cantidad=int(input("ingrese la cantidad: "))

#salidas
validar_datos(tipo_hamburguesa,medio_pago,cantidad)