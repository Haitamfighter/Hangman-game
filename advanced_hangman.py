import pygame
import math
import random
pygame.init()
pygame.font.init()


def advanced():
    # Set the screen
    WIDTH, HEIGHT = 800, 500
    WHITE, BLACK = (255, 255, 255), (0, 0, 0)
    pygame.display.set_caption("Hangman game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Functions

    def write_screen(surface, text: str, pos_x, pos_y,color, size=50):
        font = pygame.font.SysFont("comicsans", size)
        text_font = font.render(text, False, color)
        surface.blit(text_font, (pos_x-(text_font.get_width()+pos_x/15), pos_y))

    def draw_ltr(letters: list, width: int, height: int, empty_list=[]):
        x = width/13
        y = height*(3/4)
        radius = 25

        for num, ltr in enumerate(letters):
            # empty_list = [[(36, 350), "A"], [(93, 350), "B"], ...]
            empty_list.append([(x, y), ltr])
            if num < 12:
                y = height*(3/4)
                x += width/14
            elif num == 12:
                y = height*(7/8)
                x = width/13
            else:
                x += width/14
                y = height*(7/8)
        return empty_list, radius

    # Some code
    list_words = ["phone", "mother", "watch", "book", "party", "lucky", "death", "treat", "shame", "lame",
                  "break", "love", "hate", "bomb", "spy", "dead", "life", "duck", "cow", "man", "row", "fox",
                  "job", "spit", "lie"]

    word = random.choice(list_words).upper()  # MAX IS 6 LETTERS
    list_word = list(word)
    output_list = ["_" for i in range(len(word))]
    ltrs = [chr(65+i) for i in range(26)]
    circles_list, radius = draw_ltr(ltrs, WIDTH, HEIGHT)
    font = pygame.font.SysFont("comicsans", 40)
    ltr_pressed = "abc"
    num_guesses, max_num_guesses = 0, 6

    # Main loop
    run = True

    while run:
        hangman_img = pygame.transform.scale(pygame.image.load(f"Assets/hangman{num_guesses}.png"),
                                             (WIDTH/2, HEIGHT/1.5))

        screen.fill(WHITE)
        screen.blit(hangman_img, (0, 0))
        write_screen(screen, " ".join(output_list), WIDTH, int(HEIGHT/4), BLACK)
        pygame.display.update(hangman_img.get_rect())

        # CHECK IF MAX_NUM_GUESSES == NUM_GUESSES
        if num_guesses == max_num_guesses:
            run = False
            pygame.time.delay(1000)
            screen.fill(WHITE)
            write_screen(screen, "YOU LOSE!!", WIDTH, HEIGHT/3, BLACK, size=100)
            write_screen(screen, f"IT WAS '{word}' !", WIDTH, HEIGHT*(3/4), BLACK, size=30)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            break

        # DEF A NO SPACE OUTPUT LIST VAR
        no_sp_output = []
        for x in output_list:
            for i in x:
                if i == " ":
                    sp = ""
                else:
                    sp = i
                no_sp_output.append(sp)

        for i in circles_list:
            x, y = i[0][0], i[0][1]
            text_font = font.render(i[1], False, BLACK)
            screen.blit(text_font, (x - text_font.get_width() / 2, y - text_font.get_height() / 2))

            # i = [(x, y), ltr]
            pygame.draw.circle(screen, BLACK, (x, y), radius, width=1)

        if ("".join(no_sp_output)) == word:
            run = False
            pygame.time.delay(1000)
            screen.fill(WHITE)
            write_screen(screen, "YOU WON!!", WIDTH, HEIGHT/3, BLACK, size=100)
            write_screen(screen, f"IT WAS '{word}' !", WIDTH, HEIGHT*(3/4), BLACK, size=30)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            break

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for circle in circles_list:
                    # circle = [(x, y), ltr]
                    dis = math.sqrt((mouse_x-circle[0][0])**2 + (mouse_y-circle[0][1])**2)
                    if dis < radius:
                        ltr_pressed = circle[1]
                        circles_list.remove(circle)
                        # CHECK IF REMAINING POSSIBLE CHOICES != 0
                        if ltr_pressed in word:
                            for x, y in enumerate(list_word):
                                if ltr_pressed == y:
                                    output_list[x] = f"{ltr_pressed} "
                        else:
                            num_guesses += 1

                        break
