import sys
import math
import pygame
import time
from sympy import *
from pygame import event
pygame.init()

def isPrime(n):
    for i in range(2,math.ceil(n**(1/2))):
        if n%i == 0 and n != 1:
            return False
    return True


screen = pygame.display.set_mode([1000,1000])
screen.fill((255, 255, 255))
running = True
step = 1
x = 500
y = 500
xdirect = 1
ydirect = -1
amount = 1
xtime = True
i = 2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    while True:
        #print(i)
        #print(i, xtime, step, amount)
        if amount > step:
            if xtime:
                xtime = False
                amount = 1
                xdirect = -xdirect
            else:
                xtime = True
                amount = 1
                step += 1
                #print("step added")
                ydirect = -ydirect
            #print(i, xtime, step, amount)
        if amount <= step:
            if xtime:
                #print("here")
                x += xdirect
                amount += 1
                if isprime(i):
                    screen.set_at((x,y), (0,0,0))
                    #print("phere")
                    pygame.display.flip()
            else:
                y += ydirect
                amount +=1
                if isprime(i):
                    screen.set_at((x,y), (0,0,0))
        i += 1
        #print(x,y)
    time.sleep(100)
            
        

  

# Done! Time to quit.
pygame.quit()