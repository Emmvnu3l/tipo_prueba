import os
import csv

def continueclear():
    os.system('cls')
    input("Presiona cualquier tecla para continuar.....")
    
def clear():
    os.system('cls')

def continuar():
    input("Presiona cualquier tecla para continuar.....")
                
def Add_Worker():
    
    name = input("Nombre: ")
    lastName = input("Apellido: ")
    salary = 0 
    with open ("puestos.txt", "r") as cargos:
        lecura_cargos = cargos.read()
        print(lecura_cargos)
        
    while True:
        try:    
            jobTitle = int(input("Puesto: "))
            if jobTitle == 1:
                jobTitle = "Operario General"
                salary = 500000 
                break
            elif jobTitle == 2:
                jobTitle = "Operario"
                salary = 540000 
                break
            elif jobTitle == 3:
                jobTitle = "Operario Especializado"
                salary = 600000
                break
            else: print("Solo Opciones permitidas!")
            
        except ValueError: print("Solo números enteros!")
    
    afp = int(salary * 12/100)
    salud = int(salary * 7/100)
    liquid = (salary - afp) - salud
    
    newWorker = {
        "Name": name,
        "Last Name": lastName,
        "Job Title": jobTitle,
        "Salary": salary,
        "Desc. Salud": salud,
        "Desc. Afp": afp,
        "Liquido": liquid
        }
    
    def save_Worker():
        with open('trabajadores.csv', 'a', newline="") as trabajadores_csv:
            writer = csv.writer(trabajadores_csv)
            writer.writerow([newWorker['Name'], newWorker['Last Name'], newWorker['Job Title'], newWorker['Salary'], newWorker['Desc. Salud'], newWorker['Desc. Afp'], newWorker['Liquido']])
            #escritor_csv.writerows([newWorker['Name']], [newWorker['Last Name']], [newWorker['Job Title']], [newWorker['Salary']], [newWorker['Desc. Salud']], [newWorker['Desc. Afp']], [newWorker['Liquido']])    
    save_Worker()
    clear()
    input("Trabajador Agregado!")
    

def impress_Worker():
    clear()
    try:
        with open("trabajadores.csv", "r") as trabajadores:
            reader = csv.reader(trabajadores)
            print(f"Nombre\t   Apellido\tCargo\t\t\tS.Bruto\tDes.Salud\tDes.AFP\tLiquido")
            for row in reader:
                if len(row)>0:
                    name, lastName, jobTitle, salary, salud, afp, liquid = row
                    print(f"{name}   {lastName}\t{jobTitle}\t{salary}\t{salud}\t\t{afp}\t{liquid}")
    except FileNotFoundError:
        print("No se encontro el archivo")
    input("Presiona cualquier tecla para continuar.....")
    
def impress_salary():
    clear()
    try:
        with open("trabajadores.csv", "r") as trabajadores:
            reader = csv.reader(trabajadores)
            print(f"Cargo\t\t\tLiquido")
            for row in reader:
                if len(row)>0:
                    name, lastName, jobTitle, salary, salud, afp, liquid = row
                    print(f"{jobTitle}\t{liquid}")
    except FileNotFoundError:
        print("No se encontro el archivo")
    input("Presiona cualquier tecla para continuar.....")