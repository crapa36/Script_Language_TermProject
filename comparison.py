from tkinter import *
from tkinter import ttk


class Comparison:
    def __init__(self, notebook, bookmark_list):
        self.notebook = notebook
        self.bookmark_list = bookmark_list
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
        self.bookmark_listBoxL = ttk.Combobox(left_frame, width=105)
        self.bookmark_listBoxL.pack(side=LEFT)

        # 우측 콤보박스
        self.canvas.create_rectangle(800 + 20, 20, 1600 - 20, 900 - 20, tags="Right")
        right_frame = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        right_frame.place(x=800 + 20, y=20)
        self.bookmark_listBoxR = ttk.Combobox(right_frame, width=105)
        self.bookmark_listBoxR.pack(side=LEFT)

        # 콤보박스에 이벤트 바인드
        self.bookmark_listBoxL.bind('<<ComboboxSelected>>', self.on_select_left)
        self.bookmark_listBoxR.bind('<<ComboboxSelected>>', self.on_select_right)
    def on_select_left(self, event):
        # 선택된 항목의 인덱스 가져오기
        index = self.bookmark_listBoxL.current()

        # 선택된 캠핑장의 정보 가져오기
        selected_campsite = self.bookmark_list[index]

        # 선택된 캠핑장의 정보 출력 (또는 다른 작업 수행)
        print(selected_campsite)
    def on_select_right(self, event):
        # 선택된 항목의 인덱스 가져오기
        index = self.bookmark_listBoxR.current()

        # 선택된 캠핑장의 정보 가져오기
        selected_campsite = self.bookmark_list[index]

        # 선택된 캠핑장의 정보 출력 (또는 다른 작업 수행)
        print(selected_campsite)

    def update(self, bookmark_list):
        self.bookmark_list = bookmark_list
        self.bookmark_listBoxL["values"] = [N["name"] for N in self.bookmark_list]
        self.bookmark_listBoxR["values"] = [N["name"] for N in self.bookmark_list]
