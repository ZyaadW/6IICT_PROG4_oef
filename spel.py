import sys
import pygame
import glob


# Initialisation of Pygame

pygame.init()

# The main Surface where everything's blitted

screen = pygame.display.set_mode((400, 600))

# The container of all the Sprite
# attributes (position...)
# and methods (change position...)


class Cat:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.imgslist = [
        pygame.image.load(f) for f in
            glob.glob("cat/Idle*.png")
        ]
        self.counter = 0
        self.image = self.imgslist[0]
        self.dir = "right"

    def update(self):
        self.counter += .4
        if self.counter >= len(self.imgslist):
            self.counter = 0
        if cat.dir == "right":
            self.image = self.imgslist[int(self.counter)]
        if cat.dir == "left":
            self.image = pygame.transform.flip(self.imgslist[int(self.counter)], True, False)
        self.pos = self.x, self.y
        screen.blit(self.image, self.pos)

# Let's create a sprite with Cat class

cat = Cat(100, 100)

# This is for the frame rate

clock = pygame.time.Clock()


# Everything goes on forever here

loop = 1
while loop:
    screen.fill((128, 255, 128))

    # Close with the window's x' button

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        # Now we get the Key inputs
        if event.type == pygame.KEYDOWN:

            # Close if press Esc

            if event.key == pygame.K_ESCAPE:
                loop = 0

            # Move with arrow Keys:

            if event.key == pygame.K_RIGHT:
                cat.dir = "right"
                cat.x += 10
            if event.key == pygame.K_LEFT:
                cat.dir = "left"
                cat.x -= 10
            if event.key == pygame.K_UP:
                cat.y -= 10
            if event.key == pygame.K_DOWN:
                cat.y += 10

    # Call every frame method to move cat

    cat.update()

    # Update the screen to see something
    pygame.display.update()

    # at 60 frame rate

    clock.tick(60)

# Pressing Esc or 'x' button you exit here and..

pygame.quit()
sys.exit()