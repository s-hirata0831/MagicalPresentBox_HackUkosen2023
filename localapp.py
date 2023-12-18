import tkinter as tk
import customtkinter
import os
from PIL import Image, ImageTk

FONT_TYPE = "meiryo"

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 30, "bold")
        self.displayfont = (FONT_TYPE, 50, "bold")
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

        #全体の背景色設定
        self.config(bg="#e3e3e3")

        #タイトル画面へ移行
        self.title_frame()

#タイトル画面(画面01)========================================================================
    def title_frame(self):
        #クローズボタン
        self.closeB = customtkinter.CTkButton(master=self, text="Close", command=self.destroy,font=self.smallFonts,width=10, height=5, corner_radius=self.corner, text_color="yellow")
        self.closeB.place(x = 985, y = 10)
        
        #タイトル画像
        self.title_image()

        #交換開始ボタン
        self.exchangeB = customtkinter.CTkButton(master=self, text="交換する！", command=self.go_to_openBox,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.exchangeB.place(relx = 0.5, y = 500, anchor="center")

        #サンタ画像
        self.santa_image()

        #プレゼントイメージ画像
        self.present_image()

    def title_image(self):
        #画像の読み込み
        self.image_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/logo_big_resize-removebg-preview.png")
        self.image = Image.open(self.image_path)
        self.image = ImageTk.PhotoImage(self.image)
        #キャンバスの作成
        self.canvas = customtkinter.CTkCanvas(master=self, width=self.image.width()-5, height=self.image.height()-5, bd=0)
        self.canvas.place(x=179, y=90, anchor="nw")
        #キャンバスに画像を描画
        self.canvas.create_image(0,0, image = self.image, anchor="nw")

    def santa_image(self):
        #画像の読み込み
        self.santa_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa.png")
        self.santa = Image.open(self.santa_path)
        self.santa = ImageTk.PhotoImage(self.santa)
        #キャンバスの作成
        self.santa_canvas = customtkinter.CTkCanvas(master=self, width=self.santa.width()-1, height=self.santa.height()-1, bd =0)
        self.santa_canvas.place(x=50, y=250, anchor="nw")
        #キャンバスに画像を描画
        self.santa_canvas.create_image(0,0,image=self.santa, anchor="nw")

    def present_image(self):
        #画像の読み込み
        self.present_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/present.png")
        self.present = Image.open(self.present_path)
        self.present = ImageTk.PhotoImage(self.present)
        #キャンバスの作成
        self.present_canvas = customtkinter.CTkCanvas(master=self, width=self.present.width()-1, height=self.present.height()-1, bd =0)
        self.present_canvas.place(x=780, y=468, anchor="nw")
        #キャンバスに画像を描画
        self.present_canvas.create_image(0,0,image=self.present, anchor="nw")

#プレゼント入れる(02)========================================================================
    def go_to_openBox(self):
        self.canvas.destroy()
        self.santa_canvas.destroy()
        self.present_canvas.destroy()
        self.exchangeB.destroy()
        self.openBox_frame()

    def openBox_frame(self):
        self.judge = 0
        #どちらの箱が空いているか判定
        if self.judge == 1:
            print("上の箱が空いています")
            self.overBox_open()
        else:
            print("下の箱が空いています")
            self.underBox_open()

    def header_image(self):
        #画像の読み込み
        self.header_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/logo_mini_resize.png")
        self.header = Image.open(self.header_path)
        self.header = ImageTk.PhotoImage(self.header)
        #キャンバスの作成
        self.header_canvas = customtkinter.CTkCanvas(master=self, width=self.header.width()-1, height=self.header.height()-1, bd =0)
        self.header_canvas.place(x=0, y=-50, anchor="nw")
        #キャンバスに画像を描画
        self.header_canvas.create_image(0,0,image=self.header, anchor="nw")
        
    def overBox_open(self):
        #ヘッダー
        self.header_image()
        #プレゼント入れるのを促す
        self.overOpen_image()
        #交換開始ボタン
        self.kaishi = customtkinter.CTkButton(master=self, text="プレゼントを入れた！", command=self.go_to_lockBox,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.kaishi.place(x = 585, y = 470)
        self.label1 = customtkinter.CTkLabel(self, text="上の箱の扉を開けて",  font=self.displayfont, text_color="red", bg_color="#e3e3e3")
        self.label1.place(x = 515, y = 200)
        self.label2 = customtkinter.CTkLabel(self, text="次の人へのプレゼント",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.label2.place(x = 515, y = 270)
        self.label3 = customtkinter.CTkLabel(self, text="を入れよう！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.label3.place(x = 515, y = 340)

    def overOpen_image(self):
        #画像の読み込み
        self.overOpen_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/overBoxOpen.png")
        self.overOpen = Image.open(self.overOpen_path)
        self.overOpen = ImageTk.PhotoImage(self.overOpen)
        #キャンバスの作成
        self.overOpen_canvas = customtkinter.CTkCanvas(master=self, width=self.overOpen.width()-1, height=self.overOpen.height()-1, bd =0)
        self.overOpen_canvas.place(x=70, y=125, anchor="nw")
        #キャンバスに画像を描画
        self.overOpen_canvas.create_image(0,0,image=self.overOpen, anchor="nw")

    def underBox_open(self):
        #ヘッダー
        self.header_image()
        #プレゼント入れるのを促す
        self.underOpen_image()
        #交換開始ボタン
        self.underIn = customtkinter.CTkButton(master=self, text="プレゼントを入れた！", command=self.go_to_lockBox,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.underIn.place(x = 585, y = 470)
        self.underLabel1 = customtkinter.CTkLabel(self, text="下の箱の扉を開けて",  font=self.displayfont, text_color="red", bg_color="#e3e3e3")
        self.underLabel1.place(x = 515, y = 200)
        self.underLabel2 = customtkinter.CTkLabel(self, text="次の人へのプレゼント",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.underLabel2.place(x = 515, y = 270)
        self.underLabel3 = customtkinter.CTkLabel(self, text="を入れよう！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.underLabel3.place(x = 515, y = 340)

    def underOpen_image(self):
        #画像の読み込み
        self.underOpen_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/underBoxOpen.png")
        self.underOpen = Image.open(self.underOpen_path)
        self.underOpen = ImageTk.PhotoImage(self.underOpen)
        #キャンバスの作成
        self.underOpen_canvas = customtkinter.CTkCanvas(master=self, width=self.underOpen.width()-1, height=self.underOpen.height()-1, bd =0)
        self.underOpen_canvas.place(x=70, y=125, anchor="nw")
        #キャンバスに画像を描画
        self.underOpen_canvas.create_image(0,0,image=self.underOpen, anchor="nw")

#箱をロックする(03)========================================================================
    def go_to_lockBox(self):
        if self.judge == 1:
            self.kaishi.destroy()
            self.label1.destroy()
            self.label2.destroy()
            self.label3.destroy()
            self.overOpen_canvas.destroy()
            self.lockBox_frame()
        else:
            self.underIn.destroy()
            self.underLabel1.destroy()
            self.underLabel2.destroy()
            self.underLabel3.destroy()
            self.underOpen_canvas.destroy()
            self.lockBox_frame()

    def lockBox_frame(self):
        self.lockLabel = customtkinter.CTkLabel(self, text="箱をロックします。ボタンをタッチ！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.lockLabel.place(relx = 0.5, y = 200, anchor="center")
        self.lockBtn = customtkinter.CTkButton(master=self, text="ロック", command=self.go_to_judgePresent,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.lockBtn.place(relx = 0.5, y = 520, anchor="center")
        self.loaddingSanta_image()
    
    def loaddingSanta_image(self):
        #画像の読み込み
        self.loadingSanta_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/loading_santa.png")
        self.loadingSanta = Image.open(self.loadingSanta_path)
        self.loadingSanta = ImageTk.PhotoImage(self.loadingSanta)
        #キャンバスの作成
        self.loadingSanta_canvas = customtkinter.CTkCanvas(master=self, width=self.loadingSanta.width()-1, height=self.loadingSanta.height()-1, bd =0)
        self.loadingSanta_canvas.place(relx=0.5, y=350, anchor="center")
        #キャンバスに画像を描画
        self.loadingSanta_canvas.create_image(0,0,image=self.loadingSanta, anchor="nw")

#プレゼントを判定(03)========================================================================
    def go_to_judgePresent(self):
        self.lockBtn.destroy()
        self.loadingSanta_canvas.destroy()
        self.lockLabel.destroy()
        self.judgeLabel = customtkinter.CTkLabel(self, text="プレゼントを確認中！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.judgeLabel.place(relx = 0.5, y = 200, anchor="center")
        self.judgePresent_image()
    
    def judgePresent_image(self):
        #画像の読み込み
        self.judgePresent_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/present_big.png")
        self.judgePresent = Image.open(self.judgePresent_path)
        self.judgePresent = ImageTk.PhotoImage(self.judgePresent)
        #キャンバスの作成
        self.judgePresent_canvas = customtkinter.CTkCanvas(master=self, width=self.judgePresent.width()-1, height=self.judgePresent.height()-1, bd =0)
        self.judgePresent_canvas.place(relx=0.5, y=350, anchor="center")
        #キャンバスに画像を描画
        self.judgePresent_canvas.create_image(0,0,image=self.judgePresent, anchor="nw")        

if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()
