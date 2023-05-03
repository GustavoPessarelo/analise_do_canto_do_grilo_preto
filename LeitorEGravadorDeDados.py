import csv
import serial
from datetime import datetime

#Recebe o nome do arquivo a ser gravado
nome = input('Insira o nome do arquivo: ')
nomeArquivo = nome + '.csv'

#Dados serial
porta = '/dev/ttyUSB0'
rate = 9600

#contador de tempo
contador = 0
tempoSeg = int(input('Insira o intervalo de tempo em segundos: '))
n = tempoSeg/6

#ordem dos dados coletados
header = ['temperatura', 'pressao', 'umidade', 'data']

#checa a disponibilidade do arduino
while True:
    try:
        arduino = serial.Serial(porta, rate)
        print('Arduino conectado')
        print()
        break
    except:
        pass



#le e grava em arquivo .csv os dados recebidos
with open(nomeArquivo, 'a', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    
    while contador<=n:
            
        msg = str(arduino.readline())
        msg = msg[2:-5]
        
                
        dt = datetime.now()
        
        writer.writerow([msg.split(',')[0],msg.split(',')[1],msg.split(',')[2], dt])
        
        print(contador*6, 'segundos - ', msg.split(','))
        
        arduino.flush()
        
        contador+=1
file.close()    

col = n+1

print('Tempo decorrido: %s segundos' %tempoSeg)
print('Numero de dados coletados: %.0f' %col)