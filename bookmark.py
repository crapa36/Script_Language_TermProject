from tkinter import *


class Bookmark:

    def __init__(self, notebook):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="찜하기")

        self.canvas = Canvas(
            self.frame, width=1200, height=900, bg="white"
        )  # frame을 부모로 가지는 Canvas 생성
        self.canvas.pack(expand=True, fill="both")  # Canvas를 확장하여 채우도록 설정

        # 좌측 리스트박스
        self.canvas.create_rectangle(20, 20, 400 - 20, 900 - 20, tags="BookmarkList")
        bookmark_frame = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        bookmark_frame.place(x=20, y=20)
        self.bookmark_listBox = Listbox(bookmark_frame, selectmode="extended", width=50,height=60)
        self.bookmark_listBox.pack(side=LEFT)

        bookmark_scroll = Scrollbar(bookmark_frame, orient="vertical")
        bookmark_scroll.config(command=self.bookmark_listBox.yview)
        bookmark_scroll.pack(side=LEFT, fill="y")
        self.bookmark_listBox.config(yscrollcommand=bookmark_scroll.set)


        # 상세항목
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 200 - 20, tags="Details")



