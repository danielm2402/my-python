# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

lista_contactos = list()
op = 0

while (op < 10):
    if (op == 1):
        nombre_contacto = input('Digite nombre de contacto :')
        numero_contacto = input('Digite Numero de contacto :')
        dato_contacto = False
        posicion = 0
        for c in lista_contactos:
            if (list(c)[0] == nombre_contacto):
                dato_contacto = True
                posicion = lista_contactos.index(c)

        if (dato_contacto):
            aux = list(lista_contactos[posicion])
            aux.append(numero_contacto)
            lista_contactos[posicion] = tuple(aux)
        else:
            datos_contacto = nombre_contacto, numero_contacto
            lista_contactos.append(datos_contacto)

    if (op == 2):
        nombre_eliminar = input('Digite nombre de contacto :')
        for n in lista_contactos:
            if (list(n)[0] == nombre_eliminar):  # La función List convierte una tupla a una lista
                lista_contactos.remove(n)

    if (op == 3):
        print(' -------- Lista de contactos -------')
        for c in lista_contactos:
            nombre = list(c)[0]
            print('Nombre : {}'.format(nombre))
            print(' ---- Numeros : ', list(c[1:]))

    if (op == 4):
        encuentra = False
        posicionX = 0
        nombre_buscar = input('Digite nombre de contacto :')
        for n in lista_contactos:
            if (list(n)[0] == nombre_buscar):  # La función List convierte una tupla a una lista
                encuentra = True
                posicionX = lista_contactos.index(n)

        if (encuentra):
            print('Nobre contacto {} Numero {}'.format(lista_contactos[posicionX][0], lista_contactos[posicionX][1]))
        else:
            print('Contacto no Existe')
    if (op == 5):
        opcion = 0
        for index, tupla in enumerate(lista_contactos):
            print('{} -> {}'.format(index, tupla[0]))
        opcion = int(input('Ingrese opción de contacto para agregar números: '))
        salir = True
        auxList = list(lista_contactos[opcion])
        while (salir) :
            numero = input('Ingrese numero a agregar: ')
            auxList.append(numero)
            capturaSalir = input('Desea seguir agregando más numeros? y/n:')
            if(capturaSalir=='n'):
                salir = False
        lista_contactos.pop(opcion)
        lista_contactos.insert(opcion, tuple(auxList))
    if (op == 6):
         encuentra = False
         posicionX = 0
         nombre_buscar = input('Digite nombre de contacto :')
         for n in lista_contactos:
             if (list(n)[0] == nombre_buscar):  # La función List convierte una tupla a una lista
                 encuentra = True
                 posicionX = lista_contactos.index(n)

         if (encuentra):
            opcion = 0
            opcion2 = 0
            print('Lista de números del contacto')
            for index, number in enumerate(lista_contactos[posicionX][1:]):
                print('{} -> {}'.format(index, number))
            opcion = int(input('Seleccione el número: '))
            opcion2 = int(input('Ingrese 1 si desea eliminar o 2 si desea modificar '))
            auxList = list(lista_contactos[posicionX])
            auxList.pop(opcion + 1)
            if opcion2 == 1:
               lista_contactos.pop(posicionX)
               lista_contactos.insert(posicionX, tuple(auxList))
               print(lista_contactos)
            if opcion2 == 2:
                newNumber = int(input('Digite el numero: '))
                auxList.insert(opcion+1,newNumber)
                lista_contactos.pop(posicionX)
                lista_contactos.insert(posicionX, tuple(auxList))
                print(lista_contactos)
         else:
             print('Contacto no Existe')

    if (op == 7):
        try:
            opcion = 0
            for index, tupla in enumerate(lista_contactos):
                print('{} -> {}'.format(index, tupla[0]))
            opcion = int(input('Ingrese opción de contacto para eliminar: '))
            if (opcion>=0 & opcion<=len(lista_contactos)):
                lista_contactos.pop(opcion)
            else:
                print('NUMERO NO VALIDO')
        except:
            print('Error')
    if (op == 8):
        for index, tupla in enumerate(lista_contactos):
            print('{} -> {}'.format(index, tupla[0]))
        opcion = int(input('Ingrese opción de contacto para cambiar el nombre: '))
        nombre = input('Ingrese nuevo nombre de contacto: ')
        auxList = list(lista_contactos[opcion])
        auxList.pop(0)
        auxList.insert(0, nombre)
        lista_contactos.pop(opcion)
        lista_contactos.insert(opcion, tuple(auxList))

    if (op == 9):
        numeroingresado= input('Número a buscar: ')
        encontrado = False
        pos = 0
        # enumerate para poder obtener el indice actual en cada recorrido
        for index, contacto in enumerate(lista_contactos):
            for numero in contacto[1::]:
                if numero == numeroingresado:
                    encontrado =True
                    pos=index
        if encontrado:
            print('Nombre de contacto', lista_contactos[pos][0])
            print('Numeros:', lista_contactos[pos][1::])
        else:
            print('Contacto no encontrado')

    print('--------------------------')
    print('1...Adicionar contactos')
    print('2...Eliminar contactos')
    print('3...Listar contactos')
    print('4...Buscar...Listar contactos')
    print('5...Agregar numeros a un determinado contacto')
    print('6...Eliminar o modificar un determinado numero de un contacto')
    print('7...Eliminar un contacto')
    print('8...Modificar nombre de un contacto')
    print('9...Buscar contacto por su numero')
    print('10...Salir')
    print('--------------------------')
    op = int(input('Digite su Opcion: '))
