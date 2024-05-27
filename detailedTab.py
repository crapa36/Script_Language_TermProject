from tkinter import *
import Pro_City_Dic


class DetailedTab:
    def __init__(self, notebook):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="세부정보")

        self.canvas = Canvas(
            self.frame, width=1600, height=900, bg="white"
        )  # frame을 부모로 가지는 Canvas 생성
        self.canvas.pack(expand=True, fill="both")  # Canvas를 확장하여 채우도록 설정
        # 지도탭
        self.canvas.create_rectangle(20, 20, 800 - 20, 900 - 220, tags="Details")
        # 주소 정보
        self.canvas.create_rectangle(20, 900 - 200, 800 - 20, 900 - 20, tags="Details")
        # 좌측 체크박스
