def dicts_por_input():
    mydict = {}
    try:
        dict_len = int(input("Ingresa el numero de elementos para el diccionario: "))
        for i in range(dict_len):
            key_name = str(input(f"Ingresa el nombre para la clave, posicion {i}: "))
            value_amount = input(f"Ingresa el valor para la llave, posicion {i}: ")
            mydict[key_name] = value_amount
        print(mydict)
    except ValueError:
        print("Por favor, ingresa un valor de tipo entero.")