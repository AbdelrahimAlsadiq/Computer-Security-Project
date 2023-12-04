from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, Frame, messagebox, filedialog
from pathlib import Path
from algorithms.SHA_1 import *

class SHA1_FORM:
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

    def sign(self, msg):
        hashed_msg = SHA1(msg)
        result = {
            "MESSAGE": str(msg),
            "HASH-VALUE": str(hashed_msg.sha1_hash()),
        }
        with open(Path(__file__).parent / Path(r'outputs/SHA1_output.txt'), 'a') as file:
            file.write(f'{str(result)}\n')
        messagebox.showinfo("Hash Value", f'The Hash Value of the Message:\n{hashed_msg.sha1_hash()}\n------------------------------\nstored in SHA1_output.txt Successfully.')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
        l = content.split("\n")
        for msg in l:
            if msg != "":
                hashed_msg = SHA1(msg)
                result = {
                    "MESSAGE": str(msg),
                    "HASH-VALUE": str(hashed_msg.sha1_hash()),
                }
                with open(Path(__file__).parent / Path(r'outputs/SHA1_output.txt'), 'a') as file:
                    file.write(f'{str(result)}\n')
        messagebox.showinfo("Result", f'The Hash Values of the messages are stored in SHA1_output.txt Successfully.')


    def show_sha1_form(self):
        sha1_form = Toplevel()
        sha1_form.geometry("1250x700")
        sha1_form.configure(bg="#041626")
        sha1_form.title("Secure Hash Function 1 (SHA-1) Form")


        canvas = Canvas(
            sha1_form,
            bg="#041626",
            height=700,
            width=1250,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack()

        sha1_form_image_image_image_1 = PhotoImage(file=self.relative_to_assets("sha1_form_image_1.png"))
        sha1_form_image_image_1 = canvas.create_image(
            625.0,
            350.0,
            image=sha1_form_image_image_image_1
        )

        entry_image_1 = PhotoImage(file=self.relative_to_assets("sha1_form_entry_1.png"))
        entry_bg_1 = canvas.create_image(
            373.0,
            230.0,
            image=entry_image_1
        )

        frame = Frame(sha1_form, bg="#041626", bd=0, highlightthickness=0)
        entry_1 = Entry(
            frame,
            bd=0,
            bg="#041626",
            fg="#FFFFFF",
            highlightthickness=0,
            font=("Inter Light", 15),
            width=42,
        )
        entry_1.pack(padx=5, pady=5, ipady=5)  # Add internal padding in the Y direction

        canvas.create_window(133, 206, anchor="nw", window=frame)

        canvas.create_text(
            86.0,
            106.0,
            anchor="nw",
            text="Enter the text here:",
            fill="#9DD9FF",
            font=("Inter Light", 36)
        )

        # Buttons
        button_image_1 = PhotoImage(file=self.relative_to_assets("sha1_form_button_1.png"))
        button_1 = Button(
            sha1_form,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sign(entry_1.get()),
            relief="flat"
        )
        button_1.place(
            x=828.0,
            y=521.0,
            width=329.0,
            height=75.0
        )

        button_image_2 = PhotoImage(file=self.relative_to_assets("sha1_form_button_2.png"))
        button_2 = Button(
            sha1_form,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_file(),
            relief="flat"
        )
        button_2.place(
            x=828.0,
            y=412.0,
            width=329.0,
            height=75.0
        )
        sha1_form.resizable(False, False)
        self.center_window(sha1_form)
        sha1_form.mainloop()