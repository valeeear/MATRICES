
matriz = [['-','-','-','-','-','-',], ['-','-','-','-','-','-',]]

def fnt_agregar(dato,x,y):
    if dato == 'A' and (x == 0 and y == 0):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'B' and (x == 0 and y == 1):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'C' and (x == 0 and y == 2):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'D' and (x == 0 and y == 3):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'E' and (x == 0 and y == 4):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'F' and (x == 0 and y == 5):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'G' and (x == 1 and y == 0):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'H' and (x == 1 and y == 1):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'I' and (x == 1 and y == 2):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'J' and (x == 1 and y == 3):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'K' and (x == 1 and y == 4):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    elif dato == 'L' and (x == 1 and y == 5):
        if matriz[x][y] == '-':
            matriz[x][y] = dato.upper()
    
            
            
def fnt_impresion_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()

sw = True
while sw == True:
    import os
    os.system('cls')
    fnt_impresion_matriz()
    fnt_agregar(input('Dato:  '),int(input('Fila:  ')),int(input('Columna:  ')))
