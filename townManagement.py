import pygame
import time





def buildMenu(screen,font):
    overlay = pygame.Surface((255, 255))  #size of the menu box
    overlay.fill((255, 255, 255))  #white background
    screen.blit(overlay, (300, 200)) #positioning at centre of screen

    # drawing  the buttons

    # gold mine button
    goldMine = pygame.draw.rect(screen, (255, 0, 0), (320, 210, 190, 40))  #
    goldMineText = font.render("Gold mine", True, (0, 0, 0))
    screen.blit(goldMineText, (330, 210))

    # wgold storage  button
    goldStorage = pygame.draw.rect(screen, (0, 0, 255), (320, 260, 190, 40))
    goldStorageText = font.render("gold storage", True, (0, 0, 0))
    screen.blit(goldStorageText, (330, 260))

    # lab button
    lab = pygame.draw.rect(screen, (0, 255, 0), (320, 310, 190, 40))
    labText = font.render("Lab", True, (0, 0, 0))
    screen.blit(labText, (330, 310))

    #elixir storage button
    elixirStorage = pygame.draw.rect(screen, (0, 255, 0), (320, 370, 200, 40))
    elixirStorageText = font.render("Elixir storage ", True, (0, 0, 0))
    screen.blit(elixirStorageText, (320, 370))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if goldMine.collidepoint(pygame.mouse.get_pos()):
                    return 'gold mine'
                elif goldStorage.collidepoint(pygame.mouse.get_pos()):
                    return 'Gold Storage'
                elif lab.collidepoint(pygame.mouse.get_pos()):
                    return 'Lab'
                elif elixirStorage.collidepoint(pygame.mouse.get_pos()):
                    return 'Elixir Storage'

def checkCollision(newRect,placedBuildings):
    for _, rect in placedBuildings:
        if newRect.colliderect(rect):
            return True
    return False








