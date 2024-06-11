from tkinter import *


class Bookmark:

    def __init__(self, notebook, bookmark_list):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="찜하기")

        self.bookmark_list = bookmark_list

        self.canvas = Canvas(
            self.frame, width=1200, height=900, bg="white"
        )  # frame을 부모로 가지는 Canvas 생성
        self.canvas.pack(expand=True, fill="both")  # Canvas를 확장하여 채우도록 설정

        # 좌측 리스트박스
        self.canvas.create_rectangle(20, 20, 400 - 20, 900 - 20, tags="BookmarkList")
        bookmark_frame = Frame(self.frame)  # 부모 위젯을 self.frame으로 변경
        bookmark_frame.place(x=20, y=20)
        self.bookmark_listBox = Listbox(
            bookmark_frame, selectmode="extended", width=50, height=60
        )
        self.bookmark_listBox.pack(side=LEFT)

        bookmark_scroll = Scrollbar(bookmark_frame, orient="vertical")
        bookmark_scroll.config(command=self.bookmark_listBox.yview)
        bookmark_scroll.pack(side=LEFT, fill="y")
        self.bookmark_listBox.config(yscrollcommand=bookmark_scroll.set)
        self.bookmark_listBox.bind("<<ListboxSelect>>", self.on_select)

        # 이름, 설명
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 200 - 20, tags="name")
        name_frame = Frame(self.frame, bg="white")
        name_frame.place(x=400 + 40, y=20 + 20)

        self.name_label = Label(name_frame, font=30, bg="white")
        self.name_label.pack(side=TOP, anchor="w")

        self.description_label = Label(
            name_frame, wraplength=720, justify=LEFT, bg="white"
        )
        self.description_label.pack(side=TOP)
        # 상세
        self.canvas.create_rectangle(
            400 + 20, 200 + 20, 1600 - 20, 900 - 20, tags="Details"
        )
        details_frame = Frame(self.frame, bg="white")
        details_frame.place(x=400 + 40, y=200 + 40)

        self.category_label = Label(details_frame, font=30, bg="white")
        self.category_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)

        self.position_label = Label(details_frame, font=30, bg="white")
        self.position_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)

        self.season_label = Label(details_frame, font=30, bg="white")
        self.season_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)

        self.date_label = Label(details_frame, font=30, bg="white")
        self.date_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)

        self.can_animal_label = Label(details_frame, font=30, bg="white")
        self.can_animal_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)

        self.additional_facilities_label = Label(details_frame, font=30, bg="white")
        self.additional_facilities_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)

        self.brazier_stand_label = Label(details_frame, font=30, bg="white")
        self.brazier_stand_label.pack(side=TOP, anchor="w")

        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)

        self.address_label = Label(details_frame, font=30, bg="white")
        self.address_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)
        self.wep_address_label = Label(details_frame, font=30, bg="white")
        self.wep_address_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)
        self.call_num_label = Label(details_frame, font=30, bg="white")
        self.call_num_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(details_frame, bg="white").pack(side=TOP)
        self.way_to_book_label = Label(details_frame, font=30, bg="white")
        self.way_to_book_label.pack(side=TOP, anchor="w")

        for N in self.bookmark_list:
            self.bookmark_listBox.insert(END, N["name"])

    def on_select(self, event):
        # 선택된 항목의 인덱스 가져오기
        index = self.bookmark_listBox.curselection()

        # 선택된 캠핑장의 정보 가져오기
        selected_campsite = self.bookmark_list[index[0]]

        # 선택된 캠핑장의 정보 출력 (또는 다른 작업 수행)
        self.address_label.config(text="주소: " + selected_campsite["address"])
        self.wep_address_label.config(text="홈페이지: " + selected_campsite["homepage"])
        self.call_num_label.config(text="전화번호: " + selected_campsite["telNum"])
        self.way_to_book_label.config(text="예약방법: " + selected_campsite["reserve"])
        self.name_label.config(text="이름: " + selected_campsite["name"])
        self.description_label.config(text=selected_campsite["intro"])
        self.category_label.config(text="업종: " + selected_campsite["induty"])
        self.position_label.config(text="입지: " + selected_campsite["siteView"])
        self.season_label.config(text="계절: " + selected_campsite["openSeason"])
        self.date_label.config(text="운영일: " + selected_campsite["openDate"])
        self.can_animal_label.config(
            text="동물 동반 여부: " + selected_campsite["animalAllow"]
        )
        self.additional_facilities_label.config(
            text="부대시설: " + selected_campsite["amenities"]
        )
        self.brazier_stand_label.config(text="화로대: " + selected_campsite["brazier"])

        # 삭제하기 버튼
        self.button_frame = Frame(self.frame)
        self.button_frame.place(x=1520, y=220)
        self.bookmark_button = Button(
            self.button_frame, text="삭제하기"
        )
        self.bookmark_button.pack(side=TOP)

    def update(self, bookmarks):
        self.bookmark_listBox.delete(0, "end")  # 기존 항목 삭제
        for bookmark in bookmarks:
            self.bookmark_listBox.insert("end", bookmark["name"])  # 새 항목 추가
