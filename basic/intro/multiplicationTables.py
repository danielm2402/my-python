# Find the multiplication tables given a starting number and an ending number

initialTable = int(input('Initial table: '))
finalTable = int(input('Final Table: '))

for i in range(initialTable, finalTable+1, 1):
    for j in range(1, 11, 1):
        print("{}*{}={}".format(i, j, i*j))