import pygame,sys

pygame.init()

screen = pygame.display.set_mode((770,595))
pygame.display.set_caption('Calendar')
image = pygame.image.load('Document/January.png')
font = pygame.font.Font('Document/Number.otf',35)
image = pygame.transform.scale(image,(770,595))

Ma_nam = 6
Ma_thang = {
    1:1,
    2:4,
    3:4,
    4:0,
    5:2,
    6:5,
    7:0,
    8:3,
    9:6,
    10:1,
    11:4,
    12:6
}
Ngay_1 = (1 + Ma_thang[7] +Ma_nam) % 7
So_ngay_dong_dau = 7 - Ngay_1 + 1

Num_list = []
dem = 1
x_pos,y_pos = 121,185
Num = font.render('1',True,(0,0,0))
Num_list.append((Num,(x_pos+(Ngay_1-1)*98,185)))
x_pos+=(Ngay_1)*98
if So_ngay_dong_dau == 8:
    x_pos = 121
    y_pos+=81
for i in range(2,32):
    Num = font.render(str(i),True,(0,0,0))
    Num_list.append((Num,(x_pos,y_pos)))
    x_pos+=98
    dem+=1
    if dem == So_ngay_dong_dau:
        x_pos = 121
        y_pos+=81
        So_ngay_dong_dau+=7
    #y_pos+=81
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    screen.blit(image,(0,0))

    '''Num3 = font.render('12',True,(0,0,0))
    screen.blit(Num3,(0,0))'''
    for i in Num_list:
        screen.blit(i[0],i[1])

    pygame.display.update()