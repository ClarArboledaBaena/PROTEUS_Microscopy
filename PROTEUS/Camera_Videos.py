from picamera import PiCamera, Color
from time import sleep


camera = PiCamera()

camera.resolution = (1920, 1080) # Resolucion maxima para la grabacion de video es 1920 x 1080.
camera.framerate = 15  # Para lograr la resolucion maxima se debe configurar los cuadros por segundo en "15". 
camera.rotation = 0 # Rotar la imagen en 0, 90, 180 o 270 grados
camera.start_preview() # Dentro del parentesis se puede escribir (alpha=200) lo que permite generar transparencia en la preview. Pero no en el video. 
camera.exposure_mode = 'auto' # Exposicion de la fotografia. Por defecto es "auto". Opciones (off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, fireworks)
camera.awb_mode = 'auto' # Balance de blacos. Por defecto es "auto". Opciones (off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, horizon)
camera.image_effect = 'none' # Opciones de efectos en la fotografia (none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1, deinterlace2)
camera.annotate_background = Color('white') # Color del background del texto
camera.annotate_foreground = Color('black') # Color de las letras del texto
camera.annotate_text = "Escuela Las Cruces" # Texto que llevara el video
camera.annotate_text_size = 70 # Va de 6 a 160. Por defecto es 32.
camera.brightness = 50 #  Brillo de la fotografia (Por defecto es 50%). Va de 0 a  100.
camera.contrast = 50  #  Constraste de la fotografia (Por defecto es 50%). Va de 0 a  100.
camera.start_recording('/home/pi/video.h264') # Direccion donde se guardara el video, se debe cambiar el nombre de cada archivo.
sleep(10) # Tiempo(en segundos) de grabacion
camera.stop_recording()
camera.stop_preview()

# Para observar el video se debe abrir la Terminal e igresar el siguiente codigo
  # omxplayer video.h264 y se da ENTER. El nombre del video dependera del nombre "video.h264" que le hayamos dado al archivo. 
