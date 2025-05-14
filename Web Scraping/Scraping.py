import csv

import requests
from bs4 import BeautifulSoup

"""
El Scrap inspeciona todo lo que es codigo HTML de la pagina.
"""
filtro = ''


def obtener_html(url):
    """
    Obtiene el contenido HTML de una URL
    :rtype: object
    :arg:
        url: La URL de la pagina a descarga
    :return:
        str: El Contenido HTML de la pagina, o None si hay error
    """
    try:
        # Configuracion del User-Agent para evitar bloqueos, nos permite evitar ciertos bloques de pagina, basicamente simula el compertamiento humano
        headers = {
            # user agent
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        # realizar la peticion GET, timeout es el tiempo de espera sin recibir informacion, timeout= 10 espera 10 (s)  hasta que reciba el ok
        req = requests.get(url, headers=headers, timeout=10)

        # verificar si la operacion fue exsitosa
        if req.status_code == 200:  # verifica que el request de status 200 (OK)
            return req.text  # manda el texto de la respuesta OK
        else:
            print(f'Error al obtener la pagina: codigo de estado {req.status_code}')
            return None
    # manejo de los error que pueden ocurrir dentro de Try, es como el catch en java
    except Exception as e:
        print(f'error al obtener la pagina :{e}')
        return None


# print(obtener_html("https://www.emol.com/"))


""" Con beautiful soup vamos a crear una funcion para extraer los titulos del HTML  """


def extraer_titulos_noticias(html):
    """
    Extrae lostitulos de noticas de una pagina HTML
    con beautifulSoup se pueden hacer muchisimas mas funciones
    :arg:
        html: el contenido HTML de la pagina

    :returns:
    list: Lista de titulos de noticas encontradas
    """
    """
    1- inspeccionamos el codigo html,para ver con que tag (etiqueta) 
    se tienen los titulos de las noticias, generalmente 
    son H2 o H3.
    se va a tomar todo el contenido de esas tags
    """
    # inicializamos BeautifulSoup
    """
    le euntregamos el HTML y la guardamos en la variable soup
    se utiliza el 'html.parser' para que lo reconosca bien
    """
    soup = BeautifulSoup(html, 'html.parser')

    # buscar todos los elementos que podrian contener titulos de noticias
    # Nota: Estos selectores songenericos y pueden nesecitar ajustes segun el sitio web
    titulos = []

    # Buscams los elementos h1, h2, h3 que podrian contener titulos
    # Utilizamos un bucle for para filtrar y extraer los tags que necesitamos
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        # filtrar solo los que parecen ser titulos de noticias ( por ejemplo, con ciertas longitudes)
        if heading.text.strip() and len(heading.text.strip()) > 15:
            titulos.append(heading.text.strip())
    # Buscar tambien en elementoscon clases comunes para titulos de noticias
    for elemento in soup.select('.title, .article-title, .news-title .andes-visually-hidden .poly-reviews__rating'):
        # filtra los titulos que ya existen en la lista
        if elemento.text.strip() and elemento.text.strip() not in titulos:
            titulos.append(elemento.text.strip())

    return titulos


html = obtener_html("https://listado.mercadolibre.com.ar/smart-tv#trends_tracking_id=a3f4f73a-77e0-40e7-b58d-263442dbc538&component_id=MOST_WANTED")

titulo = extraer_titulos_noticias(html)
title = ''
#Revisar y mejorar en el futuro como completar las imprecion de los numeros
# for t in titulo:
#     palabra = 'pulgadas'
#     pregunta = ['¿Cuál es la diferencia entre Smart Hub y Smart TV?', 'Todo sobre Smart tv']
#     if palabra.lower() in t.lower():
#         title = t


# extracion de Span y calificacion

# def extraer_estrellas(html):
#     """
#     Extrae lostitulos de noticas de una pagina HTML
#     con beautifulSoup se pueden hacer muchisimas mas funciones
#     :arg:
#         html: el contenido HTML de la pagina
#
#     :returns:
#     list: Lista de titulos de noticas encontradas
#     """
#     """
#     1- inspeccionamos el codigo html,para ver con que tag (etiqueta)
#     se tienen los titulos de las noticias, generalmente
#     son H2 o H3.
#     se va a tomar todo el contenido de esas tags
#     """
#     # inicializamos BeautifulSoup
#     """
#     le euntregamos el HTML y la guardamos en la variable soup
#     se utiliza el 'html.parser' para que lo reconosca bien
#     """
#     sopa = BeautifulSoup(html, 'html.parser')
#
#     # buscar todos los elementos que podrian contener titulos de noticias
#     # Nota: Estos selectores songenericos y pueden nesecitar ajustes segun el sitio web
#     estrellas = []
#
#     # Buscams los elementos h1, h2, h3 que podrian contener titulos
#     # Utilizamos un bucle for para filtrar y extraer los tags que necesitamos
#     for heading in sopa.find_all(['span']):
#         # filtrar solo los que parecen ser estrellas ( por ejemplo, con ciertas longitudes)
#         if heading.text.strip() and len(heading.text.strip()) > 12:
#             estrellas.append(heading.text.strip())
#     # Buscar tambien en elementoscon clases comunes para estrellas
#     for elemento in sopa.select('andes-visually-hidden poly-reviews__rating'):
#         # filtra las estrellas que ya existen en la lista
#         if elemento.text.strip() and elemento.text.strip() not in estrellas:
#             estrellas.append(elemento.text.strip())
#
#     return estrellas


def extraer_articulos(html):
    """
    Args:
        html: El contenido HTML de la pagina

    :return:
    list: Lista de diccionarios con informacion de los articulos
    """

    # Crear el objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Listas para almacenar los articulos
    articulos = []

    # Buscar elementos que podrían ser artículos
    # Nota: Estos selectores son génericos y pueden necesitar ajustes según el sitio web
    for articulo_elem in soup.select('article, .article, .post, .new-item'):
        articulo= {}

        # Extraer titulo
        titulo_elem = articulo_elem.find(['h1','h2','h3']) or articulo_elem.select_one('.title, .headline')
        if titulo_elem:
            articulo['titulo'] = titulo_elem.text.strip()
        else:
            continue #Si no hay articulo pasa al siguiente

        # Extraer fecha si está disponible
        fecha_elem = articulo_elem.select_one('.date, .time, .published, .timestamp')
        articulo['fecha'] = fecha_elem.text.strip() if fecha_elem else ""

        # Extraer resumen si está disponible
        resumen_elem = articulo_elem.select_one('.summaty, .excerpt, .description, .snippet, p')
        articulo['resumen']= resumen_elem.text.strip() if resumen_elem else ""

        # Añadir a la lista de artículos
        articulos.append(articulo)

    return articulos

def guardar_en_csv(datos, nombre_archivo):
    """
    Guarda ua lista de diccionarios en un archivo CSV
    :arg:
        datos: Listade diccionarios con los datos a guardar
        nombre_archivo: Nobre del archivo CSV a crear

    :return:
        bool: True si se guardo correctamente, False en caso contrario
    """
    try:
        # Verificar que hay datos para guardar
        if not datos:
            print("No hay datos para guardar.")
            return False

        # Obtener los nombres de las columnas del primer diccionario
        columnas = datos[0].keys()

        # Escribier en el archivo CSV
        with open(nombre_archivo, 'w', newline='', encoding='utd-8') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=columnas)
            writer.writeheader() # Escribir encabezados
            writer.writerow(datos) # Escribir filas de datos

        print(f"Datos guardaos exitosamente en '{nombre_archivo}'")
        return True
    except Exception as e:
        print(f"Datos guardados exitosamente en '{nombre_archivo}'")
        return False

