import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Polygon and Transformations")

# Kolory
BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)

# Zmienne do transformacji
scale_x = 1.0  # Skalowanie szerokości
scale_y = 1.0  # Skalowanie wysokości
rotation_angle = 0
position_offset = [0, 0]
skew_x = 0  # Pokrzywienie poziome
skew_y = 0  # Pokrzywienie pionowe
flip_x = False
flip_y = False

# Główna pętla gry
run = True
while run:
    win.fill(BIALY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scale_x *= 1.1  # Powiększenie szerokości
            elif event.key == pygame.K_2:
                scale_x *= 0.9  # Pomniejszenie szerokości
            elif event.key == pygame.K_3:
                scale_y *= 1.1  # Powiększenie wysokości
            elif event.key == pygame.K_4:
                scale_y *= 0.9  # Pomniejszenie wysokości
            elif event.key == pygame.K_5:
                rotation_angle += 15  # Obrót w prawo
            elif event.key == pygame.K_6:
                rotation_angle -= 15  # Obrót w lewo
            elif event.key == pygame.K_7:
                skew_x += 0.1  # Pokrzywienie poziome
            elif event.key == pygame.K_8:
                skew_y += 0.1  # Pokrzywienie pionowe
            elif event.key == pygame.K_9:
                flip_x = not flip_x  # Odbicie w poziomie
            elif event.key == pygame.K_0:
                flip_y = not flip_y  # Odbicie w pionie
    
    # Rysowanie wielokąta z przekształceniami
    transformed_points = []
    angle_offset = math.radians(rotation_angle)
    for i in range(10):
        angle = 2 * math.pi * i / 10 + angle_offset
        x = (150 * scale_x) * math.cos(angle) + skew_x * (150 * scale_y) * math.sin(angle)
        y = (150 * scale_y) * math.sin(angle) + skew_y * (150 * scale_x) * math.cos(angle)
        
        if flip_x:
            x = -x
        if flip_y:
            y = -y
        
        transformed_points.append((300 + position_offset[0] + x, 300 + position_offset[1] + y))
    
    pygame.draw.polygon(win, CZERWONY, transformed_points)
    
    pygame.display.update()
    
pygame.quit()