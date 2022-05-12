#Nama  : Novita Nurul Hidayati
#NIM   : 20051397001
#Kelas : MI 2020 A

import matplotlib.pyplot as plt
plt.title("Algoritma Bresenham")
plt.xlabel("X")
plt.ylabel("Y")

def bres(x1, y1, x2, y2):
    #Menentukan garis x dan y
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    #Menghitung nilai p
    p = 2 * dy - dx
    print('x = %s, y = %s' % (x, y))

    #Menentukan titik koordinat x dan y
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx):
        #Menentukan nilai x dan y
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print('x = %s, y = %s' % (x, y))
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()

def main():
    x1 = int(input('Masukkan x1 = '))
    y1 = int(input('Masukkan y1 = '))
    x2 = int(input('Masukkan x2 = '))
    y2 = int(input('Masukkan y2 = '))

    bres(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
