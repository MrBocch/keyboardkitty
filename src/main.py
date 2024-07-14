import pygame
from pynput import keyboard

UP = True

def on_press(key):
    global UP
    try:
        # print(f"Key {key.char} is pressed")
        if UP:
            UP = False
    except:
        # print(f"Special {key} pressed")
        if UP:
            UP = False


def on_release(key):
    global UP
    UP = True
    # global running


def loop():
    WIDTH = 319
    HEIGHT = 498

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        global UP
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("hi")
        frame = pygame.image.load("src/frame1.png").convert()

        running = True
        while running:
            if not UP:
                frame = pygame.image.load("src/frame2.png").convert()
            else:
                frame = pygame.image.load("src/frame1.png").convert()

            screen.blit(frame, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            pygame.display.flip()

        listener.join()

loop()
