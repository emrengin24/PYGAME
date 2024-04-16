import pygame

pygame.init()
screen = pygame.display.set_mode((1300, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkred")

    pygame.draw.lines(screen, ("white"), False,((100,200),(300,200),(300,250),(150,250),(150,300),(250,300),(250,350)
                                                ,(150,350),(150,400),(300,400),(300,450),(100,450),(100,200)),3)
    pygame.draw.lines(screen, ("white"), False,((400,450),(400,200),(450,200),(525,300),(600,200),(650,200),
                                                (650,450),(600,450),(600,325),(560,375),(500,375),(450,325),(450,450),(400,450)),3)
    pygame.draw.lines(screen, ("white"), False,((750,450),(750,200),(900,200),(900,320),(840,320),(900,350),(900,450),(840,450),
                                                (840,375),(800,350),(800,450),(750,450)),3)
    pygame.draw.lines(screen, ("white"), False,((800,280),(800,240),(850,240),(850,280),(800,280)),3)
    pygame.draw.lines(screen, ("white"), False,((1000,200),(1200,200),(1200,250),(1050,250),(1050,300),(1150,300),(1150,350)
                                                ,(1050,350),(1050,400),(1200,400),(1200,450),(1000,450),(1000,200)),3)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()



