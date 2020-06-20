import pygame
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()
# Define some colors
GREY =(230, 230, 230)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =(0, 0, 255)
YELLOW = (255 ,255, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 45
HEIGHT = 45
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
start = grid[0][0] = -1
end = grid[9][9] = 2
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [505, 550]
screen = pygame.display.set_mode(WINDOW_SIZE)
icon = pygame.image.load('maze.png')
pygame.display.set_icon(icon)
font = pygame.font.SysFont('comicsansms', 25)
text = font.render("Press 'Space' to start.", True, RED, GREY)
textRect = text.get_rect()
textRect.center = (160, 525) 
 
# Set title of screen
pygame.display.set_caption("Maze Solver")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def search(x, y):
    if grid[x][y] == 2:
        return True
    elif grid[x][y] == 1:
        return False
    elif grid[x][y] == 3:
        return False
    grid[x][y] = 3
    
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
            return True
	
    return False
	
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            grid[0][0] = -1
            grid[9][9] = 2
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mouse.set_visible(False)
                success = search(0, 0)
                grid[0][0] = -1
                for row in range(10):
                    for column in range(10):
                        if grid[row][column] == 3:
                            color = BLUE
                            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
                            pygame.display.update()
                            pygame.time.wait(100)
                if success == True:
                    messagebox.showinfo('Path Found', 'Success')
                else:
                    messagebox.showinfo('Path Not Found', 'Failure')
 
    # Set the screen background
    screen.fill(GREY)
    screen.blit(text, textRect)
 
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == -1:
                color = YELLOW
            if grid[row][column] == 1:
                color = GREEN
            if grid[row][column] == 2:
                color = RED
            #if grid[row][column] == 3:
                #color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
