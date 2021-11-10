# tsnake 1.0.0 by Mirodyn
import keyboard
import os
import time
import random


def draw_map():
    global height
    global width
    map = ''
    for y in range(0, height):
        for x in range(0, width):
            if snake_hit(x, y):
                map += 'O'
            elif food_hit(x, y):
                map += 'X'
            elif border_hit(x, y):
                map += '#'
            else:
                map += ' '
        if (y < height):
            map += '\n'
    return map


def feed_snake():
    global snake
    x = snake[len(snake)-1][0]
    y = snake[len(snake)-1][1]
    d = snake[len(snake)-1][2]

    if d == 1:
        snake.append([x, y+1, d])
    if d == 2:
        snake.append([x, y-1, d])
    if d == 3:
        snake.append([x+1, y, d])
    if d == 4:
        snake.append([x-1, y, d])


def move_snake(direction):
    global snake
    for i in range(1, len(snake)):
        snake[len(snake)-i][0] = snake[len(snake)-i-1][0]
        snake[len(snake)-i][1] = snake[len(snake)-i-1][1]
        snake[len(snake)-i][2] = snake[len(snake)-i-1][2]

    if direction == 1:
        snake[0][1] -= 1
    if direction == 2:
        snake[0][1] += 1
    if direction == 3:
        snake[0][0] -= 1
    if direction == 4:
        snake[0][0] += 1
    snake[0][2] = direction


def check_snake():
    global snake
    global height
    global width

    if border_hit(snake[0][0], snake[0][1]):
        return False
    return not snake_hit(snake[0][0], snake[0][1], 1)


def snake_hit(x, y, offset=0):
    global snake
    for i in range(offset, len(snake)):
        if snake[i][0] == x and snake[i][1] == y:
            return True
    return False


def food_hit(x, y):
    global foodx
    global foody

    if x == foodx and y == foody:
        return True
    else:
        return False


def border_hit(x, y):
    global width
    global height
    if (x == width - 1 or x == 0) or (y == height - 1 or y == 0):
        return True
    else:
        return False


def make_food():
    global foodx
    global foody
    foodx = random.randint(1, width-1)
    foody = random.randint(1, height-1)
    while snake_hit(foodx, foody) and border_hit(foodx, foody):
        foodx = random.randint(1, width-1)
        foody = random.randint(1, height-1)


def init():
    global score
    global snake
    global direction
    global tickcounter
    global gamespeed
    score = 0
    # init snake
    # body tuple X,Y,direction
    head = [11, 9, 1]
    snake = [head]
    # init snakes direction
    # 1 up, 2 down, 3 left, 4 right
    direction = 1
    # init food location
    make_food()
    tickcounter = 1
    gamespeed = 3


random.seed(None)

# default map size
width = 21
height = 17

# global vars
score = 0
direction = 1
snake = []
foodx = 0
foody = 0
tickcounter = 0
gamespeed = 0
init()


# draw_map()

while True:
    time.sleep(0.1)
    if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
        if direction != 2 or len(snake) == 1:
            direction = 1
    if keyboard.is_pressed('s') or keyboard.is_pressed('down'):
        if direction != 1 or len(snake) == 1:
            direction = 2
    if keyboard.is_pressed('a') or keyboard.is_pressed('left'):
        if direction != 4 or len(snake) == 1:
            direction = 3
    if keyboard.is_pressed('d') or keyboard.is_pressed('right'):
        if direction != 3 or len(snake) == 1:
            direction = 4
    if keyboard.is_pressed('r'):
        init()
    if keyboard.is_pressed('p'):
        while True:
            if keyboard.is_pressed('u'):
                break
    if keyboard.is_pressed('q'):
        break

    if (tickcounter == gamespeed):
        tickcounter = 1
        # turn_snake(direction)
        move_snake(direction)

        if not check_snake():
            print('--------------------')
            print('Game over!')
            print('SCORE: ' + str(score))
            print('--------------------')
            break
        else:
            if food_hit(snake[0][0], snake[0][1]):
                feed_snake()
                make_food()
                score += 1
            os.system('clear')
            print(draw_map())
            print('movement: w,a,s,d')
            print('pause: p | unpause: u')
            print('quit: q  | restart: r')

    tickcounter += 1
