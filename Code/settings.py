import pygame
from os import walk
from os import listdir
from os.path import join
from enum import Enum


class Movement(str, Enum):
    LEFT = "Left_Walk_Leaf"
    RIGHT = "Right_Walk_Leaf"
    IDLE = "Idle_Leaf"
    JUMP = "Jump_Leaf"
    CROUCH = "Crouch_Leaf"


class Splash(str, Enum):
    TITLE = "Title_Screen"
    WIN = "Win_Screen"
    LOSE = "Lose_Screen"
    NONE = "NONE"


class Button_State(str, Enum):
    PRESSED = "pressed"
    NONE = "NONE"


WIDTH = 1280
HEIGHT = 640

BOUNDARY = 80

TILE_SIZE = 32

FRAME_RATE = 30

VELOCITY = 300


# Loading images here so constructor for player is not chaos
# IDLE
