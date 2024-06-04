import os
import pytest
import pygame
from main import Track, Player

def test_load_tracks_success():
    player = Player()
    player.load_tracks('~/zaebushek/Загрузки')
    assert len(player.track_list) > 0
