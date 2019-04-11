from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(15)  # Tiempo (en segundos)que se quiere tener la camara trabajando
camera.stop_preview()
