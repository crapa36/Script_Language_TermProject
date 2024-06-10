from tkinter import *
from tkinter import ttk
import Pro_City_Dic
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import io
import requests
from googlemaps import Client


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
        Checkbutton(frameC, text="캐러반", variable=self.CheckBox1).pack(side=TOP)
        self.CheckBox2 = IntVar()
        Checkbutton(frameC, text="카캠핑", variable=self.CheckBox2).pack(side=TOP)
        self.CheckBox3 = IntVar()
        Checkbutton(frameC, text="글램핑", variable=self.CheckBox3).pack(side=TOP)
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

        # 시 콤보박스
        self.cit_combobox = ttk.Combobox(frameL)
        self.cit_combobox.pack(side=LEFT)

        # Google Maps API 클라이언트 생성
        self.Google_API_Key = "AIzaSyCzFgc9OGnXckq1-JNhSCVGo9zIq1kSWcE"
        self.gmaps = Client(key=self.Google_API_Key)

        # 지도의 초기 위치를 서울특별시로 설정
        self.address = "서울특별시"
        self.zoom = 13

        # 지도 이미지 라벨 생성
        self.map_label = Label(frameL)
        self.map_label.pack()

        # 지도 업데이트
        self.update_map()

    def update_map(self):
        # 지도의 중심을 주소로 설정
        center = self.gmaps.geocode(self.address)[0]["geometry"]["location"]
        map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={center['lat']},{center['lng']}&zoom={self.zoom}&size=400x400&maptype=roadmap"

        # # 캠핑장 코드로 수정 필요
        # hospitals_in_city = [hospital for hospital in self.hospitals if hospital['address'].split()[0] == self.address]
        # for hospital in hospitals_in_city:
        #     if hospital['lat'] and hospital['lng']:
        #         lat, lng = float(hospital['lat']), float(hospital['lng'])
        #         marker_url = f"&markers=color:red%7C{lat},{lng}"
        #         map_url += marker_url

        # 지도 이미지 다운로드
        response = requests.get(map_url + "&key=" + self.Google_API_Key)
        image = Image.open(io.BytesIO(response.content))
        photo = ImageTk.PhotoImage(image)

        # 지도 이미지 라벨 업데이트
        self.map_label.configure(image=photo)
        self.map_label.image = photo

    def update_city_combobox(self, event):
        # 선택된 도의 이름을 가져옴
        selected_do = self.pro_combobox.get()

        # 시 콤보박스 초기화
        self.cit_combobox.set("")

        # 지도 위치 업데이트
        self.map_widget.set_address(selected_do)
