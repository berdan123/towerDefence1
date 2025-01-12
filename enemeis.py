
import pygame    #importing pygame
from pygame.math import Vector2  #importing the vector2 class

#creating the enemy class
class Enemy(pygame.sprite.Sprite):#inheriting sprite.Sprite and defining class
    def __init__(self,waypoints,image):       #intialising the class

       pygame.sprite.Sprite.__init__(self) #intialising parent class
       self.waypoints=waypoints           #creating a variable for waypoints
       self.image=image
       self.rect= self.image.get_rect()

       #health and damage
       self.enemyHealth=100
       self.damage=10
       self.maxHealth=100 #maximum health of enemy


        #movement variables
       self.startingPos = Vector2(self.waypoints[0])
       self.rect.center = self.startingPos
       self.next=1

       #attack cooldown
       self.attackCooldown = 1000  #creates a 1 second delay
       self.lastAttackTime = pygame.time.get_ticks() #takes the last attacks time


    def draw(self, screen):     #defining draw method
        screen.blit(self.image, self.rect)  # Draws the enemy on the given screen

        #draw the health bar
        barX=self.rect.x #position of enemy
        barY=self.rect.y-10 #position just above enemies head
        barWidth=self.rect.width #width appropiate to enemy
        barHeight=5

        #health ratio
        healthRatio=self.enemyHealth/self.maxHealth
        currentWidth=int(barWidth*healthRatio)

        pygame.draw.rect(screen, (255, 0, 0), (barX, barY, barWidth, barHeight))  # Background in red
        pygame.draw.rect(screen, (0, 255, 0), (barX, barY, currentWidth, barHeight)) #health in green

    def enemyMovement(self):

        #working out the next waypoint

        self.nextPoint=Vector2(self.waypoints[self.next])
        self.distance=self.nextPoint-self.startingPos
        #making the enemy stop at the last waypoint
        if self.next==len(self.waypoints)-1:
            self.rect.center=self.nextPoint
            return

        if self.distance.length() < 0.1:  # checks small values
            self.startingPos = self.nextPoint
            self.rect.center = self.startingPos
            self.next += 1  # increments next variable
        else:
            #Normalize's and moves the goblin if distance is not small
            self.startingPos += self.distance.normalize()
            self.rect.center = self.startingPos
    def attacking(self,townEntrance):
        currentAttackTime=pygame.time.get_ticks()
        if currentAttackTime-self.lastAttackTime>=self.attackCooldown:
            townEntrance.health-=self.damage  #does damage to town entrance
            print(townEntrance.health) #prints entrance health
            self.lastAttackTime=currentAttackTime # adjusting the last attack time
    #enemy taking damage method
    def takeDamage(self,damage):
        self.enemyHealth-=damage #takes the damage away from enemy health
        if self.enemyHealth<=0:  #checking if enemy health is 0
            self.alive=False
            self.kill() #removes enemy




