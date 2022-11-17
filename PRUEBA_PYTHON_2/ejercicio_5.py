def main():
    print("Escriba 'salir' para terminar e imprimir colores")
    flag = True
    inputs = []
    while flag:
        a = input('Ingrese color: ')
        if a == 'salir':
            flag = False
        else:
            inputs.append(a.upper())
    for color in inputs:

        print(color)


if __name__ == '__main__':
    main()