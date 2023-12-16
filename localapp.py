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
        self.fonts = (FONT_TYPE, 15, "bold")
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
        self.closeB = customtkinter.CTkButton(master=self, text="Close", command=self.destroy,font=self.smallFonts,width=10, height=5, corner_radius=self.corner, text_color="yellow")
        self.closeB.place(x = 10, y = 10)
        
        #タイトル画像
        self.title_image()

        #交換開始ボタン
        self.exchangeB = customtkinter.CTkButton(master=self, text="交換する！", command=self.destroy,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.exchangeB.place(relx = 0.5, y = 500, anchor="center")

    def title_image(self):
        #画像の読み込み
        self.image_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/logo_big_resize-removebg-preview.png")
        self.image = Image.open(self.image_path)
        self.image = ImageTk.PhotoImage(self.image)
        #キャンバスの作成
        self.canvas = customtkinter.CTkCanvas(master=self, width=self.image.width()-5, height=self.image.height()-5)
        self.canvas.place(relx=0.5, y=300, anchor="center")
        #キャンバスに画像を描画
        self.canvas.create_image(0,0, image = self.image, anchor="nw")

if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()
