from gtts import gTTS
from playsound import playsound as play

nome_audio = 'Olámundo.mp3'

idioma_audio = 'pt'

texto = input("")
audio = gTTS(text=texto,
           lang=idioma_audio,
           slow=False)

audio.save(nome_audio)
play(nome_audio)
