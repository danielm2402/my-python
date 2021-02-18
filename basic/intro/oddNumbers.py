# print odd numbers between two numbers

init = int(input('Inicio: '))
finish = int(input('Fin: '))

for i in range(init, finish, 1):
    value = 2*i+1
    if value < finish:
        print(value)
