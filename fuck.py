import tkinter as tk
import customtkinter
import os
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

        # フォームのセットアップをする
        self.setup_form()
    
    def setup_form(self):
        # CustomTkinter のフォームデザイン設定
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")

        # フォームサイズ設定
        self.geometry("1024x600")
        self.title("Magical Present Box")

        #行方向のマスのレイアウトを設定
        self.grid_rowconfigure(0)
        #列方向のマスのレイアウトを設定
        self.grid_columnconfigure(0)

        #クローズボタン
        self.closeB = customtkinter.CTkButton(master=self, text="Close", command=self.destroy,font=self.smallFonts,width=10, height=5, corner_radius=self.corner)
        self.closeB.grid(row=0, column=0, padx=0, pady=0)
        
        #1つ目のフレームの設定
        #stinkyは拡大したときに広がる方向のこと。nsewで4方向で指定
        self.title_frame=TitleFrame(master=self)
        self.title_frame.grid(row=1, column=0, padx=200, pady=50, sticky="nsew")

class TitleFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="TitleFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.fonts = (FONT_TYPE, 15)
        self.smallFonts = (FONT_TYPE, 10)
        self.corner= (50)

        #フォームのセットアップをする
        self.setup_form()
    
    def setup_form(self):
        #行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定するが，今回は拡大しないので特に関係ない。
        self.grid_rowconfigure(0)
        #列方向のマスのレイアウトを設定する。
        self.grid_columnconfigure(0)

        #タイトル画面表示
        self.title_image()

    def title_image(self):
        #画像の読み込み
        self.image_path = os.path.join(os.path.dirname(__file__), R"C:\Users\hirat\Documents\MagicalPresentBox_HackUkosen2023\src_localapp\logo_big_resize.png")
        self.image = Image.open(self.image_path)
        self.image = ImageTk.PhotoImage(self.image)
        #キャンバスの作成
        self.canvas = customtkinter.CTkCanvas(master=self, width=self.image.width(), height=self.image.height())
        self.canvas.grid(row = 0, column=0, padx=0, pady=0)
        #キャンバスに画像を描画
        self.canvas.create_image(0,0, image = self.image, anchor="nw")

if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()
