# потрібно замінити клас Wall на наявний клас Wall та підставити своє зображення
class Wall:
    def __init__(self, x, y, width, height, image_path=None):
        self.rect = pygame.Rect(x, y, width, height)
        if image_path:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (width, height))
        else:
            self.image = None
        self.color = (22, 26, 31)

    def draw(self, window):
        if self.image:
            window.blit(self.image, self.rect)
        else:
            pygame.draw.rect(window, self.color, self.rect)
