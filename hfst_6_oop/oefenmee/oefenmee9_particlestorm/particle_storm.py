import pygame
from particle import BoringParticle
import random
# Constantes.
breedte, hoogte = 600,600
fps = 120
aantal_particles = 100

# Start pygame.
pygame.init()
pygame.display.set_caption("Fire Storm Simulation")
scherm = pygame.display.set_mode((breedte,hoogte))
klok = pygame.time.Clock()

# TODO 1: Vul lijst *particles* met objecten van de klasse *BoringParticle*.
#         Het aantal aangemaakte objecten is gelijk aan de variabele *aantal_particles*.
particles = []  
for i in range(aantal_particles):
    v_x = (random.random()* 1.7)-0.85
    v_y = (random.random()* 1.7)-0.85
    particles.append(BoringParticle(breedte//2, hoogte//2, v_x, v_y))

running = True
while running:
    # Maak scherm schoon.
    scherm.fill((0,0,0))

    # Zorg voor constante FPS. interval is de tijd tussen iedere frame (in ms)
    interval = klok.tick(fps)
    
    # Controleer of quit-knop is ingeduwd.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO 2: Overloop iedere particle in lijst met particles:
    #   1. Beweeg positie van particle
    #   2. Reset particle wanneer ze uit het scherm zijn.
    #   3. Teken particle op scherm (deels gemaakt).

    for particle in particles:
        particle.bewegen(interval)
        particle.reset(breedte,hoogte)
        # Rood = random.randint(0,255)
        # Groen = random.randint(0,255)
        # Blauw = random.randint(0,255)

        pygame.draw.circle(scherm, (particle.kleur),(int(particle.x), int(particle.y)), 10)

    """ 1. Beweeg particle """
    """ 2. Reset particle """
        
    print(1/interval*1000)
    # Toon scherm aan gebruiker.
    pygame.display.update()

pygame.quit()