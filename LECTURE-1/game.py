import random
import os
import time

WIDTH = 20
HEIGHT = 10

snake = [(5, 5)]
direction = "RIGHT"

food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))

score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear()

    # Draw board
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == snake[0]:
                print("O", end="")
            elif (x, y) in snake:
                print("o", end="")
            elif (x, y) == food:
                print("*", end="")
            else:
                print(".", end="")
        print()

    print(f"\nScore: {score}")
    print("Controls: W A S D")

    move = input("Move: ").upper()

    if move == "W":
        direction = "UP"
    elif move == "S":
        direction = "DOWN"
    elif move == "A":
        direction = "LEFT"
    elif move == "D":
        direction = "RIGHT"

    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= 1
    elif direction == "DOWN":
        head_y += 1
    elif direction == "LEFT":
        head_x -= 1
    elif direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)

    # Wall collision
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake
    ):
        print("\nGame Over!")
        print("Final Score:", score)
        break

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = (
            random.randint(0, WIDTH - 1),
            random.randint(0, HEIGHT - 1)
        )
    else:
        snake.pop()

    time.sleep(0.1)