import os
import shutil
import pytest
import pygame
from main import Track, Player, PlayerApp
import tkinter as tk


# Path to the test MP3 file
TEST_MP3_PATH = os.path.join(os.path.dirname(__file__), 'test.mp3')

# Test Track class
def test_track_initialization():
    track = Track(TEST_MP3_PATH)
    assert track.file_path == TEST_MP3_PATH
    assert track.title == os.path.basename(TEST_MP3_PATH)

def test_track_str():
    track = Track(TEST_MP3_PATH)
    assert str(track) == os.path.basename(TEST_MP3_PATH)

# Test Player class
@pytest.fixture
def player():
    pygame.mixer.init()
    return Player()

def test_load_tracks(player, tmpdir):
    shutil.copy(TEST_MP3_PATH, tmpdir.join("song1.mp3"))
    shutil.copy(TEST_MP3_PATH, tmpdir.join("song2.mp3"))
    player.load_tracks(tmpdir)
    assert len(player.track_list) == 2
    assert player.track_list[0].title == "song1.mp3"
    assert player.track_list[1].title == "song2.mp3"

def test_load_tracks_no_files(player, tmpdir):
    assert not player.load_tracks(str(tmpdir))

def test_play_track_with_track_index(player, tmpdir):
    # Подготавливаем данные для теста
    song1 = tmpdir.join("song1.mp3")
    song2 = tmpdir.join("song2.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    shutil.copy(TEST_MP3_PATH, song2)
    player.track_list = [Track(song1), Track(song2)]

    # Устанавливаем индекс текущего трека на нулевой
    player.current_track_index = 0

    # Вызываем метод play_track с указанием индекса трека
    player.play_track(track_index=1)

    # Проверяем, что индекс текущего трека изменился на 1
    assert player.current_track_index == 1

def test_play_track_empty_track_list(player):
    # Проверяем, что метод возвращает пустую строку при пустом списке треков
    assert player.play_track() == ""

def test_play_track(player, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    player.track_list = [Track(song1)]
    track_title = player.play_track()
    assert track_title == "song1.mp3"

def test_pause_track(player, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    player.track_list = [Track(song1)]
    player.play_track()
    player.pause_track()
    assert player.is_paused
    player.pause_track()
    assert not player.is_paused

def test_stop_track(player):
    player.stop_track()
    # Since we're not mocking, we can't assert on mixer calls. Just ensure no exceptions.

def test_next_track(player, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    song2 = tmpdir.join("song2.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    shutil.copy(TEST_MP3_PATH, song2)
    player.track_list = [Track(song1), Track(song2)]
    player.current_track_index = 0
    track_title = player.next_track()
    assert track_title == "song2.mp3"
    assert player.current_track_index == 1

def test_next_track_empty_track_list(player):
    # Проверяем, что метод возвращает пустую строку при пустом списке треков
    assert player.next_track() == ""

def test_prev_track(player, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    song2 = tmpdir.join("song2.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    shutil.copy(TEST_MP3_PATH, song2)
    player.track_list = [Track(song1), Track(song2)]
    player.current_track_index = 1
    track_title = player.prev_track()
    assert track_title == "song1.mp3"
    assert player.current_track_index == 0

def test_prev_track_empty_track_list(player):
    # Проверяем, что метод возвращает пустую строку при пустом списке треков
    assert player.prev_track() == ""
def test_toggle_mute(player):
    pygame.mixer.music.set_volume(0.0)
    correct_mute_vol = pygame.mixer.music.get_volume()
    player.toggle_mute()
    player.toggle_mute()
    muted_volume = pygame.mixer.music.get_volume()
    assert muted_volume == correct_mute_vol


def test_toggle_unmute(player):
    pygame.mixer.music.set_volume(1.0)
    initial_volume = pygame.mixer.music.get_volume()
    player.toggle_mute()
    player.toggle_mute()
    unmuted_volume = pygame.mixer.music.get_volume()

    assert unmuted_volume == initial_volume

# Test PlayerApp class
@pytest.fixture
def player_app():
    root = tk.Tk()
    app = PlayerApp(root)
    return app

def test_load_directory(player_app, tmpdir):
    shutil.copy(TEST_MP3_PATH, tmpdir.join("song1.mp3"))
    shutil.copy(TEST_MP3_PATH, tmpdir.join("song2.mp3"))
    player_app.player.load_tracks(tmpdir)
    player_app.update_playlist()
    assert player_app.playlist_box.size() == 2


def test_play_track_app(player_app, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    player_app.player.track_list = [Track(song1)]
    player_app.play_track()
    assert player_app.track_label.cget("text") == "Now playing: song1.mp3"

def test_next_track_app(player_app, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    song2 = tmpdir.join("song2.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    shutil.copy(TEST_MP3_PATH, song2)
    player_app.player.track_list = [Track(song1), Track(song2)]
    player_app.player.current_track_index = 0
    player_app.next_track()
    assert player_app.track_label.cget("text") == "Now playing: song2.mp3"

def test_prev_track_app(player_app, tmpdir):
    song1 = tmpdir.join("song1.mp3")
    song2 = tmpdir.join("song2.mp3")
    shutil.copy(TEST_MP3_PATH, song1)
    shutil.copy(TEST_MP3_PATH, song2)
    player_app.player.track_list = [Track(song1), Track(song2)]
    player_app.player.current_track_index = 1
    player_app.prev_track()
    assert player_app.track_label.cget("text") == "Now playing: song1.mp3"

def test_update_track_label_no_track(player_app, tmpdir):
    # Вызываем метод update_track_label без аргументов
    player_app.update_track_label()

    # Проверяем, что метка трека обновлена с текстом "No track loaded"
    assert player_app.track_label.cget("text") == "No track loaded"


def test_on_playlist_select(player_app, tmpdir):
    # Подготавливаем тестовые файлы и добавляем их в плейлист
    song1_path = tmpdir.join("song1.mp3")
    song2_path = tmpdir.join("song2.mp3")
    song1_path.write("dummy content")
    song2_path.write("dummy content")
    player_app.player.load_tracks(tmpdir)

    # Выбираем второй трек из плейлиста (индекс 1)
    player_app.playlist_box.select_set(1)

    # Вызываем метод on_playlist_select
    player_app.on_playlist_select(None)

    # Проверяем, что метод play_track был вызван с правильным аргументом (индекс выбранного трека)
    assert player_app.player.current_track_index == 0
