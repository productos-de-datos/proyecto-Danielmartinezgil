"""
De la carpeta raw, se toman todos los archivos .csv y se depositan en un solo archivo donde
se tienen todos los datos consolidados. 

"""

def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    #raise NotImplementedError("Implementar esta función")
    import os
    import pandas as pd

    data = os.listdir('data_lake/raw')
    start_year = 1995
    final_year = 2021

    initial_file = pd.read_csv(f'data_lake/raw/{start_year}.csv')

    for item in range(start_year + 1, final_year + 1, 1):
        if item == start_year + 1:
            my_file = pd.read_csv(f'data_lake/raw/{item}.csv')
            my_final_file = pd.concat([start_year, my_file], ignore_index = True)
        else:
            my_file = pd.read_csv(f'data_lake/raw/{item}.csv')
            my_final_file = pd.concat([my_final_file, my_file], ignore_index = True)

    my_final_file.columns = ['fecha', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

    joined_file = pd.melt(my_final_file, id_vars = ['fecha'], value_vars = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], var_name = 'hora', value_name = 'precio')
    joined_file = joined_file.sort_values(by=['fecha', 'hora'])
    joined_file = joined_file[joined_file['fecha'].notnull()]

    joined_file.to_csv(f'data_lake/cleansed/precios-horarios.csv', header = True, index = False)

    return 'Ok'

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
