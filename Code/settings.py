import pygame
from os.path import join
from enum import Enum


# {"Idle_Leaf": [], "Right_Walk_Leaf": [], "Left_Walk_Leaf": []}
class Movement(str, Enum):
    LEFT = "Idle_Leaf"
    RIGHT = "Right_Walk_Leaf"
    IDLE = "Left_Walk_Leaf"
    JUMP = "Jump_Leaf"
    CROUCH = "Crouch_Leaf"


WIDTH = 1280
HEIGHT = 640

BOUNDARY = 80

TILE_SIZE = 32

FRAME_RATE = 30

VELOCITY = 300


# Loading images here so constructor for player is not chaos
# IDLE
