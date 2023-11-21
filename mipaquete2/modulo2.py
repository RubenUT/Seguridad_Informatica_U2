def listas_por_input():
    list_size = (int(input("Especifica un tamanio para la lista: ")))

    list = []

    for i in range(list_size):
        num = int(input(f"Escribe el valor de la posicion {i}: "))
        list.append(num)
    print(list)