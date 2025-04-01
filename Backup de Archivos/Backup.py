import zipfile
import os  # perimite trabajar con la direccion de archivos
import datetime  # permite trabajar con el tiempo


def create_name_backup():
    """genera un nombre para el archivo de backup en la fecha y hora actual"""
    # guardamos la feha y la hora, tambien le damos formato
    fecha_hora = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S")  # %Y:año,%m:mes,%d:dia, %H:hora, %M:minutos, %S:segundos
    return f'backup_{fecha_hora}.zip'


def create_backup(carpeta_origen, carpeta_destino):
    """
    Crea una archivo ZIP con el contenido de la carpeta de origen
    :param carpeta_origen: ruta de la carpeta a respaldar
    :param carpeta_destino: ruta donde se guardara el archivo backup
    :return:
        str:Ruta completa del archivo de backup creado
    """
    # Validamos que la carpeta de origan exista
    if not os.path.exists(carpeta_origen):
        return None  # no devuelve nada

    if not os.path.exists(carpeta_destino):
        print(f"Creando carpeta de  destino {carpeta_destino}...")
        os.makedirs(carpeta_destino)  # crea la carpeta en el destino

    # crear nombre del archivo de backup
    nombre_backup = create_name_backup()  # crea el nombre de la carpeta
    ruta_backup = os.path.join(carpeta_destino, nombre_backup)  # agrega a la ruta de destino el nombre de la carpeta

    # crear archivo ZIP
    print(f"Creando backup en {ruta_backup}...")

    with zipfile.ZipFile(ruta_backup, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # iteramos para que recorra todos los archivos y carpetas en la carpeta origen
        for carpeta_actual, subcarpetas, archivos in os.walk(
                carpeta_origen):  # os.walk recorre toda la carpeta ingresada
            for archivo in archivos:
                ruta_archivo = os.path.join(carpeta_actual, archivo)
                # guarda la ruta relativa en el zip
                ruta_relativa = os.path.relpath(ruta_archivo, os.path.dirname(carpeta_origen))
                zip_file.write(ruta_archivo, ruta_relativa)
                print(f"añadido: {ruta_relativa}")



def main():
    """Funcion principal del programa"""
    print("=== BACKUP AUTOMATICO ===")

    # configuracion de carpetas (se modifican estas rutas segun las necesidades)
    carpeta_origen = input("Ingrese la ruta de la carpeta a respaldar: ")
    carpeta_destino = input("Ingrese la ruta donde guardar el backup (deja en blanco para usar './backups'): ")

    # condicional que verifica si ingresamos la direccion de la carpeta de destino
    if not carpeta_destino:
        carpeta_destino = "./backups"

    # crear backup
    ruta_backup = create_backup(carpeta_origen, carpeta_destino)
    if (ruta_backup):
        print(f'\nTamaño del backup: {os.path.getsize(ruta_backup) / 1024 * 1024:.2f} MB')
        print("\n¡Backup completado con exito")


if __name__ == "__main__":
    main()
