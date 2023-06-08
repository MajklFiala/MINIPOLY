import pygame
import random
import copy


pygame.init()
width = 950
height = 950


surface = pygame.display.set_mode((width,height))
pygame.display.set_caption("MINIPOLY")

#BARVY

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
redb = (0,0,255)

#KONEC HRY - ZKOUŠKA

písmo1 = "Arial"


k = 0
lol = 0

#AGAIN

bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)



    
#OBRÁZKY POSTAVIČEK
čdum1 = pygame.image.load(r'čdum.png')
čdum_pruvodce1 = pygame.image.load(r'čdum_pruvodce.png')

čdum2 = pygame.image.load(r'čdum1.png')
čdum_pruvodce2 = pygame.image.load(r'čdum_pruvodce1.png')

čdum3 = pygame.image.load(r'čdum2.png')
čdum_pruvodce3 = pygame.image.load(r'čdum_pruvodce2.png')

čdum4 = pygame.image.load(r'čdum3.png')
čdum_pruvodce4 = pygame.image.load(r'čdum_pruvodce3.png')

čdumm = pygame.image.load(r'čdumm.png')
čdumb = pygame.image.load(r'čdumb.png')
čdumh = pygame.image.load(r'čdumh.png')
čdums = pygame.image.load(r'čdums.png')
čdumamb = pygame.image.load(r'čdumamb.png')
čdumcel = pygame.image.load(r'čdumcel.png')


mdum1 = pygame.image.load(r'mdum.png')
mdum_pruvodce1 = pygame.image.load(r'mdum_pruvodce.png')

mdum2 = pygame.image.load(r'mdum1.png')
mdum_pruvodce2 = pygame.image.load(r'mdum_pruvodce1.png')

mdum3 = pygame.image.load(r'mdum2.png')
mdum_pruvodce3 = pygame.image.load(r'mdum_pruvodce2.png')

mdum4 = pygame.image.load(r'mdum3.png')
mdum_pruvodce4 = pygame.image.load(r'mdum_pruvodce3.png')

mdumm = pygame.image.load(r'mdumm.png')
mdumb = pygame.image.load(r'mdumb.png')
mdumh = pygame.image.load(r'mdumh.png')
mdums = pygame.image.load(r'mdums.png')
mdumamb = pygame.image.load(r'mdumamb.png')
mdumcel = pygame.image.load(r'mdumcel.png')


dog1 = pygame.image.load(r'dog1.png') #.convert_alpha()
car1 = pygame.image.load(r'car1.png')
hat1 = pygame.image.load(r'hat1.png')
boat1 = pygame.image.load(r'boat1.png')

#pixel obrázku 25
dog2 = pygame.image.load(r'dog2.png') ##.convert_alpha()
car2 = pygame.image.load(r'car2.png')
hat2 = pygame.image.load(r'hat2.png')
boat2 = pygame.image.load(r'boat2.png')

písmo1 = "arial"
fontmest = pygame.font.SysFont(písmo1, 15)
fontmest1 = pygame.font.SysFont(písmo1, 18)
fontfs = pygame.font.SysFont(písmo1, 18)

znacka_meny = "Ħ"
hrac_na_rade = 0



#mesta
class mesta:
    
    def __init__(self, jmeno, kupni_cena, navsteva, domecek, nova_kupni_cena, vlastnik):
        self.jmeno = jmeno
        self.kupni_cena = kupni_cena
        self.navsteva = navsteva
        self.domecek = domecek
        self.vlastnik = vlastnik
        self.nova_kupni_cena = nova_kupni_cena

    def karticky(self):
        if hrac_na_rade == x:
            textk = fontmest.render(f"Název města: {self.jmeno}", True, (red))
            surface.blit(textk, (960,600))
            textk1 = fontmest.render(f"Kupní cena města: {self.kupni_cena}{znacka_meny}", True, (red))
            surface.blit(textk1, (960,620))
            textk2 = fontmest.render(f"Cena za návštěvu tohoto města: {self.navsteva}{znacka_meny}", True, (red))
            surface.blit(textk2, (960,640))
            textk3 = fontmest.render(f"Pořizovací cena za místního průvodce pro město: {self.domecek}{znacka_meny}", True, (red))
            surface.blit(textk3, (960,660))
            textk4 = fontmest.render(f"Kupní cena s průvodcem je: {self.nova_kupni_cena}{znacka_meny}", True, (red))
            surface.blit(textk4, (960,680))
            textk5 = fontmest.render(f"Vlastníkem města je: {self.vlastnik}", True, (red))
            surface.blit(textk5, (960,700))
        if hrac_na_rade == y:
            textk = fontmest.render(f"Název města: {self.jmeno}", True, (blue))
            surface.blit(textk, (960,600))
            textk1 = fontmest.render(f"Kupní cena města: {self.kupni_cena}{znacka_meny}", True, (blue))
            surface.blit(textk1, (960,620))
            textk2 = fontmest.render(f"Cena za návštěvu tohoto města: {self.navsteva}{znacka_meny}", True, (blue))
            surface.blit(textk2, (960,640))
            textk3 = fontmest.render(f"Pořizovací cena za místního průvodce pro město: {self.domecek}{znacka_meny}", True, (blue))
            surface.blit(textk3, (960,660))
            textk4 = fontmest.render(f"Kupní cena s průvodcem je: {self.nova_kupni_cena}{znacka_meny}", True, (blue))
            surface.blit(textk4, (960,680))
            textk5 = fontmest.render(f"Vlastníkem města je: {self.vlastnik}", True, (blue))
            surface.blit(textk5, (960,700))
        

    def upgrade(self):
        if hrac_na_rade == x:
            textu = fontmest.render(f"Jste vlastníkem tohoto města tudíž si můžete koupit průvodce.", True, (red))
            textu2 = fontmest.render(f"Cena průvodce je {self.domecek}{znacka_meny}", True, (red))
            textu3 = fontmest.render(f"Nová cena za návštěvu bude {self.nova_kupni_cena}{znacka_meny}", True, (red))
            surface.blit(textu, (960,600))
            surface.blit(textu2, (960,620))
            surface.blit(textu3, (960,640))
            textu1 = fontmest.render("Pokud si chcete průvodce koupit stiskněte číslo 2", True, (red))
            surface.blit(textu1, (960,660))
        if hrac_na_rade == y:
            textu = fontmest.render(f"Jste vlastníkem tohoto města tudíž si můžete koupit průvodce.", True, (blue))
            textu2 = fontmest.render(f"Cena průvodce je {self.domecek}{znacka_meny}", True, (blue))
            textu3 = fontmest.render(f"Nová cena za návštěvu bude {self.nova_kupni_cena}{znacka_meny}", True, (blue))
            surface.blit(textu, (960,600))
            surface.blit(textu2, (960,620))
            surface.blit(textu3, (960,640))
            textu1 = fontmest.render("Pokud si chcete průvodce koupit stiskněte číslo 2", True, (blue))
            surface.blit(textu1, (960,660))
    


    
napis = fontmest.render("Pokud si chcete koupit město zmáčkněte číslo 1", True, (red))
napis2 = fontmest.render("Pokud chcete pokračovat ve hře zmáčkněte číslo 0", True, (red))

napisy = fontmest.render("Pokud si chcete koupit město zmáčkněte číslo 1", True, (blue))
napis2y = fontmest.render("Pokud chcete pokračovat ve hře zmáčkněte číslo 0", True, (blue))

#TEXT

písmo = 'freesansbold.ttf'


font = pygame.font.Font(písmo, 25)
text = font.render('Vyberte si jednu ze čtyř postav', True, (black), (255,255,255))
font1 = pygame.font.Font(písmo, 15)
text1 = font1.render('Kliknutím na P zvolíte Psa, Kliknutím na K zvolíte Klobouk, Kliknutím na A zvolíte Auto, Kliknutím na L zvolíte Loď', True, (black), (255,255,255))
textRect = text.get_rect()
textRect.center = ((480,100))
text1Rect = text.get_rect()
text1Rect.center = ((230,200))

font2 = pygame.font.Font(písmo, 18)
text2 = font2.render('Vybírá první hráč', True, (black), (255,255,255))
text2Rect = text.get_rect()
text2Rect.center = ((580,150))

text3 = font2.render('Vybírá druhý hráč', True, (black), (255,255,255))


font = pygame.font.Font(písmo, 15)
monopoly_obrazek = pygame.image.load(r'monopoly_obrazek.png')
#monopoly_nadpis = pygame.image.load(r'monopoly_nadpis.png')
text_konec = font.render("Pokračujte stisknutím klávesy Enter!", True, (black),(255,255,255))
text_konecRect = text.get_rect()
text_konecRect.center = ((540,910))

#ÚVOD

done = True

while done == True:
    surface.fill((255,255,255))
    #surface.blit(monopoly_nadpis,(190,100))
    surface.blit(monopoly_obrazek, (0,0))
    surface.blit(text_konec,text_konecRect)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            pygame.quit()
            quit()

        key = pygame.key.get_pressed()
        
        if key[pygame.K_RETURN] or key[pygame.K_KP_ENTER]:
            done = False
            
        pygame.display.update()

#VYBÍRÁNÍ POSTAVIČEK
        
done = True


while done == True:
    surface.fill((255,255,255))
    surface.blit(text,textRect)
    #surface.blit(text1,text1Rect)
    surface.blit(text2, text2Rect)
    q = surface.blit(dog1, (110,230)) #pixel 250
    v = surface.blit(car1, (65,560)) #pixel 400
    n = surface.blit(hat1, (565,560))#pixel 300
    m = surface.blit(boat1, (515,230)) # pixel 400
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            pygame.quit()
            quit()

        
        key = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if q.collidepoint(pos):
                pygame.draw.rect(surface,(200,200,200), (75,230,250,250))
                x = dog2
                done = False
                if done == False:
                    surface.fill(white)
            elif m.collidepoint(pos):
                x = boat2
                done = False
                if done == False:
                    surface.fill(white)
            elif v.collidepoint(pos):
                x = car2
                done = False
                if done == False:
                    surface.fill(white)
            elif n.collidepoint(pos):
                x = hat2
                done = False
                if done == False:
                    surface.fill(white)
            
        else:
            pygame.MOUSEBUTTONUP
    pygame.display.update()

font4 = pygame.font.Font(písmo, 30)
text4 = font4.render("Tato postava byla již zvolena prvním hráčem. Zvolte jinou!", True, (black), (255,255,255))
text4Rect = text.get_rect()
text4Rect.center = ((250,100))


done = True

while done == True:
        surface.fill((255,255,255))
        surface.blit(text,textRect)
        #surface.blit(text1,text1Rect)
        surface.blit(text3, text2Rect)
        surface.blit(dog1, (110,230)) #pixel 250
        surface.blit(car1, (65,560))
        surface.blit(hat1, (565,560))#pixel 300
        surface.blit(boat1, (515,230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                quit()

            key = pygame.key.get_pressed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if q.collidepoint(pos):
                    if x == dog2:
                        pygame.event.wait(80)
                        #surface.fill((255,255,255))
                        pygame.draw.rect(surface, (255,255,255), (40,20,950,200))
                        surface.blit(text4, text4Rect)
                        pygame.event.wait(240)
                    else:
                        y = dog2
                        done = False
                        
                elif m.collidepoint(pos):
                    if x == boat2:
                        #surface.fill((255,255,255))
                        pygame.draw.rect(surface, (255,255,255), (40,20,950,200))
                        surface.blit(text4, text4Rect)
                        pygame.event.wait(240)
                    
                    else:
                        y = boat2
                        done = False
                        
                elif v.collidepoint(pos):
                    if x == car2:
                        pygame.event.wait(80)
                        #surface.fill((255,255,255))
                        pygame.draw.rect(surface, (255,255,255), (40,20,950,200))
                        surface.blit(text4, text4Rect)
                        pygame.event.wait(240)
                    else:
                        y = car2
                        done = False
                        
                elif n.collidepoint(pos):
                    if x == hat2:
                        pygame.event.wait(80)
                        #surface.fill((255,255,255))
                        pygame.draw.rect(surface, (255,255,255), (40,20,950,200))
                        surface.blit(text4, text4Rect)
                        pygame.event.wait(240)
                    else:
                        y = hat2
                        done = False
                        
                
            pygame.display.update()

#HRA

width = 1350
height = 950

surface = pygame.display.set_mode((width,height))


board = pygame.image.load(r'board.png')


#HRÁČ:
x_money = 35000
y_money = 35000

x_majetek = []
y_majetek = []

#připsání majetku pro hráče x
w = 1020
h = 120
wy = 1210
hy = 120
hg2y = 0

hg2 = 0
hg3 = 0
hg4 = 0
hg5 = 0
hg6 = 0
hg7 = 0
hg8 = 0
hg9 = 0
hg10 = 0
hg11 = 0
hg12 = 0
hg13 = 0
hg14 = 0
hg15 = 0
hg16 = 0
hg17 = 0
hg18 = 0
hg19 = 0
hg20 = 0
hg21 = 0
hg22 = 0
hg23 = 0
hg24 = 0
hg25 = 0
hg26 = 0
hg27 = 0
hg28 = 0
hg29 = 0
hg30 = 0
hg31 = 0
hg32 = 0
hg33 = 0
hg34 = 0
hg35 = 0
hg36 = 0
hg37 = 0
hg38 = 0
hg39 = 0
hg40 = 0

pocet_mest = 0
pridat_mesto = False
nazev_mesta = 0
pole = 0



hrac_na_rade = 0

a = 880 #880, 900
b = 900

#x = pygame.draw.rect(surface, (0,255,0), (a,b,20,20))

c = 880
d = 880
#y = pygame.draw.rect(surface, (0,0,255), (c,d,20,20))

events = pygame.event.get()

pressed_space = False

vezen = False

#player 1 text a player 2 text

písmo1 = "arial"

fontp1 = pygame.font.SysFont(písmo1,30)
textp1 = fontp1.render("HRÁČ 1", True,(red))
fontp1m = pygame.font.SysFont(písmo1,18)
textp1m = fontp1m.render(f"Peníze: {x_money}{znacka_meny}", True, (red))
textp1ma = fontp1m.render(f"Majetek: ", True, (red))



fontp2 = pygame.font.SysFont(písmo1,30)
textp2 = fontp2.render("HRÁČ 2", True,(blue))
fontp2m = pygame.font.SysFont(písmo1,18)
textp2m = fontp2m.render(f"Peníze: {y_money}{znacka_meny}", True, (blue))
textp2ma = fontp2m.render(f"Majetek: ", True, (blue))

fontinfo = pygame.font.SysFont(písmo1, 28)
textinfo = fontinfo.render("Informace", True, (black))

wait = pygame.event.wait(240)


    

#POZICE NA HRACÍ PLOŠE
#používáme p1h
p1w1 = 812
p1w2 = 950
p1h1 = 810
p1h2 = 950

p2w1 = 736
p2w2 = 800

p3w1 = 656
p3w2 = 720

p4w1 = 576
p4w2 = 640

p5w1 = 504
p5w2 = 568

p6w1 = 424
p6w2 = 488

p7w1 = 344
p7w2 = 408

p8w1 = 264
p8w2 = 320

p9w1 = 200
p9w2 = 248

p10w1 = 120
p10w2 = 168

p11w1 = 0
p11w2 = 88

#používáme p12w
p12w1 = 0
p12w2 = 90
p12h1 = 740
p12h2 = 788

p13h1 = 660
p13h2 = 708

p14h1 = 580
p14h2 = 644

p15h1 = 505
p15h2 = 564

p16h1 = 430
p16h2 = 484

p17h1 = 356
p17h2 = 404

p18h1 = 276
p18h2 = 324

p19h1 = 196
p19h2 = 244

p20h1 = 116
p20h2 = 166

p21h1 = 0
p21h2 = 86

#používáme p22h
p22w1 = 116
p22w2 = 164
p22h1 = 0
p22h2 = 100

p23w1 = 196
p23w2 = 244

p24w1 = 276
p24w2 = 324

p25w1 = 356
p25w2 = 404  

p26w1 = 430
p26w2 = 484

p27w1 = 510
p27w2 = 560

p28w1 = 580
p28w2 = 630

p29w1 = 660
p29w2 = 708

p30w1 = 740
p30w2 = 788

p31w1 = 820
p31w2 = 950

#používáme p32w
p32w1 = 820
p32w2 = 950
p32h1 = 116
p32h2 = 164

p33h1 = 196
p33h2 = 244

p34h1 = 276
p34h2 = 324

p35h1 = 350
p35h2 = 400

p36h1 = 430
p36h2 = 480

p37h1 = 510
p37h2 = 552

p38h1 = 583
p38h2 = 630

p39h1 = 663
p39h2 = 708

p40h1 = 740
p40h2 = 788



fps = pygame.time.Clock()
ticks=pygame.time.get_ticks()
s = 0

value = int(8)

#KOSTKA
smth = 0

kostka1 = pygame.image.load(r'kostka1.png')
kostka2 = pygame.image.load(r'kostka2.png')
kostka3 = pygame.image.load(r'kostka3.png')
kostka4 = pygame.image.load(r'kostka4.png')
kostka5 = pygame.image.load(r'kostka5.png')
kostka6 = pygame.image.load(r'kostka6.png')

e = 450
f = 600
kostka = pygame.draw.rect(surface, (255,255,255), (e,f,40,40))
posun = 0
max_posun = 10 #random.randint(10,30)

font_roller2 = pygame.font.Font(písmo, 40)
text_roller2 = font_roller2.render(f" ", True, (0,0,0), (255,255,255))
text_roller2Rect = text_roller2.get_rect()
text_roller2Rect.center = kostka.center

"""
font_roller = pygame.font.Font(písmo,30)
text_roller = font_roller.render("Kostka: ", True, (0,0,0), (255,255,255))
text_rollerRect = text_roller.get_rect()
text_rollerRect.center = ((400,650))
"""

cislo_kostka = kostka1
draha1 = 50
draha2 = 60

u = 0
hrac_hodil_kostkou = False

            
done = True


while done == True:
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    surface.fill((255,255,255))
    surface.blit(board,(0, 0))
    #surface.blit(text_roller, text_rollerRect)
    surface.blit(textp1, (960,20))
    surface.blit(textp2, (1150,20))
    surface.blit(textp1m, (960,80))
    surface.blit(textp1ma, (960,120))
    surface.blit(textp2m, (1150,80))
    surface.blit(textp2ma, (1150,120))
    surface.blit(textinfo, (1100,560))
    #############surface.fill((255,255,255), rect=(960,400,200,200))

   
    
    for event in pygame.event.get():
  
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] :
            done = False
            pygame.quit()
            quit()

                    
        fontp1m = pygame.font.SysFont(písmo1,18)
        textp1m = fontp1m.render(f"Peníze: {x_money}{znacka_meny}", True, (red))
        textp1ma = fontp1m.render(f"Majetek: ", True, (red))

        fontp2m = pygame.font.SysFont(písmo1,18)
        textp2m = fontp2m.render(f"Peníze: {y_money}{znacka_meny}", True, (blue))
        textp2ma = fontp2m.render(f"Majetek: ", True, (blue))
                    
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_i]:
            if d <= 825 and c not in range(0,105) and c not in range(810,910) and d not in range(0,110):
                d = d + 10
                c = c
            else:
                d -= value
                c = c
        
        if keys[pygame.K_k]:
            if d in range(90,830) and c not in range (0,105) and c not in range (810,910) and d not in range(815,910):
                d = d - 10
                c = c
            else:
                d += value
                c = c

        if keys[pygame.K_l]:
            if c in range(85,825) and d not in range(0,105) and d not in range(815,910) and c not in range(810,910):
                c = c - 10
                d = d
            else:
                c += value
                d = d

        if keys[pygame.K_j]:
            if c <= 820 and d not in range(0,105) and d not in range(815,910) and c not in range (0,110):
                c = c +10
                d = d
            else:
                c -= value
                d = d
        
        
        if y == dog2:
            if c >= 910:
                c = c - 10
                d = d
            if c <= 0:
                c = c + 10
                b = b
            if d >= 910:
                d = d - 10
                c = c
            if d <= 0:
                d = d + 10
                c = c
        if y == car2:
            if c >= 890:
                c = c - 10
                d = d
            if c <= -1:
                c = c + 10
                b = b
            if d >= 910:
                d = d - 10
                c = c
            if d <= 0:
                d = d + 10
                c = c
        if y == hat2:
            if c >= 910:
                c = c - 10
                d = d
            if c <= 0:
                c = c + 10
                b = b
            if d >= 910:
                d = d - 10
                c = c
            if d <= 0:
                d = d + 10
                c = c
        if y == boat2:
            if c >= 891:
                c = c - 10
                d = d
            if c <= -20:
                c = c + 10
                b = b
            if d >= 910:
                d = d - 10
                c = c
            if d <= 0:
                d = d + 10
                c = c
        
        #fps.tick(60)
        surface.blit(board,(0, 0))
        surface.blit(y, (c,d))


        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if b <= 825 and a not in range(0,105) and a not in range(810,910) and b not in range(0,110):
                b = b + 10
                a = a
            else:
                b -= value
                a = a
        
        if keys[pygame.K_s]:
            if b in range(90,830) and a not in range (0,105) and a not in range (810,910) and b not in range(815,910):
                b = b - 10
                a = a
            else:
                b += value
                a = a

        if keys[pygame.K_d]:
            if a in range(85,825) and b not in range(0,105) and b not in range(815,910) and a not in range(810,910):
                a = a - 10
                b = b
            else:
                a += value
                b = b

        if keys[pygame.K_a]:
            if a <= 820 and b not in range(0,105) and b not in range(815,910) and a not in range (0,110):
                a = a +10
                b = b
            else:
                a -= value
                b = b
                
        
        
        if x == dog2:
            if a >= 910:
                a = a - 10
                b = b 
            if a <= 0:
                a = a + 10
                b = b 
            if b >= 910:
                b = b - 10
                a = a 
            if b <= 0:
                b = b + 10
                a = a 
                

                
        if x == car2:
            if a >= 890:
                a = a - 10
                b = b
            if a <= -1:
                a = a + 10
                b = b
            if b >= 910:
                b = b - 10
                a = a
            if b <= 0:
                b = b + 10
                a = a
        if x == hat2:
            if a >= 910:
                a = a - 10
                b = b
            if a <= 0:
                a = a + 10
                b = b
            if b >= 920:
                b = b - 10
                a = a
            if b <= 0:
                b = b + 10
                a = a
        if x == boat2:
            if a >= 891:
                a = a - 10
                b = b
            if a <= -20:
                a = a + 10
                b = b
            if b >= 910:
                b = b - 10
                a = a
            if b <= 0:
                b = b + 10
                a = a
        
        
        #print(a)
                
        #print(b)
        #print("\n")


        #surface.blit(x, (a,b))123456789
        
        #pygame.display.update()
        #fps.tick(60)
        #surface.blit(board, (0,0))
        #fps.tick(60)
        #surface.blit(board,(0, 0))
        #surface.blit(y, (c,d))
        #surface.blit(x, (a,b))
        r = pygame.draw.rect(surface, (black), (420,700,100,22))
        fontend = pygame.font.SysFont(písmo1,20)
        textend = fontend.render(f"KONEC HRY", True, (white))
        surface.blit(textend, (420,700))    
#KOSTKA
        
        #surface.blit(text_roller,text_rollerRect)
        if keys[pygame.K_h]:
            k = random.randint(0,10)
            cislo_kostky = random.randint(1,6)
            if posun < max_posun:
                if f in range(150,750) and e in range(150,750):
                    if k in range(0,2): #UP
                        e = e #-= random.randint(20,30)
                        f -= random.randint(draha1,draha2)
                        posun += 1
                    if k in range(3,5): #DOWN
                        e = e #+= random.randint(20,30)
                        f += random.randint(draha1,draha2)
                        posun += 1
                    if k in range(6,8): #RIGHT
                        e += random.randint(draha1,draha2)
                        f = f #-= random.randint(20,30)
                        posun += 1
                    if k in range(9,10): #LEFT
                        e -= random.randint(draha1,draha2)
                        f = f #+= random.randint(20,30)
                        posun += 1
                elif f >= 751:
                     e = e
                     f -= 20
                     posun += 1
                elif e >= 751:
                    e -= 20
                    f = f
                    posun += 1
                elif f <= 151:
                        e = e
                        f += 20
                        posun += 1
                elif e <= 151:
                    e += 20
                    f = f
                    posun += 1
                    

                if cislo_kostky == 1:
                    cislo_kostka = kostka1
                    u = 1
                    
                    
                if cislo_kostky == 2:
                    cislo_kostka = kostka2
                    u = 2
                    
                    
                if cislo_kostky == 3:
                    cislo_kostka = kostka3
                    u = 3
                    

                if cislo_kostky == 4:
                    cislo_kostka = kostka4
                    u = 4
                    

                if cislo_kostky == 5:
                    cislo_kostka = kostka5
                    u = 5
                    

                if cislo_kostky == 6:
                    cislo_kostka = kostka6
                    u = 6
                   
                  
                #text_roller2 = font_roller2.render(f" {cislo_kostka}", True, (0,0,0), (255,255,255))
            elif posun >= max_posun:
                e += 0
                f += 0
                hrac_hodil_kostkou = True
                #posun = 0
                
            
            

        
            
        kostka = pygame.draw.rect(surface, (255,255,255), (e,f,40,40))
            
        surface.blit(cislo_kostka, kostka)
        #print(u)
            
        if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
            hrac_hodil_kostkou = False
            e = 450
            f = 600
            posun = 0
            max_posun = 10
            kostka = pygame.draw.rect(surface, (255,255,255), (e,f,40,40))
            cislo_kostka = kostka1
            surface.blit(cislo_kostka, kostka)
            u = 0
            
        
        
        #pygame.display.update()123456789

            


