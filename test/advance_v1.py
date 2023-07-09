import curses
import random

# Game configuration
MAP_WIDTH = 20
MAP_HEIGHT = 10
PLAYER_CHAR = "P"
ENEMY_CHAR = "E"
EXIT_CHAR = "X"
WALL_CHAR = "#"
EMPTY_CHAR = " "
PROJECTILE_CHAR = "*"

# Player starting position
player_x = random.randint(0, MAP_WIDTH - 1)
player_y = random.randint(0, MAP_HEIGHT - 1)

# Enemy starting position
enemy_x = random.randint(0, MAP_WIDTH - 1)
enemy_y = random.randint(0, MAP_HEIGHT - 1)

# Exit position
exit_x = random.randint(0, MAP_WIDTH - 1)
exit_y = random.randint(0, MAP_HEIGHT - 1)

# Projectile properties
projectile_x = -1
projectile_y = -1
projectile_direction = None
projectile_active = False

# Initialize curses
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.nodelay(1)
stdscr.timeout(100)

# Function to draw the game screen
def draw_game(stdscr):
    # Clear the screen
    stdscr.clear()

    # Draw the walls
    for x in range(MAP_WIDTH):
        stdscr.addch(0, x, WALL_CHAR)
        stdscr.addch(MAP_HEIGHT + 1, x, WALL_CHAR)
    for y in range(MAP_HEIGHT):
        stdscr.addch(y + 1, 0, WALL_CHAR)
        stdscr.addch(y + 1, MAP_WIDTH - 1, WALL_CHAR)

    # Draw the player, enemy, and exit
    stdscr.addch(player_y + 1, player_x + 1, PLAYER_CHAR)
    stdscr.addch(enemy_y + 1, enemy_x + 1, ENEMY_CHAR)
    stdscr.addch(exit_y + 1, exit_x + 1, EXIT_CHAR)

    # Draw the projectile if active
    if projectile_active:
        stdscr.addch(projectile_y + 1, projectile_x + 1, PROJECTILE_CHAR)

    # Refresh the screen
    stdscr.refresh()

# Main game loop
while True:
    # Get user input
    key = stdscr.getch()

    # Quit the game
    if key == ord('q'):
        break

    # Update player position based on input
    if key == ord('w') and player_y > 0:
        player_y -= 1
    elif key == ord('a') and player_x > 0:
        player_x -= 1
    elif key == ord('s') and player_y < MAP_HEIGHT - 1:
        player_y += 1
    elif key == ord('d') and player_x < MAP_WIDTH - 1:
        player_x += 1

    # Update projectile position and check for collision
    if projectile_active:
        if projectile_direction == 'up':
            if projectile_y > 0:
                projectile_y -= 1
            else:
                projectile_active = False
        elif projectile_direction == 'down':
            if projectile_y < MAP_HEIGHT - 1:
                projectile_y += 1
            else:
                projectile_active = False
        elif projectile_direction == 'left':
            if projectile_x > 0:
                projectile_x -= 1
            else:
                projectile_active = False
        elif projectile_direction == 'right':
            if projectile_x < MAP_WIDTH - 1:
                projectile_x += 1
            else:
                projectile_active = False

        # Check for collision with enemy or wall
        if (projectile_x, projectile_y) == (enemy_x, enemy_y) or stdscr.inch(projectile_y + 1, projectile_x + 1) == ord(WALL_CHAR):
            projectile_active = False

    # Shoot projectile
    if key == ord(' '):
        if not projectile_active:
            projectile_x = player_x
            projectile_y = player_y
            projectile_direction = 'up'
            projectile_active = True

    # Check for game over conditions
    if (player_x, player_y) == (exit_x, exit_y):
        stdscr.addstr(MAP_HEIGHT + 2, 0, "Congratulations! You found the exit.")
        break
    elif (player_x, player_y) == (enemy_x, enemy_y):
        stdscr.addstr(MAP_HEIGHT + 2, 0, "Game Over! You were caught by an enemy.")
        break

    # Draw the game screen
    draw_game(stdscr)

# End curses
curses.endwin()
