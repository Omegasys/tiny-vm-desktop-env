# gui.py
import tkinter as tk
from tkinter import PhotoImage
import json
import os

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tiny VM Desktop")
        self.load_config()
        self.load_theme()
        self.create_widgets()

    def load_config(self):
        """Load configuration settings from default_config.json."""
        config_path = "config/default_config.json"
        with open(config_path, 'r') as file:
            self.config = json.load(file)

    def load_theme(self):
        """Load the current theme from the theme directory."""
        theme_name = self.config.get("theme", "light")
        theme_path = f"assets/themes/{theme_name}.json"
        with open(theme_path, 'r') as file:
            self.theme = json.load(file)

    def create_widgets(self):
        """Creates the GUI elements."""
        self.root.configure(bg=self.theme["background"])

        self.vm_status_label = tk.Label(self.root, text="VM Status: Stopped", bg=self.theme["background"], fg=self.theme["text_color"])
        self.vm_status_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start VM", command=self.start_vm,
                                      bg=self.theme["button_background"], fg=self.theme["button_text"])
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop VM", command=self.stop_vm,
                                     bg=self.theme["button_background"], fg=self.theme["button_text"])
        self.stop_button.pack(pady=5)

        # Load icon for the start button
        self.start_button_icon = PhotoImage(file="assets/icons/start_button_icon.png")
        self.start_button.config(image=self.start_button_icon, compound=tk.LEFT)

        # Load icon for the stop button
        self.stop_button_icon = PhotoImage(file="assets/icons/stop_button_icon.png")
        self.stop_button.config(image=self.stop_button_icon, compound=tk.LEFT)

    def start_vm(self):
        """Handles the start VM button click."""
        self.vm_status_label.config(text="VM Status: Running", bg=self.theme["background"], fg=self.theme["text_color"])
        print("Start VM triggered.")

    def stop_vm(self):
        """Handles the stop VM button click."""
        self.vm_status_label.config(text="VM Status: Stopped", bg=self.theme["background"], fg=self.theme["text_color"])
        print("Stop VM triggered.")

    def run(self):
        """Starts the GUI."""
        self.root.mainloop()
