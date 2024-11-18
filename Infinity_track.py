import pygame

pygame.init()
audio = pygame.mixer.Sound("C:\\Users\\davso\\Downloads\\New Life.mp3")
repetitions = 20

for _ in range(repetitions):
    audio.play()
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)
        
pygame.quit()