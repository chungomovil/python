"""Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]"""

def Decorar(mensaje):
    print(len(mensaje)*"*")
    print(mensaje.upper())
    print(len(mensaje)*"*")

def CargaEmple():
    traduccion=["primer","segundo", "tercer", "cuarto", "quinto", "sexto"]
    empleados=[]
    for x in range(5):
        Decorar("Datos del %s empleado" % (traduccion[x]))
        nombre=input("Introducir nombre: ")
        salarios=[]
        for y in range(3):
            logica=False
            while logica==False:
                salario=float(input("Introducir [%s] salario: " % (traduccion[y])))
                if salario>=100:
                    logica=True
                else:
                    print("---> El salario minimo debe de ser 100.")
            salarios.append(round(salario, 2))
        salarios=tuple(salarios)
        empleados.append([nombre,salarios])
    return empleados

def MostrarEmples(empleados):
    Decorar("plantilla de empleados")
    for x in range(len(empleados)):
        print("Nombre: %s" % (empleados[x][0]))
        print("Salarios: ", empleados[x][1]) # Se debe imprimir de esta forma ya que '%s' no admite imprimir tuplas completas, habria que desempaquetarla
        print("------------------------------")

def SalarioTotal(empleados):
    total=[]
    for x in range(len(empleados)):
        suma=0
        for y in range(len(empleados[x][1])):
            suma=suma+empleados[x][1][y]
        total.append(round(suma, 2)) #Lo redondee porque daba decimales muy largos aun estando redondeado en la funcion anterior
    Decorar("Total cobrado por empleado")
    for x in range(len(empleados)):
        print("Nombre: %s" % (empleados[x][0]))
        print("Salario Total: %s" % (total[x]))
        print("------------------------------")
    return total

def SalarioTrimestral(total, empleados):
    mayores=[]
    for x in range(len(empleados)):
        if total[x]>=10000:
            mayores.append([empleados[x][0], total[x]])
    Decorar("Empleados con salario trimestral mayor o igual a 10.000")
    for x in range(len(mayores)):
        print("Nombre: %s" % (mayores[x][0]))
        print("Salario Trimestral: %s" % (mayores[x][1]))
        print("------------------------------")

emples=CargaEmple()
MostrarEmples(emples)
total=SalarioTotal(emples)
SalarioTrimestral(total,emples)
