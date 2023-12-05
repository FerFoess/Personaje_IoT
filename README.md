[flows (1).json](https://github.com/FerFoess/Personaje_IoT/files/13572150/flows.1.json)# Personaje Navideño 

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

https://drive.google.com/file/d/1FNucIPjCzzWZKZgcOtpTVzTD78DX8zbr/view?usp=sharing
https://drive.google.com/file/d/1bGTcqEK-bOn_AY6Qf7bKaQIIcdedrDQd/view?usp=sharing

## Flujo NODE-RED

[Uploading flow[
    {
        "id": "8f9199133de76077",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "7295e244e7ba691e",
        "type": "subflow",
        "name": "Subflow 1",
        "info": "",
        "in": [],
        "out": []
    },
    {
        "id": "4ec50ea857746b44",
        "type": "ui_base",
        "theme": {
            "name": "theme-light",
            "lightTheme": {
                "default": "#0094CE",
                "baseColor": "#0094CE",
                "baseFont": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif",
                "edited": true,
                "reset": false
            },
            "darkTheme": {
                "default": "#097479",
                "baseColor": "#097479",
                "baseFont": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif",
                "edited": false
            },
            "customTheme": {
                "name": "Untitled Theme 1",
                "default": "#4B7930",
                "baseColor": "#4B7930",
                "baseFont": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif"
            },
            "themeState": {
                "base-color": {
                    "default": "#0094CE",
                    "value": "#0094CE",
                    "edited": false
                },
                "page-titlebar-backgroundColor": {
                    "value": "#0094CE",
                    "edited": false
                },
                "page-backgroundColor": {
                    "value": "#fafafa",
                    "edited": false
                },
                "page-sidebar-backgroundColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "group-textColor": {
                    "value": "#1bbfff",
                    "edited": false
                },
                "group-borderColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "group-backgroundColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "widget-textColor": {
                    "value": "#111111",
                    "edited": false
                },
                "widget-backgroundColor": {
                    "value": "#0094ce",
                    "edited": false
                },
                "widget-borderColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "base-font": {
                    "value": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif"
                }
            },
            "angularTheme": {
                "primary": "indigo",
                "accents": "blue",
                "warn": "red",
                "background": "grey",
                "palette": "light"
            }
        },
        "site": {
            "name": "Node-RED Dashboard",
            "hideToolbar": "false",
            "allowSwipe": "false",
            "lockMenu": "false",
            "allowTempTheme": "true",
            "dateFormat": "DD/MM/YYYY",
            "sizes": {
                "sx": 48,
                "sy": 48,
                "gx": 6,
                "gy": 6,
                "cx": 6,
                "cy": 6,
                "px": 0,
                "py": 0
            }
        }
    },
    {
        "id": "9c24adead9911ca7",
        "type": "ui_tab",
        "name": "Proyectos",
        "icon": "dashboard",
        "order": 1,
        "disabled": false,
        "hidden": false
    },
    {
        "id": "ceb387bfdbeed9d5",
        "type": "ui_group",
        "name": "LED",
        "tab": "9c24adead9911ca7",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "e46dce503162f26b",
        "type": "mqtt-broker",
        "name": "",
        "broker": "broker.hivemq.com",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "4",
        "keepalive": "60",
        "cleansession": true,
        "autoUnsubscribe": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthRetain": "false",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closeRetain": "false",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willRetain": "false",
        "willPayload": "",
        "willMsg": {},
        "userProps": "",
        "sessionExpiry": ""
    },
    {
        "id": "5dfa417e246a6882",
        "type": "remote-config",
        "name": "Node-RED UI",
        "host": "localhost",
        "protocol": "http",
        "port": "1880",
        "baseurl": "/ui",
        "instancehash": "nqpyq7qbv7ube2hvxcwkqykl5zpuuqtahv68duuxx7x45bkmo5nym3bnoxfmk6x4",
        "server": "nodered02.remote-red.com",
        "region": "de"
    },
    {
        "id": "33a07be288138d68",
        "type": "inject",
        "z": "8f9199133de76077",
        "name": "Inicio 3",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "",
        "payloadType": "str",
        "x": 110,
        "y": 580,
        "wires": [
            [
                "f7571123eec8aa00"
            ]
        ]
    },
    {
        "id": "f7571123eec8aa00",
        "type": "ui_switch",
        "z": "8f9199133de76077",
        "name": "",
        "label": "buzzer",
        "tooltip": "",
        "group": "ceb387bfdbeed9d5",
        "order": 2,
        "width": 0,
        "height": 0,
        "passthru": true,
        "decouple": "false",
        "topic": "topic",
        "topicType": "msg",
        "style": "",
        "onvalue": "1",
        "onvalueType": "num",
        "onicon": "",
        "oncolor": "",
        "offvalue": "0",
        "offvalueType": "num",
        "officon": "",
        "offcolor": "",
        "animate": false,
        "className": "",
        "x": 330,
        "y": 580,
        "wires": [
            [
                "56a7417ab92e2292"
            ]
        ]
    },
    {
        "id": "56a7417ab92e2292",
        "type": "mqtt out",
        "z": "8f9199133de76077",
        "name": "",
        "topic": "utng/fmr/led",
        "qos": "",
        "retain": "",
        "respTopic": "",
        "contentType": "",
        "userProps": "",
        "correl": "",
        "expiry": "",
        "broker": "e46dce503162f26b",
        "x": 550,
        "y": 580,
        "wires": []
    },
    {
        "id": "b1452db8892d761f",
        "type": "remote-access",
        "z": "8f9199133de76077",
        "confignode": "5dfa417e246a6882",
        "name": "",
        "verbose": 0,
        "x": 500,
        "y": 660,
        "wires": [
            [
                "56a7417ab92e2292",
                "cf712cad43afd788",
                "c18f06de0d1e11ee"
            ],
            [
                "f7571123eec8aa00",
                "b49e9f177b029bd9",
                "eb84f6143de5e7b6"
            ]
        ]
    },
    {
        "id": "cf712cad43afd788",
        "type": "ui_switch",
        "z": "8f9199133de76077",
        "name": "",
        "label": "LEDS",
        "tooltip": "",
        "group": "ceb387bfdbeed9d5",
        "order": 1,
        "width": 0,
        "height": 0,
        "passthru": true,
        "decouple": "false",
        "topic": "topic",
        "topicType": "msg",
        "style": "",
        "onvalue": "2",
        "onvalueType": "num",
        "onicon": "",
        "oncolor": "",
        "offvalue": "3",
        "offvalueType": "num",
        "officon": "",
        "offcolor": "",
        "animate": false,
        "className": "",
        "x": 310,
        "y": 480,
        "wires": [
            [
                "b49e9f177b029bd9"
            ]
        ]
    },
    {
        "id": "497e8520a408602c",
        "type": "inject",
        "z": "8f9199133de76077",
        "name": "",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "",
        "payloadType": "str",
        "x": 110,
        "y": 520,
        "wires": [
            [
                "cf712cad43afd788"
            ]
        ]
    },
    {
        "id": "b49e9f177b029bd9",
        "type": "mqtt out",
        "z": "8f9199133de76077",
        "name": "",
        "topic": "utng/fmr/led",
        "qos": "",
        "retain": "",
        "respTopic": "",
        "contentType": "",
        "userProps": "",
        "correl": "",
        "expiry": "",
        "broker": "e46dce503162f26b",
        "x": 550,
        "y": 480,
        "wires": []
    },
    {
        "id": "1534640287a03544",
        "type": "inject",
        "z": "8f9199133de76077",
        "name": "",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "",
        "payloadType": "num",
        "x": 90,
        "y": 740,
        "wires": [
            [
                "c18f06de0d1e11ee"
            ]
        ]
    },
    {
        "id": "c18f06de0d1e11ee",
        "type": "ui_switch",
        "z": "8f9199133de76077",
        "name": "",
        "label": "Apagar",
        "tooltip": "",
        "group": "ceb387bfdbeed9d5",
        "order": 2,
        "width": 0,
        "height": 0,
        "passthru": true,
        "decouple": "false",
        "topic": "topic",
        "topicType": "msg",
        "style": "",
        "onvalue": "4",
        "onvalueType": "num",
        "onicon": "",
        "oncolor": "",
        "offvalue": "5",
        "offvalueType": "num",
        "officon": "",
        "offcolor": "",
        "animate": false,
        "className": "",
        "x": 340,
        "y": 740,
        "wires": [
            [
                "eb84f6143de5e7b6"
            ]
        ]
    },
    {
        "id": "eb84f6143de5e7b6",
        "type": "mqtt out",
        "z": "8f9199133de76077",
        "name": "",
        "topic": "utng/fmr/led",
        "qos": "",
        "retain": "",
        "respTopic": "",
        "contentType": "",
        "userProps": "",
        "correl": "",
        "expiry": "",
        "broker": "e46dce503162f26b",
        "x": 570,
        "y": 740,
        "wires": []
    }
]s (1).json…]()
