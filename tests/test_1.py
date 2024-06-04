import os
import shutil
import pytest
import tempfile
from unittest.mock import MagicMock, patch
import pygame
import tkinter as tk
from main import Track, Player, PlayerApp

# Путь к тестовому MP3 файлу
TEST_MP3_PATH = os.path.join(os.path.dirname(__file__), 'test.mp3')

# Тестирование класса Track
def test_track_initialization():
    track = Track(TEST_MP3_PATH)
    assert track.file_path == TEST_MP3_PATH
    assert track.title == os.path.basename(TEST_MP3_PATH)

def test_track_str():
    track = Track(TEST_MP3_PATH)
    assert str(track) == os.path.basename(TEST_MP3_PATH)

# Тестирование класса Player
@pytest.fixture
def player():
    with patch('pygame.mixer.init'):
        return Player()

def test_load_tracks(player, tmpdir):
    shutil.copy(TEST_MP3_PATH, tmpdir.join("song1.mp3"))
    shutil.copy(TEST_MP3_PATH, tmpdir.join("song2.mp3"))
    player.load_tracks(tmpdir)
    assert len(player.track_list) == 2
    assert player.track_list[0].title == "song1.mp3"
    assert player.track_list[1].title == "song2.mp3"

def test_play_track(player, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    player.track_list = [Track(song1)]
    with patch('pygame.mixer.music.play'):
        track_title = player.play_track()
    assert track_title == "song1.mp3"

def test_pause_track(player, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    player.track_list = [Track(song1)]
    with patch('pygame.mixer.music.pause'):
        player.play_track()
        player.pause_track()
        assert player.is_paused
        player.pause_track()
        assert not player.is_paused

def test_stop_track(player):
    with patch('pygame.mixer.music.stop'):
        player.stop_track()
    # Не нужно ничего проверять, просто убедимся, что нет исключений.

def test_next_track(player, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    song2 = tmpdir.join("song2.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    shutil.copy(TEST_MP3_PATH, song2)
    player.track_list = [Track(song1), Track(song2)]
    player.current_track_index = 0
    with patch('pygame.mixer.music.play'):
        track_title = player.next_track()
    assert track_title == "song2.mp3"
    assert player.current_track_index == 1

def test_prev_track(player, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    song2 = tmpdir.join("song2.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    shutil.copy(TEST_MP3_PATH, song2)
    player.track_list = [Track(song1), Track(song2)]
    player.current_track_index = 1
    with patch('pygame.mixer.music.play'):
        track_title = player.prev_track()
    assert track_title == "song1.mp3"
    assert player.current_track_index == 0

def test_toggle_mute(player):
    with patch('pygame.mixer.music.get_volume', return_value=1.0), \
         patch('pygame.mixer.music.set_volume') as mock_set_volume:
        player.toggle_mute()
        mock_set_volume.assert_called_with(0.0)

        # Сбросим мок
        mock_set_volume.reset_mock()

        with patch('pygame.mixer.music.get_volume', return_value=0.0):
            player.toggle_mute()
        mock_set_volume.assert_called_with(1.0)

# Тестирование класса PlayerApp
@pytest.fixture
def player_app():
    with patch('tkinter.Tk') as mock_tk:
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        return PlayerApp()

def test_load_directory(player_app, tmpdir):
    shutil.copy(TEST_MP3_PATH, tmpdir.join("song1.mp3"))
    shutil.copy(TEST_MP3_PATH, tmpdir.join("song2.mp3"))
    player_app.player.load_tracks(tmpdir)
    player_app.update_playlist()
    assert player_app.playlist_box.size() ==
