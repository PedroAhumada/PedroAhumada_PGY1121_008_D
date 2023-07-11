import time
import funciones as fun
import msvcrt
import numpy as np

escenario = np.zeros((10,10),int) #, end""
print(escenario)


platinum=20
gold=30
silver=50
vplatinum=0
vgold=0
vsilver=0
lista_run=[]

while True:
    print("""
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistente
    4. Mostrar ganancias totales
    5. Salir""")

    opcion=fun.validar_opcion()

    if opcion == 1:
        if 0 in escenario:
             cantidad=fun.cantidad()
             for x in range(10):
                print (f"Fila {x+1}")#, end""
                print(escenario[x])
                for y in range(10):
                    print(f"Columna {y+1}")#, end""
                    print(escenario[y])
             for z  in range (cantidad):
                fila=fun.fila()
                fila=fila-1
                columna=fun.columna()
                columna=columna-1
                escenario[fila,columna] = 1
                if fila >= 2:
                    vplatinum=vplatinum+1
                elif fila <= 3 and fila >= 5:
                    vgold=vgold+1
                else:
                    vsilver=vsilver+1
             run=fun.validar_run()
             lista_run.append(run)
             print("Operación realizada de forma exitosa")
             time.sleep(3)
           
        else:
            print("No hay entradas disponibles")
    elif opcion == 2:
        print(escenario)#, end""
        print("Presione una tecla para devolverse")
        msvcrt.getch()
    elif opcion == 3:
        lista_run.sort()
        print(lista_run)
        print("Presione una tecla para devolverse")
        msvcrt.getch()
        
    elif opcion == 4:
        print(f"""
              Tipo entrada   | Cantidad   | Total
            -------------------------------------------------  
            Platinum $120.000 {vplatinum}   ${vplatinum*120000}
            Gold     $80.000  {vgold}       ${vgold*80000}
            Silver   $50.000  {vsilver}     ${vsilver*50000}
            -------------------------------------------------
            TOTAL    {vplatinum+vgold+vsilver}  {vplatinum*120000+vgold*80000+vsilver*50000}""")
        print("Presione una tecla para devolverse")
        msvcrt.getch()
    else:
        fun.salir()
        break

