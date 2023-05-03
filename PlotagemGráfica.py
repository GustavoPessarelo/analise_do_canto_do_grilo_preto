from numpy import append
import pandas as pd

header = ['temperatura', 'pressao', 'umidade', 'data']

nome = input('Insira o nome do arquivo: ')
nomeArquivo = nome + '.csv'

dado = input('Insira o nome do parâmetro: ')

step = float(input('Insira o step do eixo x: '))

nomeFigura = 'Gráfico' + nome + dado +'.png'


df = pd.read_csv(nomeArquivo, names=header)

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

a = df[dado].count()
i = 0


while i<a:
    x.append(i)
    y.append(df[dado].mean())
    i+=1
    
plt.figure(figsize=(20,10))

x_ticks = np.arange(0, len(x), step)

plt.xticks(x_ticks)

df[dado].plot()
plt.plot(x,y)

plt.title('Variação de %s' %dado)
plt.xlabel('Leitura')
plt.ylabel(dado)

plt.savefig(nomeFigura, format = 'png')