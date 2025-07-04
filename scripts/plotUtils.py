import matplotlib.pyplot as plt 

# Declaro la funcion para graficar: recibe un dataframe y el titulo del grafico (valor por defecto: 'Precio BTC')
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

# Declaro una funcion para graficar el SMA
def addSMA(df, window, color='orange'):
    """
    Anyade al grafico una SMA (Simple Moving Average) de un window dado.
    """
    sma = df['price'].rolling(window=window).mean()
    plt.plot(df['timestamp'], sma, label=f'SMA{window}', color=color)

# Declaro una funcion para graficar la EMA
def addEMA(df, span, color='green'):
    """
    Anyade al grafico una EMA (Exponential Moving Average) de un span dado.
    """
    ema = df['price'].ewm(span=span, adjust= False).mean()
    plt.plot(df['timestamp'], ema, label=f'EMA{span}', color= color)

# Declaro una funcion para graficar las bandas de Bollinger
def addBollinger(df, window=20, num_std=2):
    """
    Anyade Bandas de Bollinger al grafico
    """
    sma = df['price'].rolling(window=window).mean()
    std = df['price'].rolling(window=window).std()
    upper = sma + (num_std * std)
    lower = sma - (num_std * std)
    plt.plot(df['timestamp'], upper, label='Bollinger Upper', linestyle='--', color='gray')
    plt.plot(df['timestamp'], lower, label='Bollinger Lower', linestyle='--', color='gray')
    





