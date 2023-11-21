def calculadora():
    inicio_rango = int(input("Ingresa un inicio de rango: "))
    final_rango = int(input("Ingresa un final de rango: ")) + 1
    inicio_tabla = int(input("Ingresa un inicio para la tabla: "))
    final_tabla = int(input("Ingresa un final para la tabla: ")) + 1

    for i in range(inicio_rango, final_rango):
        print()
        for j in range(inicio_tabla, final_tabla):
            print(i, "x", j, "=", i*j)