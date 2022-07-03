"""
De la ruta data_lake/landing/ se toma el año y la extensión de los
archivos que se encuentran en dicha ruta. 
Se cargan los archivos de la ruta data_lake/landing/ diferenciando la 
columna fecha en formato YYYY-MM-DD y las horas desde H00 a H23.
Finalmente, se guardan los archivos en la ruta data_lake/raw/ en formato csv.

"""


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    #raise NotImplementedError("Implementar esta función")

    import pandas as pd
    
    for num in range(1995, 2022):        
        if num in range(1995, 2000):
            data_csv = pd.read_excel('data_lake/landing/{}.xlsx'.format(num), header=3)
            data_csv = data_csv.iloc[:, 0:25]
            data_csv.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']       
            data_csv.to_csv('data_lake/raw/{}.csv'.format(num),index=None)
        elif(num in range(2000, 2016)):
            data_csv = pd.read_excel('data_lake/landing/{}.xlsx'.format(num), header=2)
            data_csv = data_csv.iloc[:, 0:25]
            data_csv.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            data_csv.to_csv('data_lake/raw/{}.csv'.format(num),index=None)
        elif(num in range(2016, 2018)):
            data_csv = pd.read_excel('data_lake/landing/{}.xls'.format(num), header=2)
            data_csv = data_csv.iloc[:, 0:25]
            data_csv.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            data_csv.to_csv('data_lake/raw/{}.csv'.format(num), index=None)
        else:
            data_csv = pd.read_excel('data_lake/landing/{}.xlsx'.format(num), header=0)
            data_csv = data_csv.iloc[:, 0:25]
            data_csv.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            data_csv.to_csv('data_lake/raw/{}.csv'.format(num), index=None)
    return
    raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
