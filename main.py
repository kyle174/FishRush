import pygame
import random
from sprites import Orange, Blue, Pink, Puffer, Shark, Bottle, Boot, Player

def gameStart(a,b,c,d,e,f,g):
    # Good fish
    for i in range(a):
        orangeFish = Orange(40, 40)
        # Set a random location for the fish
        orangeFish.rect.x = random.randrange(400, 2000)
        orangeFish.rect.y = random.randrange(20, 380)
        # Add the fish to the lists
        goodFishList.add(orangeFish)
        allSpritesList.add(orangeFish)
    for i in range(b):
        blueFish = Blue(30, 30)
        # Set a random location for the fish
        blueFish.rect.x = random.randrange(400, 2000)
        blueFish.rect.y = random.randrange(20, 380)
        # Add the fish to the lists
        goodFishList.add(blueFish)
        allSpritesList.add(blueFish)
    for i in range(c):
        pinkFish = Pink(30, 30)
        # Set a random location for the fish
        pinkFish.rect.x = random.randrange(400, 1500)
        pinkFish.rect.y = random.randrange(20, 380)
        # Add the fish to the lists
        goodFishList.add(pinkFish)
        allSpritesList.add(pinkFish)
    # Bad fish
    for i in range(d):
        pufferFish = Puffer(40, 40)
        # Set a random location for the fish
        pufferFish.rect.x = random.randrange(400, 1000)
        pufferFish.rect.y = random.randrange(20, 380)
        # Add the fish to the lists
        badFishList.add(pufferFish)
        allSpritesList.add(pufferFish)
    for i in range(e):
        shark = Shark(130, 130)
        # Set a random location for the shark
        shark.rect.x = random.randrange(400, 1200)
        shark.rect.y = random.randrange(20, 380)
        # Add the shark to the lists
        badFishList.add(shark)
        allSpritesList.add(shark)
    for i in range(f):
        bottle = Bottle(20, 30)
        # Set a random location for the bottle
        bottle.rect.x = random.randrange(400, 2000)
        bottle.rect.y = random.randrange(20, 380)
        # Add the bottle to the lists
        badFishList.add(bottle)
        allSpritesList.add(bottle)
    for i in range(g):
        boot = Boot(30, 30)
        # Set a random location for the boot
        boot.rect.x = random.randrange(400, 2000)
        boot.rect.y = random.randrange(20, 380)
        # Add the boot to the lists
        badFishList.add(boot)
        allSpritesList.add(boot)

def healthBar():
    # Image for full heart and empty heart from: https://opengameart.org/content/pixel-hearts
    heartFull = pygame.image.load("graphics/heartfull.png").convert()
    heartFull.set_colorkey(SKYBLUE)
    heartFull = pygame.transform.scale(heartFull, (25, 25))
    heartEmpty = pygame.image.load("graphics/heartempty.png").convert()
    heartEmpty.set_colorkey(BLACK)
    heartEmpty = pygame.transform.scale(heartEmpty, (25, 25))
    # Display the hearts based on the amount of lives left
    if livesLeft == 1:
        screen.blit(heartFull, [600, 5])
        screen.blit(heartEmpty, [625, 5])
        screen.blit(heartEmpty, [650, 5])
    if livesLeft == 2:
        screen.blit(heartFull, [600, 5])
        screen.blit(heartFull, [625, 5])
        screen.blit(heartEmpty, [650, 5])
    if livesLeft == 3:
        screen.blit(heartFull, [600, 5])
        screen.blit(heartFull, [625, 5])
        screen.blit(heartFull, [650, 5])

def resetLevel():
    # Delete all old sprites
    for sprite in allSpritesList:
        allSpritesList.remove(sprite)
        if sprite in goodFishList:
            goodFishList.remove(sprite)
        if sprite in badFishList:
            badFishList.remove(sprite)

def drawScene0():
    # Title screen, set fonts, text and blit them
    font = pygame.font.SysFont("Calibri", 20, True)
    titleFont = pygame.font.SysFont("Calibri", 100, True)
    startMsg = font.render("Click Space to Start", True, (BLACK))
    instructionMsg = font.render("Click i for Instructions", True, (BLACK))
    title = titleFont.render("Fish Rush", True, (AQUA))
    screen.blit(startMsg,(270, 330))
    screen.blit(instructionMsg,(260, 360))
    screen.blit(title,(170, 200))

def drawScene2():
    # Pause screen, set fonts, text and blit them
    font = pygame.font.SysFont("Calibri", 20, True)
    titleFont = pygame.font.SysFont("Calibri", 100, True)
    title = titleFont.render("GAME PAUSED", True, (BLACK))
    restartMsg = font.render("Click Space to Resume", True, (BLACK))
    screen.blit(title,(40, 200))
    screen.blit(restartMsg,[250, 340])

