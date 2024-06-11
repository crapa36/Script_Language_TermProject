from tkinter import *
from tkinter import ttk
import Pro_City_Dic
from detailedTab import DetailedTab


class MainTab:

    def __init__(self, notebook, campsites, main_gui):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="메인")
        self.notebook = notebook
        selected_campsite = campsites[0]
        self.DetailedTab = DetailedTab(notebook, selected_campsite, main_gui)
        self.Campsites = campsites
        self.filteredCampsites = campsites
        self.canvas = Canvas(self.frame, width=1200, height=900, bg="white")
        self.canvas.pack(expand=True, fill="both")

        # 검색창
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 65 - 20, tags="Details")

        self.search_var = StringVar()
        search_entry = Entry(
            self.frame, textvariable=self.search_var, width=105, font=300
        )
        search_entry.place(x=400 + 20, y=20)

        search_button = Button(self.frame, text="검색", command=self.search_campsites)
        search_button.place(x=1550, y=20)
        self.create_checkboxes()
        # 검색결과
        self.results_frame = Frame(self.frame)
        self.results_frame.place(x=400 + 20, y=100 + 20)

        self.results_canvas = Canvas(self.results_frame, width=1100, height=700)
        self.results_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(
            self.results_frame, orient=VERTICAL, command=self.results_canvas.yview
        )
        scrollbar.pack(side=RIGHT, fill=Y)

        self.results_canvas.configure(yscrollcommand=scrollbar.set)
        self.results_canvas.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(
                scrollregion=self.results_canvas.bbox("all")
            ),
        )

        self.results_frame_inner = Frame(self.results_canvas)
        self.results_canvas.create_window(
            (0, 0), window=self.results_frame_inner, anchor="nw"
        )
        self.search_campsites()

    def create_checkboxes(self):

        # 입지구분에 대한 체크박스
        self.canvas.create_rectangle(20, 20, 400 - 20, 900 - 20, tags="CheckList")
        checkbox_frame = Frame(self.frame)
        checkbox_frame.place(x=30, y=30)

        # 운영일 체크박스
        Label(checkbox_frame, text="운영일", font=("Arial", 12), anchor="w").grid(
            row=0, column=0, columnspan=1, sticky="w"
        )
        self.weekday_var = BooleanVar()
        weekday_checkbox = Checkbutton(
            checkbox_frame,
            text="평일 운영",
            variable=self.weekday_var,
            command=self.filterCampsites,
            anchor="w",
        )
        weekday_checkbox.grid(row=1, column=0, sticky="w")

        self.weekend_var = BooleanVar()
        weekend_checkbox = Checkbutton(
            checkbox_frame,
            text="주말 운영",
            variable=self.weekend_var,
            command=self.filterCampsites,
            anchor="w",
        )
        weekend_checkbox.grid(row=1, column=1, sticky="w")

        # 계절 체크박스
        Label(checkbox_frame, text="운영 계절", font=("Arial", 12), anchor="w").grid(
            row=2, column=0, columnspan=1, sticky="w"
        )
        self.spring_var = BooleanVar()
        spring_checkbox = Checkbutton(
            checkbox_frame,
            text="봄",
            variable=self.spring_var,
            command=self.filterCampsites,
            anchor="w",
        )
        spring_checkbox.grid(row=3, column=0, sticky="w")

        self.summer_var = BooleanVar()
        summer_checkbox = Checkbutton(
            checkbox_frame,
            text="여름",
            variable=self.summer_var,
            command=self.filterCampsites,
            anchor="w",
        )
        summer_checkbox.grid(row=3, column=1, sticky="w")

        self.fall_var = BooleanVar()
        fall_checkbox = Checkbutton(
            checkbox_frame,
            text="가을",
            variable=self.fall_var,
            command=self.filterCampsites,
            anchor="w",
        )
        fall_checkbox.grid(row=3, column=2, sticky="w")

        self.winter_var = BooleanVar()
        winter_checkbox = Checkbutton(
            checkbox_frame,
            text="겨울",
            variable=self.winter_var,
            command=self.filterCampsites,
            anchor="w",
        )
        winter_checkbox.grid(row=3, column=3, sticky="w")

        # 입지 구분 체크박스
        Label(checkbox_frame, text="입지 구분", font=("Arial", 12), anchor="w").grid(
            row=4, column=0, columnspan=1, sticky="w"
        )
        self.mountain_var = BooleanVar()
        mountain_checkbox = Checkbutton(
            checkbox_frame,
            text="산",
            variable=self.mountain_var,
            command=self.filterCampsites,
            anchor="w",
        )
        mountain_checkbox.grid(row=5, column=0, sticky="w")

        self.forest_var = BooleanVar()
        forest_checkbox = Checkbutton(
            checkbox_frame,
            text="숲",
            variable=self.forest_var,
            command=self.filterCampsites,
            anchor="w",
        )
        forest_checkbox.grid(row=5, column=1, sticky="w")

        self.river_var = BooleanVar()
        river_checkbox = Checkbutton(
            checkbox_frame,
            text="강",
            variable=self.river_var,
            command=self.filterCampsites,
            anchor="w",
        )
        river_checkbox.grid(row=5, column=2, sticky="w")

        self.beach_var = BooleanVar()
        beach_checkbox = Checkbutton(
            checkbox_frame,
            text="해변",
            variable=self.beach_var,
            command=self.filterCampsites,
            anchor="w",
        )
        beach_checkbox.grid(row=5, column=3, sticky="w")

        # 동물 허용 여부 체크박스
        Label(
            checkbox_frame, text="동물 허용 여부", font=("Arial", 12), anchor="w"
        ).grid(row=6, column=0, columnspan=1, sticky="w")
        self.animal_allow_var = BooleanVar()
        animal_allow_checkbox = Checkbutton(
            checkbox_frame,
            text="허용",
            variable=self.animal_allow_var,
            command=self.filterCampsites,
            anchor="w",
        )
        animal_allow_checkbox.grid(row=7, column=0, sticky="w")

        self.animal_disallow_var = BooleanVar()
        animal_disallow_checkbox = Checkbutton(
            checkbox_frame,
            text="미허용",
            variable=self.animal_disallow_var,
            command=self.filterCampsites,
            anchor="w",
        )
        animal_disallow_checkbox.grid(row=7, column=1, sticky="w")

        # 부대시설 체크박스
        Label(checkbox_frame, text="부대시설", font=("Arial", 12), anchor="w").grid(
            row=8, column=0, columnspan=1, sticky="w"
        )
        self.electricity_var = BooleanVar()
        electricity_checkbox = Checkbutton(
            checkbox_frame,
            text="전기",
            variable=self.electricity_var,
            command=self.filterCampsites,
            anchor="w",
        )
        electricity_checkbox.grid(row=9, column=0, sticky="w")

        self.internet_var = BooleanVar()
        internet_checkbox = Checkbutton(
            checkbox_frame,
            text="무선인터넷",
            variable=self.internet_var,
            command=self.filterCampsites,
            anchor="w",
        )
        internet_checkbox.grid(row=9, column=1, sticky="w")

        self.firewood_var = BooleanVar()
        firewood_checkbox = Checkbutton(
            checkbox_frame,
            text="장작판매",
            variable=self.firewood_var,
            command=self.filterCampsites,
            anchor="w",
        )
        firewood_checkbox.grid(row=9, column=2, sticky="w")

        self.hotwater_var = BooleanVar()
        hotwater_checkbox = Checkbutton(
            checkbox_frame,
            text="온수",
            variable=self.hotwater_var,
            command=self.filterCampsites,
            anchor="w",
        )
        hotwater_checkbox.grid(row=9, column=3, sticky="w")

        self.waterplay_var = BooleanVar()
        waterplay_checkbox = Checkbutton(
            checkbox_frame,
            text="물놀이장",
            variable=self.waterplay_var,
            command=self.filterCampsites,
            anchor="w",
        )
        waterplay_checkbox.grid(row=10, column=0, sticky="w")

        self.playground_var = BooleanVar()
        playground_checkbox = Checkbutton(
            checkbox_frame,
            text="놀이터",
            variable=self.playground_var,
            command=self.filterCampsites,
            anchor="w",
        )
        playground_checkbox.grid(row=10, column=1, sticky="w")

        self.exercise_var = BooleanVar()
        exercise_checkbox = Checkbutton(
            checkbox_frame,
            text="운동시설",
            variable=self.exercise_var,
            command=self.filterCampsites,
            anchor="w",
        )
        exercise_checkbox.grid(row=10, column=2, sticky="w")

        # 업종 구분 체크박스
        Label(checkbox_frame, text="업종 구분", font=("Arial", 12), anchor="w").grid(
            row=11, column=0, columnspan=1, sticky="w"
        )
        self.general_camp_var = BooleanVar()
        general_camp_checkbox = Checkbutton(
            checkbox_frame,
            text="일반야영장",
            variable=self.general_camp_var,
            command=self.filterCampsites,
            anchor="w",
        )
        general_camp_checkbox.grid(row=12, column=0, sticky="w")

        self.car_camp_var = BooleanVar()
        car_camp_checkbox = Checkbutton(
            checkbox_frame,
            text="자동차야영장",
            variable=self.car_camp_var,
            command=self.filterCampsites,
            anchor="w",
        )
        car_camp_checkbox.grid(row=12, column=1, sticky="w")

        self.caravan_var = BooleanVar()
        caravan_checkbox = Checkbutton(
            checkbox_frame,
            text="카라반",
            variable=self.caravan_var,
            command=self.filterCampsites,
            anchor="w",
        )
        caravan_checkbox.grid(row=12, column=2, sticky="w")

        self.glamping_var = BooleanVar()
        glamping_checkbox = Checkbutton(
            checkbox_frame,
            text="글램핑",
            variable=self.glamping_var,
            command=self.filterCampsites,
            anchor="w",
        )
        glamping_checkbox.grid(row=12, column=3, sticky="w")

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
        if self.mountain_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "산" in campsite["siteView"]
            ]
        if self.forest_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "숲" in campsite["siteView"]
            ]
        if self.river_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "강" in campsite["siteView"]
            ]
        if self.beach_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "해변" in campsite["siteView"]
            ]
        if self.spring_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "봄" in campsite["openSeason"]
            ]
        if self.summer_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "여름" in campsite["openSeason"]
            ]
        if self.fall_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "가을" in campsite["openSeason"]
            ]
        if self.winter_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "겨울" in campsite["openSeason"]
            ]
        if self.animal_allow_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "불" not in campsite["animalAllow"]
            ]
        if self.animal_disallow_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "불" in campsite["animalAllow"]
            ]
        if self.electricity_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "전기" in campsite["amenities"]
            ]
        if self.internet_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "무선인터넷" in campsite["amenities"]
            ]
        if self.firewood_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "장작판매" in campsite["amenities"]
            ]
        if self.hotwater_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "온수" in campsite["amenities"]
            ]
        if self.waterplay_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "물놀이장" in campsite["amenities"]
            ]
        if self.playground_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "놀이터" in campsite["amenities"]
            ]
        if self.exercise_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "운동시설" in campsite["amenities"]
            ]
        if self.general_camp_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "일반야영장" in campsite["induty"]
            ]
        if self.car_camp_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "자동차야영장" in campsite["induty"]
            ]
        if self.caravan_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "카라반" in campsite["induty"]
            ]
        if self.glamping_var.get() == True:
            self.filteredCampsites = [
                campsite
                for campsite in self.filteredCampsites
                if "글램핑" in campsite["induty"]
            ]
        self.display_results(self.filteredCampsites)

    def display_campsite_info(self, selected_campsite):
        self.DetailedTab.update(selected_campsite)
        self.notebook.select(1)

    def display_results(self, results):
        for widget in self.results_frame_inner.winfo_children():
            widget.destroy()
        for campsite in results:
            frame = Frame(self.results_frame_inner)
            frame.pack(fill="x", padx=5, pady=5)

            # 결과를 클릭할 수 있는 버튼 생성
            result_button = Button(
                frame,
                text=f"이름: {campsite['name']}",
                command=lambda campsite=campsite: self.display_campsite_info(campsite),
            )
            result_button.pack(anchor="w")
        self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all"))

    def search_campsites(self):
        search_term = self.search_var.get().lower()
        results = [
            campsite
            for campsite in self.Campsites
            if search_term in campsite["name"].lower()
        ]
        self.display_results(results)
