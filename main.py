import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame


class Track:
    def __init__(self, file_path):
        self.file_path = file_path
        self.title = os.path.basename(file_path)

    def __str__(self):
        return self.title


class Player:
    def __init__(self):
        self.track_list = []
        self.current_track_index = 0
        self.is_paused = False
        pygame.mixer.init()

    def load_tracks(self, directory):
        self.track_list = []
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if file.endswith('.mp3') and os.access(file_path, os.R_OK):
                self.track_list.append(Track(file_path))
        if not self.track_list:
            messagebox.showerror("Error", "No readable MP3 files found in the directory")
        self.current_track_index = 0

    def play_track(self, track_index=None):
        if self.track_list:
            if track_index is not None:
                self.current_track_index = track_index
            pygame.mixer.music.load(self.track_list[self.current_track_index].file_path)
            pygame.mixer.music.play()
            self.is_paused = False
            return str(self.track_list[self.current_track_index])
        return ""

    def pause_track(self):
        if self.track_list:
            if self.is_paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
            self.is_paused = not self.is_paused

    def stop_track(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if self.track_list:
            self.current_track_index = (self.current_track_index + 1) % len(self.track_list)
            return self.play_track()
        return ""

    def prev_track(self):
        if self.track_list:
            self.current_track_index = (self.current_track_index - 1) % len(self.track_list)
            return self.play_track()
        return ""

    def toggle_mute(self):
        pygame.mixer.music.set_volume(0 if pygame.mixer.music.get_volume() > 0 else 1)


class PlayerApp:
    def __init__(self, root):
        self.player = Player()
        self.root = root
        self.root.title("Music Player")

        self.load_button = tk.Button(root, text="Load Directory", command=self.load_directory)
        self.load_button.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_track)
        self.play_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.player.pause_track)
        self.pause_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_track)
        self.next_button.pack()

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_track)
        self.prev_button.pack()

        self.mute_button = tk.Button(root, text="Mute/Unmute", command=self.player.toggle_mute)
        self.mute_button.pack()

        self.track_label = tk.Label(root, text="No track loaded")
        self.track_label.pack()

        self.playlist_box = tk.Listbox(root)
        self.playlist_box.pack(fill=tk.BOTH, expand=True)
        self.playlist_box.bind('<<ListboxSelect>>', self.on_playlist_select)

    def load_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.player.load_tracks(directory)
            self.update_playlist()
            self.update_track_label()

    def play_track(self):
        track_title = self.player.play_track()
        self.update_track_label(track_title)
        self.update_playlist_selection()

    def next_track(self):
        track_title = self.player.next_track()
        self.update_track_label(track_title)
        self.update_playlist_selection()

    def prev_track(self):
        track_title = self.player.prev_track()
        self.update_track_label(track_title)
        self.update_playlist_selection()

    def on_playlist_select(self, event):
        if self.playlist_box.curselection():
            selected_index = self.playlist_box.curselection()[0]
            track_title = self.player.play_track(selected_index)
            self.update_track_label(track_title)
            self.update_playlist_selection()

    def update_track_label(self, track_title=""):
        if track_title:
            self.track_label.config(text=f"Now playing: {track_title}")
        else:
            self.track_label.config(text="No track loaded")

    def update_playlist(self):
        self.playlist_box.delete(0, tk.END)
        for track in self.player.track_list:
            self.playlist_box.insert(tk.END, str(track))
        self.update_playlist_selection()

    def update_playlist_selection(self):
        self.playlist_box.selection_clear(0, tk.END)
        self.playlist_box.selection_set(self.player.current_track_index)
        self.playlist_box.activate(self.player.current_track_index)


if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerApp(root)
    root.mainloop()
