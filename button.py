# button class

class Button():
    def __init__(self, **config):
        # button graphic
        self.image = config['image']
        self.hover_image = config['hover_image']
        # button position
        self.x_pos = config['pos'][0]
        self.y_pos = config['pos'][1]
        # title font
        self.font = config['font']
        # colors
        self.base_color = config['base_color']
        #
        self.text_input = config['text_input']
        self.click_effect = config['click_effect']
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def display(self, screen, position):
        if self.image is not None:
            if self.isInside(position):
                screen.blit(self.hover_image, self.rect)
            else:
                screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def isInside(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def clicked(self):
        self.click_effect()

buttons = []