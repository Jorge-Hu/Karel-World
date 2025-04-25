"""
File: Steeplechase.py
Name: Jorge
---------------------------------

"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    # error:not able to stop in the end
    # while front_is_clear():
    #    move()
    #
    # while not front_is_clear():
    #     jump()
    #     while front_is_clear():
    #         move()
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-condition:Karel is on the left side of the wall, facing East
    post-condition:Karel is on the right of the wall, facing East
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is on the left side of the wall, facing East
    post-condition:Karel is on the upper left, facing East
    """
    # alternative
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_left()
    #     turn_left()
    #     turn_left()
    turn_left()
    while not right_is_clear():
        move()
    turn_right()


def cross():
    """
    pre-condition:Karel is at the upper left, facing East
    post-condition:Karel is at the upper right, facing South
    """
    move()
    turn_right()


def down():
    """
    pre-condition:Karel is at the upper right, facing South
    post-condition:Karel is at the right side of the wall, facing East
    """
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
