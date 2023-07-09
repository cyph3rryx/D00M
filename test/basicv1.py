import os
import sys
import random

# Game configuration
MAP_WIDTH = 20
MAP_HEIGHT = 10
PLAYER_CHAR = "P"
ENEMY_CHAR = "E"
EXIT_CHAR = "X"
WALL_CHAR = "#"
EMPTY_CHAR = " "

# Player starting position
player_x = random.randint(0, MAP_WIDTH - 1)
player_y = random.randint(0, MAP_HEIGHT - 1)

# Enemy starting position
enemy_x = random.randint(0, MAP_WIDTH - 1)
enemy_y = random.randint(0, MAP_HEIGHT - 1)

# Exit position
exit_x = random.randint(0, MAP_WIDTH - 1)
exit_y = random.randint(0, MAP_HEIGHT - 1)

# Game loop
while True:
    # Clear the terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Create the map
    map_data = [[EMPTY_CHAR for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    map_data[player_y][player_x] = PLAYER_CHAR
    map_data[enemy_y][enemy_x] = ENEMY_CHAR
    map_data[exit_y][exit_x] = EXIT_CHAR

    # Print the map
    for row in map_data:
        print("".join(row))

    # Check for game over conditions
    if (player_x, player_y) == (exit_x, exit_y):
        print("Congratulations! You found the exit.")
        sys.exit(0)
    elif (player_x, player_y) == (enemy_x, enemy_y):
        print("Game Over! You were caught by an enemy.")
        sys.exit(0)

    # Get user input
    move = input("Enter your move (W/A/S/D): ").upper()

    # Update player position based on input
    if move == "W" and player_y > 0:
        player_y -= 1
    elif move == "A" and player_x > 0:
        player_x -= 1
    elif move == "S" and player_y < MAP_HEIGHT - 1:
        player_y += 1
    elif move == "D" and player_x < MAP_WIDTH - 1:
        player_x += 1
