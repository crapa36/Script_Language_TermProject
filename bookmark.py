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
        self.bookmark_listBox = Listbox(bookmark_frame, selectmode="extended", width=50,height=60)
        self.bookmark_listBox.pack(side=LEFT)

        bookmark_scroll = Scrollbar(bookmark_frame, orient="vertical")
        bookmark_scroll.config(command=self.bookmark_listBox.yview)
        bookmark_scroll.pack(side=LEFT, fill="y")
        self.bookmark_listBox.config(yscrollcommand=bookmark_scroll.set)
        self.bookmark_listBox.bind('<<ListboxSelect>>', self.on_select)

        # 이름, 설명
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 200 - 20, tags="name")
        name_frame = Frame(self.frame, bg='white')
        name_frame.place(x=400 + 40, y=20 + 20)

        self.name_label = Label(name_frame, font=30, bg='white')
        self.name_label.pack(side=TOP, anchor='w')

        self.description_label = Label(name_frame, wraplength=720, justify=LEFT, bg='white')
        self.description_label.pack(side=TOP)
        #상세
        self.canvas.create_rectangle(400 + 20, 200 + 20, 1600 - 20, 900 - 20, tags="Details")
        details_frame = Frame(self.frame, bg='white')
        details_frame.place(x=400 + 40, y=200 + 40)

        for N in self.bookmark_list:
            self.bookmark_listBox.insert(END, N['name'])



    def on_select(self, event):
        # 선택된 항목의 인덱스 가져오기
        index = self.bookmark_listBox.curselection()

        # 선택된 캠핑장의 정보 가져오기
        selected_campsite = self.bookmark_list[index[0]]

        # 선택된 캠핑장의 정보 출력 (또는 다른 작업 수행)
        print(selected_campsite)
        self.name_label.config(text=selected_campsite['name'])
        self.description_label.config(text=selected_campsite['intro'])


