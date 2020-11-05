#Caso 5

from matplotlib.pylab import *
#from matplotlib.pylab import cmap
import numpy as np

# Definimos geometria

a = 1 #alto
b = 1 #ancho
Nx = 30 #numero de intervalos en x
Ny = 30 # numero de intervalos en y

dx = b/Nx
dy = a/Ny
# dx y dy tienen qye ser iguales!

if dx != dy:
    print("ERRORR  dx no es igual a dy")
    exit(-1)

h = dx

# Funcion de conveneniencia para calcular las coordenadas del punto (i,j)
def coords(i,j): return(dx*i, dy*j)
x,y = coords(4,2)


def imshowbien(u):
	imshow(u.T[Nx::-1,:], cmap=cm.coolwarm)
	cbar=colorbar(extend='both', cmap=cm.coolwarm)
	ticks = arange(0,35,5)
	ticks_Text=["{}".format(deg) for deg in ticks]
	cbar.set_ticks(ticks)
	cbar.set_ticklabels(ticks_Text)
	clim(0,30)

	xlabel('b')
	ylabel('a')
	xTicks_N = arange(0,Nx+1,3)
	yTicks_N = arange(0,Ny+1,3)
	xTicks = [coords(i,0)[0] for i in xTicks_N]
	yTicks = [coords(0,i)[1] for i in yTicks_N]
	xTicks_Text=["{0:.2f}".format(tick) for tick in xTicks]
	yTicks_Text=["{0:.2f}".format(tick) for tick in yTicks]

	xticks(xTicks_N, xTicks_Text, rotation='vertical')
	yticks(yTicks_N, yTicks_Text)
	margins(0.2)
	subplots_adjust(bottom=0.15)


u_k = zeros((Nx+1, Ny+1), dtype=double)
u_km1 = zeros((Nx+1, Ny+1), dtype=double)

# Condicion de borde inicial
u_k[:,:] = 5 #en todas las celdas

#Parametros
dt = 0.01    # s
K = 79.5     # m^2/s
c = 450      # J/Kg*C
rho = 7800   # Kg/m^3
alpha = (K*dt)/(c*rho*(dx**2))

# Loop en el tiempo
minuto = 60
hora = 60*minuto
dia = 24*hora

dt = 1*minuto
dnext_t = 0.5*hora

next_t = 0
framenum = 0

T = 1*dia
Days = 1*T # Cuantos dias quiero simunlar

graf = np.int(Days/dt)
punto_1 = np.zeros(graf)
punto_2 = np.zeros(graf)
punto_3 = np.zeros(graf)
superficie = np.zeros(graf)

def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n*multiplier)/multiplier

# Loops en el tiempo
for k in range(int32(Days/dt)):
    t =dt*(k+1)
    dias = truncate(t/dia,0)
    horas = truncate((t-dias*dia)/hora,0)
    minutos = truncate((t-dias*dia - horas*hora)/minuto,0)
    titulo = "k = {0:05.0f}".format(k) + " t = {0:02.0f}d {1:02.0f}h {2:02.0f}m ".format(dias,horas,minutos)
    
    # CB esenciales, se repiten en cada iteracion
    u_k[0, :] = 25                      #izq
    u_k[:, 0] = u_k[:,-2] + 0*dx        #inf
    u_k[:, -1] = u_k[:,-2] + 0*dx       #sup
    u_k[-1,:] = 25                      # der

    
    # Loop en el espadio i = 1....n-1
    for i in range (1,Nx):
        for j in range(1,Ny):
            
            #Algoritmo de diferencias finitas  2-D para difusion

            #Laplaciano
            nabla_u_k = (u_k[i-1,j] + u_k[i+1,j] + u_k[i,j-1] + u_k[i,j+1] -4*u_k[i,j]) /h**2
            
            #Forward Euler
            u_km1[i,j] = u_k[i,j] + alpha*nabla_u_k

    # Avanzar la solucion a k+1
    u_k = u_km1
    
    # CB denuevo para asegurar cumplimiento
    u_k[0, :] = 25                      #izq
    u_k[:, 0] = u_k[:,-2] + 0*dy        #inf
    u_k[:, -1] = u_k[:,-2] + 0*dy       #sup
    u_k[-1,:] = 25                      # der

    # Puntos para graficar evolución
    punto_1[k] = u_k[int(Nx/2),int(Ny/2)]
    punto_2[k] = u_k[int(Nx/2),int(3*Ny/4)]
    punto_3[k] = u_k[int(3*Nx/4),int(3*Ny/4)]
    superficie[k] = u_k[int(Nx/2),-1]
    
    #Grafico en d_next
    if t >= next_t:
        figure(1)
        imshowbien(u_k)
        title(titulo)
        savefig("caso5/frame_{0:04.0f}.png".format(framenum))
        framenum +=1
        next_t += dnext_t
        close(1)

show()

# ---------------------------------
import glob
from PIL import Image
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r"(\d+)", text)]

# Funcion para el gif
def gif(fp_in, fp_out):
    listaImagenes = sorted(glob.glob(fp_in))
    print("sorted(glob.glob(fp_in)): ", listaImagenes)
    listaImagenes.sort(key=natural_keys)
    print("listaImagenes: ", listaImagenes)
    img, *imgs = [Image.open(f) for f in listaImagenes]
    img.save(fp=fp_out, format="GIF", append_images=imgs, save_all=True, duration=150, loop=0)

# GIF
fp_in = "caso5/frame_*.png"
fp_out = "caso5.gif"
gif(fp_in, fp_out)

# Grafico evolución de temperatura
figure(2)
t_evolucion = np.arange(0, int(Days/dt), 1)
plot(t_evolucion, punto_1, label='N/4', color= 'orange')
plot(t_evolucion, punto_2, label='2N/4', color= 'green')
plot(t_evolucion, punto_3, label='3N/4', color= "red")
plot(t_evolucion, superficie, label='superficie', color= "blue")
legend(loc="upper right")
title("Evolución de temperatura en puntos")
savefig(f"caso5/Grafico_Evolucion_caso5.png")
show()
