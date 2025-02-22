"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os
import glob

def pregunta_01():

    archivo_entrada = "files/input/solicitudes_de_credito.csv"
    archivo_salida = "files/output/solicitudes_de_credito.csv"
    
    # eliminar archivos previos en la carpeta de salida
    if os.path.exists("files/output"):
        for archivo in glob.glob("files/output/*"):
            os.remove(archivo)
    else:
        os.makedirs("files/output")
    
    # cargar datos
    datos = pd.read_csv(archivo_entrada, sep=";", index_col=0)
    
    # limpieza de columnas
    datos["sexo"] = datos["sexo"].str.strip().str.lower()

    datos["tipo_de_emprendimiento"] = datos["tipo_de_emprendimiento"].str.strip().str.lower()

    datos["idea_negocio"] = datos["idea_negocio"].str.strip().str.lower()

    datos["idea_negocio"] = datos["idea_negocio"].str.replace("á", "a").str.replace("é", "e").str.replace("í", "i").str.replace("ó", "o").str.replace("ú", "u")

    datos["idea_negocio"] = datos["idea_negocio"].str.replace(" ", "").str.translate(str.maketrans("", "", "-._"))

    datos["barrio"] = datos["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")

    datos["comuna_ciudadano"] = datos["comuna_ciudadano"].astype(int)

    datos["fecha_de_beneficio"] = pd.to_datetime(datos["fecha_de_beneficio"], dayfirst=True, format="mixed")

    datos["monto_del_credito"] = datos["monto_del_credito"].str.strip().str.strip("$").str.replace(".00", "").str.replace(",", "").astype(int)

    datos["línea_credito"] = datos["línea_credito"].str.strip().str.lower()
    
    datos["línea_credito"] = datos["línea_credito"].str.replace(" ", "").str.translate(str.maketrans("", "", "-._"))
    
    # quitar nulos y duplicados
    datos = datos.dropna().drop_duplicates()
    
    # guardar datos limpios
    datos.to_csv(archivo_salida, index=False, sep=";")
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
