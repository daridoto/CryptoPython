import matplotlib.pyplot as plt 

# Declaro la funcion: recibe un dataframe y el titulo del grafico (valor por defecto: 'Precio BTC')
def plotBtcPrice(df, title='Precio BTC'):

    # Crea una figura con tamaño 12x6
    plt.figure(figsize=(12,6))

    # Dibuja el precio usando las columnas del dataframe
    plt.plot(df['timestamp'], df['price'], label='Precio BTC', alpha=0.7)

    # Anyado titulo, etiquetas, leyenda, cuadricula y muestro el grafico
    plt.title(title)
    plt.xlabel('Fecha')
    plt.ylabel('Precio(USD)')
    plt.legend()
    plt.grid(True)
    
    plt.show()