import biblioteca_pp as b


def main():
    legajos = [0] * 30
    nombres = [""] * 30
    generos = [""] * 30
    notas1 = [0] * 30
    notas2 = [0] * 30
    promedios = [0.0] * 30

    cargados = False
    promedios_listos = False
    opcion = 0

    while opcion != 7:
        b.mostrar_menu()

        dato = input("Ingrese una opcion: ")

        if b.es_entero(dato):
            opcion = int(dato)
        else:
            opcion = 0

        match opcion:

            case 1:
                b.cargar_datos(
                    legajos, nombres, generos,
                    notas1, notas2
                )

                cargados = True
                promedios_listos = False

                print("Datos cargados correctamente.")

            case 2:
                if cargados:
                    print("\nINFORME DE ESTUDIANTES")

                    b.recorrer_estudiantes(
                        legajos, nombres, generos,
                        notas1, notas2, promedios,
                        1, 0, promedios_listos
                    )
                else:
                    print("Primero debe cargar los datos.")

            case 3:
                if cargados:
                    b.calcular_promedios(
                        notas1, notas2, promedios
                    )

                    promedios_listos = True

                    print("Promedios calculados correctamente.")
                else:
                    print("Primero debe cargar los datos.")

            case 4:
                if cargados and promedios_listos:
                    b.ordenar(
                        legajos, nombres, generos,
                        notas1, notas2, promedios,
                        "DESC"
                    )

                    print("\nESTUDIANTES ORDENADOS POR PROMEDIO")

                    b.recorrer_estudiantes(
                        legajos, nombres, generos,
                        notas1, notas2, promedios,
                        1, 0, True
                    )
                else:
                    print("Primero cargue los datos y calcule los promedios.")

            case 5:
                if cargados and promedios_listos:
                    mayor = b.buscar_mayor(promedios)

                    print("\nESTUDIANTE/S CON MAYOR PROMEDIO")

                    b.recorrer_estudiantes(
                        legajos, nombres, generos,
                        notas1, notas2, promedios,
                        2, mayor, True
                    )
                else:
                    print("Primero cargue los datos y calcule los promedios.")

            case 6:
                if cargados:
                    legajo_buscar = b.cargar_legajo()

                    print("\nBUSQUEDA POR LEGAJO")

                    encontrados = b.recorrer_estudiantes(
                        legajos, nombres, generos,
                        notas1, notas2, promedios,
                        3, legajo_buscar, promedios_listos
                    )

                    if encontrados == 0:
                        print("No existe un estudiante con ese legajo.")
                else:
                    print("Primero debe cargar los datos.")

            case 7:
                print("Programa finalizado.")

            case _:
                print("Opcion incorrecta.")


if __name__ == "__main__":
    main()

