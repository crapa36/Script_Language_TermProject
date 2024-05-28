from tkinter import *
from tkinter import ttk
import Pro_City_Dic


class MainTab:

    def __init__(self, notebook):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="메인")

        self.canvas = Canvas(self.frame, width=1200, height=900, bg="white")
        self.canvas.pack(expand=True, fill="both")

        # 좌측 체크박스
        self.canvas.create_rectangle(20, 20, 400 - 20, 900 - 20, tags="CheckList")
        frameC = Frame(self.frame)
        frameC.place(x=30, y=30)
        self.CheckBox1 = IntVar()
        Checkbutton(frameC, text="항목1", variable=self.CheckBox1).pack(side=TOP)
        self.CheckBox2 = IntVar()
        Checkbutton(frameC, text="항목2", variable=self.CheckBox2).pack(side=TOP)

        # 상세항목
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 300 - 20, tags="Details")

        # 지도탭
        self.canvas.create_rectangle(400 + 20, 300 + 20, 1600 - 20, 900 - 20, tags="Details")
        frameL = Frame(self.frame)
        frameL.place(x=400 + 20, y=300 + 20)

        # 도 콤보박스
        self.pro_combobox = ttk.Combobox(frameL)
        self.pro_combobox.pack(side=LEFT)
        self.pro_combobox['values'] = sorted(Pro_City_Dic.korea_regions.keys())
        self.pro_combobox.bind('<<ComboboxSelected>>', self.update_city_combobox)

        # 시 콤보박스
        self.cit_combobox = ttk.Combobox(frameL)
        self.cit_combobox.pack(side=LEFT)

    def update_city_combobox(self, event):
        # 선택된 도의 이름을 가져옴
        selected_do = self.pro_combobox.get()

        # 시 콤보박스 초기화
        self.cit_combobox.set('')
        self.cit_combobox['values'] = []

        # 선택된 도의 시 리스트를 가져와서 시 콤보박스를 업데이트
        cities = Pro_City_Dic.korea_regions.get(selected_do, [])
        self.cit_combobox['values'] = cities