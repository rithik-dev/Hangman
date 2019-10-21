import pygame
from pygame.locals import *
import os
from random import randint

winWidth = 550
winHeight = 600
TEXT_COLOR = (0, 0, 0)


def display_text(text, pos, size=30, color=TEXT_COLOR):
    """displays text on the screen

    Args:
        text (string): text to displat
        pos (tuple): pos of text to display (x,y)
        size (int, optional): size of font. Defaults to 30.
        color (tuple, optional): color of font. Defaults to TEXT_COLOR.

    Returns:    
        None
    """
    myFont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myFont.render(text, False, color)
    win.blit(textsurface, (pos[0], pos[1]))


def guessed_right(word, letter):
    """checks if user input is present in word

    Args:
        word (string): word
        letter (character): user input

    Returns:
        True: letter present in word
        False: letter not present in word
    """
    if letter.lower() in word.lower():
        return True
    return False


def getRandomWord():
    """returns a random word

    Returns:    
        String [word]

    """
    words = (
        'adult',
        'acres',
        'advice',
        'arrangement',
        'attempt',
        'August',
        'Autumn',
        'border',
        'breeze',
        'brick',
        'calm',
        'canal',
        'Casey',
        'cast',
        'chose',
        'claws',
        'coach',
        'constantly',
        'contrast',
        'cookies',
        'customs',
        'damage',
        'Danny',
        'deeply',
        'depth',
        'discussion',
        'doll',
        'donkey',
        'Egypt',
        'Ellen',
        'essential',
        'exchange',
        'exist',
        'explanation',
        'facing',
        'film',
        'finest',
        'fireplace',
        'floating',
        'folks',
        'fort',
        'garage',
        'grabbed',
        'grandmother',
        'habit',
        'happily',
        'Harry',
        'heading',
        'hunter',
        'Illinois',
        'image',
        'independent',
        'instant',
        'January',
        'kids',
        'label',
        'Lee',
        'lungs',
        'manufacturing',
        'Martin',
        'mathematics',
        'melted',
        'memory',
        'mill',
        'mission',
        'monkey',
        'Mount',
        'mysterious',
        'neighborhood',
        'Norway',
        'nuts',
        'occasionally',
        'official',
        'ourselves',
        'palace',
        'Pennsylvania',
        'Philadelphia',
        'plates',
        'poetry',
        'policeman',
        'positive',
        'possibly',
        'practical',
        'pride',
        'promised',
        'recall',
        'relationship',
        'remarkable',
        'require',
        'rhyme',
        'rocky',
        'rubbed',
        'rush',
        'sale',
        'satellites',
        'satisfied',
        'scared',
        'selection',
        'shake',
        'shaking',
        'shallow',
        'shout',
        'silly',
        'simplest',
        'slight',
        'slip',
        'slope',
        'soap',
        'solar',
        'species',
        'spin',
        'stiff',
        'swung',
        'tales',
        'thumb',
        'tobacco',
        'toy',
        'trap',
        'treated',
        'tune',
        'University',
        'vapor',
        'vessels',
        'wealth',
        'wolf',
        'zoo',
    )

    random = randint(0, len(words)-1)
    return words[random].lower()


