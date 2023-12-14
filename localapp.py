import tkinter as tk
import customtkinter

FONT_TYPE = "meiryo"

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 15)
        self.smallFonts= (FONT_TYPE, 10)
        self.corner= (50)
        #タイトルバーの非表示
        self.wm_overrideredirect(True)
        # フォームサイズ設定
        self.geometry("1024x600")
        self.title("Magical Present Box")

        # フォームのセットアップをする
        self.setup_form()
    
    def setup_form(self):
        # CustomTkinter のフォームデザイン設定
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        # クローズボタン
        self.closeB = customtkinter.CTkButton(master=self, text="Close", command=self.destroy,font=self.smallFonts,width=10, height=5, corner_radius=self.corner)
        self.closeB.grid(row=0, column=0, padx=0, pady=0)

        #サイトボタン
        self.siteB = customtkinter.CTkButton(master=self, text="シェアする", font=self.smallFonts, width=10, height=5, corner_radius=self.corner)
        self.siteB.grid(row=0, column=1, padx=0, pady=20)

        # ボタンを表示する
        self.button = customtkinter.CTkButton(master=self, text="クリックしてね", command=self.button_function, font=self.fonts, corner_radius=self.corner)
        self.button.grid(row=1, column=0, padx=200, pady=50)

        #画面クローズ用ボタン
        self.close = customtkinter.CTkButton(master=self, text="Close", command=self.destroy, font=self.fonts, corner_radius=self.corner)
        self.close.place(x=100, y=150) 
    
    def button_function(self):
        # テキストボックスに入力されたテキストを表示する
        print(self.textbox.get())


if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()
