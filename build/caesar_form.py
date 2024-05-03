from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, messagebox, filedialog
from algorithms.CAESAR import *

class caesar_form:
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
        try:
            if int(key) > 26 or int(key) < 0:
                messagebox.showerror("Error", "Please Enter a Valid key.\n(Must be between 0 and 26)")
            else:
                ceaser = CAESAR(msg=plaintext, key=key)
                ciphertext = ceaser.encrypt()
        except:
            messagebox.showerror("Error", "Please Enter a Valid Plaintext and Key.")
            

        result = {
            "OPERATION": "Encryption",
            "PLAIN-TEXT": str(plaintext),
            "KEY": str(key),
            "CIPHER-TEXT": str(ciphertext)
        }
        with open(Path(__file__).parent / Path(r'outputs/CAESAR_output.txt'), 'a') as file:
            file.write(f'{str(result)}\n')
        messagebox.showinfo("Encrypted Value", f'The Encrypted Value of the Message:\n{ciphertext}\n------------------------------\nstored in CAESAR_output.txt successfully.')

    def decrypt(self, ciphertext, key):
        try:
            if int(key) > 26 or int(key) < 0:
                messagebox.showerror("Error", "Please Enter a Valid key.\n(Must be between 0 and 26)")
            else:
                ceaser = CAESAR(key=key, cipher=ciphertext)
                plaintext = ceaser.decrypt()
        except:
            messagebox.showerror("Error", "Please Enter a Valid Ciphertext and Key.")
        result = {
            "OPERATION": "Decryption",
            "PLAIN-TEXT": str(plaintext),
            "KEY": str(key),
            "CIPHER-TEXT": str(ciphertext)
        }
        with open(Path(__file__).parent / Path(r'outputs/CAESAR_output.txt'), 'a') as file:
            file.write(f'{str(result)}\n')
        messagebox.showinfo("Decrypted Value", f'The Decrypted Value of the Message:\n{plaintext}\n------------------------------\nstored in CAESAR.txt successfully.')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
        l = content.split("\n")
        for msg in l:
            if msg != "":
                plaintext, key = msg.split(",")
                ceaser = CAESAR(msg=plaintext, key=key, cipher="")
                ciphertext = ceaser.encrypt()

                result = {
                    "OPERATION": "File Encryption",
                    "PLAIN-TEXT": str(plaintext),
                    "KEY": str(key),
                    "CIPHER-TEXT": str(ciphertext)
                }
                with open(Path(__file__).parent / Path(r'outputs/CAESAR_output.txt'), 'a') as file:
                    file.write(f'{str(result)}\n')
        messagebox.showinfo("Result", f'The Encrypted Values of the messages are stored in CAESAR_output.txt Successfully.')


    def show_ceaser_form(self):
        caesar_form = Toplevel()
        caesar_form.geometry("1250x700")
        caesar_form.configure(bg="#041626")
        caesar_form.title("Ceaser Cipher Form")

        canvas = Canvas(
            caesar_form,
            bg="#041626",
            height=700,
            width=1250,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack()

        # Load and place the images
        image_image_1 = PhotoImage(file=self.relative_to_assets("CAESAR/CAESAR_form_image_1.png"))
        image_1 = canvas.create_image(625.0, 350.0, image=image_image_1)

        entry_image_1 = PhotoImage(file=self.relative_to_assets("CAESAR/CAESAR_form_text.png"))
        entry_bg_1 = canvas.create_image(373.0, 230.0, image=entry_image_1)
        
        entry_image_2 = PhotoImage(file=self.relative_to_assets("CAESAR/CAESAR_form_secret.png"))
        entry_bg_2 = canvas.create_image(373.0, 470.0, image=entry_image_2)

        # Entries
        text = Entry(caesar_form, bd=0, bg="#041626", fg="#FFFFFF", highlightthickness=0, font=("Inter Light", 15))
        text.place(x=133.0, y=206.0, width=480.0, height=46.0)

        secret = Entry(caesar_form, bd=0, bg="#041626", fg="#FFFFFF", highlightthickness=0, font=("Inter Light", 15))
        secret.place(x=133.0, y=446.0, width=480.0, height=46.0)

        # Buttons
        button_image_1 = PhotoImage(file=self.relative_to_assets("CAESAR/CAESAR_form_button_1.png"))
        button_1 = Button(
            caesar_form,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.decrypt(text.get(), secret.get()),
            relief="flat"
        )
        button_1.place(x=828.0, y=542.0, width=329.0, height=75.0)

        button_image_2 = PhotoImage(file=self.relative_to_assets("CAESAR/CAESAR_form_button_2.png"))
        button_2 = Button(
            caesar_form,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.encrypt(text.get(), secret.get()),
            relief="flat"
        )
        button_2.place(x=828.0, y=446.0, width=329.0, height=75.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("CAESAR/CAESAR_form_button_3.png"))
        button_3 = Button(
            caesar_form,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_file(),
            relief="flat"
        )
        button_3.place(x=828.0, y=350.0, width=329.0, height=75.0)

        caesar_form.resizable(False, False)
        self.center_window(caesar_form)
        caesar_form.mainloop()