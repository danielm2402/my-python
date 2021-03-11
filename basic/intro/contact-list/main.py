# This is a sample Python script.
#--Daniel Alejandro Muñoz
#--Wilmer Ancizar Benavides

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
while True:
    try:
        lista_contactos = list()
        op = 0
        while (op < 10):
            try:
                if (op == 1):
                    nombre_contacto = input('Digite nombre de contacto :')
                    try:
                        numero_contacto = int(input('Digite Numero de contacto :'))
                        if(numero_contacto<1):
                            print("--Debe escribir un numero mayor a cero..")
                            continue
                    except ValueError:
                        print("--Debe escribir un numero--")
                        continue
                    else:
                        if(numero_contacto>0):
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
                            print("--Contacto agregado--")

            except:
                print("Error")
            try:
                if (op == 2):
                    nombre_eliminar = input('Digite nombre de contacto que desea eliminar :')
                    for n in lista_contactos:
                        if (list(n)[0] == nombre_eliminar):  # La función List convierte una tupla a una lista
                            lista_contactos.remove(n)
                            print("--Contacto eliminado--")
                        else:
                            print("--Contacto no existe--")
            except:
                print("Error")
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
                    print('Nombre contacto: {}, Numero: {}'.format(lista_contactos[posicionX][0], lista_contactos[posicionX][1]))
                else:
                    print('--Contacto no Existe--')
            if (op == 5):
                opcion5 = 0
                #auxList = list()
                for index, tupla in enumerate(lista_contactos):
                    print('{} -> {}'.format(index, tupla[0]))
                try:
                    opcion5 = int(input('Ingrese opción de contacto para agregar números: '))
                    if (opcion5 >= 0 & opcion5 <= len(lista_contactos)):
                        salir = True
                        auxList = list(lista_contactos[opcion5])
                    else:
                        print("Numero Invalido")
                    while (salir) :
                        try:
                            numero5 = int(input('Ingrese numero de contacto para agregar: '))
                            if(numero5<1):
                                print("--Debe ser mayor a cero--")
                                continue
                        except ValueError:
                            print("--Debe escribir un numero--")
                            continue
                        else:
                            break

                        print("--Numero Agregado a contacto--")
                        auxList.append(numero5)
                        capturaSalir = input('Desea seguir agregando más numeros? y/n:')
                        if(capturaSalir=='n'):
                            salir = False
                    lista_contactos.pop(opcion5)
                    lista_contactos.insert(opcion5, tuple(auxList))
                except:
                    print("Error de validacion")
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
                    if(opcion >= 0 & opcion <= len(lista_contactos)):
                        try:
                            opcion2 = int(input('Ingrese 1 si desea eliminar o 2 si desea modificar '))
                            if(opcion2 < 1 & opcion2 > 2):
                                print("Ingrese otra opcion")
                                continue
                        except ValueError:
                            print("Opcion Invalida")
                            continue

                        auxList = list(lista_contactos[posicionX])
                        auxList.pop(opcion + 1)
                        if opcion2 == 1:
                           lista_contactos.pop(posicionX)
                           lista_contactos.insert(posicionX, tuple(auxList))
                           print(lista_contactos)
                           print("--Contacto Eliminado--")
                        if opcion2 == 2:
                            newNumber = int(input('Digite el numero: '))
                            auxList.insert(opcion+1,newNumber)
                            lista_contactos.pop(posicionX)
                            lista_contactos.insert(posicionX, tuple(auxList))
                            print(lista_contactos)
                            print("Contacto Modificado")
                    else:
                        print("Opcion no valida")
                 else:
                     print('Contacto no Existe')

            if (op == 7):
                try:
                    opcion = 0
                    for index, tupla in enumerate(lista_contactos):
                        print('{} -> {}'.format(index, tupla[0]))
                    opcion = int(input('Ingrese opción de contacto para eliminar: '))
                    if (opcion >= 0 & opcion<=len(lista_contactos)):
                        lista_contactos.pop(opcion)
                    else:
                        print('NUMERO NO VALIDO')
                except:
                    print('Error')
            if (op == 8):
                try:
                    for index, tupla in enumerate(lista_contactos):
                        print('{} -> {}'.format(index, tupla[0]))
                    opcion = int(input('Ingrese opción de contacto para cambiar el nombre: '))
                    nombre = input('Ingrese nuevo nombre de contacto: ')
                    auxList = list(lista_contactos[opcion])
                    auxList.pop(0)
                    auxList.insert(0, nombre)
                    lista_contactos.pop(opcion)
                    lista_contactos.insert(opcion, tuple(auxList))
                except:
                    print("Error")

            if (op == 9):
                try:
                    numeroingresado= int(input('Número a buscar: '))
                    if(numeroingresado < 1):
                        print("Ingrese un valor mayor a cero")
                        continue
                except ValueError:
                    print("Ingrese una letra")
                    continue

                encontrado = False
                pos = 0
                # enumerate para poder obtener el indice actual en cada recorrido
                for index, contacto in enumerate(lista_contactos):
                    for numero in contacto[1::]:
                        if numero == numeroingresado:
                            encontrado =True
                            pos=index
                if encontrado:
                    print("---Encontrado---")
                    print('Nombre de contacto: ', lista_contactos[pos][0])
                    print('Numeros:', lista_contactos[pos][1::])
                else:
                    print('--Contacto no encontrado--')

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
    except ValueError:
        print("error")