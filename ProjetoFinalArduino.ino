#include <DHT.h> //INCLUSÃO DE BIBLIOTECA

#include <Wire.h>
#include <Adafruit_BMP085.h>

#define DHTPIN 7 //PINO DIGITAL UTILIZADO PELO DHT22
#define DHTTYPE DHT22 //DEFINE O MODELO DO SENSOR (DHT22 / AM2302)
 
DHT dht(DHTPIN, DHTTYPE); //PASSA OS PARÂMETROS PARA A FUNÇÃO

Adafruit_BMP085 bmp;

void setup(){
  Serial.begin(9600); //INICIALIZA A SERIAL
  dht.begin(); //INICIALIZA A FUNÇÃO
  delay(2000); //INTERVALO DE 2 SEGUNDO ANTES DE INICIAR
}
void loop(){
    Serial.print("Umidade: "); //IMPRIME O TEXTO NA SERIAL
    Serial.print(dht.readHumidity()); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO
    Serial.print("%"); //IMPRIME O TEXTO NA SERIAL 
    Serial.print(" / Temperatura: "); //IMPRIME O TEXTO NA SERIAL
    Serial.print(dht.readTemperature()); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO
    Serial.println("º C"); //IMPRIME O TEXTO NA SERIAL
    delay(2000); //INTERVALO DE 2 SEGUNDOS * NÃO DIMINUIR ESSE VALOR
}
