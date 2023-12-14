import customtkinter

FONT_TYPE = "meiryo"

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # ?????????
        self.fonts = (FONT_TYPE, 15)
        # ?????????
        self.geometry("350x200")
        self.title("Basic GUI")

        # ??????????????
        self.setup_form()
    
    def setup_form(self):
        # CustomTkinter ???????????
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # ?????????????
        self.textbox = customtkinter.CTkEntry(master=self, placeholder_text="文字を入力", width=220, font=self.fonts)
        self.textbox.place(x=60, y=50)

        # ????????
        self.button = customtkinter.CTkButton(master=self, text="???????", command=self.button_function, font=self.fonts)
        self.button.place(x=100, y=100)

    def button_function(self):
        # ???????????????????????
        print(self.textbox.get())


if __name__ == "__main__":
    # ??????????{}
    app = App()
    app.mainloop()
