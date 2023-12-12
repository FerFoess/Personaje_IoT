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