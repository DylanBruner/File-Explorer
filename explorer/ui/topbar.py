import os
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
from consts import *

class TopBar:
    def __init__(self, window):
        self.frame = tk.Frame(window, height=50, bg=BG_ONE)

        self._EVENT_HOOKS = {
            'on_path_change': [],
        }

        backward_img = ImageTk.PhotoImage(images['arrow_back'])
        self.back_button = tk.Button(self.frame, image=backward_img, bg=BG_ONE, fg=BG_ONE, bd=0,
                                     command=self.on_back_button_click)
        forward_image = ImageTk.PhotoImage(images['arrow_forward'])
        self.forward_button = tk.Button(self.frame, image=forward_image, bg=BG_ONE, fg=BG_ONE, bd=0,
                                        command=self.on_forward_button_click)
        up_image = ImageTk.PhotoImage(images['arrow_upward'])
        self.up_button = tk.Button(self.frame, image=up_image, bg=BG_ONE, fg=BG_ONE, bd=0,
                                   command=self.on_up_button_click)
        refresh_image = ImageTk.PhotoImage(images['refresh'])
        self.refresh_button = tk.Button(self.frame, image=refresh_image, bg=BG_ONE, fg=BG_ONE, bd=0,
                                        command=self.on_refresh_button_click)
        # set border color to BORDER_COLOR
        self.path_entry = tk.Entry(self.frame, bg=BG_ONE, fg=toHex((255, 255, 255)),
                            font=("Segoe UI", 10), highlightcolor=BORDER_COLOR, 
                            insertbackground="white", relief=tk.SOLID,
                            insertwidth=1)
        self.path_entry.bind("<Return>", lambda e: self.on_update_path())
        self.path_entry.insert(0, os.getcwd())
        self.search_entry = tk.Entry(self.frame, width=25, bg=BG_ONE, fg=toHex((255, 255, 255)),
                                font=("Segoe UI", 10), highlightcolor=BORDER_COLOR,
                                insertbackground="white", relief=tk.SOLID,
                                insertwidth=1)
        self.search_entry.bind("<Return>", lambda e: self.on_update_search())

        self.back_button.grid(row=0, column=0, padx=5, pady=5)
        self.forward_button.grid(row=0, column=1, padx=5, pady=5)
        self.up_button.grid(row=0, column=2, padx=5, pady=5)
        self.refresh_button.grid(row=0, column=3, padx=5, pady=5)
        self.path_entry.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W+tk.E)
        self.search_entry.grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)


    def on_back_button_click(self):
        ...
    
    def on_forward_button_click(self):
        ...
    
    def on_up_button_click(self):
        # move the path up one directory
        path = self.path_entry.get()
        path = os.path.dirname(path)
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, path)

        for hook in self._EVENT_HOOKS['on_path_change']:
            hook()

    def on_refresh_button_click(self):
        ...
    
    def on_update_path(self): # When enter is pressed in the path_entry
        if not os.path.exists(self.path_entry.get()):
            messagebox.showerror('File Explorer', f'Windows can\'t find \'{self.path_entry.get()}\', check the spelling and try again.')
        for hook in self._EVENT_HOOKS['on_path_change']:
            hook()

    def on_update_search(self): # When enter is pressed in the search_entry
        print(self.search_entry.get())
    
    def refresh_images(self):
        backward_img = ImageTk.PhotoImage(images['arrow_back'])
        forward_image = ImageTk.PhotoImage(images['arrow_forward'])
        up_image = ImageTk.PhotoImage(images['arrow_upward'])
        refresh_image = ImageTk.PhotoImage(images['refresh'])
        self.back_button.config(image=backward_img)
        self.forward_button.config(image=forward_image)
        self.up_button.config(image=up_image)
        self.refresh_button.config(image=refresh_image)
        self.back_button.image = backward_img
        self.forward_button.image = forward_image
        self.up_button.image = up_image
        self.refresh_button.image = refresh_image