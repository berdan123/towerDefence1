import pygame
from enemeis import Enemy
from map import Map
from map import TownEntrance
from Towers import *
from townManagement import *


def drawMenu(screen,font,titleFont):
    #creating start buttom
    startButton=pygame.draw.rect(screen,(0,0,255),[200,130,260,40],0,5) #creating the button
    text = font.render('start',True,(0,0,0))    #creating the text that goes into the button
    screen.blit(text,(210,137)) #placing the text in the button

    #creating title
    title=titleFont.render('Tower defence game',True,(0,0,0))   #creating the title
    screen.blit(title,(150,60)) #placing the title onto the screen

    #creating exit button
    exitButton=pygame.draw.rect(screen,(0,0,255),[200,200,260,40],0,5) #creating the button
    exitText=font.render('quit',True,(0,0,0))    #creating the text that goes into the button
    screen.blit(exitText,(210,207)) #placing text onto the screen where the button is

    #creating help screen

    helpButton=pygame.draw.rect(screen,(0,0,255),[200,270,260,40],0,5)
    helpText=font.render('help',True,(0,0,0))
    screen.blit(helpText, (210, 273))

    #button click functions
    if exitButton.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:  #if the quit button is pressed
        return 'quit'
    elif startButton.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]: #if mouse cursor is over the menu button and left click is clicked
        return 'start'
    elif helpButton.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]: #checsk the mouses position and if it is presssed
        return 'help'
#town side button
def drawTownButton(screen,font):
    #creating button
    button=pygame.draw.rect(screen,(0,0,255),[700,560,80,30],0,5)
    #adding text
    buttonText=font.render('Town',True,(0,0,0))
    screen.blit(buttonText,(700,560))


#creating the games functions
def drawGame(enemyGroup, screen,NorthMapImage,wayPoints,goblinImage,lastSpawn,waves,townEntrance,towerGroup):

    pygame.display.set_caption('Game') #caption of the game window
    NorthMapImage.mapDraw(screen) #drawing map onto window

    #timers
    currentTime=pygame.time.get_ticks()
    spawnDelay=1000 #delay between enemy spawns
    if len(waves[0])>0: #checks if the waves array is not empty
        if currentTime-lastSpawn>spawnDelay:  #checking if the spawn delay has exceeded 5 seconds
            goblin=Enemy(wayPoints,goblinImage)   #creating a goblin instance
            enemyGroup.add(goblin)   #adding goblin to group
            lastSpawn=currentTime     #setting lastSpawn to the currentTime
            waves[0].pop(0)
    for goblin in enemyGroup:
        goblin.draw(screen)   #drawing every goblin in the enemy group
        goblin.enemyMovement()   #allowing them to move
        if goblin.next == len(wayPoints)-1:  # checks if the enemy is at the final waypoint
            goblin.attacking(townEntrance)

    for tower in towerGroup:
        tower.towerDraw(screen)

    if townEntrance.health<=0:
        townEntrance.gameOver(screen)



    return lastSpawn  # returning the value of lastSpawn
#creating the help screen
def helpScreen():
    helpWindow=pygame.display.set_mode((800, 600))
    pygame.display.set_caption('help')
    helpRunning=True
    while helpRunning:
        helpWindow.fill((0, 0, 0))
        print('help screen active')

pygame.display.set_caption('main menu')


#town side button
def drawTownButton(screen,font):
    #creating button
    button=pygame.draw.rect(screen,(0,0,255),[700,560,80,30],0,5)
    #adding text
    buttonText=font.render('Town',True,(0,0,0))
    screen.blit(buttonText,(700,560))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if button.collidepoint(pygame.mouse.get_pos()):
                return 'town'