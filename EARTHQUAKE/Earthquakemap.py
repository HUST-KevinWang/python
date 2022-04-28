import pygame
import sys
import pygame.freetype


pygame.init()
size = width, height = 1200, 590
screen = pygame.display.set_mode(size)
pygame.display.set_caption("地震时间动画")
screen.fill((255, 255, 255))
earthmap = pygame.image.load("earthmap.jpg")
f = open("sheet.txt", "r")
line = f.readlines()
fclock = pygame.time.Clock()
flag = -1
screen1 = screen.convert_alpha()
screen1.fill((255, 255, 255, 0))  # alpha=0,全透明


while flag >= -53680:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    f1 = pygame.freetype.Font("C:/Users/86155/Desktop/STUDY/PYTHON/Earthquake/venv/Lib/site-packages/pygame/tests/fixtures/fonts/test_sans.ttf", 36)
    current = line[flag].split(",")
    screen.blit(earthmap, (0, 0))
    screen.blit(screen1, (0, 0))
    if flag + 300 < 0:
        screen1.blit(earthmap, (0, 0))
        for i in range(flag+1, flag+301):
            pygame.draw.circle(screen1, (255, 0, 0, 128), (
            int((eval(line[i].split(",")[5]) + 180) * 10 / 3 + 700) % 1200,
            int(-3 * eval(line[i].split(",")[4]) + 270)), int(eval(line[i].split(",")[1])**3//10))
    while current[2] == line[flag].split(",")[2]:
        pygame.draw.circle(screen1, (255, 0, 0, 128), (
            int((eval(line[flag].split(",")[5])+180)*10/3+700) % 1200,
            int(-3*eval(line[flag].split(",")[4])+270)), int(eval(line[flag].split(",")[1])**3//10))
        flag -= 1
    f1rect = f1.render_to(screen, (0, 545), current[2]+"    Magnitude >= 3", fgcolor=(255, 0, 0), size=50)
    pygame.display.update()
    fclock.tick(200)
    pygame.draw.rect(screen, (255, 255, 255), (0, 540, 1200, 590))
sys.exit()
