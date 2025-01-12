import pygame

class Map():
    def __init__(self,mapImage,screen): #constructor
        self.map=mapImage  #creating a map instance
        self.towerEntrance=pygame.draw.rect(screen,(0,0,255),[200,130,300,40],0,5) #creating the button
    def mapDraw(self,screen):  #creating a draw method
        screen.blit(self.map,(0,0))
class TownEntrance():
    def __init__(self):
        self.health=100
    def gameOver(self,screen):
        screen.fill((0,0,0))  #filling the screen with black
        gameOverFont=pygame.font.SysFont('Arial',50)    #setting font type
        gameOverText=gameOverFont.render('GAME OVER',True,(255,255,255))    #creating the game over text
        screen.blit(gameOverText,(250,200)) #placing text on screen






