import json
import pygame
import shutil
import firebase_admin
from firebase_admin import credentials, storage

#Initalize
pygame.init()
#cred = credentials.Certificate('private/firebase.json')
#firebase_admin.initialize_app(cred, {'storageBucket': 'gs://file-explorer-plus.appspot.com'})

#Fonts
standard_large = pygame.font.SysFont('Arial', 60, False)
standard = pygame.font.SysFont('Arial', 30, False)
standard_small = pygame.font.SysFont('Arial', 15, False)

#Updater
window = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
runtime = True

pygame.display.set_caption('File Explorer Plus Updater | Getting Update')
icon = pygame.image.load('File Explorer Plus.png')
pygame.display.set_icon(icon)

while runtime == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False
    
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()