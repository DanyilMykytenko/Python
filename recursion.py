def drawLine(size):
    for i in range(size):
        print('*', end='')

def drawFrame(size):
    for i in range(size):
        if i == 0 or i == size-1:
            print('*', end='')
        else:
            print(' ', end='')

def drawSquare(size, i):
    if i == 0 or i == size-1:
        drawLine(size)
    else:
        drawFrame(size)
    i = i+1
    if i < size:
        print()
        drawSquare(size, i)

drawSquare(5, 0)
