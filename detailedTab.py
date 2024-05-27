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
        self.canvas.create_rectangle(20, 20, 800 - 20, 900 - 220, tags="Map")
        # 주소 정보
        self.canvas.create_rectangle(20, 900 - 200, 800 - 20, 900 - 20, tags="Address")
        address_frame = Frame(self.frame, bg='white')
        address_frame.place(x=40, y=900-180)
        #예시용
        address = '강원도 춘천시 남면 가옹개길 52-9'
        address_label = Label(address_frame, text=address, bg='white')
        address_label.pack(side=TOP, anchor='w')
        #예시용
        wep_address = 'http://outofpark.com/main/'
        wep_address_label = Label(address_frame, text=wep_address, bg='white')
        wep_address_label.pack(side=TOP, anchor='w')
        #예시용
        call_num = '1522-1861-'
        call_num_label = Label(address_frame, text=call_num, bg='white')
        call_num_label.pack(side=TOP, anchor='w')



        # 캠핑장 이름
        self.canvas.create_rectangle(800 + 20, 20, 1600 - 20, 200 - 20, tags="Name")

        name_frame = Frame(self.frame, bg='white')
        name_frame.place(x=800+40, y=20+20)
        #예시용
        name = '(주)아웃오브파크'
        name_label = Label(name_frame, text=name, font=(30), bg='white')
        name_label.pack(side=TOP, anchor='w')
        #예시용
        description = '아웃오브파트는 강원도 춘천시 남면에 자리했다. 서울양양고속도로 강촌IC에서 엘리시안강촌 방면으로 30분가량 달리면 도착한다. 이곳은 북 한강 변의 수려한 풍광을 배경으로 캐러밴 40대가 들어찼다. 고급스러움이 돋보이는 유럽피안 캐러밴과 에어스트림 캐러밴이다. 모든 캐러밴은 각기 다른 주제로 꾸몄다. 이 덕분에 욕실에 중점을 둔 객실이나 침실에 초점을 맞춘 객실 등 취향에 따라 선택하는 재미가 있다. 외부에는 어닝 아래  테이블, 의자, 노천욕탕, 바비큐 시설을 마련했다. 캠핑장의 강점 중 하나는 부대시설이다. 카페, 수영장, 찜질방, 스파, 중앙 무대, 분수, 노래방 등 고급스러움으로 치장한 시설이 차고 넘친다.'
        description_label = Label(name_frame, text=description, wraplength=720, justify=LEFT, bg='white')
        description_label.pack(side=TOP)