def main():
    """Funcion principal del programa"""
    print("=== WEB SCRAPER Básico ===")

    # Solicitar la URL al usuario
    url = input("Ingresa la URL de la página web a analizar: ")

    #Solicitar el HTML de la pagina
    print (f'Descargando contenido de {url}...')
    html = obtener_html(url)

    if not html:
        print("No se pudo obtener el contenido de la página.")
        return
    print("Contenido descargado correctamente")

    # Menu de opciones
    print("\nOpciones:")
    print("1. Extraer títulos de noticias")
    print("2. Extraer articulos completos")

    opcion = input("opcion (1-2): ")

    if opcion == "1":
        # Extraer titulos de noticias
        print("\nExtrayendo t'itulos de noticias...")
        titulos = extraer_titulos_noticias(html)

        print(f"\nSe encontraron {len(titulos)} titulos:")
        for i, titulo in enumerate (titulos, 1):
            print(f"{i}. {titulo}")

        # Guardar en CSV
        if titulo and input("\n¿Deseas guardar los títulos en un archivo CVS? (s/n): ").lower() == 's':
            #convertir la lista de títulos a una lista de diccionarios
            datos =[{'numero': i, 'titulo': titulo} for i, titulo in enumerate (titulo, 1)]
            guardar_en_csv(datos, "titulos_noticias.csv")

    elif opcion == "2":
        # Extraer artículos
        print("\nExtrayendo articulos ...")
        articulos = extraer_articulos(html)

        print(f"\nSe encontraron {len(articulos)} articulos.")
        for i, articulo in enumerate(articulos,1):
            print(f"\n{i}. {articulo.get(('titulo', 'Sin titulo'))}")
            if articulo.get('fecha'):
                print(f"   Fecha: {articulo['fecha']}")
            if articulo.get('resumen'):
                print(f"   Resumen: {articulo['resumen'][:100]}...")
            if articulo.get('enlace'):
                print(f"   Enlace: {articulo['enlace']}")

         # Guardar en CSV
        if articulo and input("\n¿Deseas guardar los títulos en un archivo CVS? (s/n): ").lower() == 's':
            guardar_en_csv(articulos, "articulos.csv")

    else:
        print("Opcion no valida")

if __name__ == "__main__":
    main()