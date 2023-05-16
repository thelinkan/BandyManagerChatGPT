import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font,very_small_font ,very_small_bold_font , button_width, button_height, button_x, button_spacing

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def draw_media(game):
    mouse_pos = pygame.mouse.get_pos()
    media_surface,news_rects = draw_media_newslist(game,(140,125))
    screen.blit(media_surface,(140,125))

    news_item_surface = draw_media_news(game)
    screen.blit(news_item_surface,(640,125))

    return news_rects

def draw_media_newslist(game,newslist_offset):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_list = mouse_pos[0] - newslist_offset[0], mouse_pos[1] - newslist_offset[1]
    news_rects = []
    media_surface = pygame.Surface((600,600), pygame.SRCALPHA)
    header_rect = pygame.Rect(0, 0, 450, 30)

    
    pygame.draw.rect(media_surface, TABLE_HEADER_COLOR, header_rect)
    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Date", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    media_surface.blit(text, text_rect)

    text = header_font.render("News", True, BLACK)
    text_rect = text.get_rect(right=header_rect.right - 10, centery=header_rect.centery)
    media_surface.blit(text, text_rect)

    player_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = 30

    for i, newsitem in enumerate(game.newsitems):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR
        #print(game.selected_news_index )
        row_rect = pygame.Rect(0, 30 + i * row_height, 450, row_height)
        if(game.selected_news_index == i):
           row_color = (200,0,0)
           newsitem.is_read = True
        if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
            row_color = (255,200,200)

        pygame.draw.rect(media_surface, row_color, row_rect) 
        news_rects.append(row_rect)
        year = newsitem.date[0]
        month = newsitem.date[1]
        day = newsitem.date[2]
        text = player_font.render(f"{str(year)}-{str(month)}-{str(day)}", True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        media_surface.blit(text, text_rect)

        if(not newsitem.is_read):
            headline_text = f"(new) {newsitem.headline}"
        else:
            headline_text = newsitem.headline

        text = player_font.render(headline_text, True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        media_surface.blit(text, text_rect)


    return media_surface,news_rects

def draw_media_news(game):
    news_surface = pygame.Surface((450,600), pygame.SRCALPHA)
    for i, newsitem in enumerate(game.newsitems):
        if i == game.selected_news_index:
            news_headline = newsitem.headline
            news_text = newsitem.text

            header_font = pygame.font.Font(None, FONTSIZE_MEDIUM)
            text = header_font.render(news_headline, True, BLACK)
            text_rect = text.get_rect(left=10, top=10)
            news_surface.blit(text, text_rect)

            #news_font = pygame.font.Font(None, FONTSIZE_SMALL)
            #text = news_font.render(news_text, True, BLACK)
            #text_rect = text.get_rect(left=10, top=40)
            #news_surface.blit(text, text_rect)

            news_font = pygame.font.Font(None, FONTSIZE_SMALL)
            news_rect = pygame.Rect(10, 40, 430, 550)
            rendered_text = render_wrapped_text(news_text, news_font, news_rect, BLACK)
            news_surface.blit(rendered_text, news_rect)

    return news_surface
    pass

def render_wrapped_text(text, font, rect, color):
    words = text.split()
    lines = []
    current_line = words[0]
    for word in words[1:]:
        test_line = current_line + ' ' + word
        if font.size(test_line)[0] > rect.width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = test_line
    lines.append(current_line)

    surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    line_spacing = 5
    y = rect.top
    for line in lines:
        rendered_line = font.render(line, True, color)
        line_rect = rendered_line.get_rect(left=rect.left, top=y)
        surface.blit(rendered_line, line_rect)
        y += line_rect.height + line_spacing

    return surface
'''

def render_wrapped_text(text, font, rect, color):
    words = text.split()
    lines = []
    current_line = words[0]
    for word in words[1:]:
        test_line = current_line + ' ' + word
        if font.size(test_line)[0] > rect.width:
            if font.size(word)[0] > rect.width * 0.8:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
        else:
            current_line = test_line
    lines.append(current_line)

    surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    line_spacing = 5
    y = rect.top
    for line in lines:
        rendered_line = font.render(line, True, color)
        line_rect = rendered_line.get_rect(left=rect.left, top=y)
        surface.blit(rendered_line, line_rect)
        y += line_rect.height + line_spacing

    return surface
'''