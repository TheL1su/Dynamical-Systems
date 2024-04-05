#Filip Rutka
import numpy as np
from PIL import Image as im 
import imageio

def f(x,y,u):
    t = T(x,y)
    c = np.cos(t)
    s = np.sin(t)
    return (1 + u*(x*c-y*s), u*(x*s+y*c))

def T(x,y):
    return 0.4-6/(x**2+y**2+1)

def which(x,y):
    return ((0.4+x)*1000/2.4,(2.5+y)*1000/3.5) #funkcja podajaca numer piksela dla danego punktu

images=[]
n_points = 1000000 #ilosc punktow jednej operacji
x_now = 1. 
y_now = 0.
index = 0
for u in np.arange(0.6,0.9,0.001):
    point_catcher = np.zeros((1000, 1000),dtype=int) #"licznik punktow w pikselach"
    bitmap = np.zeros((1000,1000),dtype=np.uint8) #tablica sluzaca za bit mape

    for i in range(0,n_points):
        x,y = f(x_now,y_now,u)
        x_tab = x
        y_tab = y
        x,y = which(x,y)
        if(x >=0 and x <= 999 and y <= 999 and y >= 0):
            point_catcher[int(x)][int(y)] += 1

    maxi = np.amax(point_catcher) #maksymalna ilosc punktow ktore wpadly do pojedycznych pikseli
    for i in range(1000):
        for j in range(1000):
            point_catcher[i][j] *= (255) #przeskalowanie szarosci
            point_catcher[i][j] /= maxi
            bitmap[i][j] = point_catcher[i][j]

    data = im.fromarray(bitmap) 
    data.save('zdjecia/test'+str(index)+'.png') 
    images.append(imageio.imread('zdjecia/test'+str(index)+'.png'))
    index+=1
imageio.mimsave('zdjecia/movie.gif', images)
