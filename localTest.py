import tkinter as tk
import customtkinter
import time
import os
import servo
#import led
#import led2
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials, storage

FONT_TYPE = "meiryo"

cred=credentials.Certificate("magicalpresentbox-firebase-adminsdk-mmdua-2ad3d08eca.json")
firebase_admin.initialize_app(cred)
bucket = storage.bucket("magicalpresentbox.appspot.com")

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 30, "bold")
        self.displayfont = (FONT_TYPE, 50, "bold")
        self.smallFonts= (FONT_TYPE, 10)
        self.bigFonts = (FONT_TYPE,100, "bold")
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

        #初期状態では上が空いている。Trueのときは上が空いている
        self.unlockedBox = True

        #前の判定結果格納
        self.beforePresent = 1

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
        #どちらの箱が空いているか判定
        if self.unlockedBox == True:
            print("上の箱が空いています")
            #led.rainbow_cycle(0.01)
            self.overBox_open()
        else:
            print("下の箱が空いています")
            #led2.rainbow_cycle(0.01)
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
        if self.unlockedBox == True:
            self.kaishi.destroy()
            self.label1.destroy()
            self.label2.destroy()
            self.label3.destroy()
            self.overOpen_canvas.destroy()
            #led.No_led()
            self.lockBox_frame()
        else:
            self.underIn.destroy()
            self.underLabel1.destroy()
            self.underLabel2.destroy()
            self.underLabel3.destroy()
            self.underOpen_canvas.destroy()
            #led2.No_led()
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

