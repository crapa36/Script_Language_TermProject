from tkinter import *
from tkinter import ttk
class Comparison:

    def __init__(self, notebook, bookmark_list):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="비교하기")

        self.bookmark_list = bookmark_list


        self.canvas = Canvas(
            self.frame, width=1600, height=900, bg="white"
        )  # frame을 부모로 가지는 Canvas 생성
        self.canvas.pack(expand=True, fill="both")  # Canvas를 확장하여 채우도록 설정

        # 좌측 콤보박스
        self.canvas.create_rectangle(20, 20, 800 - 20, 900 - 20, tags="Left")
        left_frame = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        left_frame.place(x=20, y=20)
        self.bookmark_listBoxL = ttk.Combobox(left_frame, width=105)
        self.bookmark_listBoxL.pack(side=LEFT)

        # 우측 콤보박스
        self.canvas.create_rectangle(800 + 20, 20, 1600 - 20, 900 - 20, tags="Left")
        right_frame = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        right_frame.place(x=800 + 20, y=20)
        self.bookmark_listBoxR = ttk.Combobox(right_frame, width=105)
        self.bookmark_listBoxR.pack(side=LEFT)

        for N in self.bookmark_list:
            self.bookmark_listBoxL.insert(END, N['name'])
            self.bookmark_listBoxR.insert(END, N['name'])


