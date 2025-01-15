import pygame
class Player():
    def __init__(self):
        #attributes
        self.gold=50 #amount of gold player has
        self.elixir=50 #amount of elixir player has
        self.maxGold=100 #maximum gold player can have
        self.maxElixir=100 #maximum elixir player can have
        self.goldPerTime=10 #the rate of gold increase
        self.elixirPerTime=10 #rate of elixir increase
        self.lastGoldUpdate= pygame.time.get_ticks() #last gold  increase time
        self.lastElixirUpdate= pygame.time.get_ticks() #last  elixir increase time

    def drawCurrency(self,screen,font):
        goldText = font.render(f"Gold: {self.gold}/{self.maxGold}", True, (0, 0, 0)) #gold text
        elixirText = font.render(f"Elixir: {self.elixir}/{self.maxElixir}", True, (0, 0, 0)) #elixir text
        screen.blit(goldText, (10, 10))
        screen.blit(elixirText, (200, 10))

    def addGold(self,goldMineNum):
        currentTime=pygame.time.get_ticks() #taking the current time
        goldPerCycle=goldMineNum*self.goldPerTime #working out the amount of gold per cycle
        if currentTime-self.lastGoldUpdate>= 30000: #checking if 30 seconds have passed
            if self.gold<self.maxGold: #checking if the player is at max gold
                self.gold+=goldPerCycle #increasaing gold
            else: #if player is at max gold or more
                self.gold=self.maxGold     #making sure player can not go over max gold
            self.lastGoldUpdate=pygame.time.get_ticks() #updating the timer variable
    def addElixir(self,labNum):
        currentTime=pygame.time.get_ticks() #taking current time
        elixirPerCycle = labNum * self.elixirPerTime #working out the amount of elixir per cycle

        if currentTime-self.lastElixirUpdate>=30000: #checking if 30 seconds have passed
            if self.elixir<self.maxElixir: #checking if player is at max elixir
                self.elixir+=elixirPerCycle #increasing the elixir
            else: #if player is at max elixir
                self.elixir=self.maxElixir #ensuring player can not go past max elixir
            self.lastElixirUpdate=pygame.time.get_ticks() #updating timer

    #method to increase storage
    def increaseGoldStorage(self):
        self.maxGold+=50 #add 50 to max gold
    def increaseElixirStorage(self):
        self.maxElixir+=50 #add 50 to max elixir










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


#back to tower defence battle
def drawBattleButton(screen,font):
    #creating button
    towerButton=pygame.draw.rect(screen,(0,0,255),[0,560,90,30],0,5)
    towerButtonText=font.render('Battle',True,(0,0,0)) #adding text
    screen.blit(towerButtonText,(0,560)) #drawing text onto button
    return towerButton #returning position of button

def buildingUpgradeMenu(screen,font):
    overlay = pygame.Surface((255, 255))  # size of the menu box
    overlay.fill((255, 255, 255))  # white background
    screen.blit(overlay, (300, 200))  # positioning at centre of screen

    upgradeButton = pygame.draw.rect(screen, (255, 0, 0), (320, 210, 190, 40))  #
    upgradeButtonText = font.render("Upgrade", True, (0, 0, 0))
    screen.blit(upgradeButtonText, (330, 210))

    # wgold storage  button
    quitButton = pygame.draw.rect(screen, (0, 0, 255), (320, 260, 190, 40))
    quitButtonText = font.render("Quit", True, (0, 0, 0))
    screen.blit(quitButtonText, (330, 260))
    pygame.display.update()
    return {"upgrade": upgradeButton, "quit": quitButton}










