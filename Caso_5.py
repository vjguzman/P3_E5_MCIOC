# Caso 5
from caso_generico import caso_generico, gif


fp_in = "Ejemplo/frame_*.png"
fp_out = "Ejemplo.gif"

# Caso 5
# (a, b, Nx, Ny, c_in, c_sup, c_inf, c_izq, c_der, g_sup, g_inf, g_izq, g_der, caso)
 

a = 1                    # alto
b = 1                    # ancho
Nx = 30                  # numero de intervalos en x
Ny = 30                  # numero de intervalos en y

# Condiciones de borde
c_in = 5                 # T° inicial                 
c_sup = 0				 # Borde superior
c_inf = 0                # Borde inferior
c_izq = 25               # Borde izquierdo
c_der = 25			     # Borde derecho

# Gradientes
g_sup = 0                # Gradiente superior
g_inf = 0                # Gradiente inferior
g_izq = 0                # Gradiente izquierdo
g_der = 0                # Gradiente derecho

caso = "Caso_5"          # Nombre del caso

caso_generico(a, b, Nx, Ny, c_in, c_sup, c_inf, c_izq, c_der, g_sup, g_inf, g_izq, g_der, caso)