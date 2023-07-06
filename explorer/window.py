import tkinter as tk
from ui.topbar import TopBar
from ui.fileview import FileView

# Create the main window
window = tk.Tk()
window.title("File Explorer")
window.geometry("800x600")

components = {'top_bar': TopBar(window)}
components.update({
    'file_view': FileView(window, components)
})

# Configure grid column weights to make path_entry expand
components['top_bar'].frame.columnconfigure(4, weight=1)
components['top_bar'].frame.pack(fill=tk.X)
components['top_bar'].refresh_images() # cause tkniter is stupid we need to refresh the images to make them actually appear

components['file_view'].frame.pack(fill=tk.BOTH, expand=True)

# run the application
window.mainloop()
