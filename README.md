# Personaje Navideño 

## Nombre del Personaje 
- Muñeco de Nieve

## Integrantes
- Fernando Martínez Rodríguez
- Fernando Moncada Juarez

## Grupo
- GDS0541

 ## Materiales a utilizar
 
 |Nombre del componente|Descripción|Cantidad|Precio|
 |-|-|-|-|
 |ESP32|Microcontrolador con 30 pines con comunicación WiFi y Bluetooth|1|$140.00|
 |Cables Dupont|Cables para conexión de prototipos de purebas|50|$60.00|
 |Luces LED|Luces para la estetica del muñeco de nieve|5|$50.00|
 |Sensor|Sensor de proximidad|1|$60|
 |Regulador de velocidad|Regulador para darle una velocidad personalizada|1|$70|
 |Motor|Motor para el movimiento de brazos|2|$70|
 |Bocina|Para que el muñeco cuente con diferentes sonidos|1|$60|
 |Unicel|Bolas de unicel de diferente tamaño|3|$30.00|
 |Alambre|Alambres para las manos del muñeco de nueve|4|$30|
 |Alimentación| Un adaptador de corriente o una batería para alimentar el ESP32 y las luces LED|1|$150.00|


 ## Software a Utilizar

 |Nombre|Versión|Tipo Software|
 |-|-|-|
 |Thonny|4.2.1|Software libre|
 |SSD1602|1.8.1|Software libre|
 |Arduino IDE|2.2.1|Software libre
 |Visual Studio Code (Platformio)|1.82.2|Software libre|
 |Node Red|v3.1.0|Software libre|
 
 ## Prototipo en dibujo
 
 - Fotografia del dibujo a mano alzada de tu personaje
 
 - <img width="500" alt="Prototipo" src = "https://github.com/FerFoess/Personaje_IoT/assets/135056080/ef39334a-33c5-4de8-b4f8-e465e5bca2f5"> 


 ## Arquitectura
 - ![image](https://github.com/FerFoess/Personaje_IoT/assets/135056080/9832c1c9-5a03-43fa-8735-f80da435e581)



 - 
 ## Base de Datos
 - Imagen tabla o tablas que usarias (Ej. Sensores, actuadores, en un modelo relacional)
 - <img width="500" alt="Prototipo" src = "https://github.com/FerFoess/Personaje_IoT/assets/135056080/5c2dfd60-bcef-409b-8cd9-053258ea31e8"> 


## Videos

- Node Red Funcionamiento
https://drive.google.com/file/d/1FNucIPjCzzWZKZgcOtpTVzTD78DX8zbr/view?usp=sharing

- Funcionamiento Muñeco de nieve
https://drive.google.com/file/d/1bGTcqEK-bOn_AY6Qf7bKaQIIcdedrDQd/view?usp=sharing


## Flujo NODE-RED
[flows (1).json](https://github.com/FerFoess/Personaje_IoT/files/13572150/flows.1.json)


## Codigo Python

from machine import Pin, PWM
from time import sleep
from hcsr04 import HCSR04

# Definir pines para el control del motor
motorIN1 = Pin(23, Pin.OUT)
motorIN2 = Pin(22, Pin.OUT)

# Configurar pines para los LEDs
led_pins = [33, 25, 26, 14, 27]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Configurar el sensor HC-SR04
sensor_trigger = Pin(12, Pin.OUT)
sensor_echo = Pin(13, Pin.IN)
sensor = HCSR04(trigger_pin=sensor_trigger, echo_pin=sensor_echo)

# Configurar el buzzer
buzzer_pin = 32
buzzer = PWM(Pin(buzzer_pin))
volumen = 800  # Ajusta el volumen según sea necesario (0 a 1023)
buzzer.duty(volumen)

# Función para reproducir un tono
def sonido(frecuencia, duracion):
    buzzer.freq(frecuencia)
    buzzer.duty(volumen)
    sleep(duracion)
    buzzer.duty(0)

# Función para reproducir la melodía de Navidad con la estructura deseada
def reproducir_melodia_navidad():
    melodia_navidad = [
        (440, 0.6), (900, 0.6),
        # ... (resto de la melodía)
    ]
    for frecuencia, duracion in melodia_navidad:
        sonido(frecuencia, duracion)

# Número máximo de iteraciones antes de salir del bucle
max_iteraciones = 1000  # Puedes ajustar este valor según sea necesario

iteracion_actual = 0

while iteracion_actual < max_iteraciones:
    # Incrementar el contador de iteraciones
    iteracion_actual += 1

    # Medir la distancia
    distancia = sensor.distance_cm()

    # Imprimir la distancia
    print("Distancia:", distancia, "cm")

    # Si la distancia es menor a 100 cm, realizar las acciones
    if distancia < 100:
        # Avanzar
        motorIN1.value(1)
        motorIN2.value(0)
        sleep(2)

        # Detenerse
        motorIN1.value(0)
        motorIN2.value(0)

        # Encender los LEDs secuencialmente
        for led in leds:
            led.value(1)
            sleep(0.5)
            led.value(0)

        # Retroceder
        motorIN1.value(0)
        motorIN2.value(1)
        sleep(2)

        # Detenerse nuevamente
        motorIN1.value(0)
        motorIN2.value(0)

        # Apagar los LEDs
        for led in leds:
            led.value(0)

        # Reproducir la melodía de Navidad
        reproducir_melodia_navidad()

    else:
        # Si la distancia es mayor a 100 cm, detener el motor y apagar los LEDs
        motorIN1.value(0)
        motorIN2.value(0)

        # Apagar los LEDs
        for led in leds:
            led.value(0)

# Detener el zumbador al salir del bucle
buzzer.duty(0)


## Codigo Python Node-Red

from machine import Pin, PWM
from time import sleep
import network
from umqtt.simple import MQTTClient

# Definir las frecuencias para las notas musicales en Hz
D5 = 587
E5 = 659
F5 = 698
G5 = 784
A5 = 880
B5 = 988
C6 = 1047
B4 = 494
C5 = 523
D6 = 1175

reproduciendo_melodia = False

# Configurar el pin del zumbador como PWM
buzzer = PWM(Pin(12))
buzzer.duty(0)  # Inicializar el zumbador con un ciclo de trabajo del 0%

# Función para iniciar una nota con una frecuencia específica
def iniciar_nota(frecuencia):
    if frecuencia > 0:
        buzzer.freq(frecuencia)
        buzzer.duty(512)

# Función para detener la nota
def detener_nota():
    buzzer.duty(0)

def detener_todo():
    global reproduciendo_melodia
    detener_nota()  # Detener la melodía si se está reproduciendo
    reproduciendo_melodia = False
    apagar_leds()  # Apagar todos los LEDs    

# Función encargada de encender el zumbador cuando llega un mensaje
def llegada_mensaje(topic, msg):
    global reproduciendo_melodia

    print(msg)
    if msg == b'1':
        # Reproducir melodías y establecer la bandera en True
        reproducir_melodia(melodia_jingle_bells)
        reproducir_melodia(melodia_wish_you_merry_christmas)
        reproduciendo_melodia = True
    elif msg == b'0':
        detener_nota()
        reproduciendo_melodia = False
    elif msg == b'2':
        encender_leds()
    elif msg == b'3':
        apagar_leds()
    elif msg == b'4':
        detener_todo()  # Detener la melodía y apagar LEDs inmediatamente
    elif msg == b'5':
        encender_leds()  # Encender LEDs


# Función para reproducir una melodía
def reproducir_melodia(melodia):
    for frecuencia, duracion in melodia:
        iniciar_nota(frecuencia)
        sleep(duracion / 1000)
        detener_nota()
        sleep(0.1)

# Función para encender todos los LEDs
def encender_leds():
    for led in leds:
        led.value(1)

# Función para apagar todos los LEDs
def apagar_leds():
    for led in leds:
        led.value(0)

# Declarar función para conectarnos a WiFi
def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Wokwi-GUEST', '')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi Connected!!")

# Configurar pines para los LEDs
led_pins = [23, 22, 21, 19, 18]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Conectar a WiFi
conectar_wifi()
# Detalles de MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/fmr/led"
MQTT_PORT = 1883

# Subscribirse al broker MQTT
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
client.set_callback(llegada_mensaje)
client.connect()
client.subscribe(MQTT_TOPIC)
print("Conectado a %s, en el topic %s" % (MQTT_BROKER, MQTT_TOPIC))

# Melodía de "Jingle Bells"
melodia_jingle_bells = [
    (E5, 300), (E5, 300), (E5, 600),
    (E5, 300), (E5, 300), (E5, 600),
    (E5, 300), (G5, 300), (D5, 300), (C6, 300),
    (B5, 300), (A5, 300), (G5, 1200),
    (E5, 300), (E5, 300), (E5, 600),
    (E5, 300), (E5, 300), (E5, 600),
    (E5, 300), (G5, 300), (D5, 300), (C6, 300),
    (B5, 300), (A5, 300), (G5, 1200)
]

# Melodía de "We Wish You a Merry Christmas"
melodia_wish_you_merry_christmas = [
    (G5, 500), (G5, 500), (A5, 500),
    (G5, 500), (C6, 1000), (B5, 500),
    (B5, 500), (A5, 500), (G5, 500),
    (F5, 1000), (E5, 500), (E5, 500),
    (D5, 500), (B4, 500), (C5, 1000),
    (G5, 500), (G5, 500), (A5, 500),
    (G5, 500), (D6, 1000), (C6, 500),
    (B5, 500), (A5, 500), (F5, 1000),
    (E5, 500), (E5, 500), (D5, 500),
    (B4, 500), (C5, 1000)
]

# Ciclo infinito para esperar mensajes MQTT
while True:
    client.check_msg()  # Revisa si hay nuevos mensajes MQTT

