import pygame, sys, random              #mooduli pygame,sys, random importimine




lBlue = [153, 204, 255]                            #muutuja mille väärtus värv helesinine
pygame.init()                                      #pygame käivitamine


screenX = 640                                             #muutuja väärtus akna pikkus
screenY = 480                                             #muutuja väärtus akna kõrgus
screen = pygame.display.set_mode([screenX, screenY])      #soovitud suurusega akna tekitamine, mis lisatakse muutujasse.
pygame.display.set_caption("Ylesanne 7")                  #aknale nimetuse andmine
screen.fill(lBlue)                                        #ekraani tausta täitmine helesinine

RADIUS = 10                                               #muutuja, raadius mille väärtus 10px
ZEROINTENSITY = 0                                         #muutuja mille väärtus 0
MAXINTENSITY = 255                                        #muutuja mille väärtus 255
border_width = 1                                          #muutja mille väärtus 1, ringi joone paksus

while True:                                               #korduslause kui tõsi
    pos = pygame.mouse.get_pos()                          #muutuja pos mis omab hiire asukoha
    for events in pygame.event.get():                     #event omistab tsüklis väärtuse kasutades pygame moodulit
        if events.type == pygame.QUIT:                    #kui event tüübi väärtuseks sulgumine(pygame.QUIT)
            pygame.quit()                                 #mängu sulgemine
            sys.exit()                                    #sys sulgemine

        if events.type == pygame.MOUSEBUTTONDOWN:                             #tingimusel kui event tüübi väärtuseks võrdne hiire nupp all
                                                                              #muutuja COLOR mille väärtus juhuslik värvivalik
            COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
            pygame.draw.circle(screen, COLOR, pos, RADIUS, border_width)      #ringi joonistamine ekraanile
            RADIUS += 2                                                       #ringi enda raadiuse suurendamine 2 võrra







    pygame.display.update()                                                    #ekraani uuendamine

pygame.quit()                                                                  #mängu sulgemine