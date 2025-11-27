import csv
import pathlib

def leer_csv_login(ruta_archivo):
    """Lee un CSV de login y devuelve una lista de tuplas:
       (usuario, clave, debe_funcionar) con debe_funcionar como bool
    """
    datos = []
    ruta = pathlib.Path(ruta_archivo)

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            
            usuario = fila['usuario'].strip()
            clave = fila['clave'].strip()
            # Convertir a booleano
            debe_funcionar = fila['debe_funcionar'].strip().lower() == 'true'
            
            datos.append((usuario, clave, debe_funcionar))

    return datos
