from picamera import PiCamera, Color
from time import sleep


camera = PiCamera()


camera.resolution = (2592, 1944) # Resolucion maxima de las fotografias 2592 x 1944, la resolucion minima que se permite es 64 x 64. 
camera.framerate = 15  # Para lograr la resolucion maxima se debe configurar los cuadros por segundo en "15". 
camera.rotation = 0 # Rotar la imagen en 0, 90, 180 o 270 grados
camera.start_preview()  # Dentro del parentesis se puede escribir (alpha=200) lo que permite generar transparencia en la preview. Pero no en el video. 
camera.exposure_mode = 'auto' # Exposicion de la fotografia. Por defecto es "auto". Opciones (off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, fireworks)
camera.awb_mode = 'auto' # Balance de blacos. Por defecto es "auto". Opciones (off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, horizon)
camera.image_effect = 'none' # Opciones de efectos en la fotografia. Por defecto es "none". (none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1, deinterlace2)
camera.annotate_background = Color('white') # Color del background del texto
camera.annotate_foreground = Color('black') # Color de las letras del texto
camera.annotate_text = "Escuela Las Cruces" # Texto que llevara la fotografia
camera.annotate_text_size = 100 # Va de 6 a 160. Por defecto es 32.
camera.brightness = 50 #  Brillo de la fotografia (Por defecto es 50%). Va de 0 a  100.
camera.contrast = 50  #  Constraste de la fotografia (Por defecto es 50%). Va de 0 a  100.
for i in range(1): # El numero dentro del parentesis indica el numero de fotografias que se quieren tomar al correr el script
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)#Direccion donde se guardaran las fotografias. Se nombraran como "imagen" y el numero que corresponde a el orden de toma.
camera.stop_preview()


 # LOOPS DE AYUDA


 # BRILLO
 # camera.start_preview()
 # for i in range(100):
     # camera.annotate_text = "Brightness: %s" % i
     # camera.brightness = i
     # sleep(0.1)
 # camera.stop_preview()




 # CONTRASTE
 # camera.start_preview()
 # for i in range(100):
    # camera.annotate_text = "Contrast: %s" % i
    # camera.contrast = i
    # sleep(0.1)
 # camera.stop_preview()




 #  EFECTOS
 # camera.start_preview()
 # for effect in camera.IMAGE_EFFECTS:
     # camera.image_effect = effect
     # camera.annotate_text = "Effect: %s" % effect
     # sleep(5)
 # camera.stop_preview()



 
