# Resuelva los siguientes bloques de código añadiendo las sentencias Try/Except que considere necesarias. Si el bloque de código no tiene errores, imprima "El bloque de código no tiene errores" en la consola y el resultado del bloque según corresponda. Si el bloque de código tiene errores, imprima el error en la consola.

def bloque_1():
    mi_lista = ["Python","C","C++","JavaScript"]
    try:
        print(mi_lista[5])
        print("El bloque de código no tiene errores")
    except Exception as err:
        print("El error es: ", err)

def bloque_2(num):
    try:
        resultado = num + 10
        print(resultado)
        print("El bloque de código no tiene errores")
    except Exception as err:
        print("El error es: ", err)

def bloque_3():
    try:
        capitales  = {
            "Colombia": "Bogotá",
            "Argentina": "Buenos Aires",
            "Perú": "Lima",
            "Chile": "Santiago de Chile",
        }
        print(capitales["Brasil"])
        print("El bloque de código no tiene errores")
    except Exception as err:
        print("Valor no encontrado: ", err)

        

def main():
    # Esta función no debe ser modificada. Modifique las funciones bloque_1, bloque_2, bloque_3 y bloque_4.
    # Si modifica esta sección para hacer pruebas recuerde cambiarla antes de enviar el ejercicio.
    print("Bloque 1")
    bloque_1()
    print("-------------")

    print("Bloque 2")
    bloque_2("dos")
    print("-------------")

    print("Bloque 3")
    bloque_3()
    print("-------------")

if __name__ == '__main__':
    main()













    