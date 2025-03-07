import pygame

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
WIDTH, HEIGHT = 200, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Figura w Pygame")

# Kolory
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Współrzędne dla figury
square_rect = pygame.Rect(50, 50, 100, 100)  # Kwadrat
triangle_points = [(50, 150), (150, 150), (100, 100)]  # Trójkąt

# Pętla gry
running = True
while running:
    screen.fill(WHITE)  # Tło
    
    # Rysowanie kwadratu
    pygame.draw.rect(screen, GREEN, square_rect)
    
    # Rysowanie trójkąta w kolorze tła (wycięcie)
    pygame.draw.polygon(screen, WHITE, triangle_points)
    
    # Aktualizacja ekranu
    pygame.display.flip()
    
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()