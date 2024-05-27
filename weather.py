from tkinter import *


class Weather:

    def __init__(self, notebook):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="날씨")

        self.canvas = Canvas(
            self.frame, width=1200, height=900, bg="white"
        )  # frame을 부모로 가지는 Canvas 생성
        self.canvas.pack(expand=True, fill="both")  # Canvas를 확장하여 채우도록 설정

        # 좌측 체크박스
        self.canvas.create_rectangle(20, 20, 400 - 20, 900 - 20, tags="CheckList")
        frameC = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        frameC.place(x=30, y=30)
        self.CheckBox1 = IntVar()
        Checkbutton(frameC, text="항목1", variable=self.CheckBox1).pack(side=TOP)
        self.CheckBox2 = IntVar()
        Checkbutton(frameC, text="항목2", variable=self.CheckBox2).pack(side=TOP)
        # 항목 숫자별로 추가

        # 상세항목
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 200 - 20, tags="Details")



