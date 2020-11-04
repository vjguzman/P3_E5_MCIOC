from matplotlib.pylab import *
#from matplotlib.pylab import cmap
import numpy as np

# Funcion de conveneniencia para calcular las coordenadas del punto (i,j)
def coords(i,j,dx,dy): 
    return(dx*i, dy*j)

# Funcion para graficar
def imshowbien(u, Nx, Ny, dx, dy):
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
    xTicks = [coords(i,0,dx,dy)[0] for i in xTicks_N]
    yTicks = [coords(0,i,dx,dy)[1] for i in yTicks_N]
    xTicks_Text=["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text=["{0:.2f}".format(tick) for tick in yTicks]

    xticks(xTicks_N, xTicks_Text, rotation='vertical')
    yticks(yTicks_N, yTicks_Text)
    margins(0.2)
    subplots_adjust(bottom=0.15)

# Funcion para truncar
def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n*multiplier)/multiplier


# Funcion para los casos
def caso_generico(a, b, Nx, Ny, c_in, c_sup, c_inf, c_izq, c_der, g_sup, g_inf, g_izq, g_der, caso):

    dx = b/Nx
    dy = a/Ny

    dt = 0.01    # s
    K = 79.5     # m^2/s
    c = 450      # J/Kg*C
    rho = 7800   # Kg/m^3
    alpha = (K*dt)/(c*rho*(dx**2))


    # dx y dy tienen qye ser iguales!
    if dx != dy:
        return(print("ERRORR  dx no es igual a dy"))
        exit(-1)

    h = dx

    x = 4*dx
    y = 2*dy

    u_k = zeros((Nx+1, Ny+1), dtype=double)
    u_km1 = zeros((Nx+1, Ny+1), dtype=double)

    # Condicion de borde inicial
    u_k[:,:] = c_in    #en todas las celdas

# ---------------------------------
    # Loop en el tiempo
    minuto = 60
    hora = 60*minuto
    dia = 24*hora

    dt = 1*minuto
    dnext_t = 0.5*hora

    next_t = 0
    framenum = 0

    T = 1*dia
    Days = 1*T # Cuantos dias quiero simular

    # Graficar evolucion de temperatura en puntos importantes
    
    graf = np.int(Days/dt)
    punto_1 = np.zeros(graf)
    punto_2 = np.zeros(graf)
    punto_3 = np.zeros(graf)
    superficie = np.zeros(graf)

    # Loops en el tiempo
    for k in range(int32(Days/dt)):
        t = dt*(k+1)
        dias = truncate(t/dia,0)
        horas = truncate((t-dias*dia)/hora,0)
        minutos = truncate((t-dias*dia - horas*hora)/minuto,0)
        titulo = "k = {0:05.0f}".format(k) + " t = {0:02.0f}d {1:02.0f}h {2:02.0f}m ".format(dias,horas,minutos)
        
        # CB esenciales, se repiten en cada iteracion
        u_k[0, :] = c_izq + g_izq*dx                       #izq
        u_k[:, 0] = c_inf + g_inf*dx                       #inf
        u_k[:, -1] = c_sup + g_sup*dx                      #sup

        if c_sup != 7:
            u_k[-1,:] = u_k[-2, :] + g_der*dx              #der
        
        if c_sup == 7:
            seno = (2*int(int(3.14)/T)*t)
            caso_superior = 20 + 10*np.sin(seno)
            u_k[-1,:] = caso_superior


        # Loop en el espacio i = 1....n-1
        for i in range (1,Nx):
            for j in range(1,Ny):
                #Algoritmo de diferencias finitas  2-D para difusion
#---------------
                #Laplaciano
                nabla_u_k = (u_k[i-1,j] + u_k[i+1,j] + u_k[i,j-1] + u_k[i,j+1] -4*u_k[i,j]) /h**2
#---------------                
                #Forward Euler
                u_km1[i,j] = u_k[i,j] + alpha*nabla_u_k

        # Avanzar la solucion a k+1
        u_k = u_km1
        
        # CB denuevo para asegurar cumplimiento
        u_k[0, :] = c_izq + g_izq*dx                       #izq
        u_k[:, 0] = c_inf + g_inf*dx                       #inf
        u_k[:, -1] = c_sup + g_sup*dx                      #sup

        if c_sup != 'caso7':
            u_k[-1,:] = u_k[-2, :] + g_der*dx              #der
        
        if c_sup == 7:
            seno = (2*int(int(3.14)/T)*t)
            caso_superior = 20 + 10*np.sin(seno)
            u_k[-1,:] = caso_superior


        # Puntos para graficar evolución
        punto_1[k] = u_k[int(Nx/2),int(Ny/2)]
        punto_2[k] = u_k[int(Nx/2),int(3*Ny/4)]
        punto_3[k] = u_k[int(3*Nx/4),int(3*Ny/4)]
        superficie[k] = u_k[int(Nx/2),-1]

        #Grafico en d_next
        if t > next_t:
            figure(1)
            imshowbien(u_k, Nx, Ny, dx, dy)
            title(titulo)
            savefig(f"{caso}/frame_{0:04.0f}.png".format(framenum))
            framenum +=1
            next_t += dnext_t
            close(1)
    
    return punto_1, punto_2, punto_3, superficie


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

def puntos(punto_1, punto_2, punto_3, superficie, caso):
    # Loop en el tiempo
    minuto = 60
    hora = 60*minuto
    dia = 24*hora

    dt = 1*minuto
    dnext_t = 0.5*hora

    next_t = 0
    framenum = 0

    T = 1*dia
    Days = 1*T # Cuantos dias quiero simular

    t_evolucion = np.arange(0, int(Days/dt), 1)
    plot(t_evolucion, punto_1, label='Punto 1 -> (a/2, b/2)', color= 'orange')
    plot(t_evolucion, punto_2, label='Punto 2 -> (a/2, 3b/4)', color= 'green')
    plot(t_evolucion, punto_3, label='Punto 3 -> (3a/4, 3b/4)', color= "red")
    plot(t_evolucion, superficie, label='Nivel de superficie', color='blue')
    legend(loc="upper right")
    title("Evolución de temperatura en puntos")
    savefig(f"{caso}/Grafico_Evolucion_{caso}.png")