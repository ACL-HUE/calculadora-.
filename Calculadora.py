"""Esta es una calculadora funcional que permite realizar sumas, restas, multiplicar este codigo esta elaborado por su servidor 
Allan García el dia 13 de Agosto del 2025, se espera que sea de su total agrado feliz día"""
def calculadora():#inicio 
    print("elegir la operacion hacerse:")#elegir Operacion deseada 
    print("1. Sumar")#eligio suma
    print("2. Restar")#eligio resta 
    print("3. Multiplicar")#eligio miltiplicacion
    print("4.divicion")#eligio divicion

    operacion = input("Ingrese el número de la operación que desea (1,2,3): ")#ingresar el numero de operacion deseada 

    num1 = float(input("Ingrese el primer número: "))#ingrese primer numero 
    num2 = float(input("Ingrese el segundo número: "))#ingrese segundo numero 
    if operacion == "1":#operacion suma
        resultado = num1 + num2#numeros ingresados
        print(f"El resultado de la suma es: {resultado}")#mostrando el resultado 
    elif operacion == "2":#operacion resta
        resultado = num1 - num2#numeros ingresados
        print(f"El resultado de la resta es: {resultado}")#mostrando el resultado 
    elif operacion == "3":#operacion multiplicacion 
        resultado = num1 * num2#numeros ingresados 
        print(f"El resultado de la multiplicación es: {resultado}")#mostrando el resultado
    elif operacion == "4": #operaccion divicion 
            resultado = num1 / num2 #numeros ingresados 
            print(f"El resultado de la división es: {resultado}")#mostrando resultado
calculadora()#fin de calculadora 