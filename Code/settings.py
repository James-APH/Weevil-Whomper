import pygame
from os.path import join
from enum import Enum


class Movement(Enum):
    LEFT = 1
    RIGHT = 2
    IDLE = 3
    JUMP = 4
    CROUCH = 5


WIDTH = 1280
HEIGHT = 640

BOUNDARY = 80

TILE_SIZE = 32

FRAME_RATE = 30

VELOCITY = 300


# Loading images here so constructor for player is not chaos
# IDLE
