import matplotlib.pyplot as plt
import pandas as pd

temperatura = [26]
taxa = [0]
for i in range (1,5):
    temperatura.append(26+2*i)
    taxa.append(0)

dados = {'Temperatura (C)': temperatura,
          'Taxa de canto': taxa }

df = pd.DataFrame(dados)

df.to_csv("D:/Gustavo/Faculdade/Disciplinas/2022.2/BECN/ProjetoFinal/ProjetoFinalArduino/DadosFinais/TaxaDeCanto.csv", index=False)

print(df)