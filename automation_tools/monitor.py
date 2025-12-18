import os
import time

#ip del dispositivo IoT(la webcam)
camera_ip = "192.168.50.2"

#funcion que verifica el estado de la camara
def check_security():
    print(f"--- Iniciando vigilancia de {camera_ip} ---")
    
    # El comando "ping" revisa si la cámara responde
    # -n 1 significa que solo enviaremos un solo saludo
    response = os.system(f"ping -n 1 {camera_ip}")

    if response == 0:
        print("ESTADO: [ SEGURO ] - Cámara activa y transmitiendo.")
    else:
        print("ALERTA: [ PELIGRO ] - Cámara desconectada.")


# Esto hace que el programa corra para siempre cada 5 segundos
try:
    while True:
        check_security()
        time.sleep(5)
except KeyboardInterrupt:
    print("Vigilancia apagada por el dueño.")