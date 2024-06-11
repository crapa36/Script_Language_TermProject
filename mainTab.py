from tkinter import *
from tkinter import ttk
import Pro_City_Dic


class MainTab:

    def __init__(self, notebook, campsites):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="메인")

        self.Campsites = campsites
        self.filteredCampsites = campsites
        self.canvas = Canvas(self.frame, width=1200, height=900, bg="white")
        self.canvas.pack(expand=True, fill="both")

        # 좌측 체크박스
        self.canvas.create_rectangle(20, 20, 400 - 20, 900 - 20, tags="CheckList")
        checkbox_frame = Frame(self.frame)
        checkbox_frame.place(x=30, y=30)
        self.weekday_var = BooleanVar()
        weekday_checkbox = Checkbutton(
            checkbox_frame,
            text="평일 운영",
            variable=self.weekday_var,  # self 추가
            command=self.update_map,
        )
        weekday_checkbox.grid(row=0, column=0)

        self.weekend_var = BooleanVar()
        weekend_checkbox = Checkbutton(
            checkbox_frame,
            text="주말 운영",
            variable=self.weekend_var,  # self 추가
            command=self.update_map,
        )
        weekend_checkbox.grid(row=0, column=1)

        self.filterCampsites()
        # 상세항목
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 300 - 20, tags="Details")

        # 지도탭
        self.canvas.create_rectangle(
            400 + 20, 300 + 20, 1600 - 20, 900 - 20, tags="Details"
        )
        frameL = Frame(self.frame)
        frameL.place(x=400 + 20, y=300 + 20)

        # 도 콤보박스
        self.pro_combobox = ttk.Combobox(frameL)
        self.pro_combobox.pack(side=LEFT)
        self.pro_combobox["values"] = sorted(Pro_City_Dic.korea_regions.keys())
        self.pro_combobox.bind("<<ComboboxSelected>>", self.update_city_combobox)
        self.pro_combobox.set(
            self.pro_combobox["values"][0]
        )  # 첫 번째 값으로 초기값 설정

        # 시 콤보박스
        self.cit_combobox = ttk.Combobox(frameL)
        self.cit_combobox.pack(side=LEFT)
        self.cit_combobox["values"] = sorted(
            Pro_City_Dic.korea_regions[self.pro_combobox.get()]
        )
        self.cit_combobox.set(
            self.cit_combobox["values"][0]
        )  # 첫 번째 값으로 초기값 설정
        # 시 콤보박스 선택 변경 시 update_map 호출
        self.cit_combobox.bind("<<ComboboxSelected>>", lambda event: self.update_map())

    def filterCampsites(self):
        self.filteredCampsites = self.Campsites
        if self.weekday_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "평일" in campsite["openDate"]
            ]
        if self.weekend_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "주말" in campsite["openDate"]
            ]

    def update_city_combobox(self, event):
        # 선택된 도의 이름을 가져옴
        selected_do = self.pro_combobox.get()

        # 시 콤보박스 초기화
        self.cit_combobox.set("")
        self.cit_combobox["values"] = []

        # 선택된 도의 시 리스트를 가져와서 시 콤보박스를 업데이트
        cities = Pro_City_Dic.korea_regions.get(selected_do, [])
        self.cit_combobox["values"] = cities
        self.cit_combobox.set(
            self.cit_combobox["values"][0]
        )  # 첫 번째 값으로 초기값 설정
        # 지도 위치 업데이트
        self.update_map()

    def update_map(self):
        pass
