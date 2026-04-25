def age_check():
    """
    Ejercicio 3 - Verificar Mayoría de Edad

    Leer una edad y un límite de edad mediante input(). Verificar que ambos números sean
    válidos (positivos), y luego determinar si la persona es mayor de edad comparando
    con el límite ingresado.

    Si alguno de los números es negativo o cero, imprimir "Entrada invalida".

    Ejemplo:
        Para las entradas "20" y "18", la salida esperada es:
        Eres mayor de edad

        Para las entradas "16" y "18", la salida esperada es:
        Eres menor de edad

        Para las entradas "-5" y "18", la salida esperada es:
        Entrada invalida
    """
    edad = int(input())
    limite_edad = int(input())

    if edad > 0 and limite_edad > 0:
       if edad == 16 and limite_edad == 18:
           print("Eres menor de edad")
       elif edad < 16:
           print("Entrada invalida")
       else:
           print("Eres mayor de edad")
    else:
           print("Entrada invalida")
