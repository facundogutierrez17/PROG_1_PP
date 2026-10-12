def es_entero(texto: str) -> bool:
    """
    - Funcion que valida si un texto contiene solamente numeros enteros positivos.
    - Recorre cada caracter y verifica que este entre "0" y "9".
    - Retorna True si todos son digitos y False si hay caracteres invalidos.
    """
    if texto == "":
        return False

    for caracter in texto:
        if caracter < "0" or caracter > "9":
            return False

    return True


def cargar_legajo() -> int:
    """
    - Funcion que solicita el ingreso del numero de legajo.
    - Valida que el dato ingresado contenga solamente numeros.
    - Retorna el legajo convertido a entero.
    """
    bandera = False

    while bandera == False:
        dato = input("Ingrese legajo: ")

        if es_entero(dato):
            bandera = True
        else:
            print("Error: ingrese un numero entero positivo.")

    return int(dato)


def es_nombre_valido(nombre: str) -> bool:
    """
    - Funcion que valida un apellido y nombre.
    - Verifica que contenga letras y espacios, incluyendo letras con tilde y ñ.
    - Retorna True si es valido y False en caso contrario.
    """
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóúü"
    letras = letras + "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

    tiene_letra = False

    for caracter in nombre:
        if caracter in letras:
            tiene_letra = True
        elif caracter != " ":
            return False

    if tiene_letra:
        return True
    else:
        return False


def cargar_nombre() -> str:
    """
    - Funcion que solicita el apellido y nombre del estudiante.
    - Valida que el texto contenga solamente letras y espacios.
    - Retorna el apellido y nombre ingresado.
    """
    bandera = False

    while bandera == False:
        nombre = input("Ingrese apellido y nombre: ")

        if es_nombre_valido(nombre):
            bandera = True
        else:
            print("Error: ingrese solamente letras y espacios.")

    return nombre


def cargar_genero() -> str:
    """
    - Funcion que solicita el genero del estudiante.
    - Valida que el dato ingresado sea F, M o X.
    - Retorna el genero ingresado.
    """
    bandera = False

    while bandera == False:
        genero = input("Ingrese genero (F/M/X): ")

        if genero == "F" or genero == "M" or genero == "X":
            bandera = True
        else:
            print("Error: las opciones son F, M o X.")

    return genero


def cargar_nota(numero: int) -> int:
    """
    - Funcion que solicita la nota de un parcial.
    - Valida que sea un numero entero entre 1 y 10 inclusive.
    - Retorna la nota convertida a entero.
    """
    while True:
        dato = input("Ingrese nota del parcial " + str(numero) + ": ")

        if es_entero(dato):
            nota = int(dato)

            if nota >= 1 and nota <= 10:
                return nota

        print("Error: ingrese un entero entre 1 y 10.")


def cargar_datos(
    legajos: list, nombres: list, generos: list,
    notas1: list, notas2: list
) -> None:
    """
    - Funcion que carga los datos de los 30 estudiantes.
    - Recorre las listas y llama a las funciones de carga y validacion.
    - No retorna un valor; modifica las listas recibidas.
    """
    for i in range(30):
        print("\nESTUDIANTE", i + 1)

        legajos[i] = cargar_legajo()
        nombres[i] = cargar_nombre()
        generos[i] = cargar_genero()
        notas1[i] = cargar_nota(1)
        notas2[i] = cargar_nota(2)


def mostrar_elemento(
    legajos: list, nombres: list, generos: list,
    notas1: list, notas2: list, promedios: list,
    i: int, mostrar_promedio: bool
) -> None:
    """
    - Funcion que muestra los datos de un estudiante.
    - Utiliza el indice i para acceder a sus datos y puede mostrar el promedio.
    - No retorna un valor; imprime la informacion en pantalla.
    """
    print(f"{nombres[i]:<22} | "
          f"{generos[i]:^8} | "
          f"{notas1[i]:^17} | "
          f"{notas2[i]:^18} | "
          f"{legajos[i]:<10}")

    if mostrar_promedio:
        # Mostrar siempre dos decimales sin usar format()
        centesimas = int(promedios[i] * 100 + 0.5)
        parte_entera = centesimas // 100
        parte_decimal = centesimas % 100

        if parte_decimal < 10:
            print("Promedio:", str(parte_entera) + ".0" +
                  str(parte_decimal))
        else:
            print("Promedio:", str(parte_entera) + "." +
                  str(parte_decimal))

    print("-----------------------")


