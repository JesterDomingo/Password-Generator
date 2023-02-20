"""Custom Tkinter PassGen UI"""

from password_generator import generate
from customtkinter import CTk, CTkButton, CTkEntry, CTkCheckBox, CTkLabel, CTkSlider, CTkFont #this is library imported
from customtkinter import IntVar, StringVar, BooleanVar
# pip3 install customtkinter | <- way to install it


class Model: #it handles the outputs(?) in GUI
    def __init__(self):
        self.password = StringVar(value='')
        self.length = IntVar(value=12)
        self.uppercase = BooleanVar(value=True)
        self.lowercase = BooleanVar(value=True)
        self.numbers = BooleanVar(value=True)
        self.special_characters = BooleanVar(value=True)


class View: #is visual of GUI | "main" holds the previous above class
    def __init__(self, main):
        self.main = main
        self.model = main.model #getting access to the class above

    #password length slider
        self.length_label = CTkLabel(self.main, text="Password\nLength")
        self.length_display = CTkLabel(self.main, textvariable=self.model.length) #it updates when"self.length" updates
        self.length_slider = CTkSlider(self.main, variable=self.model.length, from_=4, to=100, 
        width=300, height=10 ,orientation='horizontal') #it updates when"self.length" updates

    #password choices checkboxes
        self.uppercase_checkbutton = CTkCheckBox(self.main, text='Uppercase', variable=self.model.uppercase)
        self.lowercase_checkbutton = CTkCheckBox(self.main, text='Lowercase', variable=self.model.lowercase)
        self.numbers_checkbutton = CTkCheckBox(self.main, text='Numbers', variable=self.model.numbers)
        self.special_checkbutton = CTkCheckBox(self.main, text='Special Characters', 
                    variable=self.model.special_characters)
    
    #buttons
        self.generate_button = CTkButton(self.main, text='Generate', fg_color='green', hover_color='darkgreen')
        self.copy_button = CTkButton(self.main, text='Copy', fg_color='blue', hover_color='darkblue')
        self.exit_button = CTkButton(self.main, text='Exit', fg_color='red')

        self.password_entry = CTkEntry(self.main, textvariable=self.model.password, width=715, state='readonly',
            font=CTkFont(size=12, family='Consolas'), justify='center')

    #place all widgets
        self.length_label.place(rely=0.15, relx=0.2, anchor='center')
        self.length_slider.place(rely=0.15, relx=0.5, anchor='center')
        self.length_display.place(rely=0.1, relx=0.5, anchor='center')

        self.uppercase_checkbutton.place(relx=0.250, rely=0.25, anchor='nw')
        self.lowercase_checkbutton.place(relx=0.250, rely=0.35, anchor='nw')
        self.numbers_checkbutton.place(relx=0.250, rely=0.45, anchor='nw')
        self.special_checkbutton.place(relx=0.250, rely=0.55, anchor='nw')

        self.generate_button.place(relx=0.655, rely=0.345, anchor='center')
        self.copy_button.place(relx=0.655, rely=0.445, anchor='center')
        self.exit_button.place(relx=0.655, rely=0.545, anchor='center')

        self.password_entry.place(relx=0.5, rely=0.8, anchor='center')
    


class Controller: #functionality of GUI
    def __init__(self, main):
        self.main = main
        self.model = main.model
        self.view = main.view

        self.view.generate_button.configure(command=self.generate_password)
        self.view.copy_button.configure(command=self.copy_password)
        self.view.exit_button.configure(command=self.main.destroy)

    def generate_password(self):
        self.model.password.set(
            generate(
                length=self.model.length.get(),
                uppercase = self.model.uppercase.get(),
                lowercase = self.model.lowercase.get(),
                numbers = self.model.numbers.get(),
                special_characters = self.model.special_characters.get()
            )
        )

    def copy_password(self):
        self.main.clipboard_clear()
        self.main.clipboard_append(self.model.password.get())

class App(CTk): 
    def __init__(self):
        super().__init__()
        self.config()
        self.model = Model()
        self.view = View(self)
        self.Controller = Controller(self)


    def config(self):
        self.title('Password Generator | Made by: Jester Domingo')   
        self.resizable(False, False)
        self.geometry('750x500')
        self.iconbitmap('lock.ico')


if __name__ == '__main__':
    app = App()
    app.mainloop()
