from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
from main_menu import *

# Helpful Functions:
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

def hide_main_window():
    splash.withdraw()  # Hide the main window
    open_second_window()  # Show the second window

def open_second_window():
    obj = main_menu(ASSETS_PATH)
    obj.show_main()

def center_window(window):
    window.update_idletasks()  # Ensure window dimensions are updated
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = window.winfo_width()
    window_height = window.winfo_height()

    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    window.geometry(f"+{x_coordinate}+{y_coordinate}")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


### SPLASH FORM
splash = Tk()

splash.geometry("1250x700")
splash.configure(bg = "#FFFFFF")

canvas = Canvas(
    splash,
    bg = "#FFFFFF",
    height = 700,
    width = 1250,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
splash_img = PhotoImage(file=relative_to_assets("splash_img.png"))
image_1 = canvas.create_image(
    625.0,
    350.0,
    image=splash_img
)

splash.resizable(False, False)
splash.after(2500, hide_main_window)
splash.overrideredirect(True)  # Hide window decorations
splash.attributes('-toolwindow', True)  # Hide from taskbar
center_window(splash)
splash.mainloop()