# gui.py
import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tiny VM Desktop")
        self.create_widgets()

    def create_widgets(self):
        """Creates the GUI elements."""
        self.vm_status_label = tk.Label(self.root, text="VM Status: Stopped")
        self.vm_status_label.pack(pady=10)
        
        self.start_button = tk.Button(self.root, text="Start VM", command=self.start_vm)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop VM", command=self.stop_vm)
        self.stop_button.pack(pady=5)

    def start_vm(self):
        """Handles the start VM button click."""
        self.vm_status_label.config(text="VM Status: Running")
        print("Start VM triggered.")
        
    def stop_vm(self):
        """Handles the stop VM button click."""
        self.vm_status_label.config(text="VM Status: Stopped")
        print("Stop VM triggered.")
        
    def run(self):
        """Starts the GUI."""
        self.root.mainloop()
