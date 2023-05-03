#Importando Pandas
import pandas as pd

#Importando e setando biblioteca serial
import serial
porta = 'COM6'
baud_rate = 9600


#Listas com os dados coletados
leituras=[]
temperatura=[]
pressao=[]
umidade=[]
tempo=[]

#contador
i=0

tempoSeg = int(input('Insira o intervalo de tempo em segundos: '))
n = tempoSeg/6 + 1

while True:
    try:
        arduino = serial.Serial(porta, baud_rate)
        print('Arduino conectado')
        print()
        break
    except:
        pass
while i<n:
    
    msg = str(arduino.readline())
    msg = msg[2:-5]
    print(i*6, 'segundos - ', msg.split(','))
    
    leituras.append(msg.split(','))
    
    arduino.flush()
    tempo.append(i*6)
    i+=1
    
for l in leituras:
    temperatura.append(l[0])
    pressao.append(l[1])
    umidade.append(l[2])

#Dados para o DataFrame
dados = { 'Instante (seg)': tempo,
          'Temperatura (C)': temperatura,
          'Pressao (Pa)': pressao,
          'Umidade (%)': umidade   
}

#Criar o DataFrame
df = pd.DataFrame(dados)

#Exportando para Excel e para CSV
df.to_excel("D:/Gustavo/Faculdade/Disciplinas/2022.2/BECN/ProjetoFinalArduino/DadosExcel.xlsx", index=False)
df.to_csv("D:/Gustavo/Faculdade/Disciplinas/2022.2/BECN/ProjetoFinalArduino/DadosCSV.csv", index=False)

#Mostrando o data frame
print(df)

print('Tempo decorrido: %s segundos' %tempoSeg)
print('Medições realizadas: %.0f' %n)
