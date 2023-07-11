import time
import msvcrt
import numpy
def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese el número de la opción que desea (Del 1 al 5): "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("Debe escoger una opción valida")
        except:
            print("ERROR INGRESA UN NÚMERO ENTERO")
def cantidad():
     while True:
        try:
            entradas = int(input("Ingresa la cantidad de entradas recuerda que puedes comprar 3 máximo: "))
            if entradas in (1,2,3):
                return entradas
            else:
                print("Debe escoger una opción valida")
        except:
            print("ERROR INGRESA UN NÚMERO ENTERO")

def validar_run():
    while True:
        try:
            run = int(input("Ingresa su run (Sin puntos, sin guion ni dígito identificador) "))
            if run >= 10000000 and run <= 99999999:
                return run
            else:
                print("Debe escoger una opción valida")
        except:
            print("ERROR INGRESA UN NÚMERO ENTERO")
def fila():
    while True:
        try:
            fila = int(input("Ingrese el número de fila: "))
            if fila >=0 and fila <=9:
                return fila
            else:
                print("Número de fila invalida")
        except:
            print("ERROR INGRESA UN NÚMERO ENTERO")
            
def columna():
    while True:
        try:
            columna = int(input("Ingrese el número de columna: "))
            if columna >=0 and columna <=9:
                return columna
            else:
                print("Número de columna invalida")
        except:
            print("ERROR INGRESA UN NÚMERO ENTERO")
#def total():
    print(f"""
              Tipo entrada   | Cantidad   | Total
            -------------------------------------------------  
            Platinum $120.000 {vplatinum}   ${vplatinum*120000}
            Gold     $80.000  {vgold}       ${vgold*80000}
            Silver   $50.000  {vsilver}     ${vsilver*50000}
            -------------------------------------------------
            TOTAL    {vplatinum+vgold+vsilver}  {vplatinum*120000+vgold*80000+vsilver*50000}""")
def salir():
    print("¡¡Gracias por usar mi programa!!")
    print("Creado por: Pedro Javier Ahumada Flores")
    print("Fecha: 11/07/2023")
    print("Saliendo....")
    time.sleep(5)
def recorrer():
    for x in range(10):
            print (f"Fila {x+1}")#, end""
            for y in range(10):
                print(f"Columna {y+1}") #, end""