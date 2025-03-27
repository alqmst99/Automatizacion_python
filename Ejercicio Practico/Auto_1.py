import os
import shutil

from datetime import datetime



#formatea fecha año-mes-día
fecha= datetime.now().strftime("%Y-%m-%d")

print(fecha)

# declara nueva carpeta
nueva_carpeta = f'{fecha}_Archivo'

print(os.path.exists(nueva_carpeta))
#condicional que verifica que la carpeta no exista antes de crear
if not os.path.exists(nueva_carpeta):
    #os.makedirs -> crea una nueva carpeta
    os.makedirs(nueva_carpeta)
    print(f'Carpeta {nueva_carpeta} creada.')

#mover archivos de una carpeta a otra

#declaramos Carpeta de origen, se pone la direccion completa
carpeta_origen= "C:\\Users\\Nahue\\OneDrive\\Escritorio\\develop's\\python\\Automatizacion Python\\Ejercicio Practico\\Archivo"

carpeta_destino = "C:\\Users\\Nahue\\OneDrive\\Escritorio\\develop's\\python\\Automatizacion Python\\Ejercicio Practico\\2025-03-27_Archivo"
#declarar contador
contador= 0
i=0
#iteramos el archivo de carpeta_origen
#os.listdir -> crea una lista de direccion path carpeta_origen
for archivo in os.listdir(carpeta_origen):
    i+=1
    #archivo guarda
    print(archivo)
    #en lista con la direccion de la carpeta y los
    #guarda en una variable. imprime la direccion completa con el archivo
    origen = os.path.join(carpeta_origen, archivo)
    print(f'direccion {i}: {origen}')
#hacemos lo mismo, con la carpeta de destino y copiamos los archivos
    destino= os.path.join(nueva_carpeta,archivo)
    print(f'direcciones destino {i}: {destino}')

    #movemos los archivos de carpeta_origen a nueva carpeta
    #shutil.move(archivos de origen, direcciones de destino)
    shutil.move(origen, destino)
    contador += 1

    print(f'Se movieron {contador} archivos a la carpeta {nueva_carpeta}.')

#lo mismo pero con un filtro para que solo busque y copie .txt
for archivos in os.listdir(carpeta_destino):
    i+=1
    #archivo guarda
    print(archivos)

    #Condicional que da true si encuentra los que terminan en .txt
    #endswith("")-> busca al final del String
    if archivos.endswith(".txt"):
        # en lista con la direccion de la carpeta y los
        # guarda en una variable. imprime la direccion completa con el archivo
        origen = os.path.join(carpeta_origen, archivos)
        print(f'direccion {i}: {origen}')
        # hacemos lo mismo, con la carpeta de destino y copiamos los archivos
        destino = os.path.join(nueva_carpeta, archivos)
        print(f'direcciones destino {i}: {destino}')

        # movemos los archivos de carpeta_origen a nueva carpeta
        # shutil.move(archivos de origen, direcciones de destino)
        shutil.move(destino, origen)
        contador += 1
        print(f'Se movieron {contador} archivos a la carpeta {carpeta_destino}.')