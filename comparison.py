from tkinter import *
from tkinter import ttk
from bookmark import bookmarked_list
class Comparison:

    def __init__(self, notebook):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="비교하기")

        self.canvas = Canvas(
            self.frame, width=1600, height=900, bg="white"
        )  # frame을 부모로 가지는 Canvas 생성
        self.canvas.pack(expand=True, fill="both")  # Canvas를 확장하여 채우도록 설정

        # 좌측 콤보박스
        self.canvas.create_rectangle(20, 20, 800 - 20, 900 - 20, tags="Left")
        left_frame = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        left_frame.place(x=20, y=20)
        self.bookmark_listBox = ttk.Combobox(left_frame, values=bookmarked_list, width=105)
        self.bookmark_listBox.pack(side=LEFT)

        # 우측 콤보박스
        self.canvas.create_rectangle(800 + 20, 20, 1600 - 20, 900 - 20, tags="Left")
        right_frame = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        right_frame.place(x=800 + 20, y=20)
        self.bookmark_listBox = ttk.Combobox(right_frame, values=bookmarked_list, width=105)
        self.bookmark_listBox.pack(side=LEFT)



