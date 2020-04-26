"""Se ingresan tres valores por teclado, 
si todos son iguales se imprime la suma del primero con el segundo 
y a este resultado se lo multiplica por el tercero."""

num1=int(input("primer valor: "))
num2=int(input("segundo valor: "))
num3=int(input("tercer valor: "))

if num1==num2 and num1==num3:
    suma=num1+num2
    multi=suma*num3
    print("la suma de",num1,"+",num2,"es",suma)
    print("la suma anterior (",suma,") multiplacada por ",num3," es ",multi,sep="")
else:
    print("para realizar la operacion correcta ingresar tres valores identicos")
