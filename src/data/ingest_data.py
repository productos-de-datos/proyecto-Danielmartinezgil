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
    import os
    import pandas as pd
    import xlwt
    import openpyxl

    try:
        os.chdir("data_lake/landing/")
        for num in range(1995, 2022):
            if num in range(2016, 2018):
                wdir = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'.format(
                    num)
                wget.download(wdir)
            else:
                wdir = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'.format(
                    num)
                wget.download(wdir)
        os.chdir('../../')
    except:
        raise NotImplementedError("Implementar esta función")


def test_ruta_origen():
    assert set(os.listdir()) - set(['.git', '.github', '.gitignore',
                                    '.vscode', 'data_lake', 'grader.py', 'Makefile', 'README.md', 'src']) == set()



if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
