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

        #좌측특성들
        self.left_trait_frame = Frame(self.frame,bg="white")
        self.left_trait_frame.place(x=25, y=50)

        self.Linduty_label = Label(
            self.left_trait_frame,
            font=30,
            bg="white",
        )
        self.Linduty_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.left_trait_frame, bg="white").pack(side=TOP)

        self.LsiteView_label = Label(
            self.left_trait_frame,

            font=30,
            bg="white",
        )
        self.LsiteView_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.left_trait_frame, bg="white").pack(side=TOP)

        self.LopenSeason_lable = Label(
            self.left_trait_frame,

            font=30,
            bg="white",
        )
        self.LopenSeason_lable.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.left_trait_frame, bg="white").pack(side=TOP)

        self.LopenDate_label = Label(
            self.left_trait_frame,
            font=30,
            bg="white",
        )
        self.LopenDate_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.left_trait_frame, bg="white").pack(side=TOP)

        self.LanimalAllow_lable = Label(
            self.left_trait_frame,
            font=30,
            bg="white",
        )
        self.LanimalAllow_lable.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.left_trait_frame, bg="white").pack(side=TOP)

        self.Lamenities_label = Label(
            self.left_trait_frame,
            font=30,
            bg="white",
        )
        self.Lamenities_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.left_trait_frame, bg="white").pack(side=TOP)

        self.Lbrazier_label = Label(
            self.left_trait_frame,
            font=30,
            bg="white",
        )
        self.Lbrazier_label.pack(side=TOP, anchor="w")

        # 우측 콤보박스
        self.canvas.create_rectangle(800 + 20, 20, 1600 - 20, 900 - 20, tags="Right")
        right_frame = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        right_frame.place(x=800 + 20, y=20)
        self.bookmark_listBoxR = ttk.Combobox(right_frame, width=105)
        self.bookmark_listBoxR.pack(side=LEFT)

        # 우측특성들
        self.right_trait_frame = Frame(self.frame, bg="white")
        self.right_trait_frame.place(x=800+25, y=50)

        self.Rinduty_label = Label(
            self.right_trait_frame,
            font=30,
            bg="white",
        )
        self.Rinduty_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.right_trait_frame, bg="white").pack(side=TOP)

        self.RsiteView_label = Label(
            self.right_trait_frame,

            font=30,
            bg="white",
        )
        self.RsiteView_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.right_trait_frame, bg="white").pack(side=TOP)

        self.RopenSeason_lable = Label(
            self.right_trait_frame,

            font=30,
            bg="white",
        )
        self.RopenSeason_lable.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.right_trait_frame, bg="white").pack(side=TOP)

        self.RopenDate_label = Label(
            self.right_trait_frame,
            font=30,
            bg="white",
        )
        self.RopenDate_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.right_trait_frame, bg="white").pack(side=TOP)

        self.RanimalAllow_lable = Label(
            self.right_trait_frame,
            font=30,
            bg="white",
        )
        self.RanimalAllow_lable.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.right_trait_frame, bg="white").pack(side=TOP)

        self.Ramenities_label = Label(
            self.right_trait_frame,
            font=30,
            bg="white",
        )
        self.Ramenities_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(self.right_trait_frame, bg="white").pack(side=TOP)

        self.Rbrazier_label = Label(
            self.right_trait_frame,
            font=30,
            bg="white",
        )
        self.Rbrazier_label.pack(side=TOP, anchor="w")

        # 콤보박스에 이벤트 바인드
        self.bookmark_listBoxL.bind('<<ComboboxSelected>>', self.on_select_left)
        self.bookmark_listBoxR.bind('<<ComboboxSelected>>', self.on_select_right)
    def on_select_left(self, event):
        # 선택된 항목의 인덱스 가져오기
        index = self.bookmark_listBoxL.current()

        # 선택된 캠핑장의 정보 가져오기
        selected_campsite = self.bookmark_list[index]

        # 선택된 캠핑장의 정보 출력 (또는 다른 작업 수행)
        self.Linduty_label.config(text="업종: " + selected_campsite["induty"])
        self.LsiteView_label.config(text="입지: " + selected_campsite["siteView"])
        self.LopenSeason_lable.config(text="운영 계절: " + selected_campsite["openSeason"])
        self.LopenDate_label.config(text="운영일: " + selected_campsite["openDate"])
        self.LanimalAllow_lable.config(text="동물 동반 여부: " + selected_campsite["animalAllow"])
        self.Lamenities_label.config(text="부대시설: " + selected_campsite["amenities"])
        self.Lbrazier_label.config(text="화로대: " + selected_campsite["brazier"])
    def on_select_right(self, event):
        # 선택된 항목의 인덱스 가져오기
        index = self.bookmark_listBoxR.current()

        # 선택된 캠핑장의 정보 가져오기
        selected_campsite = self.bookmark_list[index]

        # 선택된 캠핑장의 정보 출력 (또는 다른 작업 수행)
        self.Rinduty_label.config(text="업종: " + selected_campsite["induty"])
        self.RsiteView_label.config(text="입지: " + selected_campsite["siteView"])
        self.RopenSeason_lable.config(text="운영 계절: " + selected_campsite["openSeason"])
        self.RopenDate_label.config(text="운영일: " + selected_campsite["openDate"])
        self.RanimalAllow_lable.config(text="동물 동반 여부: " + selected_campsite["animalAllow"])
        self.Ramenities_label.config(text="부대시설: " + selected_campsite["amenities"])
        self.Rbrazier_label.config(text="화로대: " + selected_campsite["brazier"])

    def update(self, bookmark_list):
        self.bookmark_list = bookmark_list
        self.bookmark_listBoxL["values"] = [N["name"] for N in self.bookmark_list]
        self.bookmark_listBoxR["values"] = [N["name"] for N in self.bookmark_list]



