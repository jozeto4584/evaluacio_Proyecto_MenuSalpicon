def ingresar_fruta():
    while True:
        nombre = input("Nombre de la fruta: ")
        if nombre.isalpha():
            break
        else:
            print("Por favor, ingrese solo letras para el nombre de la fruta.")
    
    while True:
        while True:
            precio_unitario = input("Precio unitario de la fruta $ : ")
            if precio_unitario.isdigit():
                precio_unitario = float(precio_unitario)
                break
            else:
                print("Por favor, ingrese solo números enteros para el precio unitario.")
        while True:
            cantidad = input("Cantidad de la fruta: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)
                break
            else:
                print("Por favor, ingrese solo números enteros para la cantidad.")
        return {"nombre": nombre, "precio_unitario": precio_unitario, "cantidad": cantidad}

def valor_total_salpicon(frutas):
    total = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in frutas)
    total_formateado = "{:.2f}".format(total).rstrip('0').rstrip('.')
    print("El valor total del salpicón es $ :", total_formateado)


def fruta_mas_barata(frutas):
    if not frutas:
        print("No hay frutas registradas.")
        return
    
    fruta_mas_barata = min(frutas, key=lambda x: x["precio_unitario"])
    print("La fruta más barata es:", fruta_mas_barata["nombre"], "con un precio unitario de", fruta_mas_barata["precio_unitario"])

frutas = []

while True:
    print("*****Menu-- Salpicon --Frutas******")
    print("***********************************")
    print("Menu--------------------------Fruta")
    print("1.-Ingresa la-----------------fruta")
    print("2.-Valor-------------Total Salpicon")
    print("3.-Cual es------la fruta mas barata")
    print("4.-Cancelar------------------Pedido")
    print("***********************************")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            cantidad_frutas = input("¿Que cantidad de frutas Que Desea  agregar al salpicón? : ")
            if cantidad_frutas.isdigit():
                cantidad_frutas = int(cantidad_frutas)
                break
            else:
                print("Por favor, ingrese solo números enteros para la cantidad de frutas.")
        for _ in range(cantidad_frutas):
            frutas.append(ingresar_fruta())
    elif opcion == "2":
        valor_total_salpicon(frutas)
    elif opcion == "3":
        fruta_mas_barata(frutas)
    elif opcion == "4":
        print(" Pedido Cancelando...")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
