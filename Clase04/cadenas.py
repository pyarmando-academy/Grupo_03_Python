from gtts import gTTS
import os
texto = "Hola Mi Nombre es Armando cual es el Tuyo:"
lenguage = "es"
myobj = gTTS(text=texto, lang=lenguage, slow=False)
myobj.save("robot.mp3")
os.system("start robot.mp3")
