import random
import pygame
from pygame import mixer
import button
GRAY = (192, 192, 192)
MAGENTA = (255, 0, 255)

pygame.init()
mixer.init()
clock = pygame.time.Clock()
### Peliruutu

width = 700
height = 500
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
pygame.display.set_caption("Kivi, Paperi ja Sakset 3")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#FPS

FPS = 60

#MUUTTUJAT

start_game = False
setup_menu = False
game_over = False
kierrokset = 0
kierros = 0
Player_score = 0
CPU_score = 0
tasapelit = 0
arvaus = 0
random_index = 0
sound_counter = 0
first_round = True
CPU_guess = 0


### FONTIT

mainfont = pygame.font.SysFont("CURLZ___", 50)

### Kuvien lataus

kivi = pygame.image.load('kivi.png')
kiviON = pygame.image.load('kiviON.png')
paperi = pygame.image.load('paperi.png')
paperiON = pygame.image.load('paperiON.png')
sakset = pygame.image.load('sakset.png')
saksetON = pygame.image.load('saksetON.png')
kpstitle = pygame.image.load('kpstitle.png')
pelaaIMG = pygame.image.load('pelaa.png')
poistuIMG = pygame.image.load('poistu.png')
pelaaONIMG = pygame.image.load('pelaaON.png')
poistuONIMG = pygame.image.load('poistuON.png')
kolme = pygame.image.load('3.png')
kolmeON = pygame.image.load('3ON.png')
viisi = pygame.image.load('5.png')
viisiON = pygame.image.load('5ON.png')
kymppi = pygame.image.load('10.png')
kymppiON = pygame.image.load('10ON.png')
first = pygame.image.load('first.png')

### Äänien lataus
win_fx = pygame.mixer.Sound('win.wav')
win_fx.set_volume(0.5)
loss_fx = pygame.mixer.Sound('loss.wav')
loss_fx.set_volume(0.5)
choice1 = pygame.mixer.Sound('choice1.wav')
choice1.set_volume(0.5)
choice2 = pygame.mixer.Sound('choice2.wav')
choice2.set_volume(0.5)

### Listat

MenuKivet = []
MenuPaperit = []
MenuSakset = []
kps_list = ["kivi", "paperi", "sakset"]

### Alkuvalikon lentävien objektien koordinaatit:

for i in range(2):
    kivi_fly_x = random.randrange(0, 700)
    kivi_fly_y = random.randrange(0, 500)
    paperi_fly_x = random.randrange(0, 700)
    paperi_fly_y = random.randrange(0, 500)
    sakset_fly_x = random.randrange(0, 700)
    sakset_fly_y = random.randrange(0, 500)
    MenuKivet.append([kivi_fly_x, kivi_fly_y])
    MenuPaperit.append([paperi_fly_x, paperi_fly_y])
    MenuSakset.append([sakset_fly_x, sakset_fly_y])
    
### Tekstin piirto
def draw_text(text, font, text_col, x, y):
    img = mainfont.render(text, True, text_col)
    screen.blit(img, (x, y))
### Lentävät tausta objektit    
def FlyingObjects():
    screen.fill(GRAY) ### Tausta
    for i in range(len(MenuKivet)): ### Lentävät kivet, liike
        screen.blit(kivi, MenuKivet[i])
        MenuKivet[i][1] +=1
        MenuKivet[i][0] +=1
        if MenuKivet[i][1] > 500:
            kivi_fly_x = random.randrange(-500, 700)
            MenuKivet[i][0] = kivi_fly_x
            kivi_fly_y = -100
            MenuKivet[i][1] = kivi_fly_y
    for i in range(len(MenuSakset)): ### Lentävät sakset, liike
        screen.blit(sakset, MenuSakset[i])
        MenuSakset[i][1] += 1
        MenuSakset[i][0] += 1
        if MenuSakset[i][1] > 500:
            sakset_fly_x = random.randrange(-500, 700)
            MenuSakset[i][0] = sakset_fly_x
            sakset_fly_y = -100
            MenuSakset[i][1] = sakset_fly_y
    for i in range(len(MenuPaperit)): ### Lentävät paperit, liike
        screen.blit(paperi, MenuPaperit[i])
        MenuPaperit[i][1] += 1
        MenuPaperit[i][0] += 1
        if MenuPaperit[i][1] > 500:
            paperi_fly_x = random.randrange(-500, 700)
            MenuPaperit[i][0] = paperi_fly_x
            paperi_fly_y = -100
            MenuPaperit[i][1] = paperi_fly_y

