import time
import random
import paho.mqtt.client as mqtt

# Configurações do ThingSpeak MQTT
MQTT_SERVER = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
CHANNEL_ID = "2720534"       # Substitua pelo ID do seu canal ThingSpeak
WRITE_API_KEY = "XCZN953WQ9BNJ7OY" # Substitua pelo seu Write API Key

# Dados MQTT para o ThingSpeak
MQTT_USERNAME = "NCI6CTo3Di4zCyESMzYIHBM" # Use o API Key de MQTT
MQTT_CLIENT_ID = "NCI6CTo3Di4zCyESMzYIHBM"
MQTT_PASSWORD = "ctXpcd2lBApHxE4WYWnkmDVA"
TOPIC = f"channels/{CHANNEL_ID}/publish"

# Função de conexão MQTT
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Conectado ao ThingSpeak com sucesso!")
    else:
        print(f"Falha na conexão. Código de erro: {rc}")

# Inicialização do cliente MQTT
client = mqtt.Client(client_id=MQTT_CLIENT_ID, protocol=mqtt.MQTTv311)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.connect(MQTT_SERVER, MQTT_PORT, 60)
client.loop_start()

# Envio de dados simulados
try:
    while True:
        # Gera dados simulados
        temperatura = round(random.uniform(20.0, 50.0), 2)  # Simula entre 20 e 30 ºC
        temperatura2 = round(random.uniform(20.0, 50.0), 2)  # Simula entre 20 e 30 ºC
        umidade = round(random.uniform(20.0, 80.0), 2)      # Simula entre 40 e 60 %
        luminosidade = random.randint(100, 10000)            # Simula entre 100 e 1000 lux

        # Monta a mensagem para o ThingSpeak
        payload = f"field1={temperatura}&field2={umidade}&field3={luminosidade}&field4={temperatura2}"
        result = client.publish(TOPIC, payload)

        # Confirmação
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Dados enviados: {payload}")
        else:
            print("Erro ao enviar dados")

        # Intervalo de envio (ajuste conforme necessário)
        time.sleep(5)  # Envia a cada 15 segundos

except KeyboardInterrupt:
    print("Script interrompido pelo usuário")
finally:
    client.loop_stop()
    client.disconnect()
