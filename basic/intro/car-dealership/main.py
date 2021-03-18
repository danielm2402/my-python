
vehicles = {
    'xtw-123': {
    'Propietario': 'Jose perales', 'Referencia': 'Mazda 3', 'Modelo': 2011, 'marca': 'Mazda', 'Valor': 12222,
    'Ventas': [{
        'Fecha': '12-12-2011', 'valor': 222222, 'cliente': 'Juanito'}]
},

    'mtr-981': {
        'Propietario': 'Andres Figueroa', 'Referencia': 'Ferrari', 'Modelo': 2019, 'marca': 'Ferrari x100',
        'Valor': 91812,
        'Ventas': [{
            'Fecha': '12-12-2019', 'valor': 922222, 'cliente': 'Elmo'}]
    },

    'rw-983': {
        'Propietario': 'Yan Mioko', 'Referencia': 'Chevrolet tucano', 'Modelo': 1993, 'marca': 'Danz', 'Valor': 102222,
        'Ventas': [{
            'Fecha': '12-12-2011', 'valor': 10191910, 'cliente': 'Eltiorico'}]
    },
    'tqw-103': {
        'Propietario': 'toluca nitoma', 'Referencia': 'Mazerati 12', 'Modelo': 2014, 'marca': 'Maseratti',
        'Valor': 12578,
        'Ventas': [{
            'Fecha': '19-05-2016', 'valor': 112092, 'cliente': 'Alejandro'}]
    },
}

def listVehicles():
    for i in vehicles:
        print("Car Plate : ", i, "   ")
        print(vehicles[i])
        print("\n")
def addVehicle():
    placa = input("Car plate: ")
    confir = False
    for i in vehicles:
        # print(i)
        if i == placa:
            confir = True

    if confir == False:
        nombre_dueno = input("owner's name: ")
        Referencia = input("Ref: ")
        Modelo = input("Model: ")
        marca = input("Brand Car: ")
        valor = input("Car Value: ")

        vehicles[placa] = {'Propietario': nombre_dueno, 'Referencia': Referencia, 'Modelo': Modelo, 'marca': marca,
                         'valor': valor, 'Ventas': []}

    else:
        print("The car already exists")
def findVehicle():
    placa_auto = input("Car plate: ")
    confirmar = False
    info = vehicles.get(placa_auto)
    if info != None:
        print(info)
        return info
    else:
        print("Not found")
        return info
    print()
def listSales():
    placa_auto = input("Car plate: ")
    if placa_auto in vehicles:
        for length,venta in enumerate(vehicles[placa_auto]['Ventas']):
            print('{}. {}'.format(length,venta))
        venta = int(input('Select a sale: '))
        print('Select an option: ')
        print('1. Delete')
        print('2 Update')

        o = int(input('Select an option: '))
        if o == 1:
            vehicles[placa_auto]['Ventas'].pop(venta)
        if o == 2:
            fecha = input("Digite la fecha de venta: ")
            valor = input("Digite el valor del auto: ")
            cliente = input("Digite el nuevo dueno del auto:")
            vehicles[placa_auto]['Ventas'][venta]= {'Fecha': fecha, 'valor': valor, 'cliente': cliente}

    else:
        print('Error, not found')
lista = []
def addSale():
    placa_auto = input("Digite la placa del auto")
    confir = False
    for i in vehicles:

        if i == placa_auto:
            confir = True
    if confir == True:

        ventas = vehicles[placa_auto]['Ventas']
        print(len(ventas))
        if len(ventas) > 0:
            lista.append(ventas)

        fecha = input("Digite la fecha de venta")
        valor = input("Digite el valor del auto")
        cliente = input("Digite el nuevo dueno del auto")
        updateVentas = {'Fecha': fecha, 'valor': valor, 'cliente': cliente}
        vehicles[placa_auto]['Ventas'].append(updateVentas)
    else:
        print("No existe ese carro")
def deleteVehicle():
    placa_auto = input("Digite la placa del auto")
    confir = False
    for i in vehicles:
        if i == placa_auto:
            confir = True
    if confir == True:
        elim = vehicles.pop(placa_auto)
    else:
        print("No existe esa placa")
def updateVehicle():
    placa_auto = input("Enter Car Plate : ")
    if placa_auto in vehicles:
        nombre_dueno = input("owner's name: ")
        Referencia = input("Ref: ")
        Modelo = input("Model: ")
        marca = input("Brand Car: ")
        valor = input("Car Value: ")
        vehicles[placa_auto]={'Propietario': nombre_dueno, 'Referencia': Referencia, 'Modelo': Modelo, 'marca': marca,
                         'valor': valor, 'Ventas': vehicles[placa_auto]['Ventas']}
    else:
        print('Error, Vehicle not found')

opc = 0
while opc != 8:
    if opc == 1:
        addVehicle()
    if opc == 2:
        findVehicle()
    if opc == 3:
        deleteVehicle()
    if opc == 4:
        addSale()
    if opc == 5:
        listVehicles()
    if opc == 6:
        listSales()
    if opc == 7:
        updateVehicle()
    print("-------------------------------------------------------------")
    print("1. Add Vehicle")
    print("2. Find Vehicle")
    print("3. Delete Vehicle")
    print("4. Add Sale")
    print("5. List All Vehicles")
    print("6. List Sales")
    print("7. Update Vehicle")
    print("8. Exit")
    print("-------------------------------------------------------------")
    opc = input("Enter a menu option: ")
    if opc.isdigit() == True:
        opc = int(opc)


