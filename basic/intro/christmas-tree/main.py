#draw christmas tree
height = int(input('Enter an odd height:'))
if height % 2 != 0:
    for i in range(0, height, 1):
        print(' '*(height-i), end="")
        print('*'*(2*i+1))
    for i in range(0, int(height/2), 1):
        print(' '*int(((height-1)/2)), '*'*height)
