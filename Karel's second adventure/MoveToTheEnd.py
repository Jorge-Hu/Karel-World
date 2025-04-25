"""
File: MoveToTheEnd.py
Name:Jorge
------------------------
This file shows how to use while loop
to walk to the end of a certain row in
karel world
"""

from karel.stanfordkarel import *

def mtte():
    """
    Karel will move to the end of the first Street in any world
    """
    while front_is_clear():
        move()


def main():
    mtte()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