def drawScene3():
    # Death screen, set fonts, text and blit them
    font = pygame.font.SysFont("Calibri", 20, True)
    titleFont = pygame.font.SysFont("Calibri", 100, True)
    title = titleFont.render("YOU DIED!", True, (RED))
    restartMsg = font.render("Click Space to Try Again", True, (BLACK))
    screen.blit(title,(130, 200))
    screen.blit(restartMsg,[250, 340])

def drawScene5():
    # Level complete screen, set fonts, text and blit them
    font = pygame.font.SysFont("Calibri", 20, True)
    titleFont = pygame.font.SysFont("Calibri", 80, True)
    title = titleFont.render("LEVEL COMPLETE!", True, (BLACK))
    nextMsg = font.render("Click Space to Start Next Level", True, (BLACK))
    screen.blit(title,(50, 210))
    screen.blit(nextMsg,[225, 340])

def drawScene7():
    # Instructions screen, set fonts, text and blit them
    font = pygame.font.SysFont("Calibri", 20, True)
    titleFont = pygame.font.SysFont("Calibri", 50, True)
    title = titleFont.render("How to Play", True, (AQUA))
    instruction1 = font.render("Use the W,A,S,D or ←,↑,→,↓ keys to move your fish!", True, (BLACK))
    instruction2 = font.render("Get the amount of points needed on each level to win!", True, (BLACK))
    instruction3 = font.render("Make sure to keep an eye on your lives, 3 lives gone and you're out!", True, (BLACK))
    instruction6 = font.render("Press r at any time to restart a level!", True, (BLACK))
    instruction7 = font.render("Press Backspace at any time to return to the Home Screen!", True, (BLACK))
    instruction8 = font.render("Press Space at any time to Pause a level!", True, (BLACK))
    instruction4 = font.render("Eat these for points!", True, (BLACK))
    instruction5 = font.render("Avoid these or lose a life!", True, (BLACK))
    # Load all images, scale them and set colour key
    orangeFish = pygame.image.load("graphics/orangefish.png").convert()
    orangeFish.set_colorkey(BLACK)
    orangeFish = pygame.transform.scale(orangeFish, (40, 40))
    blueFish = pygame.image.load("graphics/bluefish.png").convert()
    blueFish.set_colorkey(BLACK)
    blueFish = pygame.transform.scale(blueFish, (40, 40))
    pinkFish = pygame.image.load("graphics/pinkfish.png").convert()
    pinkFish.set_colorkey(BLACK)
    pinkFish = pygame.transform.scale(pinkFish, (50, 50))
    pufferFish = pygame.image.load("graphics/pufferfish.png").convert()
    pufferFish.set_colorkey(BLACK)
    pufferFish = pygame.transform.scale(pufferFish, (40, 40))
    sharkFish = pygame.image.load("graphics/shark.png").convert()
    sharkFish.set_colorkey(BLACK)
    sharkFish = pygame.transform.scale(sharkFish, (80, 80))
    bottleFish = pygame.image.load("graphics/waterbottle.png").convert()
    bottleFish.set_colorkey(BLACK)
    bottleFish = pygame.transform.scale(bottleFish, (20, 30))
    bootFish = pygame.image.load("graphics/boot.png").convert()
    bootFish.set_colorkey(WHITE)
    bootFish = pygame.transform.scale(bootFish, (30, 30))
    returnMsg = font.render("Click Space to Return to Home Screen", True, (BLACK))
    # Blit each text and picture to the screen
    screen.blit(title,(220, 10))
    screen.blit(instruction1,[105, 70])
    screen.blit(instruction2,[105, 100])
    screen.blit(instruction3,[75, 130])
    screen.blit(instruction8,[160, 160])
    screen.blit(instruction6,[180, 190])
    screen.blit(instruction7,[100, 220])
    screen.blit(instruction4,[130, 260])
    screen.blit(instruction5,[370, 260])  
    screen.blit(orangeFish,(190, 320))
    screen.blit(blueFish,(240, 290))
    screen.blit(pinkFish,(160, 280))
    screen.blit(pufferFish,(380, 300))
    screen.blit(sharkFish,(455, 280))
    screen.blit(bottleFish,(430, 320))
    screen.blit(bootFish, (550, 300))
    screen.blit(returnMsg,[240, 380])

