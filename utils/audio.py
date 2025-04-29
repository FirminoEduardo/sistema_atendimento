import pygame
import threading

pygame.mixer.init()

def tocar_som(caminho):
    def _tocar():
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()
    threading.Thread(target=_tocar, daemon=True).start()