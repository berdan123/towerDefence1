import pygame
from pygame.math import Vector2

#towers class
class Towers(pygame.sprite.Sprite):
    def __init__(self,archerTowerImage,x,y,arrowImage):
        pygame.sprite.Sprite.__init__(self) #initialising the sprite class
        self.archerTowerImage=archerTowerImage #intiialising image of tower
        self.rect=self.archerTowerImage.get_rect(topleft=(x,y)) #setting the towers position using the images rectangle
        self.range=300 #range the tower can shoot
        self.fireRate=1000 #fire rate of tower
        self.lastShot=pygame.time.get_ticks() #records the last shot of the tower
        self.targetEnemy=None

        if self.rect.centery>200:
            self.image=arrowImage
        else:
            self.image=pygame.transform.rotate(arrowImage, 180)



    #tower drawing method
    def towerDraw(self,screen):
        screen.blit(self.archerTowerImage,self.rect)
    #tower shooting method
    def shooting(self,enemies,projectilesGroup,arrowImage):
        nowTime=pygame.time.get_ticks() #gets the current time in the game
        if nowTime-self.lastShot>= self.fireRate:
            if self.targetEnemy:
                distance = pygame.math.Vector2(self.rect.center).distance_to(self.targetEnemy.rect.center)
                #handling if enemy is dead or out of range
                if not self.targetEnemy.alive or distance > self.range:
                    self.targetEnemy=None

            if self.targetEnemy==None:
                closestDistance=float('inf')#sets initial closest to infinity
                for enemy in enemies:
                    distance = pygame.math.Vector2(self.rect.center).distance_to(
                        enemy.rect.center)  # distance between enemies and tower
                    if distance <= self.range:  # checking if enemy is in range
                        #setting new closest distance
                        if distance<closestDistance:
                            self.targetEnemy = enemy
                            closestDistance=distance
            #if there is a target shoot
            if self.targetEnemy:
                distance = pygame.math.Vector2(self.rect.center).distance_to(self.targetEnemy.rect.center)
                #checking ig enemy alive
                if  self.targetEnemy.alive and  distance <= self.range:
                    arrow=Projectiles(arrowImage,self.rect.center, self.targetEnemy) #creates a  projectile
                    projectilesGroup.add(arrow) #adds projectile to the group
                    self.lastShot=nowTime

#projectiles class
class Projectiles(pygame.sprite.Sprite):
    def __init__(self, projectileImage, startingPos, target):
        pygame.sprite.Sprite.__init__(self)
        self.image = projectileImage
        self.rect = self.image.get_rect(center=startingPos)
        self.target = target
        self.speed = 5

        # Check if the tower is above y=200 and rotate the arrow by 90 degrees if true
        if self.rect.centery > 150:
            # The tower is below y=200, keep the original rotation
            self.image = self.image
        else:
            # The tower is above y=200, rotate the arrow 90 degrees
            self.image = pygame.transform.rotate(self.image, 180)

        self.rect = self.image.get_rect(center=self.rect.center)
    #method to make arrow move
    def update(self):
        if self.target and self.target.alive:
            targetPos = self.target.rect.center
            direction = pygame.math.Vector2(targetPos[0] - self.rect.centerx, targetPos[1] - self.rect.centery)

            # Normalize direction to maintain consistent speed
            if direction.length() != 0:
                normalizedDirection = direction.normalize()
                self.rect.x += normalizedDirection.x * self.speed
                self.rect.y += normalizedDirection.y * self.speed







#obstruction removal menu
def obstructionRemovalMenu(screen,font):
    #obstruction menu screen
    obstructionScreen=pygame.Surface((255, 255))
    obstructionScreen.fill((255, 255, 255))
    screen.blit(obstructionScreen,(0,0))
    #button dimensions
    removeButton=pygame.draw.rect(screen, (255, 0, 0), (300, 220, 190, 40))
    removeText=font.render('remove for 50e',True,(0,0,0))
    screen.blit(removeText,(310,230))
    #quit button
    quitButton=pygame.draw.rect(screen,(255,0,0),(300, 150, 190, 40))
    quitText=font.render('quit',True,(0,0,0))
    screen.blit(quitText,(310,160))

    pygame.display.update()


    #event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if removeButton.collidepoint(pygame.mouse.get_pos()):
                    return 'remove'
                elif quitButton.collidepoint(pygame.mouse.get_pos()):
                    return 'quit'

#tower placement menu
def towerPlacementMenu(screen, font,events,towerMenuOpen):
    overlay = pygame.Surface((255, 255))  # Size of the menu box
    overlay.fill((255, 255, 255))         # Light gray background
    screen.blit(overlay, (300, 200))      # Positioning menu at center

    #drawing  the buttons

    #archer tower button
    archerTowerButton = pygame.draw.rect(screen, (255, 0, 0), (300, 220, 190, 40))  #button for archer tower
    text1 = font.render("Archer Tower", True, (0, 0, 0))
    screen.blit(text1, (310, 230))
    #wizard tower button
    cannonTowerButton=pygame.draw.rect(screen, (0, 0, 255), (300, 150, 190, 40)) #button for cannon tower
    text2=font.render("wizard Tower", True, (0, 0, 0))
    screen.blit(text2, (310, 160))

    #knight tower button
    knightTowerButton = pygame.draw.rect(screen, (0, 255, 0), (300, 290, 190, 40))  # button for cannon tower
    text2 = font.render("knight Tower", True, (0, 0, 0))
    screen.blit(text2, (310, 300))
    #Title of the tower placement menu
    titleTowerMenu=font.render('Tower placement menu',True,(0,0,0))   #creating the title
    screen.blit(titleTowerMenu,(280,60))
    #returning choice on what is clicked
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                if archerTowerButton.collidepoint(pygame.mouse.get_pos()):
                    return 'archer tower'
                elif cannonTowerButton.collidepoint(pygame.mouse.get_pos()):
                    return 'wizard tower'
                elif knightTowerButton.collidepoint(pygame.mouse.get_pos()):
                    return 'knight tower'
                return None

