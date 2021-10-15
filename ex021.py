print('=== Desafio 21 ===')
# Tocar música mp3 no python

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta?')
