from tkinter import *


class DetailedTab:
    def __init__(self, notebook):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="세부정보")


        self.address = '강원도 춘천시 남면 가옹개길 52-9'

        self.wep_address = 'http://outofpark.com/main/'

        self.call_num = '1522-1861-'

        self.way_to_book = '온라인실시간예약'

        self.name = '(주)아웃오브파크'

        self.description = '아웃오브파트는 강원도 춘천시 남면에 자리했다. 서울양양고속도로 강촌IC에서 엘리시안강촌 방면으로 30분가량 달리면 도착한다. 이곳은 북 한강 변의 수려한 풍광을 배경으로 캐러밴 40대가 들어찼다. 고급스러움이 돋보이는 유럽피안 캐러밴과 에어스트림 캐러밴이다. 모든 캐러밴은 각기 다른 주제로 꾸몄다. 이 덕분에 욕실에 중점을 둔 객실이나 침실에 초점을 맞춘 객실 등 취향에 따라 선택하는 재미가 있다. 외부에는 어닝 아래  테이블, 의자, 노천욕탕, 바비큐 시설을 마련했다. 캠핑장의 강점 중 하나는 부대시설이다. 카페, 수영장, 찜질방, 스파, 중앙 무대, 분수, 노래방 등 고급스러움으로 치장한 시설이 차고 넘친다.'

        self.category = '카라반'

        self.position = '산,강'

        self.season = '봄,여름,가을,겨울'

        self.date = '평일+주말'

        self.can_animal = '불가능'

        self.additional_facilities = '운동시설'

        self.brazier_stand = '개별'

        self.canvas = Canvas(
            self.frame, width=1600, height=900, bg="white"
        )  # frame을 부모로 가지는 Canvas 생성
        self.canvas.pack(expand=True, fill="both")  # Canvas를 확장하여 채우도록 설정
        # 지도탭
        self.canvas.create_rectangle(20, 20, 800 - 20, 900 - 220, tags="Map")
        # 주소 정보
        self.canvas.create_rectangle(20, 900 - 200, 800 - 20, 900 - 20, tags="Address")
        address_frame = Frame(self.frame, bg='white')
        address_frame.place(x=40, y=900 - 180)

        self.address_label = Label(address_frame, text=self.address, bg='white')
        self.address_label.pack(side=TOP, anchor='w')

        self.wep_address_label = Label(address_frame, text=self.wep_address, bg='white')
        self.wep_address_label.pack(side=TOP, anchor='w')

        self.call_num_label = Label(address_frame, text=self.call_num, bg='white')
        self.call_num_label.pack(side=TOP, anchor='w')

        self.way_to_book_label = Label(address_frame, text=self.way_to_book, bg='white')
        self.way_to_book_label.pack(side=TOP, anchor='w')

        # 캠핑장 이름
        self.canvas.create_rectangle(800 + 20, 20, 1600 - 20, 200 - 20, tags="Name")

        name_frame = Frame(self.frame, bg='white')
        name_frame.place(x=800 + 40, y=20 + 20)

        self.name_label = Label(name_frame, text='이름: '+self.name, font=30, bg='white')
        self.name_label.pack(side=TOP, anchor='w')

        self.description_label = Label(name_frame, text=self.description, wraplength=720, justify=LEFT, bg='white')
        self.description_label.pack(side=TOP)

        # 캠핑장 특성
        self.canvas.create_rectangle(800 + 20, 200 + 20, 1600 - 20, 900 - 20, tags="Trait")
        trait_frame = Frame(self.frame, bg='white')
        trait_frame.place(x=800 + 40, y=200 + 40)

        # 업종, 입지 구분, 운영계절, 운영일, 동물 허용, 부대시설, 화로대

        self.category_label = Label(trait_frame, text='업종: ' + self.category, font=30, bg='white')
        self.category_label.pack(side=TOP, anchor='w')
        # 띄어쓰기
        Label(trait_frame, bg='white').pack(side=TOP)


        self.position_label = Label(trait_frame, text='입지: ' + self.position, font=30, bg='white')
        self.position_label.pack(side=TOP, anchor='w')
        # 띄어쓰기
        Label(trait_frame, bg='white').pack(side=TOP)

        self.season_label = Label(trait_frame, text='계절: ' + self.season, font=30, bg='white')
        self.season_label.pack(side=TOP, anchor='w')
        # 띄어쓰기
        Label(trait_frame, bg='white').pack(side=TOP)

        self.date_label = Label(trait_frame, text='운영일: ' + self.date, font=30, bg='white')
        self.date_label.pack(side=TOP, anchor='w')
        # 띄어쓰기
        Label(trait_frame, bg='white').pack(side=TOP)

        self.can_animal_label = Label(trait_frame, text='동물 동반 여부: ' + self.can_animal, font=30, bg='white')
        self.can_animal_label.pack(side=TOP, anchor='w')
        # 띄어쓰기
        Label(trait_frame, bg='white').pack(side=TOP)

        self.additional_facilities_label = Label(trait_frame, text='부대시설: ' + self.additional_facilities, font=30, bg='white')
        self.additional_facilities_label.pack(side=TOP, anchor='w')
        # 띄어쓰기
        Label(trait_frame, bg='white').pack(side=TOP)

        self.brazier_stand_label = Label(trait_frame, text='화로대: ' + self.brazier_stand, font=30, bg='white')
        self.brazier_stand_label.pack(side=TOP, anchor='w')

    def update(self, campsite):
        if campsite is not None:
            # 캠핑장 정보를 표시하는 레이블 업데이트
            self.address_label.config(text=campsite['address'])
            self.wep_address_label.config(text=campsite['homepage'])
            self.call_num_label.config(text=campsite['telNum'])
            self.way_to_book_label.config(text=campsite['reserve'])
            self.name_label.config(text='이름: ' + campsite['name'])
            self.description_label.config(text=campsite['intro'])
            self.category_label.config(text='업종: ' + campsite['induty'])
            self.position_label.config(text='입지: ' + campsite['siteView'])
            self.season_label.config(text='계절: ' + campsite['openSeason'])
            self.date_label.config(text='운영일: ' + campsite['openDate'])
            self.can_animal_label.config(text='동물 동반 여부: ' + campsite['animalAllow'])
            self.additional_facilities_label.config(text='부대시설: ' + campsite['amenities'])
            self.brazier_stand_label.config(text='화로대: ' + campsite['brazier'])

