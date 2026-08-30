from datos import reservas

def imprimir_reservas():
    """1. Muestra todas las reservas registradas."""
    print("=================================")
    print("       Lista de Reservas         ")
    print("=================================")
    for reserva in reservas:
        print(f"ID: {reserva['id']}")
        print(f"Cliente: {reserva['cliente']}")
        print(f"Destino: {reserva['destino']}")
        print(f"Personas: {reserva['personas']}")
        print(f"Precio: C${reserva['precio']}")
        print("=================================")

def agregar_reserva(id_reserva, cliente, destino, personas, precio):
    """2. Agrega una nueva reserva."""
    nueva = {
        "id": id_reserva,
        "cliente": cliente,
        "destino": destino,
        "personas": personas,
        "precio": precio
    }
    reservas.append(nueva)
    print(f"Reserva {id_reserva} agregada con éxito.")

def buscar_por_cliente(cliente_buscar):
    """3. Busca reservas asociadas a un cliente."""
    print(f"\n--- Búsqueda para: {cliente_buscar} ---")
    encontrado = False
    for r in reservas:
        if cliente_buscar.lower() in r['cliente'].lower():
            print(f"ID: {r['id']} | Destino: {r['destino']} | Precio: C${r['precio']}")
            encontrado = True
    if not encontrado:
        print("No se encontraron reservas para este cliente.")

def calcular_ingreso_total():
    """4. Calcula la suma total de las reservas."""
    total = sum(r['precio'] for r in reservas)
    print(f"\n Total ingresos: C${total}")
    return total

def eliminar_reserva(id_eliminar):
    """5. Elimina una reserva por su ID."""
    for r in reservas:
        if r['id'] == id_eliminar:
            reservas.remove(r)
            print(f"\nReserva {id_eliminar} eliminada correctamente.")
            return
    print(f"\n No se encontró la reserva con ID: {id_eliminar}")
