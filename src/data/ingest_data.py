"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
Se descargan los datos y se depositan en la carpeta landing. 

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    import wget, os

    os.chdir('data_lake/landing')
    for num in range(1995, 2021):
        
        wdir = 'https://github.com/jdvelasq/datalabs/tree/master/datasets/precio_bolsa_nacional/xls/xxxx-{}.xls'.format(num)
        wget.download(wdir)


    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