def welcomeScreen():
    """this is the welcome screen
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_RETURN:
                return
            else:
                win.fill(BACKGROUND_COLOR)

                display_text('HANGMAN', (winWidth//2-130, winHeight*0.10), 50)
                display_text("Press 'ENTER' to start..",
                             (winWidth//2-150, winHeight*0.80))

                win.blit(hangmanPics[6],
                         ((winWidth-hangmanPics[6].get_width())//2, winHeight*0.3))
                pygame.display.update()


def spacedOut(word, guessedLetters=[]):
    """used to print underscores and update if input is given

    Args:
        word (string): word
        guessed (list, optional): list of all guessed characters. Defaults to [].
    """
    spacedWord = ''
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '__ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-3]
                    spacedWord += ' ' + word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += '    '

    return spacedWord


def draw_game_window(data, limbs, wrong_guesses, word, guesses):
    """functions used to blit on the screen

    Args:
        data (list): all data regarding buttons,text and alphabets
        limbs (int): no. of limbs
        wrong_guesses (list): list of wrong guesses
        word (string): word
        guesses (list): list of all user inputs

    Returns:
        None
    """
    win.fill(BACKGROUND_COLOR)

    # drawing buttons
    for i in range(0, 26):
        if not data[4][i] == 0:
            pygame.draw.circle(
                data[2][i][0], data[2][i][1], data[2][i][2], data[2][i][3])
            display_text(
                data[3][i][0], data[3][i][1], data[3][i][2])

    # drawing hangman according to limbs
    win.blit(hangmanPics[limbs],
             ((winWidth-hangmanPics[limbs].get_width())//2-100, winHeight*0.27))

    if 6-limbs > 2:
        display_text(f"[ {6-limbs} attempt(s) left.. ]",
                     (winWidth*0.1, winHeight*0.70), 20)
    else:
        display_text(f"[ {6-limbs} attempt(s) left.. ]",
                     (winWidth*0.1, winHeight*0.70), 20, (255, 0, 0))

    # displaying wrong guesses
    if len(wrong_guesses) > 0:
        display_text("WRONG GUESSES",
                     (winWidth*0.65, winHeight*0.3), 20)
    for wrong in range(0, len(wrong_guesses)):
        display_text(wrong_guesses[wrong],
                     (winWidth*0.8, winHeight*0.32+wrong*25+25), 20, (255, 255, 255))

    # displaying underscores
    underscores_font = pygame.font.SysFont("comicsansms", 20)
    underscores = spacedOut(word, guesses)

    if underscores.count('__') == 0:      # player wins
        return 0

    underscores_label = underscores_font.render(underscores, 1, (0, 0, 0))
    length = underscores_label.get_rect()[2]
    display_text(underscores, ((winWidth-length)//2, winHeight*0.85), 20)

    pygame.display.update()


def mainGame():
    """main game function

    Returns:
        Tuple
    """
    radius = 17

    #  data = [alphabets , button positions , circles , text displays , button is visible]
    data = [[], [], [], [], []]
    wrong_guesses = []
    guesses = []

    # adding alphabets at data[0]
    # adding button is visible at data[4]
    for i in range(65, 91):
        data[0].append(chr(i))
        data[4].append(1)

    limbs = 0
    word = getRandomWord()

    # adding button positions at data[1]
    # adding circles at data[2]
    # adding text displays at data[3]
    for i in range(0, 13):
        X = 35+i*40
        Y = 40
        data[1].append((X, Y))
        data[2].append((win, (0, 200, 0), (X, Y), radius))
        data[3].append((data[0][i], (X-10, Y-18), 25))
    Y += 45
    for i in range(0, 13):
        X = 35+i*40
        data[1].append((X, Y))
        data[2].append((win, (0, 200, 0), (X, Y), radius))
        data[3].append((data[0][i+13], (X-10, Y-18), 25))

    user_input = ''
    player_wins = False

    while True:
        player_wins = draw_game_window(
            data, limbs, wrong_guesses, word, guesses)
        if player_wins == 0:     # player wins
            return (True, word, limbs)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                # navigating through all buttons and checking if mouse cursor is above any button
                for i in range(0, len(data[1])):
                    mouseX = pygame.mouse.get_pos()[0]
                    mouseY = pygame.mouse.get_pos()[1]
                    if data[4][i] == 1:     # button is visible
                        buttonX = data[1][i][0]
                        buttonY = data[1][i][1]
                        # getting user input by checking mouse click
                        if buttonX+radius > mouseX > buttonX-radius and buttonY+radius > mouseY > buttonY-radius:
                            user_input = data[0][data[1].index(
                                (buttonX, buttonY))]
                            # making button inactive
                            data[4][data[0].index(user_input)] = 0
                            break

                if guessed_right(word, user_input):
                    guesses.append(user_input)
                else:
                    wrong_guesses.append(user_input)
                    limbs += 1
                    if limbs == 6:     # player lost
                        return (False, word, limbs)


def gameOver(player_wins, word, limbs):
    """checks if player won or lost

    Args:
        player_wins (bool): player wins or not
        word (string): word
        limbs (int): limbs

    Returns:
        None
    """
    if player_wins:
        message = 'YOU WON'
        SOUNDS['win'].play()
    else:
        message = 'YOU LOST'
        SOUNDS['lose'].play()
        limbs = 6

    win.fill(BACKGROUND_COLOR)
    display_text('HANGMAN', (winWidth//2-130, winHeight*0.06), 50)
    display_text(message, (winWidth//2-80, winHeight*0.24), 37, (255, 0, 0))
    win.blit(hangmanPics[limbs], ((
        winWidth-hangmanPics[limbs].get_width())//2, winHeight*0.4))
    display_text("The Word Was :   "+word.upper(),
                 (winWidth*0.09, winHeight*0.8), 27)
    display_text("Press 'R' to restart",
                 (winWidth*0.65, winHeight*0.92), 20)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_r:
                return True


if __name__ == "__main__":
    pygame.init()
    BACKGROUND_COLOR = (0, 0, 255)

    reset = True

    win = pygame.display.set_mode((winWidth, winHeight))
    pygame.display.set_caption("Hangman - Word Guessing Game")

    dir = os.path.dirname(__file__)

    hangmanPics = []
    for x in range(0, 7):
        path = dir + f"\\assets\\images\\hangman{x}.png"
        hangmanPics.append(pygame.image.load(path).convert_alpha())

    SOUNDS = {}
    SOUNDS['win'] = pygame.mixer.Sound(
        os.path.join(dir, 'assets/sounds', 'win.wav'))
    SOUNDS['lose'] = pygame.mixer.Sound(
        os.path.join(dir, 'assets/sounds', 'lose.wav'))

    while True:
        welcomeScreen()
        x = mainGame()
        gameOver(x[0], x[1], x[2])