#プレゼントを判定(04)========================================================================
    def go_to_judgePresent(self):
        #if self.unlockedBox == True:
            #servo.lock(True,True)
        #else:
            #servo.lock(False, True)
        self.lockBtn.destroy()
        self.lockLabel.destroy()
        self.loadingSanta_canvas.destroy()
        self.judgeLabel = customtkinter.CTkLabel(self, text="プレゼントを確認中！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.judgeLabel.place(relx = 0.5, y = 200, anchor="center")
        self.judgePresent_image()
        self.judgePresentFlow()
    
    def judgePresentFlow(self):
        image_path = "./presentImg/post.jpg"
        #camera.capture(image_path)
        self.after(2500, self.go_to_judgeResult)

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

#判定結果を表示(05)========================================================================        
    def go_to_judgeResult(self):
        self.judgePresent_canvas.destroy()
        self.judgeLabel.destroy()
        self.judgeResult_frame()
    
    def judgeResult_frame(self):
        self.resultNum = 4#判定結果(一時用，0か1か)
        if self.resultNum == 5:
            print("クリスマスっぽーい")
            self.result5_image()
            self.resultTrueLabel = customtkinter.CTkLabel(self, text="AIによる確認完了!",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
            self.resultTrueLabel.place(relx = 0.5, y = 170, anchor="center")
            self.after(2000, self.result_next)
        elif self.resultNum == 4:
            print("クリスマスっぽーい")
            self.result4_image()
            self.resultTrueLabel = customtkinter.CTkLabel(self, text="AIによる確認完了!",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
            self.resultTrueLabel.place(relx = 0.5, y = 170, anchor="center")
            self.after(2000, self.result_next)
        elif self.resultNum == 3:
            print("クリスマスっぽーい")
            self.result3_image()
            self.resultTrueLabel = customtkinter.CTkLabel(self, text="AIによる確認完了!",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
            self.resultTrueLabel.place(relx = 0.5, y = 170, anchor="center")
            self.after(2000, self.result_next)
        elif self.resultNum == 2:
            print("クリスマスっぽーい")
            self.result2_image()
            self.resultTrueLabel = customtkinter.CTkLabel(self, text="AIによる確認完了!",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
            self.resultTrueLabel.place(relx = 0.5, y = 170, anchor="center")
            self.after(2000, self.result_next)
        elif self.resultNum == 1:
            print("クリスマスっぽーい")
            self.result1_image()
            self.resultTrueLabel = customtkinter.CTkLabel(self, text="AIによる確認完了!",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
            self.resultTrueLabel.place(relx = 0.5, y = 170, anchor="center")
            self.after(2000, self.result_next)

    def result_next(self):
        self.resultTrueLabel.destroy()
        self.resultTrueLabel2 = customtkinter.CTkLabel(self, text="クリスマスっぽさ"+str(self.resultNum),  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.resultTrueLabel2.place(relx = 0.5, y = 170, anchor="center")
        self.getPresentBtn = customtkinter.CTkButton(master=self, text="次へ", command=self.go_to_canGetPresent,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.getPresentBtn.place(x = 700, y = 50)

    def result5_image(self):
        #画像の読み込み
        self.result_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa.png")
        self.result = Image.open(self.result_path)
        self.result = ImageTk.PhotoImage(self.result)
        #画像の読み込み
        self.gray_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa_gray.png")
        self.gray = Image.open(self.gray_path)
        self.gray = ImageTk.PhotoImage(self.gray)
        #キャンバスの作成
        self.result1_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result1_canvas.place(x=75, y=225)
        #キャンバスに画像を描画
        self.result1_canvas.create_image(0,0,image=self.result, anchor="nw")
        #2体目
        self.result2_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result2_canvas.place(x=255, y=225)
        self.result2_canvas.create_image(0,0,image=self.result, anchor="nw")
        #3体目
        self.result3_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result3_canvas.place(x=435, y=225)
        self.result3_canvas.create_image(0,0,image=self.result, anchor="nw")
        #4体目
        self.result4_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result4_canvas.place(x=615, y=225)
        self.result4_canvas.create_image(0,0,image=self.result, anchor="nw")
        #5体目
        self.result5_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result5_canvas.place(x=795, y=225)
        self.result5_canvas.create_image(0,0,image=self.result, anchor="nw")

    def result4_image(self):
        #画像の読み込み
        self.result_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa.png")
        self.result = Image.open(self.result_path)
        self.result = ImageTk.PhotoImage(self.result)
        #画像の読み込み
        self.gray_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa_gray.png")
        self.gray = Image.open(self.gray_path)
        self.gray = ImageTk.PhotoImage(self.gray)
        #キャンバスの作成
        self.result1_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result1_canvas.place(x=75, y=225)
        #キャンバスに画像を描画
        self.result1_canvas.create_image(0,0,image=self.result, anchor="nw")
        #2体目
        self.result2_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result2_canvas.place(x=255, y=225)
        self.result2_canvas.create_image(0,0,image=self.result, anchor="nw")
        #3体目
        self.result3_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result3_canvas.place(x=435, y=225)
        self.result3_canvas.create_image(0,0,image=self.result, anchor="nw")
        #4体目
        self.result4_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result4_canvas.place(x=615, y=225)
        self.result4_canvas.create_image(0,0,image=self.result, anchor="nw")
        #5体目
        self.result5_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result5_canvas.place(x=795, y=225)
        self.result5_canvas.create_image(0,0,image=self.gray, anchor="nw")

    def result3_image(self):
        #画像の読み込み
        self.result_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa.png")
        self.result = Image.open(self.result_path)
        self.result = ImageTk.PhotoImage(self.result)
        #画像の読み込み
        self.gray_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa_gray.png")
        self.gray = Image.open(self.gray_path)
        self.gray = ImageTk.PhotoImage(self.gray)
        #キャンバスの作成
        self.result1_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result1_canvas.place(x=75, y=225)
        #キャンバスに画像を描画
        self.result1_canvas.create_image(0,0,image=self.result, anchor="nw")
        #2体目
        self.result2_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result2_canvas.place(x=255, y=225)
        self.result2_canvas.create_image(0,0,image=self.result, anchor="nw")
        #3体目
        self.result3_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result3_canvas.place(x=435, y=225)
        self.result3_canvas.create_image(0,0,image=self.result, anchor="nw")
        #4体目
        self.result4_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result4_canvas.place(x=615, y=225)
        self.result4_canvas.create_image(0,0,image=self.gray, anchor="nw")
        #5体目
        self.result5_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result5_canvas.place(x=795, y=225)
        self.result5_canvas.create_image(0,0,image=self.gray, anchor="nw")

    def result2_image(self):
        #画像の読み込み
        self.result_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa.png")
        self.result02 = Image.open(self.result_path)
        self.result02 = ImageTk.PhotoImage(self.result02)
        #画像の読み込み
        self.gray_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa_gray.png")
        self.gray02 = Image.open(self.gray_path)
        self.gray = ImageTk.PhotoImage(self.gray)
        #キャンバスの作成
        self.result1_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result1_canvas.place(x=75, y=225)
        #キャンバスに画像を描画
        self.result1_canvas.create_image(0,0,image=self.result, anchor="nw")
        #2体目
        self.result2_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result2_canvas.place(x=255, y=225)
        self.result2_canvas.create_image(0,0,image=self.result, anchor="nw")
        #3体目
        self.result3_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result3_canvas.place(x=435, y=225)
        self.result3_canvas.create_image(0,0,image=self.gray, anchor="nw")
        #4体目
        self.result4_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result4_canvas.place(x=615, y=225)
        self.result4_canvas.create_image(0,0,image=self.gray, anchor="nw")
        #5体目
        self.result5_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result5_canvas.place(x=795, y=225)
        self.result5_canvas.create_image(0,0,image=self.gray, anchor="nw")

    def result1_image(self):
        #画像の読み込み
        self.result_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa.png")
        self.result = Image.open(self.result_path)
        self.result = ImageTk.PhotoImage(self.result)
        #画像の読み込み
        self.gray_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/santa_gray.png")
        self.gray = Image.open(self.gray_path)
        self.gray = ImageTk.PhotoImage(self.gray)
        #キャンバスの作成
        self.result1_canvas = customtkinter.CTkCanvas(master=self, width=self.result.width()-1, height=self.result.height()-1, bd =0)
        self.result1_canvas.place(x=75, y=225)
        #キャンバスに画像を描画
        self.result1_canvas.create_image(0,0,image=self.result, anchor="nw")
        #2体目
        self.result2_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result2_canvas.place(x=255, y=225)
        self.result2_canvas.create_image(0,0,image=self.gray, anchor="nw")
        #3体目
        self.result3_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result3_canvas.place(x=435, y=225)
        self.result3_canvas.create_image(0,0,image=self.gray, anchor="nw")
        #4体目
        self.result4_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result4_canvas.place(x=615, y=225)
        self.result4_canvas.create_image(0,0,image=self.gray, anchor="nw")
        #5体目
        self.result5_canvas = customtkinter.CTkCanvas(master=self, width=self.gray.width()-1, height=self.gray.height()-1, bd =0)
        self.result5_canvas.place(x=795, y=225)
        self.result5_canvas.create_image(0,0,image=self.gray, anchor="nw")

#プレゼントがもらえるかどうか(06)========================================================================  
    def go_to_canGetPresent(self):
        self.result1_canvas.destroy()
        self.result2_canvas.destroy()
        self.result3_canvas.destroy()
        self.result4_canvas.destroy()
        self.result5_canvas.destroy()
        self.resultTrueLabel2.destroy()
        self.getPresentBtn.destroy()
        self.judgeGetPresent()
    
    def judgeGetPresent(self):
        if self.resultNum >= self.beforePresent - 1:
            self.canGetPresent_frame()
            #FirebaseCloudStorageに入れたプレゼントの写真をアップロード
            blob = bucket.blob("post.jpg")
            blob.upload_from_filename("./presentImg/post.jpg")
        else:
            self.cannotGetPresent_frame()

    def canGetPresent_frame(self):
        self.canGetLabel = customtkinter.CTkLabel(self, text="プレゼント交換成立！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.canGetLabel.place(x = 500, y = 250)
        self.canGetBtn = customtkinter.CTkButton(master=self, text="→受け取る←", command=self.go_to_getPresent,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.canGetBtn.place(x = 610, y = 400)
        self.judgeTrue_image()

    def cannotGetPresent_frame(self):
        self.cannotGetLabel = customtkinter.CTkLabel(self, text="プレゼント交換失敗！",  font=self.displayfont, text_color="red", bg_color="#e3e3e3")
        self.cannotGetLabel.place(x = 500, y = 250)
        self.retryBtn = customtkinter.CTkButton(master=self, text="リトライする", command=self.go_to_retry,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.retryBtn.place(x = 610, y = 400)
        self.judgeFalse_image()

    def go_to_retry(self):
        self.cannotGetLabel.destroy()
        self.retryBtn.destroy()
        self.judgeFalse_canvas.destroy()
        #if self.unlockedBox == True:
            #servo.lock(True, False)
        #else:
            #servo.lock(False, False)
        self.openBox_frame()

    def judgeTrue_image(self):
        #画像の読み込み
        self.judgeTrue_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/judgeTrue.png")
        self.judgeTrue = Image.open(self.judgeTrue_path)
        self.judgeTrue = ImageTk.PhotoImage(self.judgeTrue)
        #キャンバスの作成
        self.judgeTrue_canvas = customtkinter.CTkCanvas(master=self, width=self.judgeTrue.width()-1, height=self.judgeTrue.height()-1, bd =0)
        self.judgeTrue_canvas.place(x=5, y=190)
        #キャンバスに画像を描画
        self.judgeTrue_canvas.create_image(0,0,image=self.judgeTrue, anchor="nw")

    def judgeFalse_image(self):
        #画像の読み込み
        self.judgeFalse_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/judgeFalse.png")
        self.judgeFalse = Image.open(self.judgeFalse_path)
        self.judgeFalse = ImageTk.PhotoImage(self.judgeFalse)
        #キャンバスの作成
        self.judgeFalse_canvas = customtkinter.CTkCanvas(master=self, width=self.judgeFalse.width()-1, height=self.judgeFalse.height()-1, bd =0)
        self.judgeFalse_canvas.place(x=75, y=190)
        #キャンバスに画像を描画
        self.judgeFalse_canvas.create_image(0,0,image=self.judgeFalse, anchor="nw")

#プレゼントをゲット(07)========================================================================  
    def go_to_getPresent(self):
        if self.unlockedBox == True:
            self.unlockedBox = False
        else:
            self.unlockedBox = True
        self.judgeTrue_canvas.destroy()
        self.canGetLabel.destroy()
        self.canGetBtn.destroy()
        self.getPresent_frame()
    
    def getPresent_frame(self):
        if self.unlockedBox == True:
            print("上の箱からプレゼントを取り出せます")
            self.getOverB()
        else:
            print("下の箱からプレゼントを取り出せます")
            self.getUnderB()
    
    def getOverB(self):
        self.getOver_image()
        self.getOverComplete = customtkinter.CTkButton(master=self, text="プレゼントを受け取った！", command=self.go_to_endRoll,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.getOverComplete.place(x = 585, y = 470)
        self.getOverCompletelabel1 = customtkinter.CTkLabel(self, text="上の箱の扉を開けて",  font=self.displayfont, text_color="red", bg_color="#e3e3e3")
        self.getOverCompletelabel1.place(x = 515, y = 200)
        self.getOverCompletelabel2 = customtkinter.CTkLabel(self, text="あなたへのプレゼント",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.getOverCompletelabel2.place(x = 515, y = 270)
        self.getOverCompletelabel3 = customtkinter.CTkLabel(self, text="を受け取ろう！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.getOverCompletelabel3.place(x = 515, y = 340)

    def getUnderB(self):
        self.getUnder_image()
        self.getUnderComplete = customtkinter.CTkButton(master=self, text="プレゼントを受け取った！", command=self.go_to_endRoll,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.getUnderComplete.place(x = 585, y = 470)
        self.getUnderCompleteLabel1 = customtkinter.CTkLabel(self, text="下の箱の扉を開けて",  font=self.displayfont, text_color="red", bg_color="#e3e3e3")
        self.getUnderCompleteLabel1.place(x = 515, y = 200)
        self.getUnderCompleteLabel2 = customtkinter.CTkLabel(self, text="あなたへのプレゼント",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.getUnderCompleteLabel2.place(x = 515, y = 270)
        self.getUnderCompleteLabel3 = customtkinter.CTkLabel(self, text="を受け取ろう！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.getUnderCompleteLabel3.place(x = 515, y = 340)

    def getOver_image(self):
        #画像の読み込み
        self.getOver_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/getOverBox.png")
        self.getOver = Image.open(self.getOver_path)
        self.getOver = ImageTk.PhotoImage(self.getOver)
        #キャンバスの作成
        self.getOver_canvas = customtkinter.CTkCanvas(master=self, width=self.getOver.width()-1, height=self.getOver.height()-1, bd =0)
        self.getOver_canvas.place(x=70, y=125, anchor="nw")
        #キャンバスに画像を描画
        self.getOver_canvas.create_image(0,0,image=self.getOver, anchor="nw")

    def getUnder_image(self):
        #画像の読み込み
        self.getUnder_path = os.path.join(os.path.dirname(__file__), R"./src_localapp/getUnderBox.png")
        self.getUnder = Image.open(self.getUnder_path)
        self.getUnder = ImageTk.PhotoImage(self.getUnder)
        #キャンバスの作成
        self.getUnder_canvas = customtkinter.CTkCanvas(master=self, width=self.getUnder.width()-1, height=self.getUnder.height()-1, bd =0)
        self.getUnder_canvas.place(x=70, y=125, anchor="nw")
        #キャンバスに画像を描画
        self.getUnder_canvas.create_image(0,0,image=self.getUnder, anchor="nw")

#エンドロール(08)========================================================================  
    def go_to_endRoll(self):
        if self.unlockedBox == True:
            self.getOver_canvas.destroy()
            self.getOverComplete.destroy()
            self.getOverCompletelabel1.destroy()
            self.getOverCompletelabel2.destroy()
            self.getOverCompletelabel3.destroy()
        else:
            self.getUnder_canvas.destroy()
            self.getUnderComplete.destroy()
            self.getUnderCompleteLabel1.destroy()
            self.getUnderCompleteLabel2.destroy()
            self.getUnderCompleteLabel3.destroy()
        self.endRoll_frame()

    def endRoll_frame(self):
        self.getOver_image()
        self.endLabel = customtkinter.CTkButton(master=self, text="最初に戻る", command=self.go_to_replay,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.endLabel.place(x = 585, y = 470)
        self.endLabel1 = customtkinter.CTkLabel(self, text="使ってくれてありがとう",  font=self.displayfont, text_color="red", bg_color="#e3e3e3")
        self.endLabel1.place(x = 475, y = 200)
        self.endLabel2 = customtkinter.CTkLabel(self, text="QRコードから皆の",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.endLabel2.place(x = 515, y = 270)
        self.endLabel3 = customtkinter.CTkLabel(self, text="プレゼントを覗こう！",  font=self.displayfont, text_color="black", bg_color="#e3e3e3")
        self.endLabel3.place(x = 515, y = 340)
    
    #最初に戻る
    def go_to_replay(self):
        self.getOver_canvas.destroy()
        self.endLabel.destroy()
        self.endLabel1.destroy()
        self.endLabel2.destroy()
        self.endLabel3.destroy()
        self.header_canvas.destroy()
        self.closeB.destroy()
        self.title_frame()

if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()
