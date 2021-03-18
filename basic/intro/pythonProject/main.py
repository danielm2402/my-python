carros = {'xtw-123': {
    'Propietario': 'Jose perales', 'Referencia': 'Mazda 3', 'Modelo': 2011, 'marca': 'Mazda', 'Valor': 12222,
    'Ventas': {
        'Fecha': '12-12-2011', 'valor': 222222, 'cliente': 'Juanito'}
},

    'mtr-981': {
        'Propietario': 'Andres Figueroa', 'Referencia': 'Ferrari', 'Modelo': 2019, 'marca': 'Ferrari x100',
        'Valor': 91812,
        'Ventas': {
            'Fecha': '12-12-2019', 'valor': 922222, 'cliente': 'Elmo'}
    },

    'rw-983': {
        'Propietario': 'Yan Mioko', 'Referencia': 'Chevrolet tucano', 'Modelo': 1993, 'marca': 'Danz', 'Valor': 102222,
        'Ventas': {
            'Fecha': '12-12-2011', 'valor': 10191910, 'cliente': 'Eltiorico'}
    },
    'tqw-103': {
        'Propietario': 'toluca nitoma', 'Referencia': 'Mazerati 12', 'Modelo': 2014, 'marca': 'Maseratti',
        'Valor': 12578,
        'Ventas': {
            'Fecha': '19-05-2016', 'valor': 112092, 'cliente': 'Alejandro'}
    }

}


def listarAutos():
    for i in carros:
        print("Auto de placa : ", i, "   ")
        print(carros[i])
        print("\n")
def anadirAuto():
    placa = input("Nombre de la placa")
    confir = False
    for i in carros:
        # print(i)
        if i == placa:
            confir = True

    if confir == False:
        nombre_dueno = input("Digite el nombre del dueno")
        Referencia = input("Digite la referencia del auto")
        Modelo = input("Digite el modelo del auto")
        marca = input("Digite la marca del auto")
        valor = input("Digite el valor del auto")

        carros[placa] = {'Propietario': nombre_dueno, 'Referencia': Referencia, 'Modelo': Modelo, 'marca': marca,
                         'valor': valor, 'Ventas': []}

    else:

        print("Pri ya existe el auto")
def buscarAuto():
    placa_auto = input("Digite la placa del auto")
    confirmar = False
    info = carros.get(placa_auto)
    if info != None:
        print(info)
        return info
    else:
        print("No existe el auto con esa placa")
        return info
    print()
def listarVentasDeUnVehiculo():
    ventas = []
    placa_auto = input("Digite la placa del auto: ")
    if placa_auto in carros:
        print(carros[placa_auto]['Ventas'])
    else:
        print('No existe el vehiculo')

lista = []


def anadirVenta():
    placa_auto = input("Digite la placa del auto")
    confir = False
    for i in carros:

        if i == placa_auto:
            confir = True
    if confir == True:

        ventas = carros[placa_auto]['Ventas']
        print(len(ventas))
        if len(ventas) > 0:
            lista.append(ventas)

        fecha = input("Digite la fecha de venta")
        valor = input("Digite el valor del auto")
        cliente = input("Digite el nuevo dueno del auto")
        updateVentas = {'Fecha': fecha, 'valor': valor, 'cliente': cliente}
        lista.append(updateVentas)
        carros[placa_auto]['Ventas'] = lista
    else:
        print("No existe ese carro")


def eliminarAuto():
    placa_auto = input("Digite la placa del auto")
    confir = False
    for i in carros:
        if i == placa_auto:
            confir = True
    if confir == True:
        elim = carros.pop(placa_auto)
    else:
        print("No existe esa placa")


opc = 0
while opc != 7:
    if opc == 1:  ## anadir
        print()
        anadirAuto()
    if opc == 2:  ## buscar
        print()
        buscarAuto()

    if opc == 3:  ## eliminar
        print()
        eliminarAuto()

    if opc == 4:  ## editar
        print()
        anadirVenta()

    if opc == 5:  # mostrar
        listarAutos()
    if opc == 6:
        listarVentasDeUnVehiculo()
    print("-------------------------------------------------------------")
    print("1. Anadir auto")
    print("2. buscar auto")
    print("3. eliminar auto")
    print("4. Anadir venta")
    print("5. Listar todo los autos")
    print("6. Listar ventas de un vehiculo")
    print("7. Salir")
    print("-------------------------------------------------------------")

    opc = input("Digite una opcion")
    opc = int(opc)

"""
1..Adicionar ventas, un carro puede tener varias ventas
2..Poder moficicar el valor de una venta
3..Poder eliminar una venta
4..poder listar la ventas que ha tenido un vehiculo especifico
5..poder modificar los datos del vehiculo

"""

