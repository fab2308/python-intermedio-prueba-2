#listas = [[lista1], [lista2], [listaN]]
#Historia, lenguaje, matematica, fisica, quimica y biologia
listas = []

def getStudents():
    while True:
        try:
            students = int(input("Cantidad de alumnos, ingrese número : "))
        except ValueError:
            print("Por favor, ingrese un número válido")
            continue
        else:
            return students

def getCalifations(cant):
    while True:
        try:
            cant = cant + 1
            print("Ingrese notas de Alumno", cant)
            his_calification = float(input("Nota de Historia : "))
            len_calification = float(input("Nota de Lenguaje : "))
            mat_calification = float(input("Nota de Matemática : "))
            fis_calification = float(input("Nota de Física : "))
            qui_calification = float(input("Nota de Química : "))
            bio_calification = float(input("Nota de Biología : "))

        except ValueError:
            print("Por favor, ingrese un número válido")
            continue
        else:
            califications = [his_calification, len_calification, mat_calification, fis_calification, qui_calification, bio_calification]
            return califications


def main():
    students = getStudents()
    classroom = []
    i = 0
    while i < students:
        califications = getCalifations(i)
        classroom.append(califications)
        i = i+1
    column_average = [sum(sub_list) / len(sub_list) for sub_list in zip(*classroom)]
    avarage = list(map(lambda x: float("{:.2f}".format(x)), column_average))

    print("Los promedios son: ", avarage)
        
    
if __name__ == '__main__':
    main()