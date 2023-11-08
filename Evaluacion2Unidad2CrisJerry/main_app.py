# Evaluacion2 Unidad2 Desarrollo de metodo de compras en pycharm
#Cristopher Jerrybandhan Programacion Web
def agregar_compra(producto, monto, compras):
    compras.append((producto, monto))
    print(f"Compra de {producto} por ${monto} agregada correctamente.")

def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for i, (producto, monto) in enumerate(compras, start=1):
            print(f"Compra {i}: {producto} - ${monto}")


def mostrar_total(compras):
    total = sum(monto for _, monto in compras)
    print(f"Total gastado: ${total:.2f}")


def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("===========================")
        print("1. Agregar compra")
        print("===========================")
        print("2. Mostrar compras")
        print("===========================")
        print("3. Mostrar total gastado")
        print("===========================")
        print("4. Salir")
        print("===========================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = str(input("Ingrese el nombre del producto: "))
            monto = float(input("Ingrese el monto de la compra: "))
            agregar_compra(producto, monto, compras)
            total_gastado += monto

        elif opcion == "2":
            mostrar_compras(compras)

        elif opcion == "3":
            mostrar_total(compras)

        elif opcion == "4":
            print("Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    main()