import tkinter as tk
from pathlib import Path
from sha1_form import *
from des_form import *
from dss_form import *

class menu:

    def __init__(self, assets):
        self.assets = assets

    def relative_to_assets(self, path: str) -> Path:
        return self.assets / Path(path)
    
    def center_window(self, window):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = window.winfo_reqwidth()
        window_height = window.winfo_reqheight()

        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    
    def open_sha1_form(self):
        obj = SHA1_FORM(self.assets)
        obj.show_sha1_form()

    def open_des_form(self):
        obj = DES_FORM(self.assets)
        obj.show_des_form()

    def open_dss_form(self):
        obj = DSS_FORM(self.assets)
        obj.show_dss_form()

    def show_main(self):
        main = tk.Toplevel()
        main.title("Main Menu")
        main.configure(bg="#041626")
        main.geometry("1250x700")

        window_width = 1250  # Use the specified width
        window_height = 700  # Use the specified height

        canvas = tk.Canvas(
            main,
            bg="#041626",
            height=window_height,
            width=window_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack()

        image_image_1 = tk.PhotoImage(file=self.relative_to_assets("menu_image_1.png"))
        image_1 = canvas.create_image(
            window_width / 2,
            window_height / 2,
            image=image_image_1
        )

        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("menu_button_1.png"))
        button_1 = tk.Button(
            main,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_dss_form(),
            relief="flat"
        )
        button_1.place(
            x=82.0,
            y=503.0,
            width=1086.0,
            height=76.0
        )

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("menu_button_2.png"))
        button_2 = tk.Button(
            main,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_des_form(),
            relief="flat"
        )
        button_2.place(
            x=82.0,
            y=378.0,
            width=1086.0,
            height=76.0
        )

        button_image_3 = tk.PhotoImage(file=self.relative_to_assets("menu_button_3.png"))
        button_3 = tk.Button(
            main,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_sha1_form(),
            relief="flat"
        )
        button_3.place(
            x=82.0,
            y=253.0,
            width=1086.0,
            height=76.0
        )

        main.resizable(False, False)
        self.center_window(main)
        main.mainloop()