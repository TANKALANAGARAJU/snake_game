import pygame
import sys
import random

# Initialize the pygame
pygame.init()

# Set the screen size
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game window
pygame.display.set_caption("Snake Game")

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set the font
font = pygame.font.SysFont(None, 50)

# Set the game variables
snake_speed = 10
snake_block = 10
snake_list = []
snake_length = 1

# Set the initial position for the snake (center of the screen)
snek_x = screen_width // 2
snek_y = screen_height // 2

# Set the movement direction
direction = "right"

# Set the food variables
food_x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
food_y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
food_spawn = True

# Set the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Fill the background color
    screen.fill(white)

    # Draw the snake
    snake_color = blue
    for x in snake_list:
        pygame.draw.rect(screen, snake_color, (x[0], x[1], snake_block, snake_block))

    # Spawn the food
    pygame.draw.rect(screen, red, (food_x, food_y, snake_block, snake_block))

    # Event handling for key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # Update the snake position
    if direction == "left":
        snek_x -= snake_block
    elif direction == "right":
        snek_x += snake_block
    elif direction == "up":
        snek_y -= snake_block
    elif direction == "down":
        snek_y += snake_block

    # Add the new head position to the snake list
    snake_head = [snek_x, snek_y]
    snake_list.append(snake_head)

    # Check if the snake has eaten the food
    if snek_x == food_x and snek_y == food_y:
        food_x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
        food_y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
        snake_length += 1
    else:
        # Remove the last element of the snake list if it hasn't grown
        if len(snake_list) > snake_length:
            del snake_list[0]

    # Check for collision with boundaries
    if snek_x >= screen_width or snek_x < 0 or snek_y >= screen_height or snek_y < 0:
        game_over()

    # Check for collision with the tail
    for block in snake_list[:-1]:
        if snek_x == block[0] and snek_y == block[1]:
            game_over()

    # Display the score
    score_text = font.render("Score: " + str(snake_length - 1), True, black)
    score_rect = score_text.get_rect()
    score_rect.center = (screen_width / 2, 10)
    screen.blit(score_text, score_rect)

    # Update the screen
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

def game_over():
    # Game over text
    game_over_text = font.render("Game Over", True, red)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(game_over_text, game_over_rect)

    # Display the score
    score_text = font.render("Score: " + str(snake_length - 1), True, black)
    score_rect = score_text.get_rect()
    score_rect.center = (screen_width / 2, screen_height / 2 + 50)
    screen.blit(score_text, score_rect)

    # Update the screen
    pygame.display.update()

    # Wait for a while before quitting
    pygame.time.wait(3000)

    # Quit the game
    pygame.quit()
    sys.exit()
