import os
import PIL
from PIL import Image


#lista los formatos
def listar_formatos_soportados():
    """Muestra los formatos de imagen soportados"""
    formatos=["JPG","JPEG","PNG","GIF","BMP","TIFF","WEBP"]
    print("Formatos soportados: ")
    for formato in formatos:
        print(f'- {formato}')
    return formatos

#Convierte la imagen y la guarda en una carpeta
def convertir_imagen(ruta_imagen, formato_salida, carpeta_destino = None):
    """
    :param ruta_imagen: ruta de la imagen a convertir
    :param formato_salida: Formato al que se convertira (ej: 'PNG'
    :param carpeta_destino: Carpeta donde se guarda la imagen convertida (opcional)
    :return:
        str: Ruta de la imagen convertida
    """
    #bloque Try
    try:
     #vVrifica que la imagen exista
        if not os.path.exists(ruta_imagen):
            print(f'Error: La magen {ruta_imagen} no existe')
            return None

        # Abrir la Imagen
        imagen = Image.open(ruta_imagen)

        # Obtener informacion de la imagen original
        nombre_archivo = os.path.basename(ruta_imagen)
        nombre_base = os.path.splitext(nombre_archivo)[0]

         # Crear la carpeta de destino si no existe
        if carpeta_destino:
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

        else:
            carpeta_destino = os.path.dirname(ruta_imagen)

        # Crear ruta de salida
        formato_salida = formato_salida.lower().strip(".")
        ruta_salida = os.path.join(carpeta_destino, f"{nombre_base}.{formato_salida}")

     # Guardar la imagen en el nuevo formato
        imagen.save(ruta_salida)
        print(f'Imagen convertida y guardada en: {ruta_salida}')
        return ruta_salida

    except Exception as e:
        print(f"Error al convertir la imagen: {e}")
        return None

#multiples imagenes
def convertir_multiples_imagenes(carpeta_origen, formato_salida, carpeta_destino = None):
    """
    convierte todas las imagenes en una carpeta al formato especificado

    Args:
        Carpeta_origen: Carpeta que contiene las imagenes a convertir
        Carpeta_salida: Formato al que se convertiran las imagenes
        carpeta_salida: Carpeta donde se guardaran las imagenes convertidas (opcional)
    Returns:
        int: numero de imagenes convertidas
    """
    # verifica que la imagen exista
    if not os.path.exists(carpeta_origen):
        print(f'Error: La magen {carpeta_origen} no existe')
        return 0

    #extension de imagenes comunes
    extenciones_imagenes = [".jpg", ".jpeg", ".png", ".gif", ".bmp", '.tiff', ".webp"]

    #contador de imagens convertidas
    contador= 0

    #Recorrer todos los archivos en la carpeta
    for archivo in os.listdir(carpeta_origen):
        ruta_archivo = os.path.join(carpeta_origen, archivo)

        #verificar si es un archivo y tiene extencion de imagen
        if os.path.isfile(ruta_archivo) and any(archivo.lower().endswith(ext) for ext in extenciones_imagenes):
            #convertir la imagen
            if convertir_imagen(ruta_archivo, formato_salida, carpeta_destino):
                contador += 1

    print(f'Total de imágenes convertidas: {contador}')

    return contador

#funcion principal
def main():
    """Funcion principal del programa"""
    print("=== CONVERSOR DE IMÁGENES ===")

    #Mostrar formatos soportados
    listar_formatos_soportados()
    print("\n")
    #mostrar opciones
    print("Opciones: ")
    print("1. Convertir una imagen")
    print("2. Convertir todas las imagenes de la carpeta")
    opcion = int(input("selecione una opcion"))

    try:
        if opcion == 1:
            ruta_imagen = input("Ingrese la ruta de la imagen: ").strip()
            formato = input("Ingrese el formato a covertir: ").strip()
            carpeta_destino = input("Ingrese la carpeta a guardar (opcional)").strip() or None
            convertir_imagen(ruta_imagen, formato, carpeta_destino)
        elif opcion == 2:
            carpeta_origen = input("Ingrese la reta de la carpeta: ").strip()
            formato = input("escriba el formato a convertir: ").strip()
            carpeta_destino = input("Ingrese la carpeta de destino: ").strip() or None
            convertir_multiples_imagenes(carpeta_origen, formato, carpeta_destino)
        else:
            print("Opciones no validas")

    except ValueError:
        print("Error: Ingrese un número válido.")


if __name__ == "__main__":
    main()


