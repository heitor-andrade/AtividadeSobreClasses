import pygame


def main():
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    input_box = pygame.Rect(100, 200, 140, 32)
    input_box0 = pygame.Rect(100, 300, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    active1 =False
    nome = ''
    cor = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                    color = color_active if active else color_inactive
                else:
                    active = False
                # Change the current color of the input box.
                if input_box0.collidepoint(event.pos):
                    color = color_active if active else color_inactive
                    active1 = not active1
                else:
                    active1 = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]
                    else:
                        nome += event.unicode
                if active1:
                    if event.key == pygame.K_RETURN:

                        done = True
                        return (nome, cor)
                    elif event.key == pygame.K_BACKSPACE:
                        cor = cor[:-1]
                    else:
                        cor += event.unicode
        screen.fill((30, 30, 30))
        font_p = pygame.font.get_default_font()
        fonte_comando = pygame.font.SysFont(font_p,30)
        titulo = fonte_comando.render('Nome do Tamagushi:', 1, (255,255,255))

        screen.blit(titulo, (100 , 150))
        titulo = fonte_comando.render('cor - azul/amarelo/vermelho - :', 1, (255,255,255))
        screen.blit(titulo, (100 , 250))

        # Render the current nome.
        txt_surface = font.render(nome, True, color)
        # Resize the box if the nome is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the nome.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        txt_surface = font.render(cor, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box0.w = width
        
        screen.blit(txt_surface, (input_box0.x+5, input_box0.y+5))

        pygame.draw.rect(screen, color, input_box, 2)
        pygame.draw.rect(screen, color, input_box0, 2)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