#KUPOVÁNÍ A PÁSSOVÁNÍ
        #(self, jmeno, kupni_cena, navsteva, cena_domecku, nova_kupni_cena, vlastnik), mesta, karticky
        #textk,textk1 - 5, textu, textu1
        #1050,450
        #pygame.event.wait(240)
        #karticky 500-600, upgrade 500-520

        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
            hrac_na_rade = x

        
        if hrac_na_rade == x:
            red = (255,0,0)
            #pole 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p1w1,p1w2) and b in range(p1h1,p1h2):
                        textst = fontmest.render("Jste na STARTU", True, (red))
                        surface.blit(textst,(960,590))
                        textstpen = fontmest.render(f"Získáváte 5000{znacka_meny}", True, (red))
                        surface.blit(textstpen, (960,610))
                        pygame.event.wait(240)
                        x_money += 5000

            #pole 2            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
            
                    if a in range(p2w1,p2w2) and b in range(p1h1,p1h2):
                       if "Nairobi" in y_majetek and "Nairobi" not in x_majetek and nairobi.navsteva != 600:
                           texta = fontmest.render(f"Vlastníkem města {nairobi.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                       if "Nairobi" in y_majetek and "Nairobi" not in x_majetek and nairobi.navsteva == 600:
                           texta = fontmest.render(f"Vlastníkem města {nairobi.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {nairobi.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= nairobi.navsteva
                           y_money += nairobi.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                       if "Nairobi" not in x_majetek and "Nairobi" not in y_majetek:
                           nairobi = mesta("Nairobi", 1000, 200, 400, 600, "prozatím nikdo")
                           nairobi.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                       elif "Nairobi" in x_majetek and nairobi.navsteva != 600:
                           nairobi.upgrade()
                           pygame.event.wait(240)
                       elif "Nairobi" in x_majetek and nairobi.navsteva == 600:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p2w1,p2w2) and b in range(p1h1,p1h2) and pressed_space == True and "Nairobi" not in x_majetek and "Nairobi" not in y_majetek:
                        if x_money - 1000 >= 0:
                              x_money -= 1000
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg2 += 20
                                      x_majetek.append("Nairobi")
                              else:
                                  x_majetek.append("Nairobi")
                              #zapsání do majetku
                              #x_majetek.append("Nairobi")
                              textmajetekx = fontmest.render(f"Koupil jste si {nairobi.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg2 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if  event.key == pygame.K_KP2 and a in range(p2w1,p2w2) and b in range(p1h1,p1h2) and nairobi.navsteva != 600 and pressed_space == True and "Nairobi" in x_majetek and "Nairobi" not in y_majetek:
                       if x_money - 400 >= 0:
                              x_money -= 400
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              nairobi.navsteva = nairobi.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {nairobi.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                       else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p2w1,p2w2) and b in range(p1h1,p1h2)and pressed_space == True and "Nairobi" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p2w1,p2w2) and b in range(p1h1,p1h2) and pressed_space == True and "Nairobi" in y_majetek and "Nairobi" not in x_majetek and nairobi.navsteva != 600:
                              if x_money - 1500 >= 0:
                                  hg2 = 0
                                  x_money -= 1500
                                  y_money += 1500
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg2 += 20
                                          x_majetek.append("Nairobi")
                                          y_majetek.remove("Nairobi")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Nairobi")
                                      y_majetek.remove("Nairobi")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {nairobi.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p2w1,p2w2) and b in range(p1h1,p1h2) and pressed_space == True and "Nairobi" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {nairobi.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {nairobi.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= nairobi.navsteva
                               y_money += nairobi.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)
                               

                
            #pole 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if a in range(p3w1,p3w2) and b in range(p1h1,p1h2) and lol == 1:
                        if hrac_na_rade == x and lol == 1:
                            rf = random.randint(1,8)
                            if rf == 1:
                                x_money += 3500
                                textf1 = fontfs.render(f"Omylem vám přišlo na účet 3500{znacka_meny}", True, (red))
                                surface.blit(textf1, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 2:
                                x_money += 3000
                                y_money -= 3000
                                textf2 = fontfs.render(f"Spoluhráč ti musí dát 3000{znacka_meny}", True, (red))
                                surface.blit(textf2, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 3:
                                x_money += 1500
                                textf3 = fontfs.render(f"Ve tvém městě probíhal festival.", True, (red))
                                textf31 = fontfs.render(f"Vydělal jsi 1500 {znacka_meny}", True, (red))
                                surface.blit(textf3, (960,600))
                                surface.blit(textf31, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 4:
                                textf4 = fontfs.render(f"Je léto a všichni chtějí k moři.", True, (red))
                                textf41 = fontfs.render(f"Za každý svůj rezort získáváš 1000{znacka_meny}", True, (red))
                                surface.blit(textf4, (960,600))
                                surface.blit(textf41, (960,620))
                                if "Maledivy" not in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    textf42 = fontfs.render(f"Nevlastníte žádný rezort.", True, (red))
                                    surface.blit(textf42, (960,640))
                                if "Maledivy" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek: 
                                    x_money += 1000
                                if "Bali" in x_majetek and "Maledivy" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 1000
                                if "Hawaii" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 1000
                                if "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 1000
                                if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" not in x_majetek and "Bali" not in x_majetek:
                                    x_money += 2000
                                if "Bali" and "Hawaii" in x_majetek and "Maledivy" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 2000
                                if "Hawaii" in x_majetek and "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 3000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Bali" in x_majetek and "Hawaii" not in x_majetek:
                                    x_money += 3000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek:
                                    x_money += 3000
                                if "Hawaii" in x_majetek and "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 3000
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 5:
                                x_money += 5000
                                textf5 = fontfs.render(f"Tvé město se ocitlo v top 10 nejhezčích měst.", True, (red))
                                textf51 = fontfs.render(f"Všichni ho nyní navštěvují... vydělalo vám to 5000{znacka_meny}", True, (red))
                                surface.blit(textf5, (960,600))
                                surface.blit(textf51, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 6:
                                x_money -= 1000
                                textf6 = fontfs.render(f"Ve vašem městě vypadla elektřina.", True, (red))
                                textf61 = fontfs.render (f"Zaplatite 1000{znacka_meny} za opravu elektrarny", True, (red))
                                surface.blit(textf6, (960,600))
                                surface.blit(textf61, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 7:
                                x_money -= 3000
                                textf7 = fontfs.render(f"Proběhlo zemětřesení, za opravy zaplatíš 3000{znacka_meny}", True, (red))
                                surface.blit(textf7, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 8:
                                x_money -= 3500
                                textf8 = fontfs.render(f"V jednom z vašich měst se rozšířila epidemie.", True, (red))
                                textf81 = fontfs.render(f"Pošlete 3500{znacka_meny} na pomoc lidem", True, (red))
                                surface.blit(textf8, (960,600))
                                surface.blit(textf81, (960,620))
                                pygame.event.wait(240)
                                lol = 0
        
            #pole 4            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if a in range(p4w1,p4w2) and b in range(p1h1,p1h2):
                        if "Káhira" in y_majetek and "Káhira" not in x_majetek and kahira.navsteva != 750:
                           texta = fontmest.render(f"Vlastníkem města {kahira.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Káhira" in y_majetek and "Káhira" not in x_majetek and kahira.navsteva == 750:
                           texta = fontmest.render(f"Vlastníkem města {kahira.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {kahira.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= kahira.navsteva
                           y_money += kahira.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Káhira" not in x_majetek and "Káhira" not in y_majetek:
                           kahira = mesta("Káhira", 1200, 250, 480, 750, "prozatím nikdo")
                           kahira.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Káhira" in x_majetek and kahira.navsteva != 750:
                           kahira.upgrade()
                           pygame.event.wait(240)
                        elif "Káhira" in x_majetek and kahira.navsteva == 750:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p4w1,p4w2) and b in range(p1h1,p1h2) and pressed_space == True and "Káhira" not in x_majetek and "Káhira" not in x_majetek and "Káhira" not in y_majetek:
                        if x_money - kahira.kupni_cena >= 0:
                              x_money -= kahira.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg4 += 20
                                      x_majetek.append("Káhira")
                              else:
                                  x_majetek.append("Káhira")
                              #zapsání do majetku
                              #x_majetek.append("Káhira")
                              textmajetekx = fontmest.render(f"Koupil jste si {kahira.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg4 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p4w1,p4w2) and b in range(p1h1,p1h2) and kahira.navsteva != 750 and pressed_space == True and "Káhira" in x_majetek and "Káhira" not in y_majetek:
                        if x_money - kahira.domecek >= 0:
                              x_money -= kahira.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              kahira.navsteva = kahira.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {kahira.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p4w1,p4w2) and b in range(p1h1,p1h2)and pressed_space == True and "Káhira" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p4w1,p4w2) and b in range(p1h1,p1h2) and pressed_space == True and "Káhira" in y_majetek and "Káhira" not in x_majetek and kahira.navsteva != 750:
                              if x_money - 1800 >= 0:
                                  x_money -= 1800
                                  y_money += 1800
                                  hg4 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg4 += 20
                                          x_majetek.append("Káhira")
                                          y_majetek.remove("Káhira")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Káhira")
                                      y_majetek.remove("Káhira")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {kahira.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg4 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p4w1,p4w2) and b in range(p1h1,p1h2) and pressed_space == True and "Káhira" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {kahira.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {kahira.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= kahira.navsteva
                               y_money += kahira.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)
                              
            #if "Káhira" in x_majetek:
                #textmest = fontmest1.render("Káhira", True, (red))
                #surface.blit(textmest, (w,h + hg4))
                #pocet_mest = 0
                
            #pole5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
            
                    if a in range(p5w1,p5w2) and b in range(p1h1,p1h2):
                        procento = int((x_money*10)/100)
                        x_money -= procento
                        textchar = fontmest.render(f"Přispějte charitě {procento}{znacka_meny}", True, (red))
                        surface.blit(textchar, (960,600))
                        pygame.event.wait()
            #pole6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p6w1,p6w2) and b in range(p1h1,p1h2):
                        if "Maledivy" in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                            texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                            surface.blit(texta, (960,600))
                            textb = fontmest.render(f"Musíte zaplatit {maledivy.navsteva} {znacka_meny} za návštěvu města", True, (red))
                            surface.blit(textb, (960,620))
                            x_money -= maledivy.navsteva
                            y_money += maledivy.navsteva
                            textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                            surface.blit(textmoneyx, (960,660))
                            textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                            surface.blit(textmoneyy, (960,640))
                            pygame.event.wait(240)  
                        if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Maledivy" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek and "Srí Lanka" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)                               
                        if "Maledivy" in y_majetek and "Bali" in y_majetek and "Hawaii" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)     
                             
                        if "Maledivy" in y_majetek and "Bali" in y_majetek and "Srí Lanka" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Maledivy" in x_majetek and "Hawai" in y_majetek and "Srí Lanka" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)     
                        if "Maledivy" not in x_majetek and "Maledivy" not in y_majetek:
                           maledivy = mesta("Maledivy", 4000, 1000, 0, 0, "prozatím nikdo")
                           maledivy.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        if "Maledivy" in x_majetek:
                           textmas = fontmest.render("Jste vlastníkem tohoto města", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                        
                           #w = 980, h = 120,pocet_mest = 1  , i = 0
                     
                if event.key == pygame.K_KP1 and a in range(p6w1,p6w2) and b in range(p1h1,p1h2) and pressed_space == True and "Maledivy" not in x_majetek and "Maledivy" not in y_majetek:
                        if x_money - maledivy.kupni_cena >= 0:
                              x_money -= maledivy.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg6 += 20
                                      x_majetek.append("Maledivy")
                              else:
                                  x_majetek.append("Maledivy")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {maledivy.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg6 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                
                if event.key == pygame.K_KP0 and a in range(p6w1,p6w2) and b in range(p1h1,p1h2)and pressed_space == True:
                              hrac_na_rade = y
                              pressed_space = False
  
            #pole 7            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p7w1,p7w2) and b in range(p1h1,p1h2):
                        if "Rio de Janeiro" in y_majetek and "Rio de Janeiro" not in x_majetek and rio.navsteva != 920:
                           texta = fontmest.render(f"Vlastníkem města {rio.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Rio de Janeiro" in y_majetek and "Rio de Janeiro" not in x_majetek and rio.navsteva == 920:
                           texta = fontmest.render(f"Vlastníkem města {rio.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {rio.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= rio.navsteva
                           y_money += rio.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Rio de Janeiro" not in x_majetek and "Rio de Janeiro" not in y_majetek:
                           rio = mesta("Rio de Janeiro", 1400, 340, 560, 920, "prozatím nikdo")
                           rio.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Rio de Janeiro" in x_majetek and rio.navsteva != 920:
                           rio.upgrade()
                           pygame.event.wait(240)
                        elif "Rio de Janeiro" in x_majetek and rio.navsteva == 920:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           #w = 980, h = 120,pocet_mest = 1  , i = 0
                     
                if event.key == pygame.K_KP1 and a in range(p7w1,p7w2) and b in range(p1h1,p1h2) and pressed_space == True and "Rio de Janeiro" not in x_majetek and "Rio de Janeiro" not in y_majetek:
                        if x_money - rio.kupni_cena >= 0:
                              x_money -= rio.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg7 += 20
                                      x_majetek.append("Rio de Janeiro")
                              else:
                                  x_majetek.append("Rio de Janeiro")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {rio.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg7 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p7w1,p7w2) and b in range(p1h1,p1h2) and rio.navsteva != 920 and pressed_space == True and "Rio de Janeiro" in x_majetek and "Rio de Janeiro" not in y_majetek:
                        if x_money - rio.domecek >= 0:
                              x_money -= rio.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              rio.navsteva = rio.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {rio.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p7w1,p7w2) and b in range(p1h1,p1h2)and pressed_space == True and "Rio de Janeiro" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p7w1,p7w2) and b in range(p1h1,p1h2) and pressed_space == True and "Rio de Janeiro" in y_majetek and "Rio de Janeiro" not in x_majetek and rio.navsteva != 920:
                              if x_money - 2100 >= 0:
                                  x_money -= 2100
                                  y_money += 2100
                                  hg7 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg7 += 20
                                          x_majetek.append("Rio de Janeiro")
                                          y_majetek.remove("Rio de Janeiro")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Rio de Janeiro")
                                      y_majetek.remove("Rio de Janeiro")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {rio.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg7 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p7w1,p7w2) and b in range(p1h1,p1h2) and pressed_space == True and "Rio de Janeiro" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {rio.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {rio.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= rio.navsteva
                               y_money += rio.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)
            
            #pole 8
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    

                    
                    if a in range(p8w1,p8w2) and b in range(p1h1,p1h2) and lol == 1:
                        if hrac_na_rade == x and lol == 1:
                                rs = random.randint(1,10)
                                if rs == 1:
                                    texts1 = fontfs.render(f"Jděte na nejbližší volné město", True, (red))
                                    surface.blit(texts1, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 2:
                                    texts2 = fontfs.render(f"Jděte na pole s letištěm", True, (red))
                                    surface.blit(texts2, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 3:
                                    texts3 = fontfs.render(f"Jděte do vězení!", True, (red))
                                    surface.blit(texts3, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 4:
                                    texts4 = fontfs.render(f"Jděte na vaše nejbližší město", True, (red))
                                    surface.blit(texts4, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 5:
                                    texts5 = fontfs.render(f"Jděte na nejbližší město vašeho spoluhráče", True, (red))
                                    surface.blit(texts5, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 6:
                                    texts6 = fontfs.render(f"Jděte na start", True, (red))
                                    surface.blit(texts6, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 7:
                                    texts7 = fontfs.render(f"Jděte na pole s letištěm", True, (red))
                                    surface.blit(texts7, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 8:
                                    texts8 = fontfs.render(f"Jděte na emisní povolenku", True, (red))
                                    surface.blit(texts8, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 9:
                                    vpred = random.randint(1,10)
                                    if vpred == 1:
                                        texts91 = fontfs.render(f"Jděte vpřed o {vpred} políčko", True, (red))
                                        surface.blit(texts91, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 2 or vpred == 3 or vpred == 4:
                                        texts92 = fontfs.render(f"Jděte vpřed o {vpred} políčka", True, (red))
                                        surface.blit(texts92, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 5 or vpred == 6 or vpred == 7 or vpred == 8 or vpred == 9 or vpred == 10:
                                        texts93 = fontfs.render(f"Jděte vpřed o {vpred} políček", True, (red))
                                        surface.blit(texts93, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
                                if rs == 10:
                                    dozadu = random.randint(1,10)
                                    if dozadu == 1:
                                        texts101 = fontfs.render(f"Jděte dozadu o {dozadu} políčko", True, (red))
                                        surface.blit(texts101, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 2 or dozadu == 3 or dozadu == 4:
                                        texts102 = fontfs.render(f"Jděte dozadu o {dozadu} políčka", True, (red))
                                        surface.blit(texts102, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 5 or dozadu == 6 or dozadu == 7 or dozadu == 8 or dozadu == 9 or dozadu == 10:
                                        texts103 = fontfs.render(f"Jděte dozadu o {dozadu} políček", True, (red))
                                        surface.blit(texts103, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0

            if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
                lol = 1
            #pole 9
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p9w1,p9w2) and b in range(p1h1,p1h2):
                        if "Buenos Aires" in y_majetek and "Buenos Aires" not in x_majetek and buenos.navsteva != 1100:
                           texta = fontmest.render(f"Vlastníkem města {buenos.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Buenos Aires" in y_majetek and "Buenos Aires" not in x_majetek and buenos.navsteva == 1100:
                           texta = fontmest.render(f"Vlastníkem města {buenos.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {buenos.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= buenos.navsteva
                           y_money += buenos.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Buenos Aires" not in x_majetek and "Buenos Aires" not in y_majetek:
                           buenos = mesta("Buenos Aires", 1600, 400, 640, 1100, "prozatím nikdo")
                           buenos.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Buenos Aires" in x_majetek and buenos.navsteva != 1100:
                           buenos.upgrade()
                           pygame.event.wait(240)
                        elif "Buenos Aires" in x_majetek and buenos.navsteva == 1100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p9w1,p9w2) and b in range(p1h1,p1h2) and pressed_space == True and "Buenos Aires" not in x_majetek and "Buenos Aires" not in y_majetek:
                        if x_money - buenos.kupni_cena >= 0:
                              x_money -= buenos.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg9 += 20
                                      x_majetek.append("Buenos Aires")
                              else:
                                  x_majetek.append("Buenos Aires")
                              #zapsání do majetku
                              #x_majetek.append("Buenos Aires")
                              textmajetekx = fontmest.render(f"Koupil jste is {buenos.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg9 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p9w1,p9w2) and b in range(p1h1,p1h2) and buenos.navsteva != 1100 and pressed_space == True and "Buenos Aires" in x_majetek and "Buenos Aires" not in y_majetek:
                        if x_money - buenos.domecek >= 0:
                              x_money -= buenos.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              buenos.navsteva = buenos.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {buenos.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p9w1,p9w2) and b in range(p1h1,p1h2)and pressed_space == True and "Buenos Aires" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p9w1,p9w2) and b in range(p1h1,p1h2) and pressed_space == True and "Buenos Aires" in y_majetek and "Buenos Aires" not in x_majetek and buenos.navsteva != 1100:
                              if x_money - 2400 >= 0:
                                  x_money -= 2400
                                  y_money += 2400
                                  hg9 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg9 += 20
                                          x_majetek.append("Buenos Aires")
                                          y_majetek.remove("Buenos Aires")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Buenos Aires")
                                      y_majetek.remove("Buenos Aires")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {buenos.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg9 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p9w1,p9w2) and b in range(p1h1,p1h2) and pressed_space == True and "Buenos Aires" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {buenos.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {buenos.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= buenos.navsteva
                               y_money += buenos.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)
            

                
            #pole10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p10w1,p10w2) and b in range(p1h1,p1h2):
                        if "Santiago de Chille" in y_majetek and "Santiago de Chille" not in x_majetek and santiago.navsteva != 1100:
                           texta = fontmest.render(f"Vlastníkem města {santiago.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Santiago de Chille" in y_majetek and "Santiago de Chille" not in x_majetek and santiago.navsteva == 1100:
                           texta = fontmest.render(f"Vlastníkem města {santiago.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {santiago.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= santiago.navsteva
                           y_money += santiago.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Santiago de Chille" not in x_majetek and "Santiago de Chille" not in y_majetek:
                           santiago = mesta("Santiago de Chille", 1600, 400, 640, 1100, "prozatím nikdo")
                           santiago.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Santiago de Chille" in x_majetek and santiago.navsteva != 1100:
                           santiago.upgrade()
                           pygame.event.wait(240)
                        elif "Santiago de Chille" in x_majetek and santiago.navsteva == 1100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if  event.key == pygame.K_KP1 and a in range(p10w1,p10w2) and b in range(p1h1,p1h2) and pressed_space == True and "Santiago de Chille" not in x_majetek and "Santiago de Chille" not in y_majetek:
                        if x_money - santiago.kupni_cena >= 0:
                              x_money -= santiago.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg10 += 20
                                      x_majetek.append("Santiago de Chille")
                              else:
                                  x_majetek.append("Santiago de Chille")
                              #zapsání do majetku
                              #x_majetek.append("Santiago de Chille")
                              textmajetekx = fontmest.render(f"Koupil jste {santiago.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg10 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p10w1,p10w2) and b in range(p1h1,p1h2) and santiago.navsteva != 1100 and pressed_space == True and "Santiago de Chille" in x_majetek and "Santiago de Chille" not in y_majetek:
                        if x_money - santiago.domecek >= 0:
                              x_money -= santiago.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              santiago.navsteva = santiago.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {santiago.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)     
                if event.key == pygame.K_KP0 and a in range(p10w1,p10w2) and b in range(p1h1,p1h2)and pressed_space == True and "Santiago de Chille" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p10w1,p10w2) and b in range(p1h1,p1h2) and pressed_space == True and "Santiago de Chille" in y_majetek and "Santiago de Chille" not in x_majetek and santiago.navsteva != 1100:
                              if x_money - 2400 >= 0:
                                  x_money -= 2400
                                  y_money += 2400
                                  hg10 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg10 += 20
                                          x_majetek.append("Santiago de Chille")
                                          y_majetek.remove("Santiago de Chille")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Santiago de Chille")
                                      y_majetek.remove("Santiago de Chille")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {santiago.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg10 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p10w1,p10w2) and b in range(p1h1,p1h2) and pressed_space == True and "Santiago de Chille" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {santiago.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {santiago.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= santiago.navsteva
                               y_money += santiago.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)
                
            #pole11
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True

                    if a in range(p11w1,p11w2) and b in range(p1h1,p1h2):
                        textvezeni = fontmest.render(f"Jste ve vězení!", True, (red))
                        surface.blit(textvezeni, (960,600))
                        textvezeni1 = fontmest.render(f"Jestli chcete hodit kostkou, zkuste to", True, (red))
                        surface.blit(textvezeni1, (960,620))
                        textvezeni2 = fontmest.render(f"Nebo zmáčkněte číslo 3 a zaplaťte 1000{znacka_meny}", True, (red))
                        surface.blit(textvezeni2, (960,640))
                        pygame.event.wait(240)
                    vezen = True
                if a in range(p11w1,p11w2) and b in range(p1h1,p1h2) and pressed_space == True and keys[pygame.K_KP3]:
                    if x_money - 1000 >= 0:
                        x_money -= 1000
                        pygame.event.wait(240)
                        vezen = False
                    else:
                        textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                        surface.blit(textnedostatekp, (960,600))
                        pygame.event.wait(240)
                        vezen = False

                        
            if event.type == pygame.KEYUP and vezen == True:   
                    if hrac_hodil_kostkou == True and a in range(p11w1,p11w2) and b in range(p1h1,p1h2):
                            if u == 6:
                                textvezeni3 = fontmest.render(f"Můžete pokračovat ve hře, jste venku z vězení!", True, (red))
                                surface.blit(textvezeni3, (960,600))
                                pygame.event.wait(240)
                                hrac_hodil_kostkou = False
                                vezen = False
                            else: 
                                textvezeni4 = fontmest.render(f"Bohužel jste hodil {u}, nejste venku!", True, (red))
                                surface.blit(textvezeni4, (960,600))
                                pygame.event.wait(240)
                                hrac_hodil_kostkou = False
                                vezen = False
                                
              
            #pole12 p12w1 = 0 p12w2 = 90 p12h1 = 740 p12h1 = 788
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p12w1,p12w2) and b in range(p12h1,p12h2):
                        if "Kodaň" in y_majetek and "Kodaň" not in x_majetek and kodan.navsteva != 1400:
                           texta = fontmest.render(f"Vlastníkem města {kodan.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Kodaň" in y_majetek and "Kodaň" not in x_majetek and kodan.navsteva == 1400:
                           texta = fontmest.render(f"Vlastníkem města {kodan.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {kodan.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= kodan.navsteva
                           y_money += kodan.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Kodaň" not in x_majetek and "Kodaň" not in y_majetek:
                           kodan = mesta("Kodaň", 2000, 560, 800, 1400, "prozatím nikdo")
                           kodan.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Kodaň" in x_majetek and kodan.navsteva != 1400:
                           kodan.upgrade()
                           pygame.event.wait(240)
                        elif "Kodaň" in x_majetek and kodan.navsteva == 1400:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p12h1,p12h2) and pressed_space == True and "Kodaň" not in x_majetek and "Kodaň" not in y_majetek:
                        if x_money - kodan.kupni_cena >= 0:
                              x_money -= kodan.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg12 += 20
                                      x_majetek.append("Kodaň")
                              else:
                                  x_majetek.append("Kodaň")
                              #zapsání do majetku
                              #x_majetek.append("Kodaň")
                              textmajetekx = fontmest.render(f"Koupil jste si {kodan.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg12 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p12w1,p12w2) and b in range(p12h1,p12h2) and kodan.navsteva != 1400 and pressed_space == True and "Kodaň" in x_majetek and "Kodaň" not in y_majetek: 
                        if x_money - kodan.domecek >= 0:
                              x_money -= kodan.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              kodan.navsteva = kodan.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {kodan.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p12h1,p12h2)and pressed_space == True and "Kodaň" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p12w1,p12w2) and b in range(p12h1,p12h2) and pressed_space == True and "Kodaň" in y_majetek and "Kodaň" not in x_majetek and kodan.navsteva != 1400:
                              if x_money - 3000 >= 0:
                                  x_money -= 3000
                                  y_money += 3000
                                  hg12 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg12 += 20
                                          x_majetek.append("Kodaň")
                                          y_majetek.remove("Kodaň")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Kodaň")
                                      y_majetek.remove("Kodaň")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {kodan.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg12 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p12h1,p12h2) and pressed_space == True and "Kodaň" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {kodan.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {kodan.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= kodan.navsteva
                               y_money += kodan.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)       

                
            #pole13
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True

                    if a in range(p12w1,p12w2) and b in range(p13h1,p13h2):
                        if "Celnice" not in x_majetek and "Celnice" not in y_majetek:
                            textcelnice = fontmest.render(f"Název města: Celnice", True, (red))
                            surface.blit(textcelnice, (960,600))
                            textkcelnice1 = fontmest.render(f"Kupní cena: 1500{znacka_meny}", True, (red))
                            surface.blit(textkcelnice1, (960,620))
                            textkcelnice2 = fontmest.render(f"Cena za návštěvu tohoto města: 200x hod kostkou", True, (red))
                            surface.blit(textkcelnice2, (960,640))
                            surface.blit(napis, (960,730))
                            surface.blit(napis2, (960,750))
                            pygame.event.wait(240)
                    
                        if "Celnice" in y_majetek:
                           textcelnice3 = fontmest.render(f"Vlastníkem Celnice je Hráč 2.", True, (red))
                           #textb = fontmest.render(f"Musíte zaplatit {kodan.navsteva}{znacka_meny} za návštěvu města", True, (red))
                           surface.blit(textcelnice3, (960,600))
                           #surface.blit(textb, (960, 620))
                           textca = fontmest.render(f"Hoďte ještě jednou kostkou!", True, (red))
                           surface.blit(textca, (960,620))
                           x_money2 = copy.copy(x_money)
                           pygame.event.wait(240)
                           
                if event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p13h1,p13h2) and pressed_space == True and "Celnice" not in x_majetek and "Celnice" not in y_majetek:
                        if x_money - 1500 >= 0:
                              x_money -= 1500
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg13 += 20
                                      x_majetek.append("Celnice")
                              else:
                                  x_majetek.append("Celnice")
                              #zapsání do majetku
                              #x_majetek.append("Kodaň")
                              textmajetekx = fontmest.render(f"Koupil jste si Celnice", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                            
            if a in range(p12w1,p12w2) and b in range(p13h1,p13h2) and pressed_space == True and "Celnice" in y_majetek and "Celnice" not in x_majetek and "Ambasáda" not in y_majetek:
                #if event.type == pygame.KEYDOWN:
                    if u == 1:
                        cacena = 1*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                    
                    if u == 2:
                        cacena = 2*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
              
                    if u == 3:
                        cacena = 3*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 4:
                        cacena = 4*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 5:
                        cacena = 5*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                            
                        
                    if u == 6:
                        cacena = 6*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                    
                    

                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                        pressed_space = False
                        smth = 0
                        
            if a in range(p12w1,p12w2) and b in range(p13h1,p13h2) and pressed_space == True and "Celnice" in y_majetek and "Celnice" not in x_majetek and "Ambasáda" in y_majetek:
                #if event.type == pygame.KEYDOWN:
                    if u == 1:
                        cacena = 1*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                    
                    if u == 2:
                        cacena = 2*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
              
                    if u == 3:
                        cacena = 3*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 4:
                        cacena = 4*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 5:
                        cacena = 5*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                            
                        
                    if u == 6:
                        cacena = 6*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                    
                    

                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                        pressed_space = False
                        smth = 0
                        
            if a in range(p12w1,p12w2) and b in range(p13h1,p13h2) and pressed_space == True and smth == 1:
                roz = x_money2 - x_money
                textca = fontmest.render(f"Musíte zaplatit {roz}{znacka_meny}", True, (red))
                surface.blit(textca, (960,600))
                pygame.event.wait(240)
                    
                if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                    smth = 0
            #pole14
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p12w1,p12w2) and b in range(p14h1,p14h2):
                        if "Berlín" in y_majetek and "Berlín" not in x_majetek and berlin.navsteva != 1700:
                           texta = fontmest.render(f"Vlastníkem města {berlin.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Berlín" in y_majetek and "Berlín" not in x_majetek and berlin.navsteva == 1700:
                           texta = fontmest.render(f"Vlastníkem města {berlin.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {berlin.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= berlin.navsteva
                           y_money += berlin.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Berlín" not in x_majetek and "Berlín" not in y_majetek:
                           berlin = mesta("Berlín", 2300, 670, 920, 1700, "prozatím nikdo")
                           berlin.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Berlín" in x_majetek and berlin.navsteva != 1700:
                           berlin.upgrade()
                           pygame.event.wait(240)
                        elif "Berlín" in x_majetek and berlin.navsteva == 1700:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if  event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p14h1,p14h2) and pressed_space == True and "Berlín" not in x_majetek and "Berlín" not in y_majetek:
                        if x_money - berlin.kupni_cena >= 0:
                              x_money -= berlin.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg14 += 20
                                      x_majetek.append("Berlín")
                              else:
                                  x_majetek.append("Berlín")
                              #zapsání do majetku
                              #x_majetek.append("Berlín")
                              textmajetekx = fontmest.render(f"Koupil jste si {berlin.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg14 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p12w1,p12w2) and b in range(p14h1,p14h2) and berlin.navsteva != 1700 and pressed_space == True and "Berlín" in x_majetek and "Berlín" not in y_majetek:
                        if x_money - berlin.domecek >= 0:
                              x_money -= berlin.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              berlin.navsteva = berlin.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {berlin.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)     
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p14h1,p14h2)and pressed_space == True and "Berlín" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p12w1,p12w2) and b in range(p14h1,p14h2) and pressed_space == True and "Berlín" in y_majetek and "Berlín" not in x_majetek and berlin.navsteva != 1700:
                              if x_money - 3450 >= 0:
                                  x_money -= 3450
                                  y_money += 3450
                                  hg14 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg14 += 20
                                          x_majetek.append("Berlín")
                                          y_majetek.remove("Berlín")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Berlín")
                                      y_majetek.remove("Berlín")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {berlin.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg14 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p14h1,p14h2) and pressed_space == True and "Berlín" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {berlin.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {berlin.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= berlin.navsteva
                               y_money += berlin.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)       
        


            #pole15
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p12w1,p12w2) and b in range(p15h1,p15h2):
                        if "Amsterdam" in y_majetek and "Amsterdam" not in x_majetek and amsterdam.navsteva != 1700:
                           texta = fontmest.render(f"Vlastníkem města {amsterdam.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Amsterdam" in y_majetek and "Amsterdam" not in x_majetek and amsterdam.navsteva == 1700:
                           texta = fontmest.render(f"Vlastníkem města {amsterdam.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {amsterdam.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= amsterdam.navsteva
                           y_money += amsterdam.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Amsterdam" not in x_majetek and "Amsterdam" not in y_majetek:
                           amsterdam = mesta("Amsterdam", 2300, 670, 920, 1700, "prozatím nikdo")
                           amsterdam.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Amsterdam" in x_majetek and amsterdam.navsteva != 1700:
                           berlin.upgrade()
                           pygame.event.wait(240)
                        elif "Amsterdam" in x_majetek and amsterdam.navsteva == 1700:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p15h1,p15h2) and pressed_space == True and "Amsterdam" not in x_majetek and "Amsterdam" not in y_majetek:
                        if x_money - amsterdam.kupni_cena >= 0:
                              x_money -= amsterdam.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg15 += 20
                                      x_majetek.append("Amsterdam")
                              else:
                                  x_majetek.append("Amsterdam")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {amsterdam.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg15 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240) 
                if event.key == pygame.K_KP2 and a in range(p12w1,p12w2) and b in range(p15h1,p15h2) and amsterdam.navsteva != 1700 and pressed_space == True and "Amsterdam" in x_majetek and "Amsterdam" not in y_majetek:
                        if x_money - amsterdam.domecek >= 0:
                              x_money -= amsterdam.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              amsterdam.navsteva = amsterdam.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {amsterdam.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)       
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p15h1,p15h2)and pressed_space == True and "Amsterdam" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p12w1,p12w2) and b in range(p15h1,p15h2) and pressed_space == True and "Amsterdam" in y_majetek and "Amsterdam" not in x_majetek and amsterdam.navsteva != 1700:
                              if x_money - 3450 >= 0:
                                  x_money -= 3450
                                  y_money += 3450
                                  hg15 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg15 += 20
                                          x_majetek.append("Amsterdam")
                                          y_majetek.remove("Amsterdam")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Amsterdam")
                                      y_majetek.remove("Amsterdam")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {amsterdam.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg15 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p15h1,p15h2) and pressed_space == True and "Amsterdam" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {amsterdam.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {amsterdam.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= amsterdam.navsteva
                               y_money += amsterdam.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)              


            #pole16
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p12w1,p12w2) and b in range(p16h1,p16h2):
                        if "Bali" in y_majetek and "Srí Lanka" not in y_majetek and "Maledivy" not in y_majetek and "Hawaii" not in y_majetek:
                            texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 2.", True, (red))
                            surface.blit(texta, (960,600))
                            textb = fontmest.render(f"Musíte zaplatit {bali.navsteva} {znacka_meny} za návštěvu města", True, (red))
                            surface.blit(textb, (960,620))
                            x_money -= bali.navsteva
                            y_money += bali.navsteva
                            textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                            surface.blit(textmoneyx, (960,660))
                            textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                            surface.blit(textmoneyy, (960,640))
                            pygame.event.wait(240)  
                        if "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Maledivy" not in y_majetek and "Hawaii" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Bali" in y_majetek and "Maledivy" in y_majetek and "Srí Lanka" not in y_majetek and "Hawaii" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Bali" in y_majetek and "Hawaii" in y_majetek and "Srí Lanka" not in y_majetek and "Maledivy" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)                               
                        if "Bali" in y_majetek and "Hawaii" in y_majetek and "Maledivy" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)     
                        if "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Maledivy" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)     
                        if "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 1.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)     
                        if "Bali" not in x_majetek and "Bali" not in y_majetek:
                           bali = mesta("Bali", 4000, 1000, 0, 0, "prozatím nikdo")
                           bali.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        if "Bali" in x_majetek:
                           textmas = fontmest.render("Jste vlastníkem tohoto města", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                        #if "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" in x_majetek and "Maledivy" in x_majetek:
                            #textvyhra = fontmest.render("Vyhrál jste hru!", True, (red))
                            #surface.blit(textvyhra, (960,600))
                            #pygame.event.wait(240)

                if event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p16h1,p16h2) and pressed_space == True and "Bali" not in x_majetek and "Bali" not in y_majetek:
                        if x_money - bali.kupni_cena >= 0:
                              x_money -= bali.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg16 += 20
                                      x_majetek.append("Bali")
                              else:
                                  x_majetek.append("Bali")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {bali.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg16 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p16h1,p16h2) and pressed_space == True:
                              hrac_na_rade = y
                              pressed_space = False

            #pole17
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p12w1,p12w2) and b in range(p17h1,p17h2):
                        if "Wellington" in y_majetek and "Wellington" not in x_majetek and wellington.navsteva != 2100:
                           texta = fontmest.render(f"Vlastníkem města {wellington.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Wellington" in y_majetek and "Wellington" not in x_majetek and wellington.navsteva == 2100:
                           texta = fontmest.render(f"Vlastníkem města {wellington.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {wellington.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= wellington.navsteva
                           y_money += wellington.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Wellington" not in x_majetek and "Wellington" not in y_majetek:
                           wellington = mesta("Wellington", 2800, 900, 1120, 2100, "prozatím nikdo")
                           wellington.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Wellington" in x_majetek and wellington.navsteva != 2100:
                           wellington.upgrade()
                           pygame.event.wait(240)
                        elif "Wellington" in x_majetek and wellington.navsteva == 2100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p17h1,p17h2) and pressed_space == True and "Wellington" not in x_majetek and "Wellington" not in y_majetek:
                        if x_money - wellington.kupni_cena >= 0:
                              x_money -= wellington.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg17 += 20
                                      x_majetek.append("Wellington")
                              else:
                                  x_majetek.append("Wellington")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {wellington.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg17 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p12w1,p12w2) and b in range(p17h1,p17h2) and wellington.navsteva != 2100 and pressed_space == True and "Wellington" in x_majetek and "Wellington" not in y_majetek:
                        if x_money - wellington.domecek >= 0:
                              x_money -= wellington.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              wellington.navsteva = wellington.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {wellington.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p17h1,p17h2)and pressed_space == True and "Wellington" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p12w1,p12w2) and b in range(p17h1,p17h2) and pressed_space == True and "Wellington" in y_majetek and "Wellington" not in x_majetek and wellington.navsteva != 2100:
                              if x_money - 4200 >= 0:
                                  x_money -= 4200
                                  y_money += 4200
                                  hg17 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg17 += 20
                                          x_majetek.append("Wellington")
                                          y_majetek.remove("Wellington")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Wellington")
                                      y_majetek.remove("Wellington")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {wellington.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg17 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p17h1,p17h2) and pressed_space == True and "Wellington" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {wellington.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {wellington.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= wellington.navsteva
                               y_money += wellington.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)              
      

            #pole18
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if a in range(p12w1,p12w2) and b in range(p18h1,p18h2) and lol == 1:
                        if hrac_na_rade == x and lol == 1:
                            rf = random.randint(1,8)
                            if rf == 1:
                                x_money += 3500
                                textf1 = fontfs.render(f"Omylem vám přišlo na účet 3500{znacka_meny}", True, (red))
                                surface.blit(textf1, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 2:
                                x_money += 3000
                                y_money -= 3000
                                textf2 = fontfs.render(f"Spoluhráč ti musí dát 3000{znacka_meny}", True, (red))
                                surface.blit(textf2, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 3:
                                x_money += 1500
                                textf3 = fontfs.render(f"Ve tvém městě probíhal festival.", True, (red))
                                textf31 = fontfs.render(f"Vydělal jsi 1500 {znacka_meny}", True, (red))
                                surface.blit(textf3, (960,600))
                                surface.blit(textf31, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 4:
                                textf4 = fontfs.render(f"Je léto a všichni chtějí k moři.", True, (red))
                                textf41 = fontfs.render(f"Za každý svůj rezort získáváš 1000{znacka_meny}", True, (red))
                                surface.blit(textf4, (960,600))
                                surface.blit(textf41, (960,620))
                                if "Maledivy" not in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    textf42 = fontfs.render(f"Nevlastníte žádný rezort.", True, (red))
                                    surface.blit(textf42, (960,640))
                                if "Maledivy" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek: 
                                    x_money += 1000
                                if "Bali" in x_majetek and "Maledivy" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 1000
                                if "Hawaii" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 1000
                                if "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 1000
                                if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" not in x_majetek and "Bali" not in x_majetek:
                                    x_money += 2000
                                if "Bali" and "Hawaii" in x_majetek and "Maledivy" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 2000
                                if "Hawaii" in x_majetek and "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 3000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Bali" in x_majetek and "Hawaii" not in x_majetek:
                                    x_money += 3000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek:
                                    x_money += 3000
                                if "Hawaii" in x_majetek and "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 3000
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 5:
                                x_money += 5000
                                textf5 = fontfs.render(f"Tvé město se ocitlo v top 10 nejhezčích měst.", True, (red))
                                textf51 = fontfs.render(f"Všichni ho nyní navštěvují... vydělalo vám to 5000{znacka_meny}", True, (red))
                                surface.blit(textf5, (960,600))
                                surface.blit(textf51, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 6:
                                x_money -= 1000
                                textf6 = fontfs.render(f"Ve vašem městě vypadla elektřina.", True, (red))
                                textf61 = fontfs.render (f"Zaplatite 1000{znacka_meny} za opravu elektrarny", True, (red))
                                surface.blit(textf6, (960,600))
                                surface.blit(textf61, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 7:
                                x_money -= 3000
                                textf7 = fontfs.render(f"Proběhlo zemětřesení, za opravy zaplatíš 3000{znacka_meny}", True, (red))
                                surface.blit(textf7, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 8:
                                x_money -= 3500
                                textf8 = fontfs.render(f"V jednom z vašich měst se rozšířila epidemie.", True, (red))
                                textf81 = fontfs.render(f"Pošlete 3500{znacka_meny} na pomoc lidem", True, (red))
                                surface.blit(textf8, (960,600))
                                surface.blit(textf81, (960,620))
                                pygame.event.wait(240)
                                lol = 0
            #pole19
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p12w1,p12w2) and b in range(p19h1,p19h2):
                        if "Melbourne" in y_majetek and "Melbourne" not in x_majetek and melbourne.navsteva != 2400:
                           texta = fontmest.render(f"Vlastníkem města {melbourne.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Melbourne" in y_majetek and "Melbourne" not in x_majetek and melbourne.navsteva == 2400:
                           texta = fontmest.render(f"Vlastníkem města {melbourne.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {melbourne.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= melbourne.navsteva
                           y_money += melbourne.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Melbourne" not in x_majetek and "Melbourne" not in y_majetek:
                           melbourne = mesta("Melbourne", 3200, 1050, 1280, 2400, "prozatím nikdo")
                           melbourne.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Melbourne" in x_majetek and melbourne.navsteva != 2400:
                           melbourne.upgrade()
                           pygame.event.wait(240)
                        elif "Melbourne" in x_majetek and melbourne.navsteva == 2400:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p19h1,p19h2) and pressed_space == True and "Melbourne" not in x_majetek and "Melbourne" not in y_majetek:
                        if x_money - melbourne.kupni_cena >= 0:
                              x_money -= melbourne.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg19 += 20
                                      x_majetek.append("Melbourne")
                              else:
                                  x_majetek.append("Melbourne")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {melbourne.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg19 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p12w1,p12w2) and b in range(p19h1,p19h2) and melbourne.navsteva != 2400 and pressed_space == True and "Melbourne" in x_majetek and "Melbourne" not in y_majetek:
                        if x_money - melbourne.domecek >= 0:
                              x_money -= melbourne.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              melbourne.navsteva = melbourne.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {melbourne.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p19h1,p19h2)and pressed_space == True and "Melbourne" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p12w1,p12w2) and b in range(p19h1,p19h2) and pressed_space == True and "Melbourne" in y_majetek and "Melbourne" not in x_majetek and melbourne.navsteva != 2400:
                              if x_money - 4800 >= 0:
                                  x_money -= 4800
                                  y_money += 4800
                                  hg19 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg19 += 20
                                          x_majetek.append("Melbourne")
                                          y_majetek.remove("Melbourne")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Melbourne")
                                      y_majetek.remove("Melbourne")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {melbourne.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg19 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p19h1,p19h2) and pressed_space == True and "Melbourne" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {melbourne.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {melbourne.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= melbourne.navsteva
                               y_money += melbourne.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                     


            #pole20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p12w1,p12w2) and b in range(p20h1,p20h2):
                        if "Sydney" in y_majetek and "Sydney" not in x_majetek and sydney.navsteva != 2400:
                           texta = fontmest.render(f"Vlastníkem města {sydney.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Sydney" in y_majetek and "Sydney" not in x_majetek and sydney.navsteva == 2400:
                           texta = fontmest.render(f"Vlastníkem města {sydney.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {sydney.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= sydney.navsteva
                           y_money += sydney.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Sydney" not in x_majetek and "Sydney" not in y_majetek:
                           sydney = mesta("Sydney", 3200, 1050, 1280, 2400, "prozatím nikdo")
                           sydney.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Sydney" in x_majetek and sydney.navsteva != 2400:
                           sydney.upgrade()
                           pygame.event.wait(240)
                        elif "Sydney" in x_majetek and sydney.navsteva == 2400:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p20h1,p20h2) and pressed_space == True and "Sydney" not in x_majetek and "Sydney" not in y_majetek:
                        if x_money - sydney.kupni_cena >= 0:
                              x_money -= sydney.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg20 += 20
                                      x_majetek.append("Sydney")
                              else:
                                  x_majetek.append("Sydney")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {sydney.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg20 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p12w1,p12w2) and b in range(p20h1,p20h2) and sydney.navsteva != 2400 and pressed_space == True and "Sydney" in x_majetek and "Sydney" not in y_majetek:
                        if x_money - sydney.domecek >= 0:
                              x_money -= sydney.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              sydney.navsteva = sydney.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {sydney.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p20h1,p20h2)and pressed_space == True and "Sydney" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p12w1,p12w2) and b in range(p20h1,p20h2) and pressed_space == True and "Sydney" in y_majetek and "Sydney" not in x_majetek and sydney.navsteva != 2400:
                              if x_money - 4800 >= 0:
                                  x_money -= 4800
                                  y_money += 4800
                                  hg20 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg20 += 20
                                          x_majetek.append("Sydney")
                                          y_majetek.remove("Sydney")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Sydney")
                                      y_majetek.remove("Sydney")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {sydney.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg20 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p12w1,p12w2) and b in range(p20h1,p20h2) and pressed_space == True and "Sydney" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {sydney.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {sydney.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= sydney.navsteva
                               y_money += sydney.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                    


            #pole21
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p12w1,p12w2) and b in range(p21h1,p21h2):
                        textlet = fontmest.render(f"Výtejte na letišti", True, (red))
                        textlet1 = fontmest.render(f"Pokud zaplatíte 2500{znacka_meny}, můžete se posunout na jakékoliv políčko", True, (red))
                        textlet2 = fontmest.render(f"Při průchodu startem si nesmíte vybrat peníze!", True, (red))
                        textlet3 = fontmest.render(f"Stiskněte číslo 1 pro platbu letenky", True, (red))
                        surface.blit(textlet, (960,600))
                        surface.blit(textlet1, (960,620))
                        surface.blit(textlet2, (960,640))
                        surface.blit(textlet3, (960,660))
                        pygame.event.wait(240)
                if event.key == pygame.K_KP1 and a in range(p12w1,p12w2) and b in range(p21h1,p21h2)and pressed_space == True:
                              x_money -= 2500
                              textleti = fontmest.render(f"Už můžete vyletět!", True, (red))
                              surface.blit(textleti, (960,600))
                              pygame.event.wait(240)

                        
                        
            #pole22 p22w1 = 116 p22w2 = 164 p22h1 = 0 p22h2 = 100
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p22w1,p22w2) and b in range(p22h1,p22h2):
                        if "San Francisco" in y_majetek and "San Francisco" not in x_majetek and san.navsteva != 2800:
                           texta = fontmest.render(f"Vlastníkem města {san.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "San Francisco" in y_majetek and "San Francisco" not in x_majetek and san.navsteva == 2800:
                           texta = fontmest.render(f"Vlastníkem města {san.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {san.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= san.navsteva
                           y_money += san.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "San Francisco" not in x_majetek and "San Francisco" not in y_majetek:
                           san = mesta("San Francisco", 3800, 1350, 1520, 2800, "prozatím nikdo")
                           san.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "San Francisco" in x_majetek and san.navsteva != 2800:
                           san.upgrade()
                           pygame.event.wait(240)
                        elif "San Francisco" in x_majetek and san.navsteva == 2800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p22w1,p22w2) and b in range(p22h1,p22h2) and pressed_space == True and "San Francisco" not in x_majetek and "San Francisco" not in y_majetek:
                        if x_money - san.kupni_cena >= 0:
                              x_money -= san.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg22 += 20
                                      x_majetek.append("San Francisco")
                              else:
                                  x_majetek.append("San Francisco")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {san.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg22 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                    
                if event.key == pygame.K_KP2 and a in range(p22w1,p22w2) and b in range(p22h1,p22h2) and san.navsteva != 2800 and pressed_space == True and "San Francisco" in x_majetek and "San Francisco" not in y_majetek:
                        if x_money - san.domecek >= 0:
                              x_money -= san.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              san.navsteva = san.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {san.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p22w1,p22w2) and b in range(p22h1,p22h2)and pressed_space == True and "San Francisco" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p22w1,p22w2) and b in range(p22h1,p22h2) and pressed_space == True and "San Francisco" in y_majetek and "San Francisco" not in x_majetek and san.navsteva != 2800:
                              if x_money - 5700 >= 0:
                                  x_money -= 5700
                                  y_money += 5700
                                  hg22 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg22 += 20
                                          x_majetek.append("San Francisco")
                                          y_majetek.remove("San Francisco")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("San Francisco")
                                      y_majetek.remove("San Francisco")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {san.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg22 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p22w1,p22w2) and b in range(p22h1,p22h2) and pressed_space == True and "San Francisco" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {san.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {san.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= san.navsteva
                               y_money += san.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                    
       


            #pole23
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p23w1,p23w2) and b in range(p22h1,p22h2) and lol == 1:
                        if hrac_na_rade == x and lol == 1:
                                rs = random.randint(1,10)
                                if rs == 1:
                                    texts1 = fontfs.render(f"Jděte na nejbližší volné město", True, (red))
                                    surface.blit(texts1, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 2:
                                    texts2 = fontfs.render(f"Jděte na pole s letištěm", True, (red))
                                    surface.blit(texts2, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 3:
                                    texts3 = fontfs.render(f"Jděte do vězení!", True, (red))
                                    surface.blit(texts3, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 4:
                                    texts4 = fontfs.render(f"Jděte na vaše nejbližší město", True, (red))
                                    surface.blit(texts4, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 5:
                                    texts5 = fontfs.render(f"Jděte na nejbližší město vašeho spoluhráče", True, (red))
                                    surface.blit(texts5, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 6:
                                    texts6 = fontfs.render(f"Jděte na start", True, (red))
                                    surface.blit(texts6, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 7:
                                    texts7 = fontfs.render(f"Jděte na pole s letištěm", True, (red))
                                    surface.blit(texts7, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 8:
                                    texts8 = fontfs.render(f"Jděte na emisní povolenku", True, (red))
                                    surface.blit(texts8, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 9:
                                    vpred = random.randint(1,10)
                                    if vpred == 1:
                                        texts91 = fontfs.render(f"Jděte vpřed o {vpred} políčko", True, (red))
                                        surface.blit(texts91, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 2 or vpred == 3 or vpred == 4:
                                        texts92 = fontfs.render(f"Jděte vpřed o {vpred} políčka", True, (red))
                                        surface.blit(texts92, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 5 or vpred == 6 or vpred == 7 or vpred == 8 or vpred == 9 or vpred == 10:
                                        texts93 = fontfs.render(f"Jděte vpřed o {vpred} políček", True, (red))
                                        surface.blit(texts93, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
                                if rs == 10:
                                    dozadu = random.randint(1,10)
                                    if dozadu == 1:
                                        texts101 = fontfs.render(f"Jděte dozadu o {dozadu} políčko", True, (red))
                                        surface.blit(texts101, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 2 or dozadu == 3 or dozadu == 4:
                                        texts102 = fontfs.render(f"Jděte dozadu o {dozadu} políčka", True, (red))
                                        surface.blit(texts102, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 5 or dozadu == 6 or dozadu == 7 or dozadu == 8 or dozadu == 9 or dozadu == 10:
                                        texts103 = fontfs.render(f"Jděte dozadu o {dozadu} políček", True, (red))
                                        surface.blit(texts103, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
            #pole24
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p24w1,p24w2) and b in range(p22h1,p22h2):
                        if "Los Angeles" in y_majetek and "Los Angeles" not in x_majetek and los.navsteva != 3500:
                           texta = fontmest.render(f"Vlastníkem města {los.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Los Angeles" in y_majetek and "Los Angeles" not in x_majetek and los.navsteva == 3500:
                           texta = fontmest.render(f"Vlastníkem města {los.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {los.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= los.navsteva
                           y_money += los.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Los Angeles" not in x_majetek and "Los Angeles" not in y_majetek:
                           los = mesta("Los Angeles", 4400, 1650, 1760, 3500, "prozatím nikdo")
                           los.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Los Angeles" in x_majetek and los.navsteva != 3500:
                           los.upgrade()
                           pygame.event.wait(240)
                        elif "Los Angeles" in x_majetek and los.navsteva == 3500:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p24w1,p24w2) and b in range(p22h1,p22h2) and pressed_space == True and "Los Angeles" not in x_majetek and "Los Angeles" not in y_majetek:
                        if x_money - los.kupni_cena >= 0:
                              x_money -= los.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg24 += 20
                                      x_majetek.append("Los Angeles")
                              else:
                                  x_majetek.append("Los Angeles")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {los.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg24 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p24w1,p24w2) and b in range(p22h1,p22h2) and los.navsteva != 3500 and pressed_space == True and "Los Angeles" in x_majetek and "Los Angeles" not in y_majetek:
                        if x_money - los.domecek >= 0:
                              x_money -= los.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              los.navsteva = los.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {los.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p24w1,p24w2) and b in range(p22h1,p22h2)and pressed_space == True and "Los Angeles" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p24w1,p24w2) and b in range(p22h1,p22h2) and pressed_space == True and "Los Angeles" in y_majetek and "Los Angeles" not in x_majetek and los.navsteva != 3500:
                              if x_money - 6600 >= 0:
                                  x_money -= 6600
                                  y_money += 6600
                                  hg24 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg24 += 20
                                          x_majetek.append("Los Angeles")
                                          y_majetek.remove("Los Angeles")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Los Angeles")
                                      y_majetek.remove("Los Angeles")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {los.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg24 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p24w1,p24w2) and b in range(p22h1,p22h2) and pressed_space == True and "Los Angeles" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {los.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {los.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= los.navsteva
                               y_money += los.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)            


            #pole25
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p25w1,p25w2) and b in range(p22h1,p22h2):
                        if "New York" in y_majetek and "New York" not in x_majetek and new.navsteva != 3500:
                           texta = fontmest.render(f"Vlastníkem města {new.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "New York" in y_majetek and "New York" not in x_majetek and new.navsteva == 3500:
                           texta = fontmest.render(f"Vlastníkem města {new.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {new.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= new.navsteva
                           y_money += new.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "New York" not in x_majetek and "New York" not in y_majetek:
                           new = mesta("New York", 4400, 1650, 1760, 3500, "prozatím nikdo")
                           new.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "New York" in x_majetek and new.navsteva != 3500:
                           new.upgrade()
                           pygame.event.wait(240)
                        elif "New York" in x_majetek and new.navsteva == 3500:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p25w1,p25w2) and b in range(p22h1,p22h2) and pressed_space == True and "New York" not in x_majetek and "New York" not in y_majetek:
                        if x_money - new.kupni_cena >= 0:
                              x_money -= new.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg25 += 20
                                      x_majetek.append("New York")
                              else:
                                  x_majetek.append("New York")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {new.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg25 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p25w1,p25w2) and b in range(p22h1,p22h2) and new.navsteva != 3500 and pressed_space == True and "New York" in x_majetek and "New York" not in y_majetek:
                        if x_money - new.domecek >= 0:
                              x_money -= new.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              new.navsteva = new.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {new.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p25w1,p25w2) and b in range(p22h1,p22h2)and pressed_space == True and "New York" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p25w1,p25w2) and b in range(p22h1,p22h2) and pressed_space == True and "New York" in y_majetek and "New York" not in x_majetek and new.navsteva != 3500:
                              if x_money - 6600 >= 0:
                                  x_money -= 6600
                                  y_money += 6600
                                  hg25 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg25 += 20
                                          x_majetek.append("New York")
                                          y_majetek.remove("New York")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("New York")
                                      y_majetek.remove("New York")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {new.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg25 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p25w1,p25w2) and b in range(p22h1,p22h2) and pressed_space == True and "New York" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {new.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {new.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= new.navsteva
                               y_money += new.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                    


            #pole26
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p26w1,p26w2) and b in range(p22h1,p22h2):
                        if "Hawaii" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek and "Srí Lanka" not in y_majetek:
                            texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 2.", True, (red))
                            surface.blit(texta, (960,600))
                            textb = fontmest.render(f"Musíte zaplatit {hawaii.navsteva} {znacka_meny} za návštěvu města", True, (red))
                            surface.blit(textb, (960,620))
                            x_money -= hawaii.navsteva
                            y_money += hawaii.navsteva
                            textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                            surface.blit(textmoneyx, (960,660))
                            textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                            surface.blit(textmoneyy, (960,640))
                            pygame.event.wait(240)  
                        if "Hawaii" in y_majetek and "Bali" in y_majetek and "Maledivy" not in y_majetek and "Srí Lanka" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Hawaii" in y_majetek and "Maledivy" in y_majetek and "Bali" not in y_majetek and "Srí Lanka" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Hawaii" in y_majetek and "Srí Lanka" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)                               
                        if "Hawaii" in y_majetek and "Bali" in y_majetek and "Maledivy" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)     
                             
                        if "Hawaii" in y_majetek and "Bali" in y_majetek and "Srí Lanka" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Hawaii" in y_majetek and "Maledivy" in y_majetek and "Srí Lanka" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)     
                        if "Hawaii" not in x_majetek and "Hawaii" not in y_majetek:
                           hawaii = mesta("Hawaii", 4000, 1000, 0, 0, "prozatím nikdo")
                           hawaii.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        if "Hawaii" in x_majetek:
                           textmas = fontmest.render("Jste vlastníkem tohoto města", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                        #if "Hawaii" in x_majetek and "Srí Lanka" in x_majetek and "Bali" in x_majetek and "Maledivy" in x_majetek:
                            #textvyhra = fontmest.render("Vyhrál jste hru!", True, (red))
                            #surface.blit(textvyhra, (960,600))
                            #pygame.event.wait(240)

                if event.key == pygame.K_KP1 and a in range(p26w1,p26w2) and b in range(p22h1,p22h2) and pressed_space == True and "Hawaii" not in x_majetek and "Hawaii" not in y_majetek:
                        if x_money - hawaii.kupni_cena >= 0:
                              x_money -= hawaii.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg26 += 20
                                      x_majetek.append("Hawaii")
                              else:
                                  x_majetek.append("Hawaii")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {hawaii.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                
                if event.key == pygame.K_KP0 and a in range(p26w1,p26w2) and b in range(p22h1,p22h2) and pressed_space == True:
                              hrac_na_rade = y
                              pressed_space = False
                              
            #pole27
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p27w1,p27w2) and b in range(p22h1,p22h2):
                        if "Bangkok" in y_majetek and "Bangkok" not in x_majetek and bangkok.navsteva != 3800:
                           texta = fontmest.render(f"Vlastníkem města {bangkok.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Bangkok" in y_majetek and "Bangkok" not in x_majetek and bangkok.navsteva == 3800:
                           texta = fontmest.render(f"Vlastníkem města {bangkok.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {bangkok.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= bangkok.navsteva
                           y_money += bangkok.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Bangkok" not in x_majetek and "Bangkok" not in y_majetek:
                           bangkok = mesta("Bangkok", 5000, 2000, 2000, 3800, "prozatím nikdo")
                           bangkok.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Bangkok" in x_majetek and bangkok.navsteva != 3800:
                           bangkok.upgrade()
                           pygame.event.wait(240)
                        elif "Bangkok" in x_majetek and bangkok.navsteva == 3800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p27w1,p27w2) and b in range(p22h1,p22h2) and pressed_space == True and "Bangkok" not in x_majetek and "Bangkok" not in y_majetek:
                        if x_money - bangkok.kupni_cena >= 0:
                              x_money -= bangkok.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg27 += 20
                                      x_majetek.append("Bangkok")
                              else:
                                  x_majetek.append("Bangkok")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {bangkok.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg27 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240) 
                if event.key == pygame.K_KP2 and a in range(p27w1,p27w2) and b in range(p22h1,p22h2) and bangkok.navsteva != 3800 and pressed_space == True and "Bangkok" in x_majetek and "Bangkok" not in y_majetek:
                        if x_money - bangkok.domecek >= 0:
                              x_money -= bangkok.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              bangkok.navsteva = bangkok.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {bangkok.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)       
                if event.key == pygame.K_KP0 and a in range(p27w1,p27w2) and b in range(p22h1,p22h2)and pressed_space == True and "Bangkok" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p27w1,p27w2) and b in range(p22h1,p22h2) and pressed_space == True and "Bangkok" in y_majetek and "Bangkok" not in x_majetek and bangkok.navsteva != 3800:
                              if x_money - 7500 >= 0:
                                  x_money -= 7500
                                  y_money += 7500
                                  hg27 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg27 += 20
                                          x_majetek.append("Bangkok")
                                          y_majetek.remove("Bangkok")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Bangkok")
                                      y_majetek.remove("Bangkok")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {bangkok.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg27 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p27w1,p27w2) and b in range(p22h1,p22h2) and pressed_space == True and "Bangkok" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {bangkok.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {bangkok.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= bangkok.navsteva
                               y_money += bangkok.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                    
       


            #pole28
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p28w1,p28w2) and b in range(p22h1,p22h2):
                        if "Šanghaj" in y_majetek and "Šanghaj" not in x_majetek and šanghaj.navsteva != 3800:
                           texta = fontmest.render(f"Vlastníkem města {šanghaj.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Šanghaj" in y_majetek and "Šanghaj" not in x_majetek and šanghaj.navsteva == 3800:
                           texta = fontmest.render(f"Vlastníkem města {šanghaj.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {šanghaj.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= šanghaj.navsteva
                           y_money += šanghaj.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Šanghaj" not in x_majetek and "Šanghaj" not in y_majetek:
                           šanghaj = mesta("Šanghaj", 5000, 2000, 2000, 3800, "prozatím nikdo")
                           šanghaj.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Šanghaj" in x_majetek and šanghaj.navsteva != 3800:
                           šanghaj.upgrade()
                           pygame.event.wait(240)
                        elif "Šanghaj" in x_majetek and šanghaj.navsteva == 3800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p28w1,p28w2) and b in range(p22h1,p22h2) and pressed_space == True and "Šanghaj" not in x_majetek and "Šanghaj" not in y_majetek:
                        if x_money - šanghaj.kupni_cena >= 0:
                              x_money -= šanghaj.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg28 += 20
                                      x_majetek.append("Šanghaj")
                              else:
                                  x_majetek.append("Šanghaj")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {šanghaj.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg28 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240) 
                if event.key == pygame.K_KP2 and a in range(p28w1,p28w2) and b in range(p22h1,p22h2) and šanghaj.navsteva != 3800 and pressed_space == True and "Šanghaj" in x_majetek and "Šanghaj" not in y_majetek:
                        if x_money - šanghaj.domecek >= 0:
                              x_money -= šanghaj.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              šanghaj.navsteva = šanghaj.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {šanghaj.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)       
                if event.key == pygame.K_KP0 and a in range(p28w1,p28w2) and b in range(p22h1,p22h2)and pressed_space == True and "Šanghaj" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p28w1,p28w2) and b in range(p22h1,p22h2) and pressed_space == True and "Šanghaj" in y_majetek and "Šanghaj" not in x_majetek and šanghaj.navsteva != 3800:
                              if x_money - 7500 >= 0:
                                  x_money -= 7500
                                  y_money += 7500
                                  hg28 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg28 += 20
                                          x_majetek.append("Šanghaj")
                                          y_majetek.remove("Šanghaj")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Šanghaj")
                                      y_majetek.remove("Šanghaj")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {šanghaj.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg28 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p28w1,p28w2) and b in range(p22h1,p22h2) and pressed_space == True and "Šanghaj" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {šanghaj.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {šanghaj.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= šanghaj.navsteva
                               y_money += šanghaj.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                    
               


            #pole29
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p29w1,p29w2) and b in range(p22h1,p22h2):
                        textemise = fontmest.render(f"Za každé město, které vlastníte, musíte zaplatit 500{znacka_meny}", True, (red))
                        surface.blit(textemise, (960,600))
                        delkaxmajetek = len(x_majetek)
                        cenadelky = delkaxmajetek*500
                        x_money -= cenadelky
                        textemise1 = fontmest.render(f"Musíte zaplatit {cenadelky}{znacka_meny}", True, (red))
                        surface.blit(textemise1, (960,620))
                        pygame.event.wait(240)
            #pole30
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p30w1,p30w2) and b in range(p22h1,p22h2):
                        if "Tokio" in y_majetek and "Tokio" not in x_majetek and tokio.navsteva != 4500:
                           texta = fontmest.render(f"Vlastníkem města {tokio.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Tokio" in y_majetek and "Tokio" not in x_majetek and tokio.navsteva == 4500:
                           texta = fontmest.render(f"Vlastníkem města {tokio.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {tokio.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= tokio.navsteva
                           y_money += tokio.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Tokio" not in x_majetek and "Tokio" not in y_majetek:
                           tokio = mesta("Tokio", 5700, 2350, 2280, 4500, "prozatím nikdo")
                           tokio.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Tokio" in x_majetek and tokio.navsteva != 4500:
                           tokio.upgrade()
                           pygame.event.wait(240)
                        elif "Tokio" in x_majetek and tokio.navsteva == 4500:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p30w1,p30w2) and b in range(p22h1,p22h2) and pressed_space == True and "Tokio" not in x_majetek and "Tokio" not in y_majetek:
                        if x_money - tokio.kupni_cena >= 0:
                              x_money -= tokio.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg30 += 20
                                      x_majetek.append("Tokio")
                              else:
                                  x_majetek.append("Tokio")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {tokio.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg30 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p30w1,p30w2) and b in range(p22h1,p22h2) and tokio.navsteva != 4500 and pressed_space == True and "Tokio" in x_majetek and "Tokio" not in y_majetek:
                        if x_money - tokio.domecek >= 0:
                              x_money -= tokio.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              tokio.navsteva = tokio.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {tokio.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p30w1,p30w2) and b in range(p22h1,p22h2)and pressed_space == True and "Tokio" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p30w1,p30w2) and b in range(p22h1,p22h2) and pressed_space == True and "Tokio" in y_majetek and "Tokio" not in x_majetek and tokio.navsteva != 4500:
                              if x_money - 8550 >= 0:
                                  x_money -= 8550
                                  y_money += 8550
                                  hg30 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg30 += 20
                                          x_majetek.append("Tokio")
                                          y_majetek.remove("Tokio")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Tokio")
                                      y_majetek.remove("Tokio")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {tokio.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg30 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p30w1,p30w2) and b in range(p22h1,p22h2) and pressed_space == True and "Tokio" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {tokio.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {tokio.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= tokio.navsteva
                               y_money += tokio.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                    
               
       


            #pole31
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p31w1,p31w2) and b in range(p22h1,p22h2):
                        textvez = fontmest.render(f"Posuňtě se na políčko vězení!", True, (red))
                        surface.blit(textvez, (960,600))
                        pygame.event.wait(240)
                        
            #pole32 p32w1 = 820 p32w1 = 950 p32h1 = 116 p32h2 = 164
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p32w1,p32w2) and b in range(p32h1,p32h2):
                        if "Praha" in y_majetek and "Praha" not in x_majetek and praha.navsteva != 5100:
                           texta = fontmest.render(f"Vlastníkem města {praha.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Praha" in y_majetek and "Praha" not in x_majetek and praha.navsteva == 5100:
                           texta = fontmest.render(f"Vlastníkem města {praha.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {praha.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= praha.navsteva
                           y_money += praha.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Praha" not in x_majetek and "Praha" not in y_majetek:
                           praha = mesta("Praha", 6800, 3000, 2720, 5100, "prozatím nikdo")
                           praha.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Praha" in x_majetek and praha.navsteva != 5100:
                           praha.upgrade()
                           pygame.event.wait(240)
                        elif "Praha" in x_majetek and praha.navsteva == 5100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p32w1,p32w2) and b in range(p32h1,p32h2) and pressed_space == True and "Praha" not in x_majetek and "Praha" not in y_majetek:
                        if x_money - praha.kupni_cena >= 0:
                              x_money -= praha.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg32 += 20
                                      x_majetek.append("Praha")
                              else:
                                  x_majetek.append("Praha")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {praha.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg32 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and a in range(p32w1,p32w2) and b in range(p32h1,p32h2) and praha.navsteva != 5100 and pressed_space == True and "Praha" in x_majetek and "Praha" not in y_majetek:
                        if x_money - praha.domecek >= 0:
                              x_money -= praha.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              praha.navsteva = praha.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {praha.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p32h1,p32h2)and pressed_space == True and "Praha" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p32w1,p32w2) and b in range(p32h1,p32h2) and pressed_space == True and "Praha" in y_majetek and "Praha" not in x_majetek and praha.navsteva != 5100:
                              if x_money - 10200 >= 0:
                                  x_money -= 10200
                                  y_money += 10200
                                  hg32 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg32 += 20
                                          x_majetek.append("Praha")
                                          y_majetek.remove("Praha")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Praha")
                                      y_majetek.remove("Praha")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {praha.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg32 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p32h1,p32h2) and pressed_space == True and "Praha" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {praha.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {praha.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= praha.navsteva
                               y_money += praha.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                    
               


            #pole33
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p32w1,p32w2) and b in range(p33h1,p33h2):
                        if "Londýn" in y_majetek and "Londýn" not in x_majetek and londyn.navsteva != 5100:
                           texta = fontmest.render(f"Vlastníkem města {londyn.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Londýn" in y_majetek and "Londýn" not in x_majetek and londyn.navsteva == 5100:
                           texta = fontmest.render(f"Vlastníkem města {londyn.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {londyn.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= londyn.navsteva
                           y_money += londyn.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Londýn" not in x_majetek and "Londýn" not in y_majetek:
                           londyn = mesta("Londýn", 6800, 3000, 2720, 5100, "prozatím nikdo")
                           londyn.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Londýn" in x_majetek and londyn.navsteva != 5100:
                           londyn.upgrade()
                           pygame.event.wait(240)
                        elif "Londýn" in x_majetek and londyn.navsteva == 5100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p32w1,p32w2) and b in range(p33h1,p33h2) and pressed_space == True and "Londýn" not in x_majetek and "Londýn" not in y_majetek:
                        if x_money - londyn.kupni_cena >= 0:
                              x_money -= londyn.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg33 += 20
                                      x_majetek.append("Londýn")
                              else: 
                                  x_majetek.append("Londýn")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {londyn.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg33 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)    
                if event.key == pygame.K_KP2 and a in range(p32w1,p32w2) and b in range(p33h1,p33h2) and londyn.navsteva != 5100 and pressed_space == True and "Londýn" in x_majetek and "Londýn" not in y_majetek:
                        if x_money - londyn.domecek >= 0:
                              x_money -= londyn.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              londyn.navsteva = londyn.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {londyn.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)          
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p33h1,p33h2)and pressed_space == True and "Londýn" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p32w1,p32w2) and b in range(p33h1,p33h2) and pressed_space == True and "Londýn" in y_majetek and "Londýn" not in x_majetek and londyn.navsteva != 5100:
                              if x_money - 10200 >= 0:
                                  x_money -= 10200
                                  y_money += 10200
                                  hg33 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg33 += 20
                                          x_majetek.append("Londýn")
                                          y_majetek.remove("Londýn")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Londýn")
                                      y_majetek.remove("Londýn")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {londyn.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg33 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p33h1,p33h2) and pressed_space == True and "Londýn" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {londyn.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {londyn.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= londyn.navsteva
                               y_money += londyn.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                    
                     

            

            #pole34
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if a in range(p32w1,p32w2) and b in range(p34h1,p34h2)and lol == 1:
                        if hrac_na_rade == x and lol == 1:
                            rf = random.randint(1,8)
                            if rf == 1:
                                x_money += 3500
                                textf1 = fontfs.render(f"Omylem vám přišlo na účet 3500{znacka_meny}", True, (red))
                                surface.blit(textf1, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 2:
                                x_money += 3000
                                y_money -= 3000
                                textf2 = fontfs.render(f"Spoluhráč ti musí dát 3000{znacka_meny}", True, (red))
                                surface.blit(textf2, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 3:
                                x_money += 1500
                                textf3 = fontfs.render(f"Ve tvém městě probíhal festival.", True, (red))
                                textf31 = fontfs.render(f"Vydělal jsi 1500 {znacka_meny}", True, (red))
                                surface.blit(textf3, (960,600))
                                surface.blit(textf31, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 4:
                                textf4 = fontfs.render(f"Je léto a všichni chtějí k moři.", True, (red))
                                textf41 = fontfs.render(f"Za každý svůj rezort získáváš 1000{znacka_meny}", True, (red))
                                surface.blit(textf4, (960,600))
                                surface.blit(textf41, (960,620))
                                if "Maledivy" not in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    textf42 = fontfs.render(f"Nevlastníte žádný rezort.", True, (red))
                                    surface.blit(textf42, (960,640))
                                if "Maledivy" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek: 
                                    x_money += 1000
                                if "Bali" in x_majetek and "Maledivy" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 1000
                                if "Hawaii" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 1000
                                if "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 1000
                                if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" not in x_majetek and "Bali" not in x_majetek:
                                    x_money += 2000
                                if "Bali" and "Hawaii" in x_majetek and "Maledivy" not in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 2000
                                if "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 2000
                                if "Hawaii" in x_majetek and "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 2000
                                if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" in x_majetek and "Srí Lanka" not in x_majetek:
                                    x_money += 3000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Bali" in x_majetek and "Hawaii" not in x_majetek:
                                    x_money += 3000
                                if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek:
                                    x_money += 3000
                                if "Hawaii" in x_majetek and "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Maledivy" not in x_majetek:
                                    x_money += 3000
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 5:
                                x_money += 5000
                                textf5 = fontfs.render(f"Tvé město se ocitlo v top 10 nejhezčích měst.", True, (red))
                                textf51 = fontfs.render(f"Všichni ho nyní navštěvují... vydělalo vám to 5000{znacka_meny}", True, (red))
                                surface.blit(textf5, (960,600))
                                surface.blit(textf51, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 6:
                                x_money -= 1000
                                textf6 = fontfs.render(f"Ve vašem městě vypadla elektřina.", True, (red))
                                textf61 = fontfs.render (f"Zaplatite 1000{znacka_meny} za opravu elektrarny", True, (red))
                                surface.blit(textf6, (960,600))
                                surface.blit(textf61, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 7:
                                x_money -= 3000
                                textf7 = fontfs.render(f"Proběhlo zemětřesení, za opravy zaplatíš 3000{znacka_meny}", True, (red))
                                surface.blit(textf7, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 8:
                                x_money -= 3500
                                textf8 = fontfs.render(f"V jednom z vašich měst se rozšířila epidemie.", True, (red))
                                textf81 = fontfs.render(f"Pošlete 3500{znacka_meny} na pomoc lidem", True, (red))
                                surface.blit(textf8, (960,600))
                                surface.blit(textf81, (960,620))
                                pygame.event.wait(240)
                                lol = 0
            #pole35
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p32w1,p32w2) and b in range(p35h1,p35h2):
                        if "Paříž" in y_majetek and "Paříž" not in x_majetek and pariz.navsteva != 5800:
                           texta = fontmest.render(f"Vlastníkem města {pariz.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Paříž" in y_majetek and "Paříž" not in x_majetek and pariz.navsteva == 5800:
                           texta = fontmest.render(f"Vlastníkem města {pariz.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {pariz.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= pariz.navsteva
                           y_money += pariz.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Paříž" not in x_majetek and "Paříž" not in y_majetek:
                           pariz = mesta("Paříž", 7500, 3400, 3000, 5800, "prozatím nikdo")
                           pariz.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Paříž" in x_majetek and pariz.navsteva != 5800:
                           pariz.upgrade()
                           pygame.event.wait(240)
                        elif "Paříž" in x_majetek and pariz.navsteva == 5800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p32w1,p32w2) and b in range(p35h1,p35h2) and pressed_space == True and "Paříž" not in x_majetek and "Paříž" not in y_majetek:
                        if x_money - pariz.kupni_cena >= 0:
                              x_money -= pariz.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg35 += 20
                                      x_majetek.append("Paříž")
                              else: 
                                  x_majetek.append("Paříž")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {pariz.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg35 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)  
                if event.key == pygame.K_KP2 and a in range(p32w1,p32w2) and b in range(p35h1,p35h2) and pariz.navsteva != 5800 and pressed_space == True and "Paříž" in x_majetek and "Paříž" not in y_majetek:
                        if x_money - pariz.domecek >= 0:
                              x_money -= pariz.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              pariz.navsteva = pariz.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {pariz.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)        
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p35h1,p35h2)and pressed_space == True and "Paříž" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p32w1,p32w2) and b in range(p35h1,p35h2) and pressed_space == True and "Paříž" in y_majetek and "Paříž" not in x_majetek and pariz.navsteva != 5800:
                              if x_money - 11250 >= 0:
                                  x_money -= 11250
                                  y_money += 11250
                                  hg35 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg35 += 20
                                          x_majetek.append("Paříž")
                                          y_majetek.remove("Paříž")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Paříž")
                                      y_majetek.remove("Paříž")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {pariz.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg35 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p35h1,p35h2) and pressed_space == True and "Paříž" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {pariz.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {pariz.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= pariz.navsteva
                               y_money += pariz.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                           

            

            #pole36
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p32w1,p32w2) and b in range(p36h1,p36h2):
                        if "Srí Lanka" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek and "Hawaii" not in y_majetek:
                            texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 2.", True, (red))
                            surface.blit(texta, (960,600))
                            textb = fontmest.render(f"Musíte zaplatit {sri.navsteva} {znacka_meny} za návštěvu města", True, (red))
                            surface.blit(textb, (960,620))
                            x_money -= sri.navsteva
                            y_money += sri.navsteva
                            textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                            surface.blit(textmoneyx, (960,660))
                            textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                            surface.blit(textmoneyy, (960,640))
                            pygame.event.wait(240)  
                        if "Srí Lanka" in y_majetek and "Bali" in y_majetek and "Maledivy" not in y_majetek and "Hawaii" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Srí Lanka" in y_majetek and "Maledivy" in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Srí Lanka" in y_majetek and "Hawaii" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 2000
                                y_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)                               
                        if "Srí Lanka" in y_majetek and "Bali" in y_majetek and "Maledivy" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)     
                             
                        if "Srí Lanka" in y_majetek and "Bali" in y_majetek and "Hawaii" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Srí Lanka" in y_majetek and "Maledivy" in y_majetek and "Hawaii" in y_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 2.", True, (red))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (red))
                                surface.blit(textb, (960,620))
                                x_money -= 3000
                                y_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyx, (960,660))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                surface.blit(textmoneyy, (960,640))
                                pygame.event.wait(240)
                        if "Srí Lanka" not in x_majetek and "Srí Lanka" not in y_majetek:
                           sri = mesta("Srí Lanka", 4000, 1000, 0, 0, "prozatím nikdo")
                           sri.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        if "Srí Lanka" in x_majetek:
                           textmas = fontmest.render("Jste vlastníkem tohoto města", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                        #if "Srí Lanka" in x_majetek and "Hawaii" in x_majetek and "Bali" in x_majetek and "Maledivy" in x_majetek:
                            #textvyhra = fontmest.render("Vyhrál jste hru!", True, (red))
                            #surface.blit(textvyhra, (960,600))
                            #pygame.event.wait(240)

                if event.key == pygame.K_KP1 and a in range(p32w1,p32w2) and b in range(p36h1,p36h2) and pressed_space == True and "Srí Lanka" not in x_majetek and "Srí Lanka" not in y_majetek:
                        if x_money - sri.kupni_cena >= 0:
                              x_money -= sri.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg36 += 20
                                      x_majetek.append("Srí Lanka")
                              else:
                                  x_majetek.append("Srí Lanka")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {sri.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p36h1,p36h2)and pressed_space == True:
                              hrac_na_rade = y
                              pressed_space = False
            #pole37
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p32w1,p32w2) and b in range(p37h1,p37h2) and lol == 1:
                        if hrac_na_rade == x and lol == 1:
                                rs = random.randint(1,10)
                                if rs == 1:
                                    texts1 = fontfs.render(f"Jděte na nejbližší volné město", True, (red))
                                    surface.blit(texts1, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 2:
                                    texts2 = fontfs.render(f"Jděte na pole s letištěm", True, (red))
                                    surface.blit(texts2, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 3:
                                    texts3 = fontfs.render(f"Jděte do vězení!", True, (red))
                                    surface.blit(texts3, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 4:
                                    texts4 = fontfs.render(f"Jděte na vaše nejbližší město", True, (red))
                                    surface.blit(texts4, (960,600))
                                    pygame.event.wait(240)
                                if rs == 5:
                                    texts5 = fontfs.render(f"Jděte na nejbližší město vašeho spoluhráče", True, (red))
                                    surface.blit(texts5, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 6:
                                    texts6 = fontfs.render(f"Jděte na start", True, (red))
                                    surface.blit(texts6, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 7:
                                    texts7 = fontfs.render(f"Jděte na pole s letištěm", True, (red))
                                    surface.blit(texts7, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 8:
                                    texts8 = fontfs.render(f"Jděte na emisní povolenku", True, (red))
                                    surface.blit(texts8, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 9:
                                    vpred = random.randint(1,10)
                                    if vpred == 1:
                                        texts91 = fontfs.render(f"Jděte vpřed o {vpred} políčko", True, (red))
                                        surface.blit(texts91, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 2 or vpred == 3 or vpred == 4:
                                        texts92 = fontfs.render(f"Jděte vpřed o {vpred} políčka", True, (red))
                                        surface.blit(texts92, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 5 or vpred == 6 or vpred == 7 or vpred == 8 or vpred == 9 or vpred == 10:
                                        texts93 = fontfs.render(f"Jděte vpřed o {vpred} políček", True, (red))
                                        surface.blit(texts93, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
                                if rs == 10:
                                    dozadu = random.randint(1,10)
                                    if dozadu == 1:
                                        texts101 = fontfs.render(f"Jděte dozadu o {dozadu} políčko", True, (red))
                                        surface.blit(texts101, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 2 or dozadu == 3 or dozadu == 4:
                                        texts102 = fontfs.render(f"Jděte dozadu o {dozadu} políčka", True, (red))
                                        surface.blit(texts102, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 5 or dozadu == 6 or dozadu == 7 or dozadu == 8 or dozadu == 9 or dozadu == 10:
                                        texts103 = fontfs.render(f"Jděte dozadu o {dozadu} políček", True, (red))
                                        surface.blit(texts103, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0

            #pole38
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p32w1,p32w2) and b in range(p38h1,p38h2):
                        if "Dubai" in y_majetek and "Dubai" not in x_majetek and dubai.navsteva != 6800:
                           texta = fontmest.render(f"Vlastníkem města {dubai.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Dubai" in y_majetek and "Dubai" not in x_majetek and dubai.navsteva == 6800:
                           texta = fontmest.render(f"Vlastníkem města {dubai.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {dubai.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= dubai.navsteva
                           y_money += dubai.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Dubai" not in x_majetek and "Dubai" not in y_majetek:
                           dubai = mesta("Dubai", 9000, 4500, 3600, 6800, "prozatím nikdo")
                           dubai.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Dubai" in x_majetek and dubai.navsteva != 6800:
                           dubai.upgrade()
                           pygame.event.wait(240)
                        elif "Dubai" in x_majetek and dubai.navsteva == 6800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p32w1,p32w2) and b in range(p38h1,p38h2) and pressed_space == True and "Dubai" not in x_majetek and "Dubai" not in y_majetek:
                        if x_money - dubai.kupni_cena >= 0:
                              x_money -= dubai.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg38 += 20
                                      x_majetek.append("Dubai")
                              else: 
                                  x_majetek.append("Dubai")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {dubai.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg38 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)  
                if event.key == pygame.K_KP2 and a in range(p32w1,p32w2) and b in range(p38h1,p38h2) and dubai.navsteva != 6800 and pressed_space == True and "Dubai" in x_majetek and "Dubai" not in y_majetek:
                        if x_money - dubai.domecek >= 0:
                              x_money -= dubai.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              dubai.navsteva = dubai.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {dubai.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)        
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p38h1,p38h2)and pressed_space == True and "Dubai" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p32w1,p32w2) and b in range(p38h1,p38h2) and pressed_space == True and "Dubai" in y_majetek and "Dubai" not in x_majetek and dubai.navsteva != 6800:
                              if x_money - 13500 >= 0:
                                  x_money -= 13500
                                  y_money += 13500
                                  hg38 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg38 += 20
                                          x_majetek.append("Dubai")
                                          y_majetek.remove("Dubai")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Dubai")
                                      y_majetek.remove("Dubai")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {dubai.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg38 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p38h1,p38h2) and pressed_space == True and "Dubai" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {dubai.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {dubai.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= dubai.navsteva
                               y_money += dubai.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                           
       

            #pole39
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True

                    if a in range(p32w1,p32w2) and b in range(p39h1,p39h2):
                        if "Ambasáda" not in x_majetek and "Ambasáda" not in y_majetek:
                            textcelnice = fontmest.render(f"Název města: Ambasáda", True, (red))
                            surface.blit(textcelnice, (960,600))
                            textkcelnice1 = fontmest.render(f"Kupní cena: 2100{znacka_meny}", True, (red))
                            surface.blit(textkcelnice1, (960,620))
                            textkcelnice2 = fontmest.render(f"Cena za návštěvu tohoto města: 200x hod kostkou", True, (red))
                            surface.blit(textkcelnice2, (960,640))
                            surface.blit(napis, (960,680))
                            surface.blit(napis2, (960,700))
                            pygame.event.wait(240)
                    
                        if "Ambasáda" in y_majetek:
                           textcelnice3 = fontmest.render(f"Vlastníkem Ambasáda je Hráč 2.", True, (red))
                           #textb = fontmest.render(f"Musíte zaplatit {kodan.navsteva}{znacka_meny} za návštěvu města", True, (red))
                           surface.blit(textcelnice3, (960,600))
                           #surface.blit(textb, (960, 620))
                           textca = fontmest.render(f"Hoďte ještě jednou kostkou!", True, (red))
                           surface.blit(textca, (960,620))
                           x_money2 = copy.copy(x_money)
                           pygame.event.wait(240)
                           
                if event.key == pygame.K_KP1 and a in range(p32w1,p32w2) and b in range(p39h1,p39h2) and pressed_space == True and "Ambasáda" not in x_majetek and "Ambasáda" not in y_majetek:
                        if x_money - 2100 >= 0:
                              x_money -= 2100
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg39 += 20
                                      x_majetek.append("Ambasáda")
                              else:
                                  x_majetek.append("Ambasáda")
                              #zapsání do majetku
                              #x_majetek.append("Kodaň")
                              textmajetekx = fontmest.render(f"Koupil jste si Ambasáda", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                            
            if a in range(p32w1,p32w2) and b in range(p39h1,p39h2) and pressed_space == True and "Ambasáda" in y_majetek and "Ambasáda" not in x_majetek and "Celnice" not in y_majetek:
                #if event.type == pygame.KEYDOWN:
                    if u == 1:
                        cacena = 1*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                    
                    if u == 2:
                        cacena = 2*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
              
                    if u == 3:
                        cacena = 3*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 4:
                        cacena = 4*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 5:
                        cacena = 5*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                            
                        
                    if u == 6:
                        cacena = 6*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                    
                    

                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                        pressed_space = False
                        smth = 0
                        
            if a in range(p32w1,p32w2) and b in range(p39h1,p39h2) and pressed_space == True and "Ambasáda" in y_majetek and "Ambasáda" not in x_majetek and "Celnice" in y_majetek:
                #if event.type == pygame.KEYDOWN:
                    if u == 1:
                        cacena = 1*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                    
                    if u == 2:
                        cacena = 2*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
              
                    if u == 3:
                        cacena = 3*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 4:
                        cacena = 4*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 5:
                        cacena = 5*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                            
                        
                    if u == 6:
                        cacena = 6*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            x_money -= cacena
                            y_money += cacena
                            u = 0
                            smth = 1
                    
                    

                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                        pressed_space = False
                        smth = 0
                        
            if a in range(p32w1,p32w2) and b in range(p39h1,p39h2) and pressed_space == True and smth == 1:
                roz = x_money2 - x_money
                textca = fontmest.render(f"Musíte zaplatit {roz}{znacka_meny}", True, (red))
                surface.blit(textca, (960,600))
                pygame.event.wait(240)
                    
                if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                    smth = 0
            #pole40
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if a in range(p32w1,p32w2) and b in range(p40h1,p40h2):
                        if "Las Vegas" in y_majetek and "Las Vegas" not in x_majetek and las.navsteva != 7800:
                           texta = fontmest.render(f"Vlastníkem města {las.jmeno} je Hráč 2.", True, (red))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (red))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (red))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Las Vegas" in y_majetek and "Las Vegas" not in x_majetek and las.navsteva == 7800:
                           texta = fontmest.render(f"Vlastníkem města {las.jmeno} je Hráč 2 a vlastní zde i průvodce.", True, (red))
                           textb = fontmest.render(f"Musíte zaplatit {las.navsteva} {znacka_meny} za návštěvu města", True, (red))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           x_money -= las.navsteva
                           y_money += las.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Las Vegas" not in x_majetek and "Las Vegas" not in y_majetek:
                           las = mesta("Las Vegas", 10000, 5200, 4000, 7800, "prozatím nikdo")
                           las.karticky()
                           surface.blit(napis, (960,730))
                           surface.blit(napis2, (960,750))
                           pygame.event.wait(240)
                        elif "Las Vegas" in x_majetek and las.navsteva != 7800:
                           las.upgrade()
                           pygame.event.wait(240)
                        elif "Las Vegas" in x_majetek and las.navsteva == 7800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (red))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and a in range(p32w1,p32w2) and b in range(p40h1,p40h2) and pressed_space == True and "Las Vegas" not in x_majetek and "Las Vegas" not in y_majetek:
                        if x_money - las.kupni_cena >= 0:
                              x_money -= las.kupni_cena
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(x_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg40 += 20
                                      x_majetek.append("Las Vegas")
                              else: 
                                  x_majetek.append("Las Vegas")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {las.jmeno}", True, (red))
                              surface.blit(textmajetekx, (960,600))
                              #hg40 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)  
                if event.key == pygame.K_KP2 and a in range(p32w1,p32w2) and b in range(p40h1,p40h2) and las.navsteva != 7800 and pressed_space == True and "Las Vegas" in x_majetek and "Las Vegas" not in y_majetek:
                        if x_money - las.domecek >= 0:
                              x_money -= las.domecek
                              textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                              surface.blit(textmoneyx, (960,600))
                              las.navsteva = las.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {las.navsteva}{znacka_meny}", True, (red))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)        
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p40h1,p40h2)and pressed_space == True and "Las Vegas" not in y_majetek:
                              hrac_na_rade = y
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and a in range(p32w1,p32w2) and b in range(p40h1,p40h2) and pressed_space == True and "Las Vegas" in y_majetek and "Las Vegas" not in x_majetek and las.navsteva != 7800:
                              if x_money - 15000 >= 0:
                                  x_money -= 15000
                                  y_money += 15000
                                  hg40 = 0
                                  textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(x_majetek) >= 1:
                                          while len(x_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg40 += 20
                                          x_majetek.append("Las Vegas")
                                          y_majetek.remove("Las Vegas")
                                          y_majetek.append(" ")
                                  else:
                                      x_majetek.append("Las Vegas")
                                      y_majetek.remove("Las Vegas")
                                      y_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {las.jmeno}", True, (red))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg40 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (red))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and a in range(p32w1,p32w2) and b in range(p40h1,p40h2) and pressed_space == True and "Las Vegas" in y_majetek:
                               texta = fontmest.render(f"Vlastníkem města {las.jmeno} je Hráč 2.", True, (red))
                               textb = fontmest.render(f"Musíte zaplatit {las.navsteva} {znacka_meny} za návštěvu města", True, (red))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               x_money -= las.navsteva
                               y_money += las.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyx, (960,660))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (red))
                               surface.blit(textmoneyy, (960,640))
                               pygame.event.wait(240)                           
       

        if "Nairobi" in x_majetek:
                textmest = fontmest1.render("Nairobi", True, (red))
                surface.blit(textmest, (w,h + hg2))
                pocet_mest = 0
                if nairobi.navsteva != 600:
                    surface.blit(čdum1, (770,908))
                if nairobi.navsteva == 600:
                    surface.blit(čdum_pruvodce1, (770,908))
           
        if "Káhira" in x_majetek:
                textmest = fontmest1.render("Káhira", True, (red))
                surface.blit(textmest, (w,h + hg4))
                pocet_mest = 0
                if kahira.navsteva != 750:
                    surface.blit(čdum1, (615,908))
                if kahira.navsteva == 750:
                    surface.blit(čdum_pruvodce1, (615,908))

        if "Rio de Janeiro" in x_majetek:
                textmest = fontmest1.render("Rio de Janeiro", True, (red))
                surface.blit(textmest, (w,h + hg7))
                pocet_mest = 0
                if rio.navsteva != 920:
                    surface.blit(čdum1, (380,908))
                if rio.navsteva == 920:
                    surface.blit(čdum_pruvodce1, (380,908))


        if "Buenos Aires" in x_majetek:
                textmest = fontmest1.render("Buenos Aires", True, (red))
                surface.blit(textmest, (w,h + hg9))
                pocet_mest = 0
                if buenos.navsteva != 1100:
                    surface.blit(čdum1, (228,908))
                if buenos.navsteva == 1100:
                    surface.blit(čdum_pruvodce1, (228,908))

        if "Santiago de Chille" in x_majetek:
                textmest = fontmest1.render("Santiago de Chille", True, (red))
                surface.blit(textmest, (w,h + hg10))
                pocet_mest = 0
                if santiago.navsteva != 1100:
                    surface.blit(čdum1, (150,908))
                if santiago.navsteva == 1100:
                    surface.blit(čdum_pruvodce1, (150,908))

        if "Kodaň" in x_majetek:
                textmest = fontmest1.render("Kodaň", True, (red))
                surface.blit(textmest, (w,h + hg12))
                pocet_mest = 0
                if kodan.navsteva != 1400:
                    surface.blit(čdum2, (12,770))
                if kodan.navsteva == 1400:
                    surface.blit(čdum_pruvodce2, (12,770))

        if "Berlín" in x_majetek:
                textmest = fontmest1.render("Berlín", True, (red))
                surface.blit(textmest, (w,h + hg14))
                pocet_mest = 0
                if berlin.navsteva != 1700:
                    surface.blit(čdum2, (12,614))
                if berlin.navsteva == 1700:
                    surface.blit(čdum_pruvodce2, (12,614))

        if "Amsterdam" in x_majetek:
                textmest = fontmest1.render("Amsterdam", True, (red))
                surface.blit(textmest, (w,h + hg15))
                pocet_mest = 0
                if amsterdam.navsteva != 1700:
                    surface.blit(čdum2, (12,536))
                if amsterdam.navsteva == 1700:
                    surface.blit(čdum_pruvodce2, (12,536))

        if "Wellington" in x_majetek:
                textmest = fontmest1.render("Wellington", True, (red))
                surface.blit(textmest, (w,h + hg17))
                pocet_mest = 0
                if wellington.navsteva != 2100:
                    surface.blit(čdum2, (12,380))
                if wellington.navsteva == 2100:
                    surface.blit(čdum_pruvodce2, (12,380))

        if "Melbourne" in x_majetek:
                textmest = fontmest1.render("Melbourne", True, (red))
                surface.blit(textmest, (w,h + hg19))
                pocet_mest = 0
                if melbourne.navsteva != 2400:
                    surface.blit(čdum2, (12,224))
                if melbourne.navsteva == 2400:
                    surface.blit(čdum_pruvodce2, (12,224))

        if "Sydney" in x_majetek:
                textmest = fontmest1.render("Sydney", True, (red))
                surface.blit(textmest, (w,h + hg20))
                pocet_mest = 0
                if sydney.navsteva != 2400:
                    surface.blit(čdum2, (12,144))
                if sydney.navsteva == 2400:
                    surface.blit(čdum_pruvodce2, (12,144))

        if "San Francisco" in x_majetek:
                textmest = fontmest1.render("San Francisco", True, (red))
                surface.blit(textmest, (w,h + hg22))
                pocet_mest = 0
                if san.navsteva != 2800:
                    surface.blit(čdum3, (150,8))
                if san.navsteva == 2800:
                    surface.blit(čdum_pruvodce3, (150,8))

        if "Los Angeles" in x_majetek:
                textmest = fontmest1.render("Los Angeles", True, (red))
                surface.blit(textmest, (w,h + hg24))
                pocet_mest = 0
                if los.navsteva != 3500:
                    surface.blit(čdum3, (302,8))
                if los.navsteva == 3500:
                    surface.blit(čdum_pruvodce3, (302,8))

        if "New York" in x_majetek:
                textmest = fontmest1.render("New York", True, (red))
                surface.blit(textmest, (w,h + hg25))
                pocet_mest = 0
                if new.navsteva != 3500:
                    surface.blit(čdum3, (382,8))
                if new.navsteva == 3500:
                    surface.blit(čdum_pruvodce3, (382,8))

        if "Bangkok" in x_majetek:
                textmest = fontmest1.render("Bangkok", True, (red))
                surface.blit(textmest, (w,h + hg27))
                pocet_mest = 0
                if bangkok.navsteva != 3800:
                    surface.blit(čdum3, (536,8))
                if bangkok.navsteva == 3800:
                    surface.blit(čdum_pruvodce3, (536,8))
                         
        if "Šanghaj" in x_majetek:
                textmest = fontmest1.render("Šanghaj", True, (red))
                surface.blit(textmest, (w,h + hg28))
                pocet_mest = 0
                if šanghaj.navsteva != 3800:
                    surface.blit(čdum3, (616,8))
                if šanghaj.navsteva == 3800:
                    surface.blit(čdum_pruvodce3, (616,8))

        if "Tokio" in x_majetek:
                textmest = fontmest1.render("Tokio", True, (red))
                surface.blit(textmest, (w,h + hg30))
                pocet_mest = 0
                if tokio.navsteva != 4500:
                    surface.blit(čdum3, (770,8))
                if tokio.navsteva == 4500:
                    surface.blit(čdum_pruvodce3, (770,8))
               
        if "Praha" in x_majetek:
                textmest = fontmest1.render("Praha", True, (red))
                surface.blit(textmest, (w,h + hg32))
                pocet_mest = 0
                if praha.navsteva != 5100:
                    surface.blit(čdum4, (904,148))
                if praha.navsteva == 5100:
                    surface.blit(čdum_pruvodce4, (904,148))

        if "Londýn" in x_majetek:
                textmest = fontmest1.render("Londýn", True, (red))
                surface.blit(textmest, (w,h + hg33))
                pocet_mest = 0
                if londyn.navsteva != 5100:
                    surface.blit(čdum4, (904,224))
                if londyn.navsteva == 5100:
                    surface.blit(čdum_pruvodce4, (904,224))

        if "Paříž" in x_majetek:
                textmest = fontmest1.render("Paříž", True, (red))
                surface.blit(textmest, (w,h + hg35))
                pocet_mest = 0
                if pariz.navsteva != 5800:
                    surface.blit(čdum4, (904,380))
                if pariz.navsteva == 5800:
                    surface.blit(čdum_pruvodce4, (904,380))

        if "Las Vegas" in x_majetek:
                textmest = fontmest1.render("Las Vegas", True, (red))
                surface.blit(textmest, (w,h + hg40))
                pocet_mest = 0
                if las.navsteva != 7800:
                    surface.blit(čdum4, (904,770))
                if las.navsteva == 7800:
                    surface.blit(čdum_pruvodce4, (904,770))

        if "Dubai" in x_majetek:
                textmest = fontmest1.render("Dubai", True, (red))
                surface.blit(textmest, (w,h + hg38))
                pocet_mest = 0
                if dubai.navsteva != 6800:
                    surface.blit(čdum4, (904,616))
                if dubai.navsteva == 6800:
                    surface.blit(čdum_pruvodce4, (904,616))
               

        if "Bali" in x_majetek:
                textmest = fontmest1.render("Bali", True, (red))
                surface.blit(textmest, (w,h + hg16))
                pocet_mest = 0
                surface.blit(čdumb, (27,481))
       
        if "Maledivy" in x_majetek:
            textmest = fontmest1.render("Maledivy", True, (red))
            surface.blit(textmest, (w,h + hg6))
            pocet_mest = 0
            surface.blit(čdumm, (482,900))
                

        if "Srí Lanka" in x_majetek:
                textmest = fontmest1.render("Srí Lanka", True, (red))
                surface.blit(textmest, (w,h + hg36))
                pocet_mest = 0
                surface.blit(čdums, (900,440))
                
        if "Hawaii" in x_majetek:
                textmest = fontmest1.render("Hawaii", True, (red))
                surface.blit(textmest, (w,h + hg26))
                pocet_mest = 0
                surface.blit(čdumh, (440,27))

        if "Celnice" in x_majetek:
                textmest = fontmest1.render("Celnice", True, (red))
                surface.blit(textmest, (w,h + hg13))
                pocet_mest = 0
                surface.blit(čdumcel, (70,698))

        if "Ambasáda" in x_majetek:
                textmest = fontmest1.render("Ambasáda", True, (red))
                surface.blit(textmest, (w,h + hg39))
                pocet_mest = 0
                surface.blit(čdumamb, (865,700))
                

        
                
#DRUHÝ HRÁČ!!!!!!!!!
#jestli něco nefunguje - u kupování nesmí být město v majetku






                
        if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l]:
            hrac_na_rade = y

        if hrac_na_rade == y:
            
            
            #pole 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p1w1,p1w2) and d in range(p1h1,p1h2):
                        textst = fontmest.render("Jste na STARTU", True, (blue))
                        surface.blit(textst,(960,590))
                        textstpen = fontmest.render(f"Získáváte 5000{znacka_meny}", True, (blue))
                        surface.blit(textstpen, (960,610))
                        pygame.event.wait(240)
                        y_money += 5000

            #pole 2            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if c in range(p2w1,p2w2) and d in range(p1h1,p1h2):
                       if "Nairobi" in x_majetek and "Nairobi" not in y_majetek and nairobi.navsteva != 600:
                           texta = fontmest.render(f"Vlastníkem města {nairobi.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                       if "Nairobi" in x_majetek and "Nairobi" not in y_majetek and nairobi.navsteva == 600:
                           texta = fontmest.render(f"Vlastníkem města {nairobi.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {nairobi.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= nairobi.navsteva
                           x_money += nairobi.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                               
                       if "Nairobi" not in x_majetek and "Nairobi" not in y_majetek:
                           nairobi = mesta("Nairobi", 1000, 200, 400, 600, "prozatím nikdo")
                           nairobi.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                       elif "Nairobi" in y_majetek and nairobi.navsteva != 600:
                           nairobi.upgrade()
                           pygame.event.wait(240)
                       elif "Nairobi" in y_majetek and nairobi.navsteva == 600:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (blue))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p2w1,p2w2) and d in range(p1h1,p1h2) and pressed_space == True and "Nairobi" not in y_majetek and "Nairobi" not in x_majetek:
                        if y_money - 1000 >= 0:
                              y_money -= 1000
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg2 += 20
                                      y_majetek.append("Nairobi")
                              else:
                                  y_majetek.append("Nairobi")
                              #zapsání do majetku
                              #x_majetek.append("Nairobi")
                              textmajeteky = fontmest.render(f"Koupil jste si {nairobi.jmeno}", True, (blue))
                              surface.blit(textmajeteky, (960,600))
                              #hg2 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)

                if event.key == pygame.K_KP2 and c in range(p2w1,p2w2) and d in range(p1h1,p1h2) and nairobi.navsteva != 600 and pressed_space == True and "Nairobi" not in x_majetek and "Nairobi" in y_majetek:
                       if y_money - 400 >= 0:
                              y_money -= 400
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                              surface.blit(textmoneyy, (960,600))
                              nairobi.navsteva = nairobi.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {nairobi.navsteva}{znacka_meny}", True, (blue))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                       else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p2w1,p2w2) and d in range(p1h1,p1h2)and pressed_space == True and "Nairobi" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p2w1,p2w2) and d in range(p1h1,p1h2) and pressed_space == True and "Nairobi" in x_majetek and "Nairobi" not in y_majetek and nairobi.navsteva != 600:
                              if y_money - 1500 >= 0:
                                  y_money -= 1500
                                  x_money += 1500
                                  hg2 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg2 += 20
                                          y_majetek.append("Nairobi")
                                          x_majetek.remove("Nairobi")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Nairobi")
                                      x_majetek.remove("Nairobi")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {nairobi.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg2 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  hg2 = 0
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p2w1,p2w2) and d in range(p1h1,p1h2) and pressed_space == True and "Nairobi" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {nairobi.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {nairobi.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= nairobi.navsteva
                               x_money += nairobi.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)
                               


            #pole 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if c in range(p3w1,p3w2) and d in range(p1h1,p1h2) and lol == 1:
                        if hrac_na_rade == y and lol == 1:
                            rf = random.randint(1,8)
                            if rf == 1:
                                y_money += 3500
                                textf1 = fontfs.render(f"Omylem vám přišlo na účet 3500{znacka_meny}", True, (redb))
                                surface.blit(textf1, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 2:
                                y_money += 3000
                                x_money -= 3000
                                textf2 = fontfs.render(f"Spoluhráč ti musí dát 3000{znacka_meny}", True, (redb))
                                surface.blit(textf2, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 3:
                                y_money += 1500
                                textf3 = fontfs.render(f"Ve tvém městě probíhal festival.", True, (redb))
                                textf31 = fontfs.render(f"Vydělal jsi 1500 {znacka_meny}", True, (redb))
                                surface.blit(textf3, (960,600))
                                surface.blit(textf31, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 4:
                                textf4 = fontfs.render(f"Je léto a všichni chtějí k moři.", True, (redb))
                                textf41 = fontfs.render(f"Za každý svůj rezort získáváš 1000{znacka_meny}", True, (redb))
                                surface.blit(textf4, (960,600))
                                surface.blit(textf41, (960,620))
                                if "Maledivy" not in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    textf42 = fontfs.render(f"Nevlastníte žádný rezort.", True, (redb))
                                    surface.blit(textf42, (960,640))
                                if "Maledivy" in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek: 
                                    y_money += 1000
                                if "Bali" in y_majetek and "Maledivy" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 1000
                                if "Hawaii" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 1000
                                if "Srí Lanka" in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 1000
                                if "Maledivy" in y_majetek and "Bali" in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Hawaii" in y_majetek and "Bali" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" not in y_majetek and "Bali" not in y_majetek:
                                    y_money += 2000
                                if "Bali" in y_majetek and "Hawaii" in y_majetek and "Maledivy" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 2000
                                if "Hawaii" in y_majetek and "Srí Lanka" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Bali" in y_majetek and "Hawaii" in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 3000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Bali" in y_majetek and "Hawaii" not in y_majetek:
                                    y_money += 3000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" in y_majetek and "Bali" not in y_majetek:
                                    y_money += 3000
                                if "Hawaii" in y_majetek and "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 3000
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 5:
                                y_money += 5000
                                textf5 = fontfs.render(f"Tvé město se ocitlo v top 10 nejhezčích měst.", True, (redb))
                                textf51 = fontfs.render(f"Všichni ho nyní navštěvují... vydělalo vám to 5000{znacka_meny}", True, (redb))
                                surface.blit(textf5, (960,600))
                                surface.blit(textf51, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 6:
                                y_money -= 1000
                                textf6 = fontfs.render(f"Ve vašem městě vypadla elektřina.", True, (redb))
                                textf61 = fontfs.render (f"Zaplatite 1000{znacka_meny} za opravu elektrarny", True, (redb))
                                surface.blit(textf6, (960,600))
                                surface.blit(textf61, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 7:
                                y_money -= 3000
                                textf7 = fontfs.render(f"Proběhlo zemětřesení, za opravy zaplatíš 3000{znacka_meny}", True, (redb))
                                surface.blit(textf7, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 8:
                                y_money -= 3500
                                textf8 = fontfs.render(f"V jednom z vašich měst se rozšířila epidemie.", True, (redb))
                                textf81 = fontfs.render(f"Pošlete 3500{znacka_meny} na pomoc lidem", True, (redb))
                                surface.blit(textf8, (960,600))
                                surface.blit(textf81, (960,620))
                                pygame.event.wait(240)
                                lol = 0
            #pole 4            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if c in range(p4w1,p4w2) and d in range(p1h1,p1h2):
                        if "Káhira" in x_majetek and "Káhira" not in y_majetek and kahira.navsteva != 750:
                           texta = fontmest.render(f"Vlastníkem města {kahira.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Káhira" in x_majetek and "Káhira" not in y_majetek and kahira.navsteva == 750:
                           texta = fontmest.render(f"Vlastníkem města {kahira.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {kahira.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= kahira.navsteva
                           x_money += kahira.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Káhira" not in x_majetek and "Káhira" not in y_majetek:
                           kahira = mesta("Káhira", 1200, 250, 480, 750, "prozatím nikdo")
                           kahira.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Káhira" in y_majetek and kahira.navsteva != 750:
                           kahira.upgrade()
                           pygame.event.wait(240)
                        elif "Káhira" in y_majetek and kahira.navsteva == 750:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p4w1,p4w2) and d in range(p1h1,p1h2) and pressed_space == True and "Káhira" not in y_majetek and "Káhira" not in x_majetek:
                        if y_money - kahira.kupni_cena >= 0:
                              y_money -= kahira.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg4 += 20
                                      y_majetek.append("Káhira")
                              else:
                                  y_majetek.append("Káhira")
                              #zapsání do majetku
                              #x_majetek.append("Káhira")
                              textmajeteky = fontmest.render(f"Koupil jste si {kahira.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg4 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p4w1,p4w2) and d in range(p1h1,p1h2) and kahira.navsteva != 750 and pressed_space == True and "Káhira" not in x_majetek and "Káhira" in y_majetek:
                        if y_money - kahira.domecek >= 0:
                              y_money -= kahira.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              kahira.navsteva = kahira.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {kahira.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p4w1,p4w2) and d in range(p1h1,p1h2)and pressed_space == True and "Káhira" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p4w1,p4w2) and d in range(p1h1,p1h2) and pressed_space == True and "Káhira" in x_majetek and "Káhira" not in y_majetek and kahira.navsteva != 750:
                              if y_money - 1800 >= 0:
                                  y_money -= 1800
                                  x_money += 1800
                                  hg4 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg4 += 20
                                          y_majetek.append("Káhira")
                                          x_majetek.remove("Káhira")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Káhira")
                                      x_majetek.remove("Káhira")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {kahira.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg4 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p4w1,p4w2) and d in range(p1h1,p1h2) and pressed_space == True and "Káhira" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {kahira.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {kahira.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= kahira.navsteva
                               x_money += kahira.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)
                              
            #if "Káhira" in x_majetek:
                #textmest = fontmest1.render("Káhira", True, (red))
                #surface.blit(textmest, (w,h + hg4))
                #pocet_mest = 0
                
            #pole5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
            
                    if c in range(p5w1,p5w2) and d in range(p1h1,p1h2):
                        procento = int((y_money*10)/100)
                        y_money -= procento
                        textchar = fontmest.render(f"Přispějte charitě {procento}{znacka_meny}", True, (redb))
                        surface.blit(textchar, (960,600))
                        pygame.event.wait()
            #pole6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p6w1,p6w2) and d in range(p1h1,p1h2):
                        if "Maledivy" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                            texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                            surface.blit(texta, (960,600))
                            textb = fontmest.render(f"Musíte zaplatit {maledivy.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                            surface.blit(textb, (960,620))
                            y_money -= maledivy.navsteva
                            x_money += maledivy.navsteva
                            textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                            surface.blit(textmoneyx, (960,640))
                            textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                            surface.blit(textmoneyy, (960,660))
                            pygame.event.wait(240)  
                        if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" not in x_majetek and "Srí Lanka" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Maledivy" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek and "Srí Lanka" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Maledivy" in x_majetek and "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)                               
                        if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)     
                             
                        if "Maledivy" in x_majetek and "Bali" in x_majetek and "Srí Lanka" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Maledivy" in x_majetek and "Hawai" in x_majetek and "Srí Lanka" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)     
                        if "Maledivy" not in x_majetek and "Maledivy" not in y_majetek:
                           maledivy = mesta("Maledivy", 4000, 1000, 0, 0, "prozatím nikdo")
                           maledivy.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        if "Maledivy" in y_majetek:
                           textmas = fontmest.render("Jste vlastníkem tohoto města", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                        #if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" in y_majetek and "Bali" in y_majetek:
                            #textvyhra = fontmest.render("Vyhrál jste hru!", True, (red))
                            #surface.blit(textvyhra, (960,600))
                            #pygame.event.wait(240)
                       
                           #w = 980, h = 120,pocet_mest = 1  , i = 0
                     
                if event.key == pygame.K_KP1 and c in range(p6w1,p6w2) and d in range(p1h1,p1h2) and pressed_space == True and "Maledivy" not in x_majetek and "Maledivy" not in y_majetek:
                        if y_money - maledivy.kupni_cena >= 0:
                              y_money -= maledivy.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg6 += 20
                                      y_majetek.append("Maledivy")
                              else:
                                  y_majetek.append("Maledivy")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {maledivy.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                
                if event.key == pygame.K_KP0 and c in range(p6w1,p6w2) and d in range(p1h1,p1h2)and pressed_space == True:
                              hrac_na_rade = x
                              pressed_space = False
            #pole 7            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p7w1,p7w2) and d in range(p1h1,p1h2):
                        if "Rio de Janeiro" in x_majetek and "Rio de Janeiro" not in y_majetek and rio.navsteva != 920:
                           texta = fontmest.render(f"Vlastníkem města {rio.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Rio de Janeiro" in x_majetek and "Rio de Janeiro" not in y_majetek and rio.navsteva == 920:
                           texta = fontmest.render(f"Vlastníkem města {rio.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {rio.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= rio.navsteva
                           x_money += rio.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Rio de Janeiro" not in x_majetek and "Rio de Janeiro" not in y_majetek:
                           rio = mesta("Rio de Janeiro", 1400, 340, 560, 920, "prozatím nikdo")
                           rio.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Rio de Janeiro" in y_majetek and rio.navsteva != 920:
                           rio.upgrade()
                           pygame.event.wait(240)
                        elif "Rio de Janeiro" in y_majetek and rio.navsteva == 920:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           #w = 980, h = 120,pocet_mest = 1  , i = 0
                     
                if event.key == pygame.K_KP1 and c in range(p7w1,p7w2) and d in range(p1h1,p1h2) and pressed_space == True and "Rio de Janeiro" not in x_majetek and "Rio de Janeiro" not in y_majetek:
                        if y_money - rio.kupni_cena >= 0:
                              y_money -= rio.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg7 += 20
                                      y_majetek.append("Rio de Janeiro")
                              else:
                                  y_majetek.append("Rio de Janeiro")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajeteky = fontmest.render(f"Koupil jste si {rio.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg7 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p7w1,p7w2) and d in range(p1h1,p1h2) and rio.navsteva != 920 and pressed_space == True and "Rio de Janeiro" not in x_majetek and "Rio de Janeiro" in y_majetek:
                        if y_money - rio.kupni_cena >= 0:
                              y_money -= rio.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              rio.navsteva = rio.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {rio.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p7w1,p7w2) and d in range(p1h1,p1h2)and pressed_space == True and "Rio de Janeiro" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p7w1,p7w2) and d in range(p1h1,p1h2) and pressed_space == True and "Rio de Janeiro" in x_majetek and "Rio de Janeiro" not in y_majetek and rio.navsteva != 920:
                              if y_money - 2100 >= 0:
                                  y_money -= 2100
                                  x_money += 2100
                                  hg7 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg7 += 20
                                          y_majetek.append("Rio de Janeiro")
                                          x_majetek.remove("Rio de Janeiro")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Rio de Janeiro")
                                      x_majetek.remove("Rio de Janeiro")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {rio.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg7 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p7w1,p7w2) and d in range(p1h1,p1h2) and pressed_space == True and "Rio de Janeiro" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {rio.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {rio.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= rio.navsteva
                               x_money += rio.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)
            
            #pole 8
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p8w1,p8w2) and d in range(p1h1,p1h2) and lol == 1:
                        if hrac_na_rade == y and lol == 1:
                                rs = random.randint(1,10)
                                if rs == 1:
                                    texts1 = fontfs.render(f"Jděte na nejbližší volné město", True, (redb))
                                    surface.blit(texts1, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 2:
                                    texts2 = fontfs.render(f"Jděte na pole s letištěm", True, (redb))
                                    surface.blit(texts2, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 3:
                                    texts3 = fontfs.render(f"Jděte do vězení!", True, (redb))
                                    surface.blit(texts3, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 4:
                                    texts4 = fontfs.render(f"Jděte na vaše nejbližší město", True, (redb))
                                    surface.blit(texts4, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 5:
                                    texts5 = fontfs.render(f"Jděte na nejbližší město vašeho spoluhráče", True, (redb))
                                    surface.blit(texts5, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 6:
                                    texts6 = fontfs.render(f"Jděte na start", True, (redb))
                                    surface.blit(texts6, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 7:
                                    texts7 = fontfs.render(f"Jděte na pole s letištěm", True, (redb))
                                    surface.blit(texts7, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 8:
                                    texts8 = fontfs.render(f"Jděte na emisní povolenku", True, (redb))
                                    surface.blit(texts8, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 9:
                                    vpred = random.randint(1,10)
                                    if vpred == 1:
                                        texts91 = fontfs.render(f"Jděte vpřed o {vpred} políčko", True, (redb))
                                        surface.blit(texts91, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 2 or vpred == 3 or vpred == 4:
                                        texts92 = fontfs.render(f"Jděte vpřed o {vpred} políčka", True, (redb))
                                        surface.blit(texts92, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 5 or vpred == 6 or vpred == 7 or vpred == 8 or vpred == 9 or vpred == 10:
                                        texts93 = fontfs.render(f"Jděte vpřed o {vpred} políček", True, (redb))
                                        surface.blit(texts93, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
                                if rs == 10:
                                    dozadu = random.randint(1,10)
                                    if dozadu == 1:
                                        texts101 = fontfs.render(f"Jděte dozadu o {dozadu} políčko", True, (redb))
                                        surface.blit(texts101, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 2 or dozadu == 3 or dozadu == 4:
                                        texts102 = fontfs.render(f"Jděte dozadu o {dozadu} políčka", True, (redb))
                                        surface.blit(texts102, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 5 or dozadu == 6 or dozadu == 7 or dozadu == 8 or dozadu == 9 or dozadu == 10:
                                        texts103 = fontfs.render(f"Jděte dozadu o {dozadu} políček", True, (redb))
                                        surface.blit(texts103, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
            #pole 9
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p9w1,p9w2) and d in range(p1h1,p1h2):
                        if "Buenos Aires" in x_majetek and "Buenos Aires" not in y_majetek and buenos.navsteva != 1100:
                           texta = fontmest.render(f"Vlastníkem města {buenos.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Buenos Aires" in x_majetek and "Buenos Aires" not in y_majetek and buenos.navsteva == 1100:
                           texta = fontmest.render(f"Vlastníkem města {buenos.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {buenos.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= buenos.navsteva
                           x_money += buenos.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Buenos Aires" not in x_majetek and "Buenos Aires" not in y_majetek:
                           buenos = mesta("Buenos Aires", 1600, 400, 640, 1100, "prozatím nikdo")
                           buenos.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Buenos Aires" in y_majetek and buenos.navsteva != 1100:
                           buenos.upgrade()
                           pygame.event.wait(240)
                        elif "Buenos Aires" in y_majetek and buenos.navsteva == 1100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p9w1,p9w2) and d in range(p1h1,p1h2) and pressed_space == True and "Buenos Aires" not in x_majetek and "Buenos Aires" not in y_majetek:
                        if y_money - buenos.kupni_cena >= 0:
                              y_money -= buenos.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg9 += 20
                                      y_majetek.append("Buenos Aires")
                              else:
                                  y_majetek.append("Buenos Aires")
                              #zapsání do majetku
                              #x_majetek.append("Buenos Aires")
                              textmajeteky = fontmest.render(f"Koupil jste si {buenos.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p9w1,p9w2) and d in range(p1h1,p1h2) and buenos.navsteva != 1100 and pressed_space == True and "Buenos Aires" not in x_majetek and "Buenos Aires" in y_majetek:
                        if y_money - buenos.kupni_cena >= 0:
                              y_money -= buenos.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              buenos.navsteva = buenos.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {buenos.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p9w1,p9w2) and d in range(p1h1,p1h2)and pressed_space == True and "Buenos Aires" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p9w1,p9w2) and d in range(p1h1,p1h2) and pressed_space == True and "Buenos Aires" in x_majetek and "Buenos Aires" not in y_majetek and buenos.navsteva != 1100:
                              if y_money - 2400 >= 0:
                                  y_money -= 2400
                                  x_money += 2400
                                  hg9 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg9 += 20
                                          y_majetek.append("Buenos Aires")
                                          x_majetek.remove("Buenos Aires")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Buenos Aires")
                                      x_majetek.remove("Buenos Aires")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {buenos.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg9 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p9w1,p9w2) and d in range(p1h1,p1h2) and pressed_space == True and "Buenos Aires" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {buenos.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {buenos.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= buenos.navsteva
                               x_money += buenos.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)

                
            #pole10 y
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p10w1,p10w2) and d in range(p1h1,p1h2):
                        if "Santiago de Chille" in x_majetek and "Santiago de Chille" not in y_majetek and santiago.navsteva != 1100:
                           texta = fontmest.render(f"Vlastníkem města {santiago.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Santiago de Chille" in x_majetek and "Santiago de Chille" not in y_majetek and santiago.navsteva == 1100:
                           texta = fontmest.render(f"Vlastníkem města {santiago.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {santiago.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= santiago.navsteva
                           x_money += santiago.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Santiago de Chille" not in x_majetek and "Santiago de Chille" not in y_majetek:
                           santiago = mesta("Santiago de Chille", 1600, 400, 640, 1100, "prozatím nikdo")
                           santiago.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Santiago de Chille" in y_majetek and santiago.navsteva != 1100:
                           santiago.upgrade()
                           pygame.event.wait(240)
                        elif "Santiago de Chille" in y_majetek and santiago.navsteva == 1100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p10w1,p10w2) and d in range(p1h1,p1h2) and pressed_space == True and "Santiago de Chille" not in x_majetek and "Santiago de Chille" not in y_majetek:
                        if y_money - santiago.kupni_cena >= 0:
                              y_money -= santiago.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg10 += 20
                                      y_majetek.append("Santiago de Chille")
                              else:
                                  y_majetek.append("Santiago de Chille")
                              #zapsání do majetku
                              #x_majetek.append("Santiago de Chille")
                              textmajeteky = fontmest.render(f"Koupil jste {santiago.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg10 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p10w1,p10w2) and d in range(p1h1,p1h2) and santiago.navsteva != 1100 and pressed_space == True and "Santiago de Chille" not in x_majetek and "Santiago de Chille" in y_majetek:
                        if y_money - santiago.domecek >= 0:
                              y_money -= santiago.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              santiago.navsteva = santiago.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {santiago.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)     
                
                if event.key == pygame.K_KP0 and c in range(p10w1,p10w2) and d in range(p1h1,p1h2)and pressed_space == True and "Santiago de Chille" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p10w1,p10w2) and d in range(p1h1,p1h2) and pressed_space == True and "Santiago de Chille" in x_majetek and "Santiago de Chille" not in y_majetek and santiago.navsteva != 1100:
                              if y_money - 2400 >= 0:
                                  y_money -= 2400
                                  x_money += 2400
                                  hg10 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg10 += 20
                                          y_majetek.append("Santiago de Chille")
                                          x_majetek.remove("Santiago de Chille")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Santiago de Chille")
                                      x_majetek.remove("Santiago de Chille")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {santiago.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg10 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p10w1,p10w2) and d in range(p1h1,p1h2) and pressed_space == True and "Santiago de Chille" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {santiago.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {santiago.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= santiago.navsteva
                               x_money += santiago.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240) 
            #pole11
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True

                    if c in range(p11w1,p11w2) and d in range(p1h1,p1h2):
                        textvezeni = fontmest.render(f"Jste ve vězení!", True, (redb))
                        surface.blit(textvezeni, (960,600))
                        textvezeni1 = fontmest.render(f"Jestli chcete hodit kostkou, zkuste to (musíte hodit 6)", True, (redb))
                        surface.blit(textvezeni1, (960,620))
                        textvezeni2 = fontmest.render(f"Nebo zmáčkněte číslo 3 a zaplaťte 3000{znacka_meny}", True, (redb))
                        surface.blit(textvezeni2, (960,640))
                        pygame.event.wait(240)
                    vezen = True
                if c in range(p11w1,p11w2) and d in range(p1h1,p1h2) and pressed_space == True and keys[pygame.K_KP3]:
                    if y_money - 1000 >= 0:
                        y_money -= 1000
                        pygame.event.wait(240)
                        vezen = False
                    else:
                        textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                        surface.blit(textnedostatekp, (960,600))
                        pygame.event.wait(240)
                        vezen = False

                        
            if event.type == pygame.KEYUP and vezen == True:   
                    if hrac_hodil_kostkou == True and c in range(p11w1,p11w2) and d in range(p1h1,p1h2):
                            if u == 6:
                                textvezeni3 = fontmest.render(f"Můžete pokračovat ve hře, jste venku z vězení!", True, (redb))
                                surface.blit(textvezeni3, (960,600))
                                pygame.event.wait(240)
                                hrac_hodil_kostkou = False
                                vezen = False
                            else: 
                                textvezeni4 = fontmest.render(f"Bohužel jste hodil {u}, nejste venku!", True, (redb))
                                surface.blit(textvezeni4, (960,600))
                                pygame.event.wait(240)
                                hrac_hodil_kostkou = False
                                vezen = False
                                
            #pole12 p12w1 = 0 p12w2 = 90 p12h1 = 740 p12h1 = 788
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p12w1,p12w2) and d in range(p12h1,p12h2):
                        if "Kodaň" in x_majetek and "Kodaň" not in y_majetek and kodan.navsteva != 1400:
                           texta = fontmest.render(f"Vlastníkem města {kodan.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Kodaň" in x_majetek and "Kodaň" not in y_majetek and kodan.navsteva == 1400:
                           texta = fontmest.render(f"Vlastníkem města {kodan.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {kodan.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= kodan.navsteva
                           x_money += kodan.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Kodaň" not in x_majetek and "Kodaň" not in y_majetek:
                           kodan = mesta("Kodaň", 2000, 560, 800, 1400, "prozatím nikdo")
                           kodan.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Kodaň" in y_majetek and kodan.navsteva != 1400:
                           kodan.upgrade()
                           pygame.event.wait(240)
                        elif "Kodaň" in y_majetek and kodan.navsteva == 1400:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p12h1,p12h2) and pressed_space == True and "Kodaň" not in x_majetek and "Kodaň" not in y_majetek:
                        if y_money - kodan.kupni_cena >= 0:
                              y_money -= kodan.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg12 += 20
                                      y_majetek.append("Kodaň")
                              else:
                                  y_majetek.append("Kodaň")
                              #zapsání do majetku
                              #x_majetek.append("Kodaň")
                              textmajeteky = fontmest.render(f"Koupil jste si {kodan.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg12 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p12w1,p12w2) and d in range(p12h1,p12h2) and kodan.navsteva != 1400 and pressed_space == True and "Kodaň" not in x_majetek and "Kodaň" in y_majetek:
                        if y_money - kodan.domecek >= 0:
                              y_money -= kodan.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              kodan.navsteva = kodan.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {kodan.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                  
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p12h1,p12h2)and pressed_space == True and "Kodaň" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p12w1,p12w2) and d in range(p12h1,p12h2) and pressed_space == True and "Kodaň" in x_majetek and "Kodaň" not in y_majetek and kodan.navsteva != 1400:
                              if y_money - 3000 >= 0:
                                  y_money -= 3000
                                  x_money += 3000
                                  hg12 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg12 += 20
                                          y_majetek.append("Kodaň")
                                          x_majetek.remove("Kodaň")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Kodaň")
                                      x_majetek.remove("Kodaň")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {kodan.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg12 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p12h1,p12h2) and pressed_space == True and "Kodaň" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {kodan.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {kodan.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= kodan.navsteva
                               x_money += kodan.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240) 
                
            #pole13
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True

                    if c in range(p12w1,p12w2) and d in range(p13h1,p13h2):
                        if "Celnice" not in x_majetek and "Celnice" not in y_majetek:
                            textcelnice = fontmest.render(f"Název města: Celnice", True, (redb))
                            surface.blit(textcelnice, (960,600))
                            textkcelnice1 = fontmest.render(f"Kupní cena: 1500{znacka_meny}", True, (redb))
                            surface.blit(textkcelnice1, (960,620))
                            textkcelnice2 = fontmest.render(f"Cena za návštěvu tohoto města: 200x hod kostkou", True, (redb))
                            surface.blit(textkcelnice2, (960,640))
                            surface.blit(napisy, (960,680))
                            surface.blit(napis2y, (960,700))
                            pygame.event.wait(240)
                    
                        if "Celnice" in x_majetek:
                           textcelnice3 = fontmest.render(f"Vlastníkem Celnice je Hráč 1.", True, (redb))
                           #textb = fontmest.render(f"Musíte zaplatit {kodan.navsteva}{znacka_meny} za návštěvu města", True, (red))
                           surface.blit(textcelnice3, (960,600))
                           #surface.blit(textb, (960, 620))
                           textca = fontmest.render(f"Hoďte ještě jednou kostkou!", True, (redb))
                           surface.blit(textca, (960,620))
                           y_money2 = copy.copy(x_money)
                           pygame.event.wait(240)
                           
                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p13h1,p13h2) and pressed_space == True and "Celnice" not in x_majetek and "Celnice" not in y_majetek:
                        if y_money - 1500 >= 0:
                              y_money -= 1500
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg13 += 20
                                      y_majetek.append("Celnice")
                              else:
                                  y_majetek.append("Celnice")
                              #zapsání do majetku
                              #x_majetek.append("Kodaň")
                              textmajeteky = fontmest.render(f"Koupil jste si Celnice", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                            
            if c in range(p12w1,p12w2) and d in range(p13h1,p13h2) and pressed_space == True and "Celnice" in x_majetek and "Celnice" not in y_majetek and "Ambasáda" not in x_majetek:
                #if event.type == pygame.KEYDOWN:
                    if u == 1:
                        cacena = 1*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                    
                    if u == 2:
                        cacena = 2*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
              
                    if u == 3:
                        cacena = 3*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 4:
                        cacena = 4*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 5:
                        cacena = 5*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                            
                        
                    if u == 6:
                        cacena = 6*200
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                    
                    

                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                        pressed_space = False
                        smth = 0
                        
            if c in range(p12w1,p12w2) and d in range(p13h1,p13h2) and pressed_space == True and "Celnice" in x_majetek and "Celnice" not in y_majetek and "Ambasáda" in x_majetek:
                #if event.type == pygame.KEYDOWN:
                    if u == 1:
                        cacena = 1*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                    
                    if u == 2:
                        cacena = 2*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
              
                    if u == 3:
                        cacena = 3*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 4:
                        cacena = 4*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 5:
                        cacena = 5*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                            
                        
                    if u == 6:
                        cacena = 6*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                    
                    

                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                        pressed_space = False
                        smth = 0
                        
            if c in range(p12w1,p12w2) and d in range(p13h1,p13h2) and pressed_space == True and smth == 1:
                roz = y_money2 - y_money
                textca = fontmest.render(f"Musíte zaplatit {roz}{znacka_meny}", True, (redb))
                surface.blit(textca, (960,600))
                pygame.event.wait(240)
                    
                if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                    smth = 0

            
            #pole14
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p12w1,p12w2) and d in range(p14h1,p14h2):
                        if "Berlín" in x_majetek and "Berlín" not in y_majetek and berlin.navsteva != 1700:
                           texta = fontmest.render(f"Vlastníkem města {berlin.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Berlín" in x_majetek and "Berlín" not in y_majetek and berlin.navsteva == 1700:
                           texta = fontmest.render(f"Vlastníkem města {berlin.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {berlin.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= kodan.navsteva
                           x_money += kodan.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Berlín" not in x_majetek and "Berlín" not in y_majetek:
                           berlin = mesta("Berlín", 2300, 670, 920, 1700, "prozatím nikdo")
                           berlin.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Berlín" in y_majetek and berlin.navsteva != 1700:
                           berlin.upgrade()
                           pygame.event.wait(240)
                        elif "Berlín" in y_majetek and berlin.navsteva == 1700:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p14h1,p14h2) and pressed_space == True and "Berlin" not in x_majetek and "Berlin" not in y_majetek:
                        if y_money - berlin.kupni_cena >= 0:
                              y_money -= berlin.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg14 += 20
                                      y_majetek.append("Berlín")
                              else:
                                  y_majetek.append("Berlín")
                              #zapsání do majetku
                              #x_majetek.append("Berlín")
                              textmajeteky = fontmest.render(f"Koupil jste si {berlin.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg14 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p12w1,p12w2) and d in range(p14h1,p14h2) and berlin.navsteva != 1700 and pressed_space == True and "Berlín" not in x_majetek and "Berlín" in y_majetek:
                        if y_money - berlin.domecek >= 0:
                              y_money -= berlin.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              berlin.navsteva = berlin.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {berlin.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)     
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p14h1,p14h2)and pressed_space == True and "Berlín" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p12w1,p12w2) and d in range(p14h1,p14h2) and pressed_space == True and "Berlín" in x_majetek and "Berlín" not in y_majetek and berlin.navsteva != 1700:
                              if y_money - 3450 >= 0:
                                  y_money -= 3450
                                  x_money += 3450
                                  hg14 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg14 += 20
                                          y_majetek.append("Berlín")
                                          x_majetek.remove("Berlín")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Berlín")
                                      x_majetek.remove("Berlín")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {berlin.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg14 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p14h1,p14h2) and pressed_space == True and "Berlín" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {berlin.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {berlin.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= berlin.navsteva
                               x_money += berlin.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)        


            #pole15
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p12w1,p12w2) and d in range(p15h1,p15h2):
                        if "Amsterdam" in x_majetek and "Amsterdam" not in y_majetek and amsterdam.navsteva != 1700:
                           texta = fontmest.render(f"Vlastníkem města {amsterdam.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Amsterdam" in x_majetek and "Amsterdam" not in y_majetek and amsterdam.navsteva == 1700:
                           texta = fontmest.render(f"Vlastníkem města {amsterdam.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {amsterdam.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= amsterdam.navsteva
                           x_money += amsterdam.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Amsterdam" not in x_majetek and "Amsterdam" not in y_majetek:
                           amsterdam = mesta("Amsterdam", 2300, 670, 920, 1700, "prozatím nikdo")
                           amsterdam.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Amsterdam" in y_majetek and amsterdam.navsteva != 1700:
                           berlin.upgrade()
                           pygame.event.wait(240)
                        elif "Amsterdam" in y_majetek and amsterdam.navsteva == 1700:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p15h1,p15h2) and pressed_space == True and "Amsterdam" not in x_majetek and "Amsterdam" not in y_majetek:
                        if y_money - amsterdam.kupni_cena >= 0:
                              y_money -= amsterdam.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg15 += 20
                                      y_majetek.append("Amsterdam")
                              else:
                                  y_majetek.append("Amsterdam")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajeteky = fontmest.render(f"Koupil jste si {amsterdam.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg15 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240) 
                if event.key == pygame.K_KP2 and c in range(p12w1,p12w2) and d in range(p15h1,p15h2) and amsterdam.navsteva != 1700 and pressed_space == True and "Amsterdam" not in x_majetek and "Amsterdam" in y_majetek:
                        if y_money - amsterdam.domecek >= 0:
                              y_money -= amsterdam.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              amsterdam.navsteva = amsterdam.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {amsterdam.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)       
                       

                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p15h1,p15h2)and pressed_space == True and "Amsterdam" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p12w1,p12w2) and d in range(p15h1,p15h2) and pressed_space == True and "Amsterdam" in x_majetek and "Amsterdam" not in y_majetek and amsterdam.navsteva != 1700:
                              if y_money - 3450 >= 0:
                                  y_money -= 3450
                                  x_money += 3450
                                  hg15 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg15 += 20
                                          y_majetek.append("Amsterdam")
                                          x_majetek.remove("Amsterdam")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Amsterdam")
                                      x_majetek.remove("Amsterdam")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {amsterdam.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg15 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p15h1,p15h2) and pressed_space == True and "Amsterdam" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {amsterdam.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {amsterdam.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= amsterdam.navsteva
                               x_money += amsterdam.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)        
            #pole16
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p12w1,p12w2) and d in range(p16h1,p16h2):
                        if "Bali" in x_majetek and "Srí Lanka" not in x_majetek and "Maledivy" not in x_majetek and "Hawaii" not in x_majetek:
                            texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 1.", True, (redb))
                            surface.blit(texta, (960,600))
                            textb = fontmest.render(f"Musíte zaplatit {bali.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                            surface.blit(textb, (960,620))
                            y_money -= bali.navsteva
                            x_money += bali.navsteva
                            textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                            surface.blit(textmoneyx, (960,640))
                            textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                            surface.blit(textmoneyy, (960,660))
                            pygame.event.wait(240)  
                        if "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Maledivy" not in x_majetek and "Hawaii" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Bali" in x_majetek and "Maledivy" in x_majetek and "Srí Lanka" not in x_majetek and "Hawaii" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Bali" in x_majetek and "Hawaii" in x_majetek and "Srí Lanka" not in x_majetek and "Maledivy" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)                               
                        if "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Maledivy" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)     
                             
                        if "Bali" in x_majetek and "Srí Lanka" in x_majetek and "Hawaii" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Bali" in x_majetek and "Maledivy" in x_majetek and "Hawaii" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {bali.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240) 
                        if "Bali" not in x_majetek and "Bali" not in y_majetek:
                           bali = mesta("Bali", 4000, 1000, 0, 0, "prozatím nikdo")
                           bali.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        if "Bali" in y_majetek:
                           textmas = fontmest.render("Jste vlastníkem tohoto města", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                        #if "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" in y_majetek and "Maledivy" in y_majetek:
                            #textvyhra = fontmest.render("Vyhrál jste hru!", True, (red))
                            #surface.blit(textvyhra, (960,600))
                            #pygame.event.wait(240)

                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p16h1,p16h2) and pressed_space == True and "Bali" not in x_majetek and "Bali" not in y_majetek:
                        if y_money - bali.kupni_cena >= 0:
                              y_money -= bali.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg16 += 20
                                      y_majetek.append("Bali")
                              else:
                                  y_majetek.append("Bali")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {bali.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p16h1,p16h2) and pressed_space == True:
                              hrac_na_rade = x
                              pressed_space = False
            #pole17
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p12w1,p12w2) and d in range(p17h1,p17h2):
                        if "Wellington" in x_majetek and "Wellington" not in y_majetek and wellington.navsteva != 2100:
                           texta = fontmest.render(f"Vlastníkem města {wellington.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Wellington" in x_majetek and "Wellington" not in y_majetek and wellington.navsteva == 2100:
                           texta = fontmest.render(f"Vlastníkem města {wellington.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {wellington.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= wellington.navsteva
                           x_money += wellington.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Wellington" not in x_majetek and "Wellington" not in y_majetek:
                           wellington = mesta("Wellington", 2800, 900, 1120, 2100, "prozatím nikdo")
                           wellington.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Wellington" in y_majetek and wellington.navsteva != 2100:
                           wellington.upgrade()
                           pygame.event.wait(240)
                        elif "Wellington" in y_majetek and wellington.navsteva == 2100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p17h1,p17h2) and pressed_space == True and "Wellington" not in x_majetek and "Wellington" not in y_majetek:
                        if y_money - wellington.kupni_cena >= 0:
                              y_money -= wellington.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg17 += 20
                                      y_majetek.append("Wellington")
                              else:
                                  y_majetek.append("Wellington")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajeteky = fontmest.render(f"Koupil jste si {wellington.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg17 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p12w1,p12w2) and d in range(p17h1,p17h2) and wellington.navsteva != 2100 and pressed_space == True and "Wellington" not in x_majetek and "Wellington" in y_majetek:
                        if y_money - wellington.domecek >= 0:
                              y_money -= wellington.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              wellington.navsteva = wellington.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {wellington.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p17h1,p17h2)and pressed_space == True and "Wellington" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p12w1,p12w2) and d in range(p17h1,p17h2) and pressed_space == True and "Wellington" in x_majetek and "Wellington" not in y_majetek and wellington.navsteva != 2100:
                              if y_money - 4200 >= 0:
                                  y_money -= 4200
                                  x_money += 4200
                                  hg17 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg17 += 20
                                          y_majetek.append("Wellington")
                                          x_majetek.remove("Wellington")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Wellington")
                                      x_majetek.remove("Wellington")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {wellington.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg17 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p17h1,p17h2) and pressed_space == True and "Wellington" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {wellington.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {wellington.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= wellington.navsteva
                               x_money += wellington.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)              

            #pole18
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if c in range(p12w1,p12w2) and d in range(p18h1,p18h2) and lol == 1:
                        if hrac_na_rade == y and lol == 1:
                            rf = random.randint(1,8)
                            if rf == 1:
                                y_money += 3500
                                textf1 = fontfs.render(f"Omylem vám přišlo na účet 3500{znacka_meny}", True, (redb))
                                surface.blit(textf1, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 2:
                                y_money += 3000
                                x_money -= 3000
                                textf2 = fontfs.render(f"Spoluhráč ti musí dát 3000{znacka_meny}", True, (redb))
                                surface.blit(textf2, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 3:
                                y_money += 1500
                                textf3 = fontfs.render(f"Ve tvém městě probíhal festival.", True, (redb))
                                textf31 = fontfs.render(f"Vydělal jsi 1500 {znacka_meny}", True, (redb))
                                surface.blit(textf3, (960,600))
                                surface.blit(textf31, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 4:
                                textf4 = fontfs.render(f"Je léto a všichni chtějí k moři.", True, (redb))
                                textf41 = fontfs.render(f"Za každý svůj rezort získáváš 1000{znacka_meny}", True, (redb))
                                surface.blit(textf4, (960,600))
                                surface.blit(textf41, (960,620))
                                if "Maledivy" not in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    textf42 = fontfs.render(f"Nevlastníte žádný rezort.", True, (redb))
                                    surface.blit(textf42, (960,640))
                                if "Maledivy" in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek: 
                                    y_money += 1000
                                if "Bali" in y_majetek and "Maledivy" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 1000
                                if "Hawaii" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 1000
                                if "Srí Lanka" in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 1000
                                if "Maledivy" in y_majetek and "Bali" in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Hawaii" in y_majetek and "Bali" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" not in y_majetek and "Bali" not in y_majetek:
                                    y_money += 2000
                                if "Bali" in y_majetek and "Hawaii" in y_majetek and "Maledivy" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 2000
                                if "Hawaii" in y_majetek and "Srí Lanka" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Bali" in y_majetek and "Hawaii" in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 3000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Bali" in y_majetek and "Hawaii" not in y_majetek:
                                    y_money += 3000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" in y_majetek and "Bali" not in y_majetek:
                                    y_money += 3000
                                if "Hawaii" in y_majetek and "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 3000
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 5:
                                y_money += 5000
                                textf5 = fontfs.render(f"Tvé město se ocitlo v top 10 nejhezčích měst.", True, (redb))
                                textf51 = fontfs.render(f"Všichni ho nyní navštěvují... vydělalo vám to 5000{znacka_meny}", True, (redb))
                                surface.blit(textf5, (960,600))
                                surface.blit(textf51, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 6:
                                y_money -= 1000
                                textf6 = fontfs.render(f"Ve vašem městě vypadla elektřina.", True, (redb))
                                textf61 = fontfs.render (f"Zaplatite 1000{znacka_meny} za opravu elektrarny", True, (redb))
                                surface.blit(textf6, (960,600))
                                surface.blit(textf61, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 7:
                                y_money -= 3000
                                textf7 = fontfs.render(f"Proběhlo zemětřesení, za opravy zaplatíš 3000{znacka_meny}", True, (redb))
                                surface.blit(textf7, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 8:
                                y_money -= 3500
                                textf8 = fontfs.render(f"V jednom z vašich měst se rozšířila epidemie.", True, (redb))
                                textf81 = fontfs.render(f"Pošlete 3500{znacka_meny} na pomoc lidem", True, (redb))
                                surface.blit(textf8, (960,600))
                                surface.blit(textf81, (960,620))
                                pygame.event.wait(240)
                                lol = 0
            #pole19
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p12w1,p12w2) and d in range(p19h1,p19h2):
                        if "Melbourne" in x_majetek and "Melbourne" not in y_majetek and melbourne.navsteva != 2400:
                           texta = fontmest.render(f"Vlastníkem města {melbourne.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Melbourne" in x_majetek and "Melbourne" not in y_majetek and melbourne.navsteva == 2400:
                           texta = fontmest.render(f"Vlastníkem města {melbourne.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {melbourne.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= melbourne.navsteva
                           x_money += melbourne.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Melbourne" not in x_majetek and "Melbourne" not in y_majetek:
                           melbourne = mesta("Melbourne", 3200, 1050, 1280, 2400, "prozatím nikdo")
                           melbourne.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Melbourne" in y_majetek and melbourne.navsteva != 2400:
                           melbourne.upgrade()
                           pygame.event.wait(240)
                        elif "Melbourne" in y_majetek and melbourne.navsteva == 2400:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p19h1,p19h2) and pressed_space == True and "Melbourne" not in x_majetek and "Melbourne" not in y_majetek:
                        if y_money - melbourne.kupni_cena >= 0:
                              y_money -= melbourne.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg19 += 20
                                      y_majetek.append("Melbourne")
                              else:
                                  y_majetek.append("Melbourne")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajeteky = fontmest.render(f"Koupil jste si {melbourne.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg19 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p12w1,p12w2) and d in range(p19h1,p19h2) and melbourne.navsteva != 2400 and pressed_space == True and "Melbourne" not in x_majetek and "Melbourne" in y_majetek:
                        if y_money - melbourne.domecek >= 0:
                              y_money -= melbourne.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              melbourne.navsteva = melbourne.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {melbourne.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p19h1,p19h2)and pressed_space == True and "Melbourne" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p12w1,p12w2) and d in range(p19h1,p19h2) and pressed_space == True and "Melbourne" in x_majetek and "Melbourne" not in y_majetek and melbourne.navsteva != 2400:
                              if y_money - 4800 >= 0:
                                  y_money -= 4800
                                  x_money += 4800
                                  hg19 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg19 += 20
                                          y_majetek.append("Melbourne")
                                          x_majetek.remove("Melbourne")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Melbourne")
                                      x_majetek.remove("Melbourne")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {melbourne.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg19 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p19h1,p19h2) and pressed_space == True and "Melbourne" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {melbourne.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {melbourne.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= melbourne.navsteva
                               x_money += melbourne.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)              
        


            #pole20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p12w1,p12w2) and d in range(p20h1,p20h2):
                        if "Sydney" in x_majetek and "Sydney" not in y_majetek and sydney.navsteva != 2400:
                           texta = fontmest.render(f"Vlastníkem města {sydney.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Sydney" in x_majetek and "Sydney" not in y_majetek and sydney.navsteva == 2400:
                           texta = fontmest.render(f"Vlastníkem města {sydney.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {sydney.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= sydney.navsteva
                           x_money += sydney.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Sydney" not in x_majetek and "Sydney" not in y_majetek:
                           sydney = mesta("Sydney", 3200, 1050, 1280, 2400, "prozatím nikdo")
                           sydney.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Sydney" in y_majetek and sydney.navsteva != 2400:
                           sydney.upgrade()
                           pygame.event.wait(240)
                        elif "Sydney" in y_majetek and sydney.navsteva == 2400:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p20h1,p20h2) and pressed_space == True and "Sydney" not in x_majetek and "Sydney" not in y_majetek:
                        if y_money - sydney.kupni_cena >= 0:
                              y_money -= sydney.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg20 += 20
                                      y_majetek.append("Sydney")
                              else:
                                  y_majetek.append("Sydney")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {sydney.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              #hg20 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p12w1,p12w2) and d in range(p20h1,p20h2) and sydney.navsteva != 2400 and pressed_space == True and "Sydney" not in x_majetek and "Sydney" in y_majetek:
                        if y_money - sydney.domecek >= 0:
                              y_money -= sydney.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              sydney.navsteva = sydney.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {sydney.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p20h1,p20h2)and pressed_space == True and "Sydney" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p12w1,p12w2) and d in range(p20h1,p20h2) and pressed_space == True and "Sydney" in x_majetek and "Sydney" not in y_majetek and sydney.navsteva != 2400:
                              if y_money - 4800 >= 0:
                                  y_money -= 4800
                                  x_money += 4800
                                  hg20 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg20 += 20
                                          y_majetek.append("Sydney")
                                          x_majetek.remove("Sydney")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Sydney")
                                      x_majetek.remove("Sydney")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {sydney.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg20 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p12w1,p12w2) and d in range(p20h1,p20h2) and pressed_space == True and "Sydney" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {sydney.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {sydney.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= sydney.navsteva
                               x_money += sydney.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)             


            #pole21
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p12w1,p12w2) and d in range(p21h1,p21h2):
                        textlet = fontmest.render(f"Výtejte na letišti", True, (redb))
                        textlet1 = fontmest.render(f"Pokud zaplatíte 2500{znacka_meny}, můžete se posunout na jakékoliv políčko", True, (redb))
                        textlet2 = fontmest.render(f"Při průchodu startem si nesmíte vybrat peníze!", True, (redb))
                        textlet3 = fontmest.render(f"Stiskněte číslo 1 pro platbu letenky", True, (redb))
                        surface.blit(textlet, (960,600))
                        surface.blit(textlet1, (960,620))
                        surface.blit(textlet2, (960,640))
                        surface.blit(textlet3, (960,660))
                        pygame.event.wait(240)
                if event.key == pygame.K_KP1 and c in range(p12w1,p12w2) and d in range(p21h1,p21h2)and pressed_space == True:
                              y_money -= 2500
                              textleti = fontmest.render(f"Už můžete vyletět!", True, (redb))
                              surface.blit(textleti, (960,600))
                              pygame.event.wait(240)
            
            #pole22 p22w1 = 116 p22w2 = 164 p22h1 = 0 p22h2 = 100
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p22w1,p22w2) and d in range(p22h1,p22h2):
                        if "San Francisco" in x_majetek and "San Francisco" not in y_majetek and san.navsteva != 2800:
                           texta = fontmest.render(f"Vlastníkem města {san.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "San Francisco" in x_majetek and "San Francisco" not in y_majetek and san.navsteva == 2800:
                           texta = fontmest.render(f"Vlastníkem města {san.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {san.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= san.navsteva
                           x_money += san.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "San Francisco" not in x_majetek and "San Francisco" not in y_majetek:
                           san = mesta("San Francisco", 3800, 1350, 1520, 2800, "prozatím nikdo")
                           san.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "San Francisco" in y_majetek and san.navsteva != 2800:
                           san.upgrade()
                           pygame.event.wait(240)
                        elif "San Francisco" in y_majetek and san.navsteva == 2800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p22w1,p22w2) and d in range(p22h1,p22h2) and pressed_space == True and "San Francisco" not in x_majetek and "San Francisco" not in y_majetek:
                        if y_money - san.kupni_cena >= 0:
                              y_money -= san.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg22 += 20
                                      y_majetek.append("San Francisco")
                              else:
                                  y_majetek.append("San Francisco")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajeteky = fontmest.render(f"Koupil jste si {san.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg22 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                    
                if event.key == pygame.K_KP2 and c in range(p22w1,p22w2) and d in range(p22h1,p22h2) and san.navsteva != 2800 and pressed_space == True and "San Francisco" not in x_majetek and "San Francisco" in y_majetek:
                        if y_money - san.domecek >= 0:
                              y_money -= san.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              san.navsteva = san.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {san.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                        

                if event.key == pygame.K_KP0 and c in range(p22w1,p22w2) and d in range(p22h1,p22h2)and pressed_space == True and "San Francisco" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p22w1,p22w2) and d in range(p22h1,p22h2) and pressed_space == True and "San Francisco" in x_majetek and "San Francisco" not in y_majetek and san.navsteva != 2800:
                              if y_money - 5700 >= 0:
                                  y_money -= 5700
                                  x_money += 5700
                                  hg22 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg22 += 20
                                          y_majetek.append("San Francisco")
                                          x_majetek.remove("San Francisco")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("San Francisco")
                                      x_majetek.remove("San Francisco")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {san.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg22 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p22w1,p22w2) and d in range(p22h1,p22h2) and pressed_space == True and "San Francisco" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {san.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {san.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= san.navsteva
                               x_money += san.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)   
            #pole23
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p23w1,p23w2) and d in range(p22h1,p22h2) and lol == 1:
                        if hrac_na_rade == y and lol == 1:
                                rs = random.randint(1,10)
                                if rs == 1:
                                    texts1 = fontfs.render(f"Jděte na nejbližší volné město", True, (redb))
                                    surface.blit(texts1, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 2:
                                    texts2 = fontfs.render(f"Jděte na pole s letištěm", True, (redb))
                                    surface.blit(texts2, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 3:
                                    texts3 = fontfs.render(f"Jděte do vězení!", True, (redb))
                                    surface.blit(texts3, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 4:
                                    texts4 = fontfs.render(f"Jděte na vaše nejbližší město", True, (redb))
                                    surface.blit(texts4, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 5:
                                    texts5 = fontfs.render(f"Jděte na nejbližší město vašeho spoluhráče", True, (redb))
                                    surface.blit(texts5, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 6:
                                    texts6 = fontfs.render(f"Jděte na start", True, (redb))
                                    surface.blit(texts6, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 7:
                                    texts7 = fontfs.render(f"Jděte na pole s letištěm", True, (redb))
                                    surface.blit(texts7, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 8:
                                    texts8 = fontfs.render(f"Jděte na emisní povolenku", True, (redb))
                                    surface.blit(texts8, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 9:
                                    vpred = random.randint(1,10)
                                    if vpred == 1:
                                        texts91 = fontfs.render(f"Jděte vpřed o {vpred} políčko", True, (redb))
                                        surface.blit(texts91, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 2 or vpred == 3 or vpred == 4:
                                        texts92 = fontfs.render(f"Jděte vpřed o {vpred} políčka", True, (redb))
                                        surface.blit(texts92, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 5 or vpred == 6 or vpred == 7 or vpred == 8 or vpred == 9 or vpred == 10:
                                        texts93 = fontfs.render(f"Jděte vpřed o {vpred} políček", True, (redb))
                                        surface.blit(texts93, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
                                if rs == 10:
                                    dozadu = random.randint(1,10)
                                    if dozadu == 1:
                                        texts101 = fontfs.render(f"Jděte dozadu o {dozadu} políčko", True, (redb))
                                        surface.blit(texts101, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 2 or dozadu == 3 or dozadu == 4:
                                        texts102 = fontfs.render(f"Jděte dozadu o {dozadu} políčka", True, (redb))
                                        surface.blit(texts102, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 5 or dozadu == 6 or dozadu == 7 or dozadu == 8 or dozadu == 9 or dozadu == 10:
                                        texts103 = fontfs.render(f"Jděte dozadu o {dozadu} políček", True, (redb))
                                        surface.blit(texts103, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
            #pole24
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p24w1,p24w2) and d in range(p22h1,p22h2):
                        if "Los Angeles" in x_majetek and "Los Angeles" not in y_majetek and los.navsteva != 3500:
                           texta = fontmest.render(f"Vlastníkem města {los.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Los Angeles" in x_majetek and "Los Angeles" not in y_majetek and los.navsteva == 3500:
                           texta = fontmest.render(f"Vlastníkem města {los.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {los.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= los.navsteva
                           x_money += los.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Los Angeles" not in x_majetek and "Los Angeles" not in y_majetek:
                           los = mesta("Los Angeles", 4400, 1650, 1760, 3500, "prozatím nikdo")
                           los.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Los Angeles" in y_majetek and los.navsteva != 3500:
                           los.upgrade()
                           pygame.event.wait(240)
                        elif "Los Angeles" in y_majetek and los.navsteva == 3500:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p24w1,p24w2) and d in range(p22h1,p22h2) and pressed_space == True and "Los Angeles" not in x_majetek and "Los Angeles" not in y_majetek:
                        if y_money - los.kupni_cena >= 0:
                              y_money -= los.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg24 += 20
                                      y_majetek.append("Los Angeles")
                              else:
                                  y_majetek.append("Los Angeles")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajeteky = fontmest.render(f"Koupil jste si {los.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg24 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p24w1,p24w2) and d in range(p22h1,p22h2) and los.navsteva != 3500 and pressed_space == True and "Los Angeles" not in x_majetek and "Los Angeles" in y_majetek:
                        if y_money - los.domecek >= 0:
                              y_money -= los.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              los.navsteva = los.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {los.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p24w1,p24w2) and d in range(p22h1,p22h2)and pressed_space == True and "Los Angeles" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p24w1,p24w2) and d in range(p22h1,p22h2) and pressed_space == True and "Los Angeles" in x_majetek and "Los Angeles" not in y_majetek and los.navsteva != 3500:
                              if y_money - 6600 >= 0:
                                  y_money -= 6600
                                  x_money += 6600
                                  hg24 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg24 += 20
                                          y_majetek.append("Los Angeles")
                                          x_majetek.remove("Los Angeles")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Los Angeles")
                                      x_majetek.remove("Los Angeles")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {los.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg24 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p24w1,p24w2) and d in range(p22h1,p22h2) and pressed_space == True and "Los Angeles" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {los.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {los.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= los.navsteva
                               x_money += los.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)          


            #pole25
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p25w1,p25w2) and d in range(p22h1,p22h2):
                        if "New York" in x_majetek and "New York" not in y_majetek and new.navsteva != 3500:
                           texta = fontmest.render(f"Vlastníkem města {new.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "New York" in x_majetek and "New York" not in y_majetek and new.navsteva == 3500:
                           texta = fontmest.render(f"Vlastníkem města {new.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {new.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= new.navsteva
                           x_money += new.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "New York" not in x_majetek and "New York" not in y_majetek:
                           new = mesta("New York", 4400, 1650, 1760, 3500, "prozatím nikdo")
                           new.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "New York" in y_majetek and new.navsteva != 3500:
                           new.upgrade()
                           pygame.event.wait(240)
                        elif "New York" in y_majetek and new.navsteva == 3500:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p25w1,p25w2) and d in range(p22h1,p22h2) and pressed_space == True and "New York" not in x_majetek and "New York" not in y_majetek:
                        if y_money - new.kupni_cena >= 0:
                              y_money -= new.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg25 += 20
                                      y_majetek.append("New York")
                              else:
                                  y_majetek.append("New York")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajeteky = fontmest.render(f"Koupil jste si {new.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg25 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p25w1,p25w2) and d in range(p22h1,p22h2) and new.navsteva != 3500 and pressed_space == True and "New York" not in x_majetek and "New York" in y_majetek:
                        if y_money - new.domecek >= 0:
                              y_money -= new.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              new.navsteva = new.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {new.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p25w1,p25w2) and d in range(p22h1,p22h2)and pressed_space == True and "New York" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p25w1,p25w2) and d in range(p22h1,p22h2) and pressed_space == True and "New York" in x_majetek and "New York" not in y_majetek and new.navsteva != 3500:
                              if y_money - 6600 >= 0:
                                  y_money -= 6600
                                  x_money += 6600
                                  hg25 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg25 += 20
                                          y_majetek.append("New York")
                                          x_majetek.remove("New York")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("New York")
                                      x_majetek.remove("New York")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {new.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg25 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p25w1,p25w2) and d in range(p22h1,p22h2) and pressed_space == True and "New York" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {new.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {new.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= new.navsteva
                               x_money += new.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)                


            #pole26
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p26w1,p26w2) and d in range(p22h1,p22h2):
                        if "Hawaii" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek and "Srí Lanka" not in x_majetek:
                            texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 1.", True, (redb))
                            surface.blit(texta, (960,600))
                            textb = fontmest.render(f"Musíte zaplatit {hawaii.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                            surface.blit(textb, (960,620))
                            y_money -= hawaii.navsteva
                            x_money += hawaii.navsteva
                            textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                            surface.blit(textmoneyx, (960,640))
                            textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                            surface.blit(textmoneyy, (960,660))
                            pygame.event.wait(240)  
                        if "Hawaii" in x_majetek and "Bali" in x_majetek and "Maledivy" not in x_majetek and "Srí Lanka" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Hawaii" in x_majetek and "Maledivy" in x_majetek and "Bali" not in x_majetek and "Srí Lanka" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Hawaii" in x_majetek and "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)                               
                        if "Hawaii" in x_majetek and "Bali" in x_majetek and "Maledivy" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {hawaii.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)     
                             
                        if "Hawaii" in x_majetek and "Bali" in x_majetek and "Srí Lanka" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Hawaii" in x_majetek and "Maledivy" in x_majetek and "Srí Lanka" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {maledivy.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Hawaii" not in x_majetek and "Hawaii" not in y_majetek:
                           hawaii = mesta("Hawaii", 4000, 1000, 0, 0, "prozatím nikdo")
                           hawaii.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        if "Hawaii" in y_majetek:
                           textmas = fontmest.render("Jste vlastníkem tohoto města", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                        #if "Hawaii" in y_majetek and "Srí Lanka" in y_majetek and "Bali" in y_majetek and "Maledivy" in y_majetek:
                            #textvyhra = fontmest.render("Vyhrál jste hru!", True, (red))
                            #surface.blit(textvyhra, (960,600))
                            #pygame.event.wait(240)

                if event.key == pygame.K_KP1 and c in range(p26w1,p26w2) and d in range(p22h1,p22h2) and pressed_space == True and "Hawaii" not in x_majetek and "Hawaii" not in y_majetek:
                        if y_money - hawaii.kupni_cena >= 0:
                              y_money -= hawaii.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg26 += 20
                                      y_majetek.append("Hawaii")
                              else:
                                  y_majetek.append("Hawaii")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {hawaii.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                
                if event.key == pygame.K_KP0 and c in range(p26w1,p26w2) and d in range(p22h1,p22h2) and pressed_space == True:
                              hrac_na_rade = x
                              pressed_space = False
            #pole27
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p27w1,p27w2) and d in range(p22h1,p22h2):
                        if "Bangkok" in x_majetek and "Bangkok" not in y_majetek and bangkok.navsteva != 3800:
                           texta = fontmest.render(f"Vlastníkem města {bangkok.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Bangkok" in x_majetek and "Bangkok" not in y_majetek and bangkok.navsteva == 3800:
                           texta = fontmest.render(f"Vlastníkem města {bangkok.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {bangkok.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= bangkok.navsteva
                           x_money += bangkok.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Bangkok" not in x_majetek and "Bangkok" not in y_majetek:
                           bangkok = mesta("Bangkok", 5000, 2000, 2000, 3800, "prozatím nikdo")
                           bangkok.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Bangkok" in y_majetek and bangkok.navsteva != 3800:
                           bangkok.upgrade()
                           pygame.event.wait(240)
                        elif "Bangkok" in y_majetek and bangkok.navsteva == 3800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p27w1,p27w2) and d in range(p22h1,p22h2) and pressed_space == True and "Bangkok" not in x_majetek and "Bangkok" not in y_majetek:
                        if y_money - bangkok.kupni_cena >= 0:
                              y_money -= bangkok.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg27 += 20
                                      y_majetek.append("Bangkok")
                              else:
                                  y_majetek.append("Bangkok")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajeteky = fontmest.render(f"Koupil jste si {bangkok.jmeno}", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              #hg27 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240) 
                if event.key == pygame.K_KP2 and c in range(p27w1,p27w2) and d in range(p22h1,p22h2) and bangkok.navsteva != 3800 and pressed_space == True and "Bangkok" not in x_majetek and "Bangkok" in y_majetek:
                        if y_money - bangkok.domecek >= 0:
                              y_money -= bangkok.domecek
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,600))
                              bangkok.navsteva = bangkok.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {bangkok.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)       
                if event.key == pygame.K_KP0 and c in range(p27w1,p27w2) and d in range(p22h1,p22h2)and pressed_space == True and "Bangkok" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p27w1,p27w2) and d in range(p22h1,p22h2) and pressed_space == True and "Bangkok" in x_majetek and "Bangkok" not in y_majetek and bangkok.navsteva != 3800:
                              if y_money - 7500 >= 0:
                                  y_money -= 7500
                                  x_money += 7500
                                  hg27 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg27 += 20
                                          y_majetek.append("Bangkok")
                                          x_majetek.remove("Bangkok")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Bangkok")
                                      x_majetek.remove("Bangkok")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {bangkok.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg27 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p27w1,p27w2) and d in range(p22h1,p22h2) and pressed_space == True and "Bangkok" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {bangkok.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {bangkok.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= bangkok.navsteva
                               x_money += bangkok.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)                
        


            #pole28
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p28w1,p28w2) and d in range(p22h1,p22h2):
                        if "Šanghaj" in x_majetek and "Šanghaj" not in y_majetek and šanghaj.navsteva != 3800:
                           texta = fontmest.render(f"Vlastníkem města {šanghaj.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Šanghaj" in x_majetek and "Šanghaj" not in y_majetek and šanghaj.navsteva == 3800:
                           texta = fontmest.render(f"Vlastníkem města {šanghaj.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {šanghaj.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= šanghaj.navsteva
                           x_money += šanghaj.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Šanghaj" not in x_majetek and "Šanghaj" not in y_majetek:
                           šanghaj = mesta("Šanghaj", 5000, 2000, 2000, 3800, "prozatím nikdo")
                           šanghaj.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Šanghaj" in y_majetek and šanghaj.navsteva != 3800:
                           šanghaj.upgrade()
                           pygame.event.wait(240)
                        elif "Šanghaj" in y_majetek and šanghaj.navsteva == 3800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p28w1,p28w2) and d in range(p22h1,p22h2) and pressed_space == True and "Šanghaj" not in x_majetek and "Šanghaj" not in y_majetek:
                        if y_money - šanghaj.kupni_cena >= 0:
                              y_money -= šanghaj.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg28 += 20
                                      y_majetek.append("Šanghaj")
                              else:
                                  y_majetek.append("Šanghaj")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {šanghaj.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              #hg28 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240) 
                if event.key == pygame.K_KP2 and c in range(p28w1,p28w2) and d in range(p22h1,p22h2) and šanghaj.navsteva != 3800 and pressed_space == True and "Šanghaj" not in x_majetek and "Šanghaj" in y_majetek:
                        if y_money - šanghaj.domecek >= 0:
                              y_money -= šanghaj.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              šanghaj.navsteva = šanghaj.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {šanghaj.navsteva}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)       
                if event.key == pygame.K_KP0 and c in range(p28w1,p28w2) and d in range(p22h1,p22h2)and pressed_space == True and "Šanghaj" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p28w1,p28w2) and d in range(p22h1,p22h2) and pressed_space == True and "Šanghaj" in x_majetek and "Šanghaj" not in y_majetek and šanghaj.navsteva != 3800:
                              if y_money - 7500 >= 0:
                                  y_money -= 7500
                                  x_money += 7500
                                  hg28 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg28 += 20
                                          y_majetek.append("Šanghaj")
                                          x_majetek.remove("Šanghaj")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Šanghaj")
                                      x_majetek.remove("Šanghaj")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {šanghaj.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg28 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p28w1,p28w2) and d in range(p22h1,p22h2) and pressed_space == True and "Šanghaj" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {šanghaj.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {šanghaj.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= šanghaj.navsteva
                               x_money += šanghaj.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)                    


            #pole29
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p29w1,p29w2) and d in range(p22h1,p22h2):
                        textemise = fontmest.render(f"Za každé město, které vlastníte, musíte zaplatit 500{znacka_meny}", True, (redb))
                        surface.blit(textemise, (960,600))
                        delkaxmajetek = len(y_majetek)
                        cenadelky = delkaxmajetek*500
                        y_money -= cenadelky
                        textemise1 = fontmest.render(f"Musíte zaplatit {cenadelky}{znacka_meny}", True, (redb))
                        surface.blit(textemise1, (960,620))
                        pygame.event.wait(240)
            #pole30
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p30w1,p30w2) and d in range(p22h1,p22h2):
                        if "Tokio" in x_majetek and "Tokio" not in y_majetek and tokio.navsteva != 4500:
                           texta = fontmest.render(f"Vlastníkem města {tokio.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Tokio" in x_majetek and "Tokio" not in y_majetek and tokio.navsteva == 4500:
                           texta = fontmest.render(f"Vlastníkem města {tokio.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {tokio.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= tokio.navsteva
                           x_money += tokio.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Tokio" not in x_majetek and "Tokio" not in y_majetek:
                           tokio = mesta("Tokio", 5700, 2350, 2280, 4500, "prozatím nikdo")
                           tokio.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Tokio" in x_majetek and tokio.navsteva != 4500:
                           tokio.upgrade()
                           pygame.event.wait(240)
                        elif "Tokio" in x_majetek and tokio.navsteva == 4500:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p30w1,p30w2) and d in range(p22h1,p22h2) and pressed_space == True and "Tokio" not in x_majetek and "Tokio" not in y_majetek:
                        if y_money - tokio.kupni_cena >= 0:
                              y_money -= tokio.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg30 += 20
                                      y_majetek.append("Tokio")
                              else:
                                  y_majetek.append("Tokio")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {tokio.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              #hg30 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p30w1,p30w2) and d in range(p22h1,p22h2) and tokio.navsteva != 4500 and pressed_space == True and "Tokio" not in x_majetek and "Tokio" in y_majetek:
                        if y_money - tokio.domecek >= 0:
                              y_money -= tokio.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              tokio.navsteva = tokio.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {tokio.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p30w1,p30w2) and d in range(p22h1,p22h2)and pressed_space == True and "Tokio" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p30w1,p30w2) and d in range(p22h1,p22h2) and pressed_space == True and "Tokio" in x_majetek and "Tokio" not in y_majetek and tokio.navsteva != 4500:
                              if y_money - 8550 >= 0:
                                  y_money -= 8550
                                  x_money += 8550
                                  hg30 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg30 += 20
                                          y_majetek.append("Tokio")
                                          x_majetek.remove("Tokio")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Tokio")
                                      x_majetek.remove("Tokio")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {tokio.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg30 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p30w1,p30w2) and d in range(p22h1,p22h2) and pressed_space == True and "Tokio" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {tokio.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {tokio.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= tokio.navsteva
                               x_money += tokio.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)                  


            #pole31
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p31w1,p31w2) and d in range(p22h1,p22h2):
                        textvez = fontmest.render(f"Posuňtě se na políčko vězení!", True, (redb))
                        surface.blit(textvez, (960,600))
                        pygame.event.wait(240)
            #pole32 p32w1 = 820 p32w1 = 950 p32h1 = 116 p32h2 = 164
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p32w1,p32w2) and d in range(p32h1,p32h2):
                        if "Praha" in x_majetek and "Praha" not in y_majetek and praha.navsteva != 5100:
                           texta = fontmest.render(f"Vlastníkem města {praha.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Praha" in x_majetek and "Praha" not in y_majetek and praha.navsteva == 5100:
                           texta = fontmest.render(f"Vlastníkem města {praha.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {praha.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= praha.navsteva
                           x_money += praha.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Praha" not in x_majetek and "Praha" not in y_majetek:
                           praha = mesta("Praha", 6800, 3000, 2720, 5100, "prozatím nikdo")
                           praha.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Praha" in y_majetek and praha.navsteva != 5100:
                           praha.upgrade()
                           pygame.event.wait(240)
                        elif "Praha" in y_majetek and praha.navsteva == 5100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p32w1,p32w2) and d in range(p32h1,p32h2) and pressed_space == True and "Praha" not in x_majetek and  "Praha" not in y_majetek:
                        if y_money - praha.kupni_cena >= 0:
                              y_money -= praha.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg32 += 20
                                      y_majetek.append("Praha")
                              else:
                                  y_majetek.append("Praha")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {praha.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              #hg32 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                if event.key == pygame.K_KP2 and c in range(p32w1,p32w2) and d in range(p32h1,p32h2) and praha.navsteva != 5100 and pressed_space == True and "Praha" not in x_majetek and "Praha" in y_majetek:
                        if y_money - praha.domecek >= 0:
                              y_money -= praha.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              praha.navsteva = praha.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {praha.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)      
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p32h1,p32h2)and pressed_space == True and "Praha" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p32w1,p32w2) and d in range(p32h1,p32h2) and pressed_space == True and "Praha" in x_majetek and "Praha" not in y_majetek and praha.navsteva != 5100:
                              if y_money - 10200 >= 0:
                                  y_money -= 10200
                                  x_money += 10200
                                  hg32 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg32 += 20
                                          y_majetek.append("Praha")
                                          x_majetek.remove("Praha")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Praha")
                                      x_majetek.remove("Praha")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {praha.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg32 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p32h1,p32h2) and pressed_space == True and "Praha" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {praha.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {praha.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= praha.navsteva
                               x_money += praha.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)              


            #pole33
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p32w1,p32w2) and d in range(p33h1,p33h2):
                        if "Londýn" in x_majetek and "Londýn" not in y_majetek and londyn.navsteva != 5100:
                           texta = fontmest.render(f"Vlastníkem města {londyn.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Londýn" in x_majetek and "Londýn" not in y_majetek and londyn.navsteva == 5100:
                           texta = fontmest.render(f"Vlastníkem města {londyn.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {londyn.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= londyn.navsteva
                           x_money += londyn.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Londýn" not in x_majetek and "Londýn" not in y_majetek:
                           londyn = mesta("Londýn", 6800, 3000, 2720, 5100, "prozatím nikdo")
                           londyn.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Londýn" in y_majetek and londyn.navsteva != 5100:
                           londyn.upgrade()
                           pygame.event.wait(240)
                        elif "Londýn" in y_majetek and londyn.navsteva == 5100:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p32w1,p32w2) and d in range(p33h1,p33h2) and pressed_space == True and "Londýn" not in x_majetek and "Londýn" not in y_majetek:
                        if y_money - londyn.kupni_cena >= 0:
                              y_money -= londyn.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg33 += 20
                                      y_majetek.append("Londýn")
                              else: 
                                  y_majetek.append("Londýn")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {londyn.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              #hg33 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)    
                if event.key == pygame.K_KP2 and c in range(p32w1,p32w2) and d in range(p33h1,p33h2) and londyn.navsteva != 5100 and pressed_space == True and "Londýn" not in x_majetek and "Londýn" in y_majetek:
                        if y_money - londyn.domecek >= 0:
                              y_money -= londyn.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              londyn.navsteva = londyn.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {londyn.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)          
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p33h1,p33h2)and pressed_space == True and "Londýn" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p32w1,p32w2) and d in range(p33h1,p33h2) and pressed_space == True and "Londýn" in x_majetek and "Londýn" not in y_majetek and londyn.navsteva != 5100:
                              if y_money - 10200 >= 0:
                                  y_money -= 10200
                                  x_money += 10200
                                  hg33 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg33 += 20
                                          y_majetek.append("Londýn")
                                          x_majetek.remove("Londýn")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Londýn")
                                      x_majetek.remove("Londýn")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {londyn.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg33 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p33h1,p33h2) and pressed_space == True and "Londýn" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {londyn.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {londyn.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= londyn.navsteva
                               x_money += londyn.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)         

            

            #pole34
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                    
                    if c in range(p32w1,p32w2) and d in range(p34h1,p34h2) and lol == 1:
                        if hrac_na_rade == y and lol == 1:
                            rf = random.randint(1,8)
                            if rf == 1:
                                y_money += 3500
                                textf1 = fontfs.render(f"Omylem vám přišlo na účet 3500{znacka_meny}", True, (redb))
                                surface.blit(textf1, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 2:
                                y_money += 3000
                                x_money -= 3000
                                textf2 = fontfs.render(f"Spoluhráč ti musí dát 3000{znacka_meny}", True, (redb))
                                surface.blit(textf2, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 3:
                                y_money += 1500
                                textf3 = fontfs.render(f"Ve tvém městě probíhal festival.", True, (redb))
                                textf31 = fontfs.render(f"Vydělal jsi 1500 {znacka_meny}", True, (redb))
                                surface.blit(textf3, (960,600))
                                surface.blit(textf31, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 4:
                                textf4 = fontfs.render(f"Je léto a všichni chtějí k moři.", True, (redb))
                                textf41 = fontfs.render(f"Za každý svůj rezort získáváš 1000{znacka_meny}", True, (redb))
                                surface.blit(textf4, (960,600))
                                surface.blit(textf41, (960,620))
                                if "Maledivy" not in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    textf42 = fontfs.render(f"Nevlastníte žádný rezort.", True, (redb))
                                    surface.blit(textf42, (960,640))
                                if "Maledivy" in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek: 
                                    y_money += 1000
                                if "Bali" in y_majetek and "Maledivy" not in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 1000
                                if "Hawaii" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 1000
                                if "Srí Lanka" in y_majetek and "Bali" not in y_majetek and "Hawaii" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 1000
                                if "Maledivy" in y_majetek and "Bali" in y_majetek and "Hawaii" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Hawaii" in y_majetek and "Bali" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" not in y_majetek and "Bali" not in y_majetek:
                                    y_money += 2000
                                if "Bali" in y_majetek and "Hawaii" in y_majetek and "Maledivy" not in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 2000
                                if "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 2000
                                if "Hawaii" in y_majetek and "Srí Lanka" in y_majetek and "Bali" not in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 2000
                                if "Maledivy" in y_majetek and "Bali" in y_majetek and "Hawaii" in y_majetek and "Srí Lanka" not in y_majetek:
                                    y_money += 3000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Bali" in y_majetek and "Hawaii" not in y_majetek:
                                    y_money += 3000
                                if "Maledivy" in y_majetek and "Srí Lanka" in y_majetek and "Hawaii" in y_majetek and "Bali" not in y_majetek:
                                    y_money += 3000
                                if "Hawaii" in y_majetek and "Bali" in y_majetek and "Srí Lanka" in y_majetek and "Maledivy" not in y_majetek:
                                    y_money += 3000
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 5:
                                y_money += 5000
                                textf5 = fontfs.render(f"Tvé město se ocitlo v top 10 nejhezčích měst.", True, (redb))
                                textf51 = fontfs.render(f"Všichni ho nyní navštěvují... vydělalo vám to 5000{znacka_meny}", True, (redb))
                                surface.blit(textf5, (960,600))
                                surface.blit(textf51, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 6:
                                y_money -= 1000
                                textf6 = fontfs.render(f"Ve vašem městě vypadla elektřina.", True, (redb))
                                textf61 = fontfs.render (f"Zaplatite 1000{znacka_meny} za opravu elektrarny", True, (redb))
                                surface.blit(textf6, (960,600))
                                surface.blit(textf61, (960,620))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 7:
                                y_money -= 3000
                                textf7 = fontfs.render(f"Proběhlo zemětřesení, za opravy zaplatíš 3000{znacka_meny}", True, (redb))
                                surface.blit(textf7, (960,600))
                                pygame.event.wait(240)
                                lol = 0
                            if rf == 8:
                                y_money -= 3500
                                textf8 = fontfs.render(f"V jednom z vašich měst se rozšířila epidemie.", True, (redb))
                                textf81 = fontfs.render(f"Pošlete 3500{znacka_meny} na pomoc lidem", True, (redb))
                                surface.blit(textf8, (960,600))
                                surface.blit(textf81, (960,620))
                                pygame.event.wait(240)
                                lol = 0
            #pole35
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p32w1,p32w2) and d in range(p35h1,p35h2):
                        if "Paříž" in x_majetek and "Paříž" not in y_majetek and pariz.navsteva != 5800:
                           texta = fontmest.render(f"Vlastníkem města {pariz.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Paříž" in x_majetek and "Paříž" not in y_majetek and pariz.navsteva == 5800:
                           texta = fontmest.render(f"Vlastníkem města {pariz.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {pariz.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= pariz.navsteva
                           x_money += pariz.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Paříž" not in x_majetek and "Paříž" not in y_majetek:
                           pariz = mesta("Paříž", 7500, 3400, 3000, 5800, "prozatím nikdo")
                           pariz.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Paříž" in y_majetek and pariz.navsteva != 5800:
                           pariz.upgrade()
                           pygame.event.wait(240)
                        elif "Paříž" in y_majetek and pariz.navsteva == 5800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p32w1,p32w2) and d in range(p35h1,p35h2) and pressed_space == True and "Paříž" not in x_majetek and "Paříž" not in y_majetek:
                        if y_money - pariz.kupni_cena >= 0:
                              y_money -= pariz.kupni_cena
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(x_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg35 += 20
                                      y_majetek.append("Paříž")
                              else: 
                                  y_majetek.append("Paříž")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {pariz.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              #hg35 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)  
                if event.key == pygame.K_KP2 and c in range(p32w1,p32w2) and d in range(p35h1,p35h2) and pariz.navsteva != 5800 and pressed_space == True and "Paříž" not in x_majetek and "Paříž" in y_majetek:
                        if y_money - pariz.domecek >= 0:
                              y_money -= pariz.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              pariz.navsteva = pariz.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {pariz.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)        
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p35h1,p35h2)and pressed_space == True and "Paříž" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p32w1,p32w2) and d in range(p35h1,p35h2) and pressed_space == True and "Paříž" in x_majetek and "Paříž" not in y_majetek and pariz.navsteva != 5800:
                              if y_money - 11250 >= 0:
                                  y_money -= 11250
                                  x_money += 11250
                                  hg35 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg35 += 20
                                          y_majetek.append("Paříž")
                                          x_majetek.remove("Paříž")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Paříž")
                                      x_majetek.remove("Paříž")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {pariz.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg35 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p35h1,p35h2) and pressed_space == True and "Paříž" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {pariz.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {pariz.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= pariz.navsteva
                               x_money += pariz.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)                 

            

            #pole36
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p32w1,p32w2) and d in range(p36h1,p36h2):
                        if "Srí Lanka" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek and "Hawaii" not in x_majetek:
                            texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 1.", True, (redb))
                            surface.blit(texta, (960,600))
                            textb = fontmest.render(f"Musíte zaplatit {sri.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                            surface.blit(textb, (960,620))
                            y_money -= sri.navsteva
                            x_money += sri.navsteva
                            textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                            surface.blit(textmoneyx, (960,640))
                            textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                            surface.blit(textmoneyy, (960,660))
                            pygame.event.wait(240)  
                        if "Srí Lanka" in x_majetek and "Bali" in x_majetek and "Maledivy" not in x_majetek and "Hawaii" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Srí Lanka" in x_majetek and "Maledivy" in x_majetek and "Bali" not in x_majetek and "Hawaii" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Srí Lanka" in x_majetek and "Hawaii" in x_majetek and "Bali" not in x_majetek and "Maledivy" not in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 2000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 2000
                                x_money += 2000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)                               
                        if "Srí Lanka" in x_majetek and "Bali" in x_majetek and "Maledivy" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)     
                             
                        if "Srí Lanka" in x_majetek and "Bali" in x_majetek and "Hawaii" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Srí Lanka" in x_majetek and "Maledivy" in x_majetek and "Hawaii" in x_majetek:
                                texta = fontmest.render(f"Vlastníkem města {sri.jmeno} je Hráč 1.", True, (redb))
                                surface.blit(texta, (960,600))
                                textb = fontmest.render(f"Musíte zaplatit 3000 {znacka_meny} za návštěvu města", True, (redb))
                                surface.blit(textb, (960,620))
                                y_money -= 3000
                                x_money += 3000
                                textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyx, (960,640))
                                textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                                surface.blit(textmoneyy, (960,660))
                                pygame.event.wait(240)
                        if "Srí Lanka" not in x_majetek and "Srí Lanka" not in y_majetek:
                           sri = mesta("Srí Lanka", 4000, 1000, 0, 0, "prozatím nikdo")
                           sri.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        if "Srí Lanka" in y_majetek:
                           textmas = fontmest.render("Jste vlastníkem tohoto města", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                    
                        #if "Srí Lanka" in y_majetek and "Hawaii" in y_majetek and "Bali" in y_majetek and "Maledivy" in y_majetek:
                            #textvyhra = fontmest.render("Vyhrál jste hru!", True, (red))
                            #surface.blit(textvyhra, (960,600))
                            #pygame.event.wait(240)

                if event.key == pygame.K_KP1 and c in range(p32w1,p32w2) and d in range(p36h1,p36h2) and pressed_space == True and "Srí Lanka" not in x_majetek and "Srí Lanka" not in y_majetek:
                        if y_money - sri.kupni_cena >= 0:
                              y_money -= sri.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg36 += 20
                                      y_majetek.append("Srí Lanka")
                              else:
                                  y_majetek.append("Srí Lanka")
                              #zapsání do majetku
                              #x_majetek.append("Rio de Janeiro")
                              textmajetekx = fontmest.render(f"Koupil jste si {sri.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p36h1,p36h2)and pressed_space == True:
                              hrac_na_rade = x
                              pressed_space = False
            #pole37
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p32w1,p32w2) and d in range(p37h1,p37h2) and lol == 1:
                        if hrac_na_rade == y and lol == 1:
                                rs = random.randint(1,10)
                                if rs == 1:
                                    texts1 = fontfs.render(f"Jděte na nejbližší volné město", True, (redb))
                                    surface.blit(texts1, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 2:
                                    texts2 = fontfs.render(f"Jděte na pole s letištěm", True, (redb))
                                    surface.blit(texts2, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 3:
                                    texts3 = fontfs.render(f"Jděte do vězení!", True, (redb))
                                    surface.blit(texts3, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 4:
                                    texts4 = fontfs.render(f"Jděte na vaše nejbližší město", True, (redb))
                                    surface.blit(texts4, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 5:
                                    texts5 = fontfs.render(f"Jděte na nejbližší město vašeho spoluhráče", True, (redb))
                                    surface.blit(texts5, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 6:
                                    texts6 = fontfs.render(f"Jděte na start", True, (redb))
                                    surface.blit(texts6, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 7:
                                    texts7 = fontfs.render(f"Jděte na pole s letištěm", True, (redb))
                                    surface.blit(texts7, (960,600))
                                    pygame.event.wait(240)
                                    lol = 0
                                if rs == 8:
                                    texts8 = fontfs.render(f"Jděte na emisní povolenku", True, (redb))
                                    surface.blit(texts8, (960,600))
                                    pygame.event.wait(240)
                                if rs == 9:
                                    vpred = random.randint(1,10)
                                    if vpred == 1:
                                        texts91 = fontfs.render(f"Jděte vpřed o {vpred} políčko", True, (redb))
                                        surface.blit(texts91, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 2 or vpred == 3 or vpred == 4:
                                        texts92 = fontfs.render(f"Jděte vpřed o {vpred} políčka", True, (redb))
                                        surface.blit(texts92, (960,600))
                                        pygame.event.wait(240)
                                    if vpred == 5 or vpred == 6 or vpred == 7 or vpred == 8 or vpred == 9 or vpred == 10:
                                        texts93 = fontfs.render(f"Jděte vpřed o {vpred} políček", True, (redb))
                                        surface.blit(texts93, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0
                                if rs == 10:
                                    dozadu = random.randint(1,10)
                                    if dozadu == 1:
                                        texts101 = fontfs.render(f"Jděte dozadu o {dozadu} políčko", True, (redb))
                                        surface.blit(texts101, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 2 or dozadu == 3 or dozadu == 4:
                                        texts102 = fontfs.render(f"Jděte dozadu o {dozadu} políčka", True, (redb))
                                        surface.blit(texts102, (960,600))
                                        pygame.event.wait(240)
                                    if dozadu == 5 or dozadu == 6 or dozadu == 7 or dozadu == 8 or dozadu == 9 or dozadu == 10:
                                        texts103 = fontfs.render(f"Jděte dozadu o {dozadu} políček", True, (redb))
                                        surface.blit(texts103, (960,600))
                                        pygame.event.wait(240)
                                    lol = 0

            #pole38
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p32w1,p32w2) and d in range(p38h1,p38h2):
                        if "Dubai" in x_majetek and "Dubai" not in y_majetek and dubai.navsteva != 6800:
                           texta = fontmest.render(f"Vlastníkem města {dubai.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Dubai" in x_majetek and "Dubai" not in y_majetek and dubai.navsteva == 6800:
                           texta = fontmest.render(f"Vlastníkem města {dubai.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {dubai.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= dubai.navsteva
                           x_money += dubai.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Dubai" not in x_majetek and "Dubai" not in y_majetek:
                           dubai = mesta("Dubai", 9000, 4500, 3600, 6800, "prozatím nikdo")
                           dubai.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Dubai" in y_majetek and dubai.navsteva != 6800:
                           dubai.upgrade()
                           pygame.event.wait(240)
                        elif "Dubai" in y_majetek and dubai.navsteva == 6800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p32w1,p32w2) and d in range(p38h1,p38h2) and pressed_space == True and "Dubai" not in x_majetek and "Dubai" not in y_majetek:
                        if y_money - dubai.kupni_cena >= 0:
                              y_money -= dubai.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg38 += 20
                                      y_majetek.append("Dubai")
                              else: 
                                  y_majetek.append("Dubai")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {dubai.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              #hg38 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)  
                if event.key == pygame.K_KP2 and c in range(p32w1,p32w2) and d in range(p38h1,p38h2) and dubai.navsteva != 6800 and pressed_space == True and "Dubai" not in x_majetek and "Dubai" in y_majetek:
                        if y_money - dubai.domecek >= 0:
                              y_money -= dubai.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              dubai.navsteva = dubai.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {dubai.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)        
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p38h1,p38h2)and pressed_space == True and "Dubai" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p32w1,p32w2) and d in range(p38h1,p38h2) and pressed_space == True and "Dubai" in x_majetek and "Dubai" not in y_majetek and dubai.navsteva != 6800:
                              if y_money - 13500 >= 0:
                                  y_money -= 13500
                                  x_money += 13500
                                  hg38 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg38 += 20
                                          y_majetek.append("Dubai")
                                          x_majetek.remove("Dubai")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Dubai")
                                      x_majetek.remove("Dubai")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {dubai.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg38 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p38h1,p38h2) and pressed_space == True and "Dubai" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {dubai.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {dubai.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= dubai.navsteva
                               x_money += dubai.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)         
            

            #pole39
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True

                    if c in range(p32w1,p32w2) and d in range(p39h1,p39h2):
                        if "Ambasáda" not in x_majetek and "Ambasáda" not in y_majetek:
                            textcelnice = fontmest.render(f"Název města: Ambasáda", True, (redb))
                            surface.blit(textcelnice, (960,600))
                            textkcelnice1 = fontmest.render(f"Kupní cena: 2100{znacka_meny}", True, (redb))
                            surface.blit(textkcelnice1, (960,620))
                            textkcelnice2 = fontmest.render(f"Cena za návštěvu tohoto města: 200x hod kostkou", True, (redb))
                            surface.blit(textkcelnice2, (960,640))
                            surface.blit(napisy, (960,680))
                            surface.blit(napis2y, (960,700))
                            pygame.event.wait(240)
                    
                        if "Ambasáda" in x_majetek:
                           textcelnice3 = fontmest.render(f"Vlastníkem Ambasáda je Hráč 1.", True, (redb))
                           #textb = fontmest.render(f"Musíte zaplatit {kodan.navsteva}{znacka_meny} za návštěvu města", True, (red))
                           surface.blit(textcelnice3, (960,600))
                           #surface.blit(textb, (960, 620))
                           textca = fontmest.render(f"Hoďte ještě jednou kostkou!", True, (redb))
                           surface.blit(textca, (960,620))
                           y_money2 = copy.copy(y_money)
                           pygame.event.wait(240)
                           
                if event.key == pygame.K_KP1 and c in range(p32w1,p32w2) and d in range(p39h1,p39h2) and pressed_space == True and "Ambasáda" not in x_majetek and "Ambasáda" not in y_majetek:
                        if y_money - 2100 >= 0:
                              y_money -= 2100
                              textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyy, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg39 += 20
                                      y_majetek.append("Ambasáda")
                              else:
                                  y_majetek.append("Ambasáda")
                              #zapsání do majetku
                              #x_majetek.append("Kodaň")
                              textmajeteky = fontmest.render(f"Koupil jste si Ambasáda", True, (redb))
                              surface.blit(textmajeteky, (960,600))
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)
                            
            if c in range(p32w1,p32w2) and d in range(p39h1,p39h2) and pressed_space == True and "Ambasáda" in x_majetek and "Ambasáda" not in y_majetek and "Celnice" not in x_majetek:
                #if event.type == pygame.KEYDOWN:
                    if u == 1:
                        cacena = 1*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                    
                    if u == 2:
                        cacena = 2*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
              
                    if u == 3:
                        cacena = 3*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 4:
                        cacena = 4*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 5:
                        cacena = 5*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                            
                        
                    if u == 6:
                        cacena = 6*300
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                    
                    

                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                        pressed_space = False
                        smth = 0
                        
            if c in range(p32w1,p32w2) and d in range(p39h1,p39h2) and pressed_space == True and "Ambasáda" in x_majetek and "Ambasáda" not in y_majetek and "Celnice" in x_majetek:
                #if event.type == pygame.KEYDOWN:
                    if u == 1:
                        cacena = 1*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                    
                    if u == 2:
                        cacena = 2*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
              
                    if u == 3:
                        cacena = 3*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 4:
                        cacena = 4*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                        
                    if u == 5:
                        cacena = 5*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                            
                        
                    if u == 6:
                        cacena = 6*500
                        #textca = fontmest.render(f"Musíte zaplatit {cacena}{znacka_meny}", True, (red))
                        #surface.blit(textca, (960,600))
                        #pygame.event.wait(240)
                        if hrac_hodil_kostkou == True:
                            y_money -= cacena
                            x_money += cacena
                            u = 0
                            smth = 1
                    
                    

                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                        pressed_space = False
                        smth = 0
                        
            if c in range(p32w1,p32w2) and d in range(p39h1,p39h2) and pressed_space == True and smth == 1:
                roz = y_money2 - y_money
                textca = fontmest.render(f"Musíte zaplatit {roz}{znacka_meny}", True, (redb))
                surface.blit(textca, (960,600))
                pygame.event.wait(240)
                    
                if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
                    smth = 0

            #pole40
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed_space = True
                
                    if c in range(p32w1,p32w2) and d in range(p40h1,p40h2):
                        if "Las Vegas" in x_majetek and "Las Vegas" not in y_majetek and las.navsteva != 7800:
                           texta = fontmest.render(f"Vlastníkem města {las.jmeno} je Hráč 1.", True, (blue))
                           textc = fontmest.render(f"Pokud chcete překoupit město stiskněte číslo 3", True, (blue))
                           textd = fontmest.render(f"Pokud chcete pouze zaplatit za návštěvu stiskněte číslo 0", True, (blue))
                           surface.blit(textc, (960,600))
                           surface.blit(textd, (960,620))
                           pygame.event.wait(240)

                        if "Las Vegas" in x_majetek and "Las Vegas" not in y_majetek and las.navsteva == 7800:
                           texta = fontmest.render(f"Vlastníkem města {las.jmeno} je Hráč 1 a vlastní zde i průvodce.", True, (redb))
                           textb = fontmest.render(f"Musíte zaplatit {las.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                           surface.blit(texta, (960,600))
                           surface.blit(textb, (960, 620))
                           y_money -= las.navsteva
                           x_money += las.navsteva
                           textmoneyx = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyx, (960,650))
                           textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                           surface.blit(textmoneyy, (960,670))
                           pygame.event.wait(240)
                           
                        if "Las Vegas" not in x_majetek and "Las Vegas" not in y_majetek:
                           las = mesta("Las Vegas", 10000, 5200, 4000, 7800, "prozatím nikdo")
                           las.karticky()
                           surface.blit(napisy, (960,730))
                           surface.blit(napis2y, (960,750))
                           pygame.event.wait(240)
                        elif "Las Vegas" in y_majetek and las.navsteva != 7800:
                           las.upgrade()
                           pygame.event.wait(240)
                        elif "Las Vegas" in y_majetek and las.navsteva == 7800:
                           textmas = fontmest.render("Jste vlastníkem tohoto města a vlastníte i průvodce", True, (redb))
                           surface.blit(textmas, (960,600))
                           pygame.event.wait(240)
                       
                           
                     
                if event.key == pygame.K_KP1 and c in range(p32w1,p32w2) and d in range(p40h1,p40h2) and pressed_space == True and "Las Vegas" not in x_majetek and "Las Vegas" not in y_majetek:
                        if y_money - las.kupni_cena >= 0:
                              y_money -= las.kupni_cena
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,620))
                              #zapsání do majetku
                              if len(y_majetek) >= 1:
                                      while len(y_majetek) > pocet_mest:
                                          pocet_mest += 1
                                          hg40 += 20
                                      y_majetek.append("Las Vegas")
                              else: 
                                  y_majetek.append("Las Vegas")
                              #zapsání do majetku
                              #x_majetek.append("Amsterdam")
                              textmajetekx = fontmest.render(f"Koupil jste si {las.jmeno}", True, (redb))
                              surface.blit(textmajetekx, (960,600))
                              #hg40 = 0
                              pressed_space = False
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)  
                if event.key == pygame.K_KP2 and c in range(p32w1,p32w2) and d in range(p40h1,p40h2) and las.navsteva != 7800 and pressed_space == True and "Las Vegas" not in x_majetek and "Las Vegas" in y_majetek:
                        if y_money - las.domecek >= 0:
                              y_money -= las.domecek
                              textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                              surface.blit(textmoneyx, (960,600))
                              las.navsteva = las.nova_kupni_cena
                              textnavstev = fontmest.render(f"Cena za návštěvu Vašeho města je {las.navsteva}{znacka_meny}", True, (redb))
                              surface.blit(textnavstev, (960,620))
                              pygame.event.wait(240)
                        else:
                            textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (redb))
                            surface.blit(textnedostatekp, (960,600))
                            pygame.event.wait(240)        
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p40h1,p40h2)and pressed_space == True and "Las Vegas" not in x_majetek:
                              hrac_na_rade = x
                              pressed_space = False
                              
                
                if event.key == pygame.K_KP3 and c in range(p32w1,p32w2) and d in range(p40h1,p40h2) and pressed_space == True and "Las Vegas" in x_majetek and "Las Vegas" not in y_majetek and las.navsteva != 7800:
                              if y_money - 15000 >= 0:
                                  y_money -= 15000
                                  x_money += 15000
                                  hg40 = 0
                                  textmoneyy = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (blue))
                                  surface.blit(textmoneyy, (960,620))
                                  #zapsání do majetku
                                  if len(y_majetek) >= 1:
                                          while len(y_majetek) > pocet_mest:
                                              pocet_mest += 1
                                              hg40 += 20
                                          y_majetek.append("Las Vegas")
                                          x_majetek.remove("Las Vegas")
                                          x_majetek.append(" ")
                                  else:
                                      y_majetek.append("Las Vegas")
                                      x_majetek.remove("Las Vegas")
                                      x_majetek.append(" ")
                                  textmajeteky = fontmest.render(f"Koupil jste si {las.jmeno}", True, (blue))
                                  surface.blit(textmajeteky, (960,600))
                                  #hg40 = 0
                                  pressed_space = False
                                  #bb = x_majetek.index("Nairobi")
                                  #del(x_majetek[y])
                                  #del(x_majetek["Nairobi"])
                                  pygame.event.wait(240)
                                  
                              else:
                                   textnedostatekp = fontmest.render(f"Nedostatek peněz", True, (blue))
                                   surface.blit(textnedostatekp, (960,600))
                                   pygame.event.wait(240)
                if event.key == pygame.K_KP0 and c in range(p32w1,p32w2) and d in range(p40h1,p40h2) and pressed_space == True and "Las Vegas" in x_majetek:
                               texta = fontmest.render(f"Vlastníkem města {las.jmeno} je Hráč 1.", True, (redb))
                               textb = fontmest.render(f"Musíte zaplatit {las.navsteva} {znacka_meny} za návštěvu města", True, (redb))
                               surface.blit(texta, (960,600))
                               surface.blit(textb, (960, 620))
                               y_money -= las.navsteva
                               x_money += las.navsteva
                               textmoneyx = fontmest.render(f"Druhý hráč má {y_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyx, (960,640))
                               textmoneyy = fontmest.render(f"První hráč má {x_money}{znacka_meny}", True, (redb))
                               surface.blit(textmoneyy, (960,660))
                               pygame.event.wait(240)         
            

        if "Nairobi" in y_majetek:
                textmest = fontmest1.render("Nairobi", True, (redb))
                surface.blit(textmest, (wy,hy + hg2))
                pocet_mest = 0
                if nairobi.navsteva != 600:
                    surface.blit(mdum1, (770,908))
                if nairobi.navsteva == 600:
                    surface.blit(mdum_pruvodce1, (770,908))
                #x_majetek.remove("Nairobi")
                

        if "Káhira" in y_majetek:
               textmest = fontmest1.render("Káhira", True, (redb))
               surface.blit(textmest, (wy,hy + hg4))
               pocet_mest = 0
               if kahira.navsteva != 750:
                    surface.blit(mdum1, (615,908))
               if kahira.navsteva == 750:
                    surface.blit(mdum_pruvodce1, (615,908))

        if "Maledivy" in y_majetek:
            textmest = fontmest1.render("Maledivy", True, (redb))
            surface.blit(textmest, (wy,hy + hg6))
            pocet_mest = 0
            surface.blit(mdumm, (482,900))
         
        if "Rio de Janeiro" in y_majetek:
                textmest = fontmest1.render("Rio de Janeiro", True, (redb))
                surface.blit(textmest, (wy,hy + hg7))
                pocet_mest = 0
                if rio.navsteva != 920:
                    surface.blit(mdum1, (380,908))
                if rio.navsteva == 920:
                    surface.blit(mdum_pruvodce1, (380,908))

        if "Buenos Aires" in y_majetek:
                textmest = fontmest1.render("Buenos Aires", True, (redb))
                surface.blit(textmest, (wy,hy + hg9))
                pocet_mest = 0
                if buenos.navsteva != 1100:
                    surface.blit(mdum1, (228,908))
                if buenos.navsteva == 1100:
                    surface.blit(mdum_pruvodce1, (228,908))

        if "Santiago de Chille" in y_majetek:
                textmest = fontmest1.render("Santiago de Chille", True, (redb))
                surface.blit(textmest, (wy,hy + hg10))
                pocet_mest = 0
                if santiago.navsteva != 1100:
                    surface.blit(mdum1, (150,908))
                if santiago.navsteva == 1100:
                    surface.blit(mdum_pruvodce1, (150,908))

        if "Kodaň" in y_majetek:
                textmest = fontmest1.render("Kodaň", True, (redb))
                surface.blit(textmest, (wy,hy + hg12))
                pocet_mest = 0
                if kodan.navsteva != 1400:
                    surface.blit(mdum2, (12,770))
                if kodan.navsteva == 1400:
                    surface.blit(mdum_pruvodce2, (12,770))

        if "Berlín" in y_majetek:
                textmest = fontmest1.render("Berlín", True, (redb))
                surface.blit(textmest, (wy,hy + hg14))
                pocet_mest = 0
                if berlin.navsteva != 1700:
                    surface.blit(mdum2, (12,614))
                if berlin.navsteva == 1700:
                    surface.blit(mdum_pruvodce2, (12,614))

        if "Amsterdam" in y_majetek:
                textmest = fontmest1.render("Amsterdam", True, (redb))
                surface.blit(textmest, (wy,hy + hg15))
                pocet_mest = 0
                if amsterdam.navsteva != 1700:
                    surface.blit(mdum2, (12,536))
                if amsterdam.navsteva == 1700:
                    surface.blit(mdum_pruvodce2, (12,536))

        if "Bali" in y_majetek:
                textmest = fontmest1.render("Bali", True, (redb))
                surface.blit(textmest, (wy,hy + hg16))
                pocet_mest = 0
                surface.blit(mdumb, (27,481))

        if "Wellington" in y_majetek:
                textmest = fontmest1.render("Wellington", True, (redb))
                surface.blit(textmest, (wy,hy + hg17))
                pocet_mest = 0
                if wellington.navsteva != 2100:
                    surface.blit(mdum2, (12,380))
                if wellington.navsteva == 2100:
                    surface.blit(mdum_pruvodce2, (12,380))

        if "Melbourne" in y_majetek:
                textmest = fontmest1.render("Melbourne", True, (redb))
                surface.blit(textmest, (wy,hy + hg19))
                pocet_mest = 0
                if melbourne.navsteva != 2400:
                    surface.blit(mdum2, (12,224))
                if melbourne.navsteva == 2400:
                    surface.blit(mdum_pruvodce2, (12,224))

        if "Sydney" in y_majetek:
                textmest = fontmest1.render("Sydney", True, (redb))
                surface.blit(textmest, (wy,hy + hg20))
                pocet_mest = 0
                if sydney.navsteva != 2400:
                    surface.blit(mdum2, (12,144))
                if sydney.navsteva == 2400:
                    surface.blit(mdum_pruvodce2, (12,144))

        if "San Francisco" in y_majetek:
                textmest = fontmest1.render("San Francisco", True, (redb))
                surface.blit(textmest, (wy,hy + hg22))
                pocet_mest = 0
                if san.navsteva != 2800:
                    surface.blit(mdum3, (150,8))
                if san.navsteva == 2800:
                    surface.blit(mdum_pruvodce3, (150,8))

        if "Los Angeles" in y_majetek:
                textmest = fontmest1.render("Los Angeles", True, (redb))
                surface.blit(textmest, (wy,hy + hg24))
                pocet_mest = 0
                if los.navsteva != 3500:
                    surface.blit(mdum3, (302,8))
                if los.navsteva == 3500:
                    surface.blit(mdum_pruvodce3, (302,8))

        if "New York" in y_majetek:
                textmest = fontmest1.render("New York", True, (redb))
                surface.blit(textmest, (wy,hy + hg25))
                pocet_mest = 0
                if new.navsteva != 3500:
                    surface.blit(mdum3, (382,8))
                if new.navsteva == 3500:
                    surface.blit(mdum_pruvodce3, (382,8))

        if "Hawaii" in y_majetek:
                textmest = fontmest1.render("Hawaii", True, (redb))
                surface.blit(textmest, (wy,hy + hg26))
                pocet_mest = 0
                surface.blit(mdumh, (440,27))
                
                
        if "Bangkok" in y_majetek:
                textmest = fontmest1.render("Bangkok", True, (redb))
                surface.blit(textmest, (wy,hy + hg27))
                pocet_mest = 0
                if bangkok.navsteva != 3800:
                    surface.blit(mdum3, (536,8))
                if bangkok.navsteva == 3800:
                    surface.blit(mdum_pruvodce3, (536,8))

        if "Šanghaj" in y_majetek:
                textmest = fontmest1.render("Šanghaj", True, (redb))
                surface.blit(textmest, (wy,hy + hg28))
                pocet_mest = 0
                if šanghaj.navsteva != 3800:
                    surface.blit(mdum3, (616,8))
                if šanghaj.navsteva == 3800:
                    surface.blit(mdum_pruvodce3, (616,8))
                
        if "Tokio" in y_majetek:
                textmest = fontmest1.render("Tokio", True, (redb))
                surface.blit(textmest, (wy,hy + hg30))
                pocet_mest = 0
                if tokio.navsteva != 4500:
                    surface.blit(mdum3, (770,8))
                if tokio.navsteva == 4500:
                    surface.blit(mdum_pruvodce3, (770,8))
                
                

        if "Praha" in y_majetek:
                textmest = fontmest1.render("Praha", True, (redb))
                surface.blit(textmest, (wy,hy + hg32))
                pocet_mest = 0
                if praha.navsteva != 5100:
                    surface.blit(mdum4, (904,148))
                if praha.navsteva == 5100:
                    surface.blit(mdum_pruvodce4, (904,148))


        if "Londýn" in y_majetek:
                textmest = fontmest1.render("Londýn", True, (redb))
                surface.blit(textmest, (wy,hy + hg33))
                pocet_mest = 0
                if londyn.navsteva != 5100:
                    surface.blit(mdum4, (904,224))
                if londyn.navsteva == 5100:
                    surface.blit(mdum_pruvodce4, (904,224))

        if "Paříž" in y_majetek:
                textmest = fontmest1.render("Paříž", True, (redb))
                surface.blit(textmest, (wy,hy + hg35))
                pocet_mest = 0
                if pariz.navsteva != 5800:
                    surface.blit(mdum4, (904,380))
                if pariz.navsteva == 5800:
                    surface.blit(mdum_pruvodce4, (904,380))


        if "Las Vegas" in y_majetek:
                textmest = fontmest1.render("Las Vegas", True, (redb))
                surface.blit(textmest, (wy,hy + hg40))
                pocet_mest = 0
                if las.navsteva != 7800:
                    surface.blit(mdum4, (904,770))
                if las.navsteva == 7800:
                    surface.blit(mdum_pruvodce4, (904,770))

        if "Dubai" in y_majetek:
                textmest = fontmest1.render("Dubai", True, (redb))
                surface.blit(textmest, (wy,hy + hg38))
                pocet_mest = 0
                if dubai.navsteva != 6800:
                    surface.blit(mdum4, (904,616))
                if dubai.navsteva == 6800:
                    surface.blit(mdum_pruvodce4, (904,616))

        

        if "Srí Lanka" in y_majetek:
                textmest = fontmest1.render("Srí Lanka", True, (redb))
                surface.blit(textmest, (wy,hy + hg36))
                pocet_mest = 0
                surface.blit(mdums, (900,440))

        if "Celnice" in y_majetek:
                textmest = fontmest1.render("Celnice", True, (redb))
                surface.blit(textmest, (wy,hy + hg13))
                pocet_mest = 0
                surface.blit(mdumcel, (70,698))

        if "Ambasáda" in y_majetek:
                textmest = fontmest1.render("Ambasáda", True, (redb))
                surface.blit(textmest, (wy,hy + hg39))
                pocet_mest = 0
                surface.blit(mdumamb, (865,700))

        #pygame.display.update()123456789
        
                       
        #r = pygame.draw.rect(surface, (black), (420,700,100,22))123456789
        #fontend = pygame.font.SysFont(písmo1,20)
        #textend = fontend.render(f"KONEC HRY", True, (white))
        #surface.blit(textend, (420,700))    
        #pygame.display.update()123456789
        surface.blit(y, (c,d))
        surface.blit(x, (a,b))
        

#GAME OVER
        if x_money <= 0:
            done = False
            k = 1
            
        if y_money <= 0:
            done = False
            k = 2

        if "Maledivy" in y_majetek and "Bali" in y_majetek and "Hawaii" in y_majetek and "Srí Lanka" in y_majetek:
            done = False
            k = 2

        if "Maledivy" in x_majetek and "Bali" in x_majetek and "Hawaii" in x_majetek and "Srí Lanka" in x_majetek:
            done = False
            k = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if r.collidepoint(pos):
                done = False
                k = 3

             
       
        pygame.display.update()



fontkonec = pygame.font.SysFont(písmo1,60)
fontkonec1 = pygame.font.SysFont(písmo1,40)
textkonec = fontkonec.render(f"KONEC HRY", True, (black))
textkonecx = fontkonec.render(f"Vyhrává první hráč", True, (red))
textkonecy = fontkonec.render(f"Vyhrává druhý hráč", True, (redb))
textkonecrem = fontkonec.render(f"REMÍZA", True, (black))
fontznovu = pygame.font.SysFont(písmo1,20)
#textznovu = fontznovu.render(f"Pokud chcete začít novou hru stiskněte ENTER", True, (black))
textneznovu = fontznovu.render(f"Pro ukončení hry stiskněte ESCAPE", True, (black))

done = True

while done == True:
        surface.fill((255,255,255))
        surface.blit(textkonec, (550,300))
        #surface.blit(textznovu, (450,710))
        surface.blit(textneznovu, (564,760))
        for event in pygame.event.get():

            key = pygame.key.get_pressed()

            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                
                pygame.quit()
                quit()

            key = pygame.key.get_pressed()


            if k == 1:
                surface.blit(textkonecx,(490,450))
            if k == 2:
                surface.blit(textkonecy,(490,450))

            if k == 3:
                lxmaj = len(x_majetek)*1000
                moneykx = x_money + lxmaj
                textmkx = fontkonec1.render(f"První hráč má {moneykx}{znacka_meny}", True, (red))
                lymaj = len(y_majetek)*1000
                moneyky = y_money + lymaj
                textmky = fontkonec1.render(f"Druhý hráč má {moneyky}{znacka_meny}", True, (redb))
                surface.blit(textmkx, (530,430))
                surface.blit(textmky, (530,480))
                if moneykx > moneyky:
                    surface.blit(textkonecx,(490,550))
                if moneyky > moneykx:
                    surface.blit(textkonecy,(490,550))
                if moneykx == moneyky:
                    surface.blit(textkonecrem, (600,550))
                
            #if key[pygame.K_KP_ENTER] or key[pygame.K_RETURN]:
                

            
            pygame.display.update()




























