"""
File: StepUp.py
Name: Jorge:
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def karel_spin():
    for i in range(4):
        turn_left()

def put_beeper99():
    for i in range(99):
        put_beeper()

def main():
    #algorithm
    move()
    pick_beeper()
    karel_spin()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper99()
    move()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
