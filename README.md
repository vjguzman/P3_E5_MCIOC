# Proyecto 3 - Entrega 5 - MCIOC
## Replicar casos 2-D para verificar
Esta entrega consistia en utilizar el codigo de la entrega anterior, el cual fue desarrollado en la ayudantia de la semana pasada, para recrear 7 casos con distintos CB y ver sus resultados. Para eso, se modificó el codigo para cada caso y se creó un codigo que transforme los frames en el gif correspondiente. Además se debio separar los frames 0, 2, 4, 12, 24 y 48 los que correspondian a los tiempos 0h, 2h, 6h, 12h, 24h para crear un gif animado con toda la evolución de temperatura.

Cabe destacar que el dia de hoy, Jueves 05/11, tuvimos una reunión con el profesor para resolver dudas finales con respecto al gráfico de la evolución de temperatura en el tiempo de los puntos indicados en el enunciado pues nos daban diferente, con lo que llegamos a que los puntos a utilizar correspondian los que se presentan a continuación.
- P1 (Nx/2),(Ny/4)
- P2 (Nx/2),(Ny/2)
- P3 (Nx/2),(3Ny/4)

## Caso 1
- Parámetros y CB
  - a = 1
  - b = 1
  - Nx = Ny = 30
  - T° inicial = 20°
  - CB borde superior = u_k[:, -1] = 0°
  - CB borde izquierdo = u_k[0, :] = 20°
  - CB borde inferior = u_k[:, 0] = 20°
  - CB borde derecho = u_k[-1,:] = 0°
  
<br>

- Gif.

  ![caso1](https://user-images.githubusercontent.com/69158551/98290976-2d8b0c00-1f89-11eb-9995-9005f0f6a4db.gif)
  
- Gráfico evolución de temperaturas.

  ![Grafico_Evolucion_caso1](https://user-images.githubusercontent.com/69158551/98291325-ba35ca00-1f89-11eb-8467-148ec2cca56c.png)

- Imagenes distribución de temperaturas.

- Gif distribución de temperaturas.

## Caso 2
- Parámetros y CB
  - a = 1
  - b = 1
  - Nx = Ny = 30
  - T° inicial = 20°
  - CB borde superior = u_k[:, -1] = 0°
  - CB borde izquierdo = u_k[0, :] = 20°
  - CB borde inferior = u_k[:, 0] = 20°
  - CB borde derecho = gradiente = u_k[-1,:] = u_k[-2,:] + 0*dx 
  
<br>
 
- Gif.

  ![caso2](https://user-images.githubusercontent.com/69158551/98291615-29abb980-1f8a-11eb-878d-e45b114b0b4b.gif)
  
- Gráfico evolución de temperaturas.

  ![Grafico_Evolucion_caso2](https://user-images.githubusercontent.com/69158551/98291668-43e59780-1f8a-11eb-82ff-aec546967c2f.png)
  
- Imagenes distribución de temperaturas.
- Gif distribución de temperaturas.

## Caso 3
- Parámetros y CB
  - a = 1
  - b = 1
  - Nx = Ny = 30
  - T° inicial = 10°
  - CB borde superior = u_k[:, -1] = 0 = 0°
  - CB borde izquierdo = u_k[0, :] = 20°
  - CB borde inferior = u_k[:, 0] = 20°
  - CB borde derecho = u_k[-1,:] = 20°

<br>

- Gif.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso3/caso3.gif)
  
- Gráfico evolución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso3/Grafico_Evolucion_caso3.png)
  
- Imagenes distribución de temperaturas.

- Gif distribución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso3/Distribucion_T_caso3.gif)

## Caso 4
- Parámetros y CB
  - a = 1
  - b = 0.5
  - Nx = 15
  - Ny = 30
  - T° inicial = 10°
  - CB borde superior = u_k[:, -1] = 0° 
  - CB borde izquierdo = u_k[0, :] = 20° 
  - CB borde inferior = u_k[:, 0] = 20°
  - CB borde derecho = Gradiente ==> 0 = u_k[-1,:] = u_k[-2,:] + 0*dx

- Gif.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso4/caso4.gif)

- Gráfico evolución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso4/Grafico_Evolucion_caso4.png)
  
- Imagenes distribución de temperaturas.
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso4/Imagenes%20Fijas/frame_0000.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso4/Imagenes%20Fijas/frame_0004.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso4/Imagenes%20Fijas/frame_0012.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso4/Imagenes%20Fijas/frame_0024.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso4/Imagenes%20Fijas/frame_0048.png)
  