### TEKSTIT
kierrosTeksti = mainfont.render("Anna pelattavien kierrosten määrä: ", 1, (MAGENTA))
voitto = mainfont.render("Sinä voitit!", 1, (MAGENTA))
tappio = mainfont.render("Sinä hävisit.", 1, (MAGENTA))
tasapeli = mainfont.render("Tasapeli!", 1, (MAGENTA))
tietokone = mainfont.render("Tietokone: ", 1, (MAGENTA))



### NAPIT
pelaa_button = button.Button(100, SCREEN_HEIGHT // 2 + 175, pelaaIMG, 1)
poistu_button = button.Button(SCREEN_WIDTH - poistuIMG.get_width() - 100, SCREEN_HEIGHT // 2 + 175, poistuIMG, 1)
kolme_button = button.Button(100, 100, kolme, 1)
viisi_button = button.Button(300, 100, viisi, 1)
kymppi_button = button.Button(500, 100, kymppi, 1)
kivi_button = button.Button(100, 300, kivi, 1)
paperi_button = button.Button(SCREEN_WIDTH // 2 - paperi.get_width() // 2, 300, paperi, 1)
sakset_button = button.Button(SCREEN_WIDTH - sakset.get_width() - 100, 300, sakset, 1)

### ITSE PELI

run = True
while run:
    
    clock.tick(FPS)
    screen.fill(GRAY)
    #MAIN MENU
    if start_game == False and setup_menu == False and game_over == False:
        FlyingObjects()
        screen.blit(kpstitle, ((SCREEN_WIDTH // 2 - kpstitle.get_width() // 2), 15))
        if pelaa_button.rect.collidepoint(pygame.mouse.get_pos()):
            pelaa_button.image = pelaaONIMG
        else:
            pelaa_button.image = pelaaIMG
        if poistu_button.rect.collidepoint(pygame.mouse.get_pos()):
            poistu_button.image = poistuONIMG
        else:
            poistu_button.image = poistuIMG
        if pelaa_button.draw(screen):
            choice1.play(0)
            setup_menu = True
            
        if poistu_button.draw(screen):
            run = False
    #SETUP MENU       
    if start_game == False and setup_menu == True and game_over == False:
        screen.blit(kierrosTeksti, (width/2 - kierrosTeksti.get_width()/2, 20))
        #NAPIT
        if kolme_button.rect.collidepoint(pygame.mouse.get_pos()):
            kolme_button.image = kolmeON
        else:
            kolme_button.image = kolme
        if kolme_button.draw(screen):
            choice1.play(0)
            kierrokset = 3
            kierros = 1
            random_index = random.randrange(3)
            start_game = True
            
        if viisi_button.rect.collidepoint(pygame.mouse.get_pos()):
            viisi_button.image = viisiON
        else:
            viisi_button.image = viisi
        if viisi_button.draw(screen):
            choice1.play(0)
            kierrokset = 5
            kierros = 1
            random_index = random.randrange(3)
            start_game = True
            
        if kymppi_button.rect.collidepoint(pygame.mouse.get_pos()):
            kymppi_button.image = kymppiON
        else:
            kymppi_button.image = kymppi
        if kymppi_button.draw(screen):
            choice1.play(0)
            kierrokset = 10
            kierros = 1
            random_index = random.randrange(3)
            start_game = True
            
        if poistu_button.rect.collidepoint(pygame.mouse.get_pos()):
            poistu_button.image = poistuONIMG
        else:
            poistu_button.image = poistuIMG
        if poistu_button.draw(screen):
            run = False
    
    # GAME SCREEN
    if start_game == True and game_over == False:
        
        draw_text(f'Kierros: {kierros} / {kierrokset}', mainfont, MAGENTA, (SCREEN_WIDTH/2 - 125), 20)
        draw_text(f'Pelaaja: {Player_score}', mainfont, MAGENTA, 75, 110)
        draw_text(f'Tietokone: {CPU_score}', mainfont, MAGENTA, 400, 110)
        screen.blit(tietokone, (SCREEN_WIDTH/2 - tietokone.get_width() - 10, 200))
        if CPU_guess == 0:
            screen.blit(first, (SCREEN_WIDTH/2 + first.get_width()/2, 200))
        if CPU_guess == 1:
            screen.blit(kivi, (SCREEN_WIDTH/2 + first.get_width()/2, 200))
        if CPU_guess == 2:
            screen.blit(paperi, (SCREEN_WIDTH/2 + first.get_width()/2, 200))
        if CPU_guess == 3:
            screen.blit(sakset, (SCREEN_WIDTH/2 + first.get_width()/2, 200))
            
        
        #NAPIT RUUDULLE
        
        #KIVI
        if kivi_button.draw(screen):
            CPU_guess = random_index + 1
            choice2.play(0)
            kierros +=1
            arvaus = 0
            if arvaus == random_index:
                tasapelit += 1
            if random_index == 1:
                CPU_score += 1
            if random_index == 2:
                Player_score += 1
            random_index = random.randrange(3)
            
        if kivi_button.rect.collidepoint(pygame.mouse.get_pos()): 
            kivi_button.image = kiviON
        else:
            kivi_button.image = kivi
        #PAPERI
        if paperi_button.draw(screen):
            CPU_guess = random_index + 1
            choice2.play(0)
            kierros += 1
            arvaus = 1
            if arvaus == random_index:
                tasapelit += 1
            if random_index == 0:
                Player_score += 1
            if random_index == 2:
                CPU_score += 1
            random_index = random.randrange(3)

        if paperi_button.rect.collidepoint(pygame.mouse.get_pos()):
            paperi_button.image = paperiON
        else:
            paperi_button.image = paperi
        #SAKSET
        if sakset_button.draw(screen):
            CPU_guess = random_index + 1
            choice2.play(0)
            kierros += 1
            arvaus = 2
            if arvaus == random_index:
                tasapelit += 1
            if random_index == 0:
                CPU_score += 1
            if random_index == 1:
                Player_score += 1
            random_index = random.randrange(3)

        if sakset_button.rect.collidepoint(pygame.mouse.get_pos()):
            sakset_button.image = saksetON
        else:
            sakset_button.image = sakset
        if poistu_button.rect.collidepoint(pygame.mouse.get_pos()):
            poistu_button.image = poistuONIMG
        else:
            poistu_button.image = poistuIMG
        if poistu_button.draw(screen):
            run = False
        if kierros > kierrokset:
            game_over = True
    
    # GAME OVER
    if game_over == True:
        draw_text(f'Kierros: {kierrokset} / {kierrokset}', mainfont, MAGENTA, (SCREEN_WIDTH/2 - 125), 20)
        draw_text(f'Pelaaja: {Player_score}', mainfont, MAGENTA, 75, 110)
        draw_text(f'Tietokone: {CPU_score}', mainfont, MAGENTA, 400, 110)
        screen.blit(tietokone, (SCREEN_WIDTH/2 - tietokone.get_width() - 10, 200))
        if CPU_guess == 0:
            screen.blit(first, (SCREEN_WIDTH/2 + first.get_width()/2, 200))
        if CPU_guess == 1:
            screen.blit(kivi, (SCREEN_WIDTH/2 + first.get_width()/2, 200))
        if CPU_guess == 2:
            screen.blit(paperi, (SCREEN_WIDTH/2 + first.get_width()/2, 200))
        if CPU_guess == 3:
            screen.blit(sakset, (SCREEN_WIDTH/2 + first.get_width()/2, 200))
        #PISTELASKU
        if Player_score > CPU_score:
            screen.blit(voitto, (width/2 - voitto.get_width()/2, 325))
            if sound_counter < 1:
                win_fx.play(0)
                sound_counter +=1
            
        if Player_score < CPU_score:
            screen.blit(tappio, (width/2 - tappio.get_width()/2, 325))
            if sound_counter < 1:
                loss_fx.play(0)
                sound_counter +=1
        if Player_score == CPU_score:
            screen.blit(tasapeli, (width/2 - tasapeli.get_width()/2, 325))
            if sound_counter < 1:
                loss_fx.play(0)
                sound_counter +=1
            
        #NAPIT
        
        if pelaa_button.rect.collidepoint(pygame.mouse.get_pos()):
            pelaa_button.image = pelaaONIMG
        else:
            pelaa_button.image = pelaaIMG
        if pelaa_button.draw(screen):
            choice1.play(0)
            setup_menu = True
            start_game = False
            game_over = False
            CPU_score = 0
            Player_score = 0
            tasapelit = 0
            kierrokset = 0
            kierros = 0
            sound_counter = 0
            CPU_guess = 0
                        
        if poistu_button.rect.collidepoint(pygame.mouse.get_pos()):
            poistu_button.image = poistuONIMG
        else:
            poistu_button.image = poistuIMG
        if poistu_button.draw(screen):
            run = False

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
pygame.quit()