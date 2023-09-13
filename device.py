#lib paho biblioteca principal para trabalhar com MQTT ("as" importar em todos as pastas mqtt
import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor
from definitions import client_id, user, password, server, port

#recebe mensagem HiveMQ
def mensagem(client, user, msg):
    aquecedor(msg.payload.decode())     #decode, decodifica a informacao binária


# Estabelecer conexão
client = mqtt.Client(client_id)  #cria objeto com nome do cliente
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagem        #call back, esta passando apenas o nome da função que está sendo evocado
client.subscribe('pucpr/iotmc/elielMT/aquecedor')
client.loop_start()               #continua o código, porém fica monitorando caso chegue uma mensagem

# comportamento do sistema, envio de informações
while True:
    client.publish('pucpr/iotmc/elielMT/temperatura', temperatura())
    client.publish('pucpr/iotmc/elielMT/umidade', umidade())
    time.sleep(5)

# client.disconnect()