- Gif distribución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso4/Distribucion_T_caso4.gif)

## Caso 5

- Parámetros y CB
  - a = 1
  - b = 1
  - Nx = Ny = 30
  - T° inicial = 5°
  - CB borde superior = Gradiente 0 => u_k[:, -1] = u_k[:,-2] - 0*dx
  - CB borde izquierdo = 25° => u_k[0, :] = 25
  - CB borde inferior = Gradiente 0 => _k[:, 0] = u_k[:,1] - 0*dx
  - CB borde derecho = 25° => u_k[-1,:] = 25

<br>

- Gif.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso5/caso5.gif)

- Gráfico evolución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso5/Grafico_Evolucion_caso5.png)
 
- Imagenes distribución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso5/Imagenes%20Fijas/frame_0000.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso5/Imagenes%20Fijas/frame_0004.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso5/Imagenes%20Fijas/frame_0012.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso5/Imagenes%20Fijas/frame_0024.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso5/Imagenes%20Fijas/frame_0048.png)
  
- Gif distribución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso5/distribucion_temperatura_caso5.gif)


## Caso 6

- Parámetros y CB
  - a = 1
  - b = 1
  - Nx = Ny = 30
  - T° inicial = 30°
  - CB borde superior = Gradiente 0 => u_k[:, -1] = u_k[:,-2] - 0*dx
  - CB borde izquierdo = 10° => u_k[0, :] = 10
  - CB borde inferior = Gradiente 0 => _k[:, 0] = u_k[:,1] - 0*dx
  - CB borde derecho = Gradiente 0 => u_k[-1,:] =  u_k[-2,:] - 0*dx

<br>

- Gif.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso6/caso6.gif)

- Gráfico evolución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso6/Grafico_Evolucion_caso6.png)
 
- Imagenes distribución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso6/Imagenes%20Fijas/frame_0000.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso6/Imagenes%20Fijas/frame_0004.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso6/Imagenes%20Fijas/frame_0012.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso6/Imagenes%20Fijas/frame_0024.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso6/Imagenes%20Fijas/frame_0048.png)
  
- Gif distribución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso6/Distribucion_T_caso6.gif)


## Caso 7

- Parámetros y CB
  - a = 1
  - b = 1
  - Nx = Ny = 30
  - T° inicial = 20°
  - CB borde superior = Temperatura ambiental (sinusoide con variacion de 10°, periodo de 1 día) => u_k[:, -1] =  20. + 10*(np.sin((2*3.14/T)*t))
  - CB borde izquierdo = Gradiente 0 => u_k[0, :] = u_k[0, :] = u_k[1,:] - 0*dx 
  - CB borde inferior = Gradiente 0 => _k[:, 0] = u_k[:,1] - 0*dx
  - CB borde derecho = Gradiente 0 => u_k[-1,:] =  u_k[-2,:] - 0*dx

<br>

- Gif.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso7/caso7.gif)

- Gráfico evolución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso7/Grafico_Evolucion_caso7.png)
 
- Imagenes distribución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso7/Imagenes%20Fijas/frame_0000.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso7/Imagenes%20Fijas/frame_0004.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso7/Imagenes%20Fijas/frame_0012.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso7/Imagenes%20Fijas/frame_0024.png)
  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso7/Imagenes%20Fijas/frame_0048.png)
  
- Gif distribución de temperaturas.

  ![alt text](https://github.com/vjguzman/P3_E5_MCIOC/blob/main/caso7/Distribucion_T_caso7.gif)

## ¿Como cambia el código para el caso 3-D? ¿Como se imponen las condiciones de borde?

Para cambiar el código en un caso 3D se debe agregar todo lo relacionado al eje z, como es el caso de la variable Nz que tiene el numero de intervalos a considerar, la variable dz correspondiente a la discretizacion, una variable k para realizar el (dz*k) para las coordenadas (donde dx*i y dy*j). Además se pueden agregar otras variables auxiliares de u_km1 para mostrar la evolución de la temperatura dentro del hormigon tanto en los planos XY, YZ, ZX.
Las condiciones de borde actualmente en el caso 2D son 4 variables pero para imponerlas en el caso 3D deben ser 6 variables donde se mantienen las 4 iniciales pero se deben agregar otras que consideren la profundidad.
