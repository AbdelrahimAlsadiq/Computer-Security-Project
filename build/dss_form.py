from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, Frame, messagebox, filedialog
from pathlib import Path
from algorithms.DSS import *

class DSS_FORM():
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
        obj = DSS(msg)
        signature, public_key = obj.sign()

        result = {
            "MESSAGE":msg,
            "BASE64-SIGNATURE":signature,
            "BASE64-PUBLIC-KEY":public_key
        }
        
        with open('outputs/DSS_output.txt', 'a') as file:
            file.write(f'{str(result)}\n')
        messagebox.showinfo("Signing Results", f'Base-64 Signature:\n{signature}\n------------------------------\nBase-64 Public Key:\n{public_key}\n------------------------------\nstored in DSS_output.txt successfully.')
    
    def verify(self, msg, public_key, signature):
        obj = DSS(msg)
        try:
            if obj.verify(signature, public_key, msg):
                messagebox.showinfo("Verification Results", "Signature is Valid.")
            else:
                messagebox.showinfo("Verification Results", "Signature is Invalid.")

        except Exception:
            messagebox.showinfo("Verification Results", "Signature is Invalid.")


    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
        l = content.split("\n")
        for msg in l:
            if msg != "":
                obj = DSS(msg)
                signature, public_key = obj.sign()

                result = {
                    "MESSAGE":msg,
                    "BASE64-SIGNATURE":signature,
                    "BASE64-PUBLIC-KEY":public_key
                }
                
                with open('outputs/DSS_output.txt', 'a') as file:
                    file.write(f'{str(result)}\n')
        messagebox.showinfo("Signing Results", f'The Signing Results of the messages are stored in DSS_output.txt Successfully.')


    def show_dss_form(self):
        dss_form = Toplevel()
        dss_form.geometry("1250x700")
        dss_form.configure(bg = "#041626")
        dss_form.title("Digital Signature Standard (DSS) Form")

        canvas = Canvas(
            dss_form,
            bg = "#041626",
            height = 700,
            width = 1250,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.pack()

        # Load and place the images
        image_image_1 = PhotoImage(file=self.relative_to_assets("dss_form_image_1.png"))
        image_1 = canvas.create_image(625.0, 350.0, image=image_image_1)

        entry_image_1 = PhotoImage(file=self.relative_to_assets("dss_form_entry_1.png"))
        entry_bg_1 = canvas.create_image(373.0, 230.0, image=entry_image_1)

        entry_image_2 = PhotoImage(file=self.relative_to_assets("dss_form_entry_2.png"))
        entry_bg_2 = canvas.create_image(373.0, 433.0, image=entry_image_2)

        entry_image_3 = PhotoImage(file=self.relative_to_assets("dss_form_entry_3.png"))
        entry_bg_3 = canvas.create_image(373.0,604.0,image=entry_image_3)

        # Entries
        msg_entry = Entry(dss_form,bd=0,bg="#030F1B",fg="#FFFFFF",highlightthickness=0, font=("Inter Light", 15))
        msg_entry.place(x=133.0,y=206.0,width=480.0,height=46.0)

        pkey_entry = Entry(dss_form,bd=0,bg="#030F1B",fg="#FFFFFF",highlightthickness=0, font=("Inter Light", 15))
        pkey_entry.place(x=133.0,y=409.0,width=480.0,height=46.0)

        sign_entry = Entry(dss_form,bd=0,bg="#030F1B",fg="#FFFFFF",highlightthickness=0, font=("Inter Light", 15))
        sign_entry.place(x=133.0,y=580.0,width=480.0,height=46.0)

        # Buttons
        button_image_1 = PhotoImage(file=self.relative_to_assets("dss_form_button_1.png"))
        button_1 = Button(
            dss_form,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.verify(msg_entry.get(), pkey_entry.get(), sign_entry.get()),
            relief="flat"
        )
        button_1.place(x=828.0,y=542.0,width=329.0,height=75.0)

        button_image_2 = PhotoImage(file=self.relative_to_assets("dss_form_button_2.png"))
        button_2 = Button(
            dss_form,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sign(msg_entry.get()),
            relief="flat"
        )
        button_2.place(x=828.0,y=446.0,width=329.0,height=75.0)

        dss_form_button_image_3 = PhotoImage(file=self.relative_to_assets("dss_form_button_3.png"))
        dss_form_button_3 = Button(
            dss_form,
            image=dss_form_button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_file(),
            relief="flat"
        )
        dss_form_button_3.place(x=828.0,y=350.0,width=329.0,height=75.0)

        dss_form.resizable(False, False)
        self.center_window(dss_form)
        dss_form.mainloop()