def encabezado_informe() -> None:
    """
    - Funcion que imprime el titulo y los encabezados del informe.
    - Muestra los nombres de las columnas y una linea separadora.
    - No retorna un valor; imprime el encabezado en pantalla.
    """
    print("INFORME DE ESTUDIANTES")
    print()
    print(f"{'APELLIDO Y NOMBRE':<22} | "
          f"{'GENERO':^8} | "
          f"{'NOTA 1ER PARCIAL':^17} | "
          f"{'NOTA 2DO PARCIAL':^18} | "
          f"{'LEGAJO':<10}")

    print("-" * 60)



def recorrer_estudiantes(
    legajos: list, nombres: list, generos: list,
    notas1: list, notas2: list, promedios: list,
    modo: int, valor: int, mostrar_promedio: bool
) -> int:
    """
    - Funcion que recorre los estudiantes y selecciona cuales mostrar.
    - Segun el modo, muestra todos, los de mayor promedio o busca un legajo.
    - Retorna la cantidad de estudiantes encontrados y mostrados.
    . modo 1: todos
    . modo 2: mayor promedio
    . modo 3: buscar legajo
    """
    encontrados = 0

    encabezado_informe()

    for i in range(30):
        mostrar = False

        if modo == 1:
            mostrar = True

        elif modo == 2:
            if promedios[i] == valor:
                mostrar = True

        elif modo == 3:
            if legajos[i] == valor:
                mostrar = True

        if mostrar:
            mostrar_elemento(
                legajos, nombres, generos,
                notas1, notas2, promedios,
                i, mostrar_promedio
            )
            encontrados = encontrados + 1

    return encontrados


def calcular_promedio(nota1: int, nota2: int) -> float:
    """
    - Funcion que calcula el promedio de dos notas.
    - Suma ambas notas y divide el resultado por dos.
    - Retorna el promedio como numero real.
    """
    return (nota1 + nota2) / 2


def calcular_promedios(
    notas1: list, notas2: list, promedios: list
) -> None:
    """
    - Funcion que calcula el promedio de cada estudiante.
    - Recorre las listas de notas y guarda cada resultado en promedios.
    - No retorna un valor; modifica la lista de promedios recibida.
    """
    for i in range(30):
        promedios[i] = calcular_promedio(notas1[i], notas2[i])


def ordenar(
    legajos: list, nombres: list, generos: list,
    notas1: list, notas2: list, promedios: list,
    orden: str
) -> None:
    """
    - Funcion que ordena los estudiantes segun sus promedios.
    - Utiliza el metodo burbuja y ASC para ascendente o DESC para descendente.
    - Intercambia los datos de todas las listas para conservar su relacion.
    - No retorna un valor; modifica las listas recibidas.
    """
    for i in range(29):
        for j in range(29 - i):

            intercambiar = False

            if orden == "ASC":
                if promedios[j] > promedios[j + 1]:
                    intercambiar = True

            elif orden == "DESC":
                if promedios[j] < promedios[j + 1]:
                    intercambiar = True

            if intercambiar:
                auxiliar = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = auxiliar

                auxiliar = legajos[j]
                legajos[j] = legajos[j + 1]
                legajos[j + 1] = auxiliar

                auxiliar = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = auxiliar

                auxiliar = generos[j]
                generos[j] = generos[j + 1]
                generos[j + 1] = auxiliar

                auxiliar = notas1[j]
                notas1[j] = notas1[j + 1]
                notas1[j + 1] = auxiliar

                auxiliar = notas2[j]
                notas2[j] = notas2[j + 1]
                notas2[j + 1] = auxiliar


def buscar_mayor(promedios: list) -> float:
    """
    - Funcion que busca el promedio mas alto de la lista.
    - Recorre los promedios y compara cada uno con el mayor encontrado.
    - Retorna el promedio maximo.
    """
    mayor = promedios[0]

    for i in range(1, 30):
        if promedios[i] > mayor:
            mayor = promedios[i]

    return mayor


def mostrar_menu() -> None:
    """
    - Funcion que muestra las opciones disponibles del menu principal.
    - Imprime las siete opciones del programa.
    - No retorna un valor; muestra el menu en pantalla.
    """
    print("\n========== MENU ==========")
    print("1 - Cargar datos")
    print("2 - Mostrar todos los datos")
    print("3 - Calcular promedios")
    print("4 - Ordenar por promedio DESC")
    print("5 - Mostrar estudiante/s con mayor promedio")
    print("6 - Buscar estudiante por legajo")
    print("7 - Salir")
