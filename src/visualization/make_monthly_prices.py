def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales. 
    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd
    import matplotlib.pyplot as plt
    path_file = r'data_lake/business/precios-mensuales.csv'
    datos = pd.read_csv(path_file, index_col=None, sep=',', header=0)
    datos["fecha"] = pd.to_datetime(datos["fecha"])
    x = datos.fecha
    y = datos.precio

    plt.figure(figsize=(15, 6))
    plt.plot(x, y, 'b', label='Promedio Mensual')
    plt.title('Promedio Mensual')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend()
    plt.xticks(rotation="vertical")
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")

if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()
    doctest.testmod()
