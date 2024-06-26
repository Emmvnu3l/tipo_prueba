import os
import funciones

while True:
    try:
        
        funciones.clear()
        print("Bienvenido al Menú!")
        
        op = int(input("1.Registrar\n2.Lista de trabajadores\n3.imprimir salarios\n4.Exit\n"))

        if op == 1:
            funciones.clear()
            print("Registrar Usuario!")
            funciones.Add_Worker()
            
        elif op ==2:
            funciones.impress_Worker()
                
        elif op ==3:
            funciones.impress_salary()

            
        elif op ==4:
            funciones.clear()
            print("Saliendo del programa")
            funciones.continuar
            break
        else: 
            funciones.clear()
            print("Solo opciones del 1 al 4.")
            
            

    except ValueError:
        funciones.clear()
        print("Ingresa un número entero")
        funciones.continuar
        
        

