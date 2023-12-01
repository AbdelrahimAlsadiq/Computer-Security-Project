from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, messagebox, filedialog
from DES import *

class DES_FORM:
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

    def encrypt(self, plaintext, key):
        des = DES(plaintext, key)
        ciphertext = des.run()[0]

        result = {
            "PLAIN-TEXT": str(plaintext),
            "KEY": str(key),
            "CIPHER-TEXT": str(ciphertext)
        }
        with open('outputs/DES_output.txt', 'a') as file:
            file.write(f'{str(result)}\n')
        messagebox.showinfo("Encrypted Value", f'The Encrypted Value of the Message:\n{ciphertext}\n------------------------------\nstored in DES_output.txt successfully.')

    def decrypt(self, ciphertext, key):
        des = DES(ciphertext, key)
        plaintext = des.run()[1]

        result = {
            "CIPHER-TEXT": str(ciphertext),
            "KEY": str(key),
            "PLAIN-TEXT": str(plaintext)
        }
        with open('outputs/DES_output.txt', 'a') as file:
            file.write(f'{str(result)}\n')
        messagebox.showinfo("Decrypted Value", f'The Decrypted Value of the Message:\n{plaintext}\n------------------------------\nstored in DES_output.txt successfully.')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
        l = content.split("\n")
        for msg in l:
            if msg != "":
                plaintext, key = msg.split(" ")
                des = DES(plaintext, key)
                ciphertext = des.run()[0]

                result = {
                    "PLAIN-TEXT": str(plaintext),
                    "KEY": str(key),
                    "CIPHER-TEXT": str(ciphertext)
                }
                with open('outputs/DES_output.txt', 'a') as file:
                    file.write(f'{str(result)}\n')
        messagebox.showinfo("Result", f'The Encrypted Values of the messages are stored in DES_output.txt Successfully.')


    def show_des_form(self):
        des_form = Toplevel()
        des_form.geometry("1250x700")
        des_form.configure(bg="#041626")
        des_form.title("Data Encryption Standard (DES) Form")

        canvas = Canvas(
            des_form,
            bg="#041626",
            height=700,
            width=1250,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack()

        # Load and place the images
        image_image_1 = PhotoImage(file=self.relative_to_assets("des_form_image_1.png"))
        image_1 = canvas.create_image(625.0, 350.0, image=image_image_1)

        entry_image_1 = PhotoImage(file=self.relative_to_assets("des_form_text.png"))
        entry_bg_1 = canvas.create_image(373.0, 230.0, image=entry_image_1)
        
        entry_image_2 = PhotoImage(file=self.relative_to_assets("des_form_secret.png"))
        entry_bg_2 = canvas.create_image(373.0, 470.0, image=entry_image_2)

        # Entries
        text = Entry(des_form, bd=0, bg="#041626", fg="#FFFFFF", highlightthickness=0, font=("Inter Light", 15))
        text.place(x=133.0, y=206.0, width=480.0, height=46.0)

        secret = Entry(des_form, bd=0, bg="#041626", fg="#FFFFFF", highlightthickness=0, font=("Inter Light", 15))
        secret.place(x=133.0, y=446.0, width=480.0, height=46.0)

        # Buttons
        button_image_1 = PhotoImage(file=self.relative_to_assets("des_form_button_1.png"))
        button_1 = Button(
            des_form,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.decrypt(text.get(), secret.get()),
            relief="flat"
        )
        button_1.place(x=828.0, y=542.0, width=329.0, height=75.0)

        button_image_2 = PhotoImage(file=self.relative_to_assets("des_form_button_2.png"))
        button_2 = Button(
            des_form,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.encrypt(text.get(), secret.get()),
            relief="flat"
        )
        button_2.place(x=828.0, y=446.0, width=329.0, height=75.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("des_form_button_3.png"))
        button_3 = Button(
            des_form,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_file(),
            relief="flat"
        )
        button_3.place(x=828.0, y=350.0, width=329.0, height=75.0)

        des_form.resizable(False, False)
        self.center_window(des_form)
        des_form.mainloop()