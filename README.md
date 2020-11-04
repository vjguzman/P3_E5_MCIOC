# Proyecto 3 - Entrega 5 - MCIOC
## Replicar casos 2-D para verificar
Como esta entrega estaba enfocada en replicar los casos 2-D entregados utilizando el código de la entrega pasada, el cual fue visto en ayudantía, se optó por realizar un código genérico que fuera útil para todos los casos planteados donde se iban modificando los parámetros que se presentan a continuación.
* Parámetros
(a, b, Nx, Ny, c_in, c_sup, c_inf, c_izq, c_der, g_sup, g_inf, g_izq, g_der, caso)
  * a: Alto
  * b: Ancho
  * Nx: Discretización en x
  * Ny: Discretización en y
  * c_in: Temperatura inicial
  * c_sup: Temperatura superior
  * c_inf: Temperatura inferior
  * c_izq: Temperatura izquierda
  * c_der: Temperatura derecha
  * Lo mismo ocurre para los parámetros que empiezan por "g_" pero cambia por Gradiente.
  
Además se implementó una función para gráficar la evolución en el tiempo de la temperatura para los tres puntos importantes y una función para crear el gif con todos los frames. Cabe destacar que se creó un código aparte para el caso 7 debido a que consideraba más trabajo y otros parámetros. 



## POR HACER
Descripción de como hay que cambiar las condiciones de borde, en el código.
En un mismo gráfico la evolución de la temperatura en el tiempo en los puntos 
En el caso 7 incluya, además, la temperatura ambiental en el mismo gŕafico como una linea negra punteada. 
Imágenes fijas para la distribución de temperatura en los tiempos 0h, 2h, 6h, 12h, 24h y un gif animado con toda la evolución de temperatura. 
Explique ¿como cambia el código para el caso 3-D? ¿Como se imponen las condiciones de borde?


#### Caso 5
- Parámetros
  - a = 1                    # alto
  - b = 1                    # ancho
  - Nx = 30                  # numero de intervalos en x
  - Ny = 30                  # numero de intervalos en y
  - c_in = 5                 # T° inicial                 
  - c_sup = 'solo'				   # Borde superior
  - c_inf = 'solo'           # Borde inferior
  - c_izq = 25               # Borde izquierdo
  - c_der = 25			         # Borde derecho
  - g_sup = 0                # Gradiente superior
  - g_inf = 0                # Gradiente inferior
  - g_izq = 0                # Gradiente izquierdo
  . g_der = 0                # Gradiente derecho
  - caso = "caso_5"          # Nombre del caso

- Gif.
- Gráfico evolución de temperaturas.
- Imagenes distribución de temperaturas.
- Gif distribución de temperaturas.

#### Caso 6
- Parámetros
  - a = 1                    # alto
  - b = 1                    # ancho
  - Nx = 30                  # numero de intervalos en x
  - Ny = 30                  # numero de intervalos en y
  - c_in = 30                # T° inicial                 
  - c_sup = 'solo'				   # Borde superior
  - c_inf = 'solo'           # Borde inferior
  - c_izq = 10               # Borde izquierdo
  - c_der = 'solo'			     # Borde derecho
  - g_sup = 0                # Gradiente superior
  - g_inf = 0                # Gradiente inferior
  - g_izq = 0                # Gradiente izquierdo
  . g_der = 0                # Gradiente derecho
  - caso = "caso_6"          # Nombre del caso

- Gif.
- Gráfico evolución de temperaturas.
- Imagenes distribución de temperaturas.
- Gif distribución de temperaturas.

#### Caso 7
- Parámetros
  - a = 1                    # alto
  - b = 1                    # ancho
  - Nx = 30                  # numero de intervalos en x
  - Ny = 30                  # numero de intervalos en y
  - c_in = 20                # T° inicial                 
  - c_sup = 'solo'				   # Borde superior
  - c_inf = 'solo'           # Borde inferior
  - c_izq = 'solo'           # Borde izquierdo
  - c_der = 'solo'			     # Borde derecho
  - g_sup = 0                # Gradiente superior
  - g_inf = 0                # Gradiente inferior
  - g_izq = 0                # Gradiente izquierdo
  . g_der = 0                # Gradiente derecho
  - caso = "caso_7"          # Nombre del caso

- Gif.
- Gráfico evolución de temperaturas.
- Imagenes distribución de temperaturas.
- Gif distribución de temperaturas.
