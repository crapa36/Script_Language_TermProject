from tkinter import *
import Pro_City_Dic


class MainTab:

    def __init__(self, notebook):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="메인")

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
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 400 - 20, tags="Details")

        # 지도탭
        self.canvas.create_rectangle(
            400 + 20, 400 + 20, 1600 - 20, 900 - 20, tags="Details"
        )
        frameL = Frame(self.frame)
        frameL.place(x=400 + 20, y=400 + 20)
        # 도 리스트박스
        self.ProListBox = Listbox(frameL, selectmode="extended")
        self.ProListBox.pack(side=LEFT)

        Proscroll = Scrollbar(frameL, orient="vertical")
        Proscroll.config(command=self.ProListBox.yview)
        Proscroll.pack(side=LEFT, fill="y")
        self.ProListBox.config(yscrollcommand=Proscroll.set)

        for k in sorted(Pro_City_Dic.korea_regions.keys()):
            self.ProListBox.insert(END, k)

        # 시 리스트박스
        self.citListBox = Listbox(frameL, selectmode="extended")
        self.citListBox.pack(side=LEFT)

        citScroll = Scrollbar(frameL, orient="vertical")
        citScroll.config(command=self.citListBox.yview)
        citScroll.pack(side=LEFT, fill="y")
        self.citListBox.config(yscrollcommand=citScroll.set)

        # 이벤트 바인딩
        self.ProListBox.bind('<<ListboxSelect>>', self.update_city_list)

    def update_city_list(self, event):
        # 선택된 도의 이름을 가져옴
        selected_indices = self.ProListBox.curselection()
        if not selected_indices:
            return

        selected_do = self.ProListBox.get(selected_indices[0])

        # 선택된 도의 시 리스트를 가져와서 시 리스트박스를 업데이트
        cities = Pro_City_Dic.korea_regions.get(selected_do, [])
        self.citListBox.delete(0, END)
        for city in cities:
            self.citListBox.insert(END, city)