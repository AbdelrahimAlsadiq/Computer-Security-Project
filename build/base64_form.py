from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, Frame, messagebox, filedialog
from pathlib import Path
from algorithms.BASE64 import *

class base64_form:
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

    def encode(self, data):
        if not data:
            messagebox.showerror("Error", "Please Enter a Non-Empty data Value.")
            return
        base64 = BASE64(data=data)
        encoded = base64.encode()
        result = {
            "OPERATION": "Encoding",
            "DATA": str(data),
            "ENCODED-VALUE": str(encoded),
        }
        with open(Path(__file__).parent / Path(r'outputs/BASE64_output.txt'), 'a') as file:
            file.write(f'{str(result)}\n')
        messagebox.showinfo("Encoded Value", f'The Encoded Value of the data:\n{encoded}\n------------------------------\nstored in BASE64_output.txt Successfully.')

    def decode(self, encoded):
        if not encoded:
            messagebox.showerror("Error", "Please Enter a Non-Empty Encoded Value.")
            return
        base64 = BASE64(encoded=encoded)
        decoded = base64.decode()
        result = {
            "OPERATION":"Decoding",
            "DATA": decoded,
            "ENCODED-VALUE": encoded
        }
        with open(Path(__file__).parent / Path(r'outputs/BASE64_output.txt'), 'a') as file:
            file.write(f'{str(result)}\n')
        messagebox.showinfo("Decoded Value", f'The Decoded Value:\n{decoded}\n------------------------------\nstored in BASE64_output.txt Successfully.')


    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
        l = content.split("\n")
        mode = l[0]
        l = l[1:]
        output = ""

        if mode.lower() == "encoding":
            for data in l:
                if data != "":
                    base64 = BASE64(data=data)
                    encoded = base64.encode()

                    output += f"{data} --> {encoded}\n"

                    result = {
                        "OPERATION": "File Encoding",
                        "DATA": str(data),
                        "ENCODED-VALUE": str(encoded),
                    }
                    with open(Path(__file__).parent / Path(r'outputs/BASE64_output.txt'), 'a') as file:
                        file.write(f'{str(result)}\n')
            messagebox.showinfo("Result", f'The Encoded Values of the messages:\n\n{output}\nstored in BASE64_output.txt Successfully.')

        elif mode.lower() == "decoding":
            for encoded in l:
                if encoded != "":
                    base64 = BASE64(encoded=encoded)
                    data = base64.decode()
                    
                    output += f"{encoded} --> {data}\n"
                    
                    result = {
                        "OPERATION": "File Decoding",
                        "DATA": str(data),
                        "ENCODED-VALUE": str(encoded),
                    }
                    with open(Path(__file__).parent / Path(r'outputs/BASE64_output.txt'), 'a') as file:
                        file.write(f'{str(result)}\n')
            messagebox.showinfo("Result", f'The Decoded Values of the messages:\n\n{output}\nstored in BASE64_output.txt Successfully.')

        else:
            messagebox.showerror("Invalid Mode", "Enter the mode at the first line of the file.\n(Encoding - Decoding)")


    def show_base64_form(self):
        base64_form = Toplevel()
        base64_form.geometry("1250x700")
        base64_form.configure(bg="#041626")
        base64_form.title("Base64 Form")


        canvas = Canvas(
            base64_form,
            bg="#041626",
            height=700,
            width=1250,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack()

        base64_form_image_image_image_1 = PhotoImage(file=self.relative_to_assets("BASE64/base64_form_image_1.png"))
        base64_form_image_image_1 = canvas.create_image(
            625.0,
            350.0,
            image=base64_form_image_image_image_1
        )

        entry_image_1 = PhotoImage(file=self.relative_to_assets("BASE64/base64_form_entry_1.png"))
        entry_bg_1 = canvas.create_image(
            373.0,
            230.0,
            image=entry_image_1
        )

        frame = Frame(base64_form, bg="#041626", bd=0, highlightthickness=0)
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
        button_image_1 = PhotoImage(file=self.relative_to_assets("BASE64/base64_form_button_1.png"))
        button_1 = Button(
            base64_form,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_file(),
            relief="flat"
        )
        button_1.place(
            x=828.0,
            y=353.0,
            width=329.0,
            height=75.0
        )

        button_image_2 = PhotoImage(file=self.relative_to_assets("BASE64/base64_form_button_2.png"))
        button_2 = Button(
            base64_form,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.encode(entry_1.get()),
            relief="flat"
        )
        button_2.place(
            x=828.0,
            y=462.0,
            width=329.0,
            height=75.0
        )

        button_image_3 = PhotoImage(file=self.relative_to_assets("BASE64/base64_form_button_3.png"))
        button_3 = Button(
            base64_form,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.decode(entry_1.get()),
            relief="flat"
        )
        button_3.place(
            x=828.0,
            y=571.0,
            width=329.0,
            height=75.0
        )
        base64_form.resizable(False, False)
        self.center_window(base64_form)
        base64_form.mainloop()