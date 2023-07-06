import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from consts import *
from ui.topbar import TopBar

class FileView:
    def __init__(self, window: tk.Tk, components: dict):
        self.frame = tk.Frame(window, bg=BG_ONE)
        self.top_bar: TopBar = components['top_bar']
        self.top_bar._EVENT_HOOKS['on_path_change'].append(self.on_path_change) # Add a hook to the on_path_change function

        # Basically, we need refresh the files whenever anything changes
        self.top_bar.forward_button.bind("<Button-1>", lambda event: self.on_path_change())


        self.file_tree = ttk.Treeview(self.frame, columns=("type", "size", "modified"), show="headings")
        self.file_tree.heading("type", text="Type")
        self.file_tree.heading("size", text="Size")
        self.file_tree.heading("modified", text="Modified")

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.file_tree.yview)
        self.file_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_tree.bind("<Double-1>", self.open_folder)  # Bind double-click event to open_folder function

        self.refresh_files()
    
    def refresh_files(self):
        self.file_tree.delete(*self.file_tree.get_children())
        path = self.top_bar.path_entry.get()

        # Load folder and file icons
        folder_icon = ImageTk.PhotoImage(images['folder'])
        file_icon = ImageTk.PhotoImage(images['file'])

        # Add files/folders to the TreeView
        try:
            for file in os.listdir(path):
                file_path = os.path.join(path, file)
                if os.path.isdir(file_path):
                    print('adding folder', file, 'to tree')
                    self.file_tree.insert("", tk.END, values=(file, "", ""), text=file, image=folder_icon)
                else:
                    print('adding file', file, 'to tree')
                    self.file_tree.insert("", tk.END, values=(file, "", ""), text=file, image=file_icon)
        except PermissionError as e:
            messagebox.showerror("Permission Error", "You do not have permission to access this folder.")
            self.top_bar.on_up_button_click() # go back to the previous folder
        
        self.file_tree.pack(fill=tk.BOTH, expand=True)
    
    def open_folder(self, event):
        selected_item = self.file_tree.focus()
        path = self.top_bar.path_entry.get()
        item_text = self.file_tree.item(selected_item)["text"]
        folder_path = os.path.join(path, item_text)

        if os.path.isdir(folder_path):
            self.top_bar.path_entry.delete(0, tk.END)
            self.top_bar.path_entry.insert(tk.END, folder_path)
            self.refresh_files()
        
        else:
            try:
                os.startfile(folder_path)
            except OSError as e:
                # This probably means there's no default program for this file type, for now just show an error message
                messagebox.showerror("File Explorer", "There is no default program for this file type.")

    def on_path_change(self):
        self.refresh_files()