def drawScene8():
    # Game complete screen, set fonts, text and blit them
    font = pygame.font.SysFont("Calibri", 20, True)
    titleFont = pygame.font.SysFont("Calibri", 80, True)
    title = titleFont.render("GAME COMPLETED!", True, (BLACK))
    returnMsg = font.render("Click Space to Return to Main Menu", True, (BLACK))
    screen.blit(title,(20, 210))
    screen.blit(returnMsg,[200, 340])

def drawScene9():
    # Game menu screen, set fonts, text and blit them
    font = pygame.font.SysFont("Calibri", 20, True)
    levelFont = pygame.font.SysFont("Calibri", 30, True)
    titleFont = pygame.font.SysFont("Calibri", 60, True)
    title = titleFont.render("Main Menu", True, (AQUA))
    anyLevel = levelFont.render("Click Space to Play Normally", True, (BLACK))
    level1 = levelFont.render("Click 1 to skip to Level 1 - EASY", True, (BLACK))
    level2 = levelFont.render("Click 2 to skip tp Level 2 - NORMAL", True, (BLACK))
    level3 = levelFont.render("Click 3 to skip to Level 3 - HARD", True, (BLACK))
    returnMsg = font.render("Click Backspace to Return to Home Screen", True, (BLACK))
    screen.blit(title,(210, 20))
    screen.blit(anyLevel,[180, 100])
    screen.blit(level1,[150, 150])
    screen.blit(level2,[150, 200])
    screen.blit(level3,[150, 250])
    screen.blit(returnMsg,[185, 350])

# Initialize Pygame
pygame.init()
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Fish Rush by Kyle Andrade")

# Define colours
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE = (0, 138, 194)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
AQUA = (59, 89, 148)
SKYBLUE = (0, 182, 255)

# Change position of player fish depending on direction, based on information from: https://stackoverflow.com/questions/45601109/how-do-i-flip-an-image-horizontally-in-pygame?rq=1
# Image from: https://kenney.nl/assets/fish-pack
fishRight = pygame.image.load("graphics/userfish.png").convert()
fishLeft = pygame.transform.flip(fishRight, True, False)
fishRight.set_colorkey(BLACK)
fishRight = pygame.transform.scale(fishRight, (55, 55))
fishLeft.set_colorkey(BLACK)
fishLeft = pygame.transform.scale(fishLeft, (55, 55))

# Create a list of sprites
goodFishList = pygame.sprite.Group()
badFishList = pygame.sprite.Group()
 
# Create a list of every sprite
allSpritesList = pygame.sprite.Group()

# Create player fish
player = Player(100, 100)
allSpritesList.add(player)

# Loop until the user clicks the close button
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set variables
score = 0
level = 1
scene = 0
level1 = True
level2 = True
livesLeft = 3
level3 = True
valid = True

# Set default font and text
font = pygame.font.SysFont("Calibri", 20, True, False)
titleFont = pygame.font.SysFont("Calibri", 30, True, False)
scoreText = font.render("Score: ", True, BLACK)
levelText = titleFont.render("Level: ", True, BLACK)
livesText = font.render("Lives Left: ", True, BLACK)
level1Goal = font.render("/ 40", True, BLACK)
level2Goal = font.render("/ 45", True, BLACK)
level3Goal = font.render("/ 50", True, BLACK)

# Sound set up, True = On, False = Off
sound = True
if sound == True:
    # Sound from: https://freesound.org/people/jacksonacademyashmore/sounds/414209/
    gameEnd = pygame.mixer.Sound("sounds/gameend.wav")
    # Sound from: http://programarcadegames.com/index.php?chapter=lab_sprite_collecting&lang=en
    goodFish = pygame.mixer.Sound("sounds/goodfish.wav")
    # Sound from: https://freesound.org/people/jivatma07/sounds/122255/
    levelComplete = pygame.mixer.Sound("sounds/levelcomplete.wav")
    # Sound from: https://freesound.org/people/Tissman/sounds/444671/
    lifeLoss = pygame.mixer.Sound("sounds/lifeloss.wav")
    lifeLoss.set_volume(0.1)

# Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Title Screen -> Game Menu
                if scene == 0:
                    scene = 9
                # Level 1 -> Pause
                elif scene == 1:
                    scene = 2
                # Pause -> Level 1
                elif scene == 2 and level == 1:
                    scene = 1
                # Death -> Level 1
                elif scene == 3 and level == 1:
                    level1 = True
                    livesLeft = 3
                    scene = 1
                    valid = True
                # Level 1 Done -> Level 2
                elif scene == 5 and level == 1:
                    level = 2
                    scene2 = True
                    scene = 4
                    livesLeft = 3
                # Level 2 -> Pause
                elif scene == 4:
                    scene = 2
                # Pause -> Level 2
                elif scene == 2 and level == 2:
                    scene = 4
                # Death -> Level 2
                elif scene == 3 and level == 2:
                    level2 = True
                    livesLeft = 3
                    scene = 4
                    valid = True
                # Level 2 Done -> Level 3
                elif scene == 5 and level == 2:
                    level = 3
                    scene3 = True
                    scene = 6
                    livesLeft = 3
                # Level 3 -> Pause
                elif scene == 6:
                    scene = 2
                # Pause -> Level 3
                elif scene == 2 and level == 3:
                    scene = 6
                # Death -> Level 3
                elif scene == 3 and level == 3:
                    level3 = True
                    livesLeft = 3
                    scene = 6
                    valid = True
                # Level 3 Done -> Game Menu
                elif scene == 8 and level == 3:
                    scene = 9
                # Instructions -> Title Screen
                elif scene == 7:
                    scene = 0
                # Game Menu -> Play Normally 
                elif scene == 9:
                    level = 1
                    scene = 1
                    level1 = True
                    livesLeft = 3
                    valid = True
            # Title Screen -> Instructions
            if event.key == pygame.K_i:
                if scene == 0:
                    scene = 7
            # Game Menu -> Level 1
            if event.key == pygame.K_1:
                if scene == 9:
                    scene = 1
                    level = 1
                    level1 = True
                    livesLeft = 3
                    valid = True
            # Game Menu -> Level 2
            if event.key == pygame.K_2:
                if scene == 9:
                    scene = 4
                    level = 2
                    level2 = True
                    livesLeft = 3
                    valid = True
            # Game Menu -> Level 3
            if event.key == pygame.K_3:
                if scene == 9:
                    scene = 6
                    level = 3
                    level3 = True
                    livesLeft = 3
                    valid = True
            # Restart
            if event.key == pygame.K_r:
                if scene == 1 and level == 1:
                    level1 = True
                elif scene == 4 and level == 2:
                    level2 = True
                elif scene == 6 and level == 3:
                    level3 = True
            # Anywhere -> Main Menu
            if event.key == pygame.K_BACKSPACE:
                scene = 0
            # Set the player direction based on the key pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.changespeed(-3, 0)
                player.image = fishLeft
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.changespeed(3, 0)
                player.image = fishRight
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.changespeed(0, -3)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.changespeed(0, 3)
           
        # Stop moving the player when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.changespeed(3, 0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.changespeed(-3, 0)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                 player.changespeed(0, 3)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.changespeed(0, -3)

    if scene == 1 or scene == 4 or scene == 6:
        # See if the player block has collided with anything
        goodFishHitList = pygame.sprite.spritecollide(player, goodFishList, True)
        badFishHitList = pygame.sprite.spritecollide(player, badFishList, True)
 
        # Check the list of collisions and set score and lives left
        for fish in goodFishHitList:
            score += 1
            if sound == True:
                goodFish.play()
        for fish in badFishHitList:
            livesLeft -= 1
            if sound == True:
                if livesLeft == 2 or livesLeft == 1:
                    lifeLoss.play()

    # Update score and level
    scoreNumText = font.render(str(score), True, BLACK)
    levelNumText = titleFont.render(str(level), True, BLACK)

    # If player has no lives left, send them to the death screen
    if livesLeft < 1:
        scene = 3

    # If player has reached the score, send them to the next level screen
    if scene == 1 and score >= 40:
        scene = 5
        if sound == True:
            levelComplete.play()     

    # If player has reached the score, send them to the next level screen
    if scene == 4 and score >= 45:
        scene = 5
        if sound == True:
            levelComplete.play()

    # If player has reached the score, send them to the game complete screen
    if scene == 6 and score >= 50:
        scene = 8
        if sound == True:
            levelComplete.play()
    
    # Clear the screen
    screen.fill(BLACK)

    if scene == 0:
        # Set background, image from: https://stock.adobe.com/ca/search?k=desert+island+cartoon
        menuImage = pygame.image.load("graphics/mainmenu.png").convert()
        menuImage = pygame.transform.scale(menuImage, (screen_width, screen_height))
        screen.blit(menuImage, [0, 0])
        # Draw the rest of the scene by calling the function
        drawScene0()

    if scene == 1:
        # Set background, image from: https://opengameart.org/content/fish-set
        backgroundImage = pygame.image.load("graphics/background.png").convert()
        backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height))
        screen.blit(backgroundImage, [0, 0])
        if level1 == True:
            # Reset level and start game by calling the functions
            resetLevel()
            score = 0
            gameStart(15, 25, 7, 2, 1, 10, 3)
            # Create player fish
            player = Player(100, 100)
            allSpritesList.add(player)
            level1 = False
        # Update every sprite in the list
        allSpritesList.update()
        # Draw all the spites
        allSpritesList.draw(screen)
        # Blit the text
        screen.blit(scoreText, [30, 10])
        screen.blit(scoreNumText, [90, 10])
        screen.blit(level1Goal, [110, 10])
        screen.blit(levelText, [300, 10])
        screen.blit(levelNumText, [380, 10])
        screen.blit(livesText, [510, 10])
        # Enable health bar by calling the function
        healthBar()

    if scene == 2:
        # Set background, draw the rest of the scene by calling the function
        pauseImage = pygame.image.load("graphics/mainmenu.png").convert()
        pauseImage = pygame.transform.scale(pauseImage, (screen_width, screen_height))
        screen.blit(pauseImage, [0, 0])
        drawScene2()

    if scene == 3:
        # Set background, draw the rest of the scene by calling the function
        if sound == True:
            if valid == True:
                gameEnd.play()
                valid = False
        deathImage = pygame.image.load("graphics/mainmenu.png").convert()
        deathImage = pygame.transform.scale(deathImage, (screen_width, screen_height))
        screen.blit(deathImage, [0, 0])
        drawScene3()

    if scene == 4:
        # Set background and new level
        level = 2
        backgroundImage = pygame.image.load("graphics/background.png").convert()
        backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height))
        screen.blit(backgroundImage, [0, 0])
        if level2 == True:
            # Reset level and start game by calling the functions
            resetLevel()
            score = 0
            gameStart(25, 20, 10, 5, 2, 12, 7)
            # Create player fish
            player = Player(100, 100)
            allSpritesList.add(player)
            level2 = False
        # Update every sprite in the list
        allSpritesList.update()
        # Draw all the spites
        allSpritesList.draw(screen)
        # Blit the text
        screen.blit(scoreText, [30, 10])
        screen.blit(scoreNumText, [90, 10])
        screen.blit(level2Goal, [110, 10])
        screen.blit(levelText, [300, 10])
        screen.blit(levelNumText, [380, 10])
        screen.blit(livesText, [510, 10])
        # Enable health bar by calling the function
        healthBar()

    if scene == 5:
        # Set background, draw the rest of the scene by calling the function
        doneImage = pygame.image.load("graphics/mainmenu.png").convert()
        doneImage = pygame.transform.scale(doneImage, (screen_width, screen_height))
        screen.blit(doneImage, [0, 0])
        drawScene5()

    if scene == 6:
        # Set background and new level
        level = 3
        backgroundImage = pygame.image.load("graphics/background.png").convert()
        backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height))
        screen.blit(backgroundImage, [0, 0])
        if level3 == True:
            # Reset level and start game by calling the functions
            resetLevel()
            score = 0
            gameStart(30, 25, 15, 7, 2, 14, 9)
            # Create player fish
            player = Player(100, 100)
            allSpritesList.add(player)
            level3 = False
        # Update every sprite in the list
        allSpritesList.update()
        # Draw all the spites
        allSpritesList.draw(screen)
        # Blit the text
        screen.blit(scoreText, [30, 10])
        screen.blit(scoreNumText, [90, 10])
        screen.blit(level3Goal, [110, 10])
        screen.blit(levelText, [300, 10])
        screen.blit(levelNumText, [380, 10])
        screen.blit(livesText, [510, 10])
        # Enable health bar by calling the function
        healthBar()

    if scene == 7:
        # Set background, image from: https://pngtree.com/freebackground/cartoon-fresh-blue-underwater-diving-background_932234.html
        backgroundImage = pygame.image.load("graphics/underwater.png").convert()
        backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height))
        screen.blit(backgroundImage, [0, 0])
        # Draw the rest of the scene by calling the function
        drawScene7()

    if scene == 8:
        # Set background, draw the rest of the scene by calling the function
        doneImage = pygame.image.load("graphics/mainmenu.png").convert()
        doneImage = pygame.transform.scale(doneImage, (screen_width, screen_height))
        screen.blit(doneImage, [0, 0])
        drawScene8()
        # Reset all levels
        score = 0
        level1 = True
        level2 = True
        level3 = True

    if scene == 9:
        # Set background, draw the rest of the scene by calling the function
        menuImage = pygame.image.load("graphics/underwater.png").convert()
        menuImage = pygame.transform.scale(menuImage, (screen_width, screen_height))
        screen.blit(menuImage, [0, 0])
        drawScene9()
        
    # Update the screen with what is drawn
    pygame.display.flip()
 
    # Limit to 40 frames per second
    clock.tick(50)

# Close the window and quit
pygame.quit()