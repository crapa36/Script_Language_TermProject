from tkinter import *
from tkinter import ttk
import Pro_City_Dic
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import io
import requests
from googlemaps import Client


class MainTab:

    def __init__(self, notebook, campsites):
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="메인")

        self.Mcampsites = campsites

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

        # Google Maps API 클라이언트 생성
        self.Google_API_Key = "AIzaSyCzFgc9OGnXckq1-JNhSCVGo9zIq1kSWcE"
        self.gmaps = Client(key=self.Google_API_Key)

        self.zoom = 10

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
        # 지도 이미지 라벨 생성
        self.map_label = Label(frameL)

        # 지도 업데이트
        self.update_map()

        # 지도 이미지 라벨 배치
        self.map_label.pack()  # 콤보박스 아래에 배치

    def update_map(self):
        # 지도의 중심을 콤보박스에서 선택한 위치로 설정
        selected_location = self.pro_combobox.get() + " " + self.cit_combobox.get()
        center = self.gmaps.geocode(selected_location)[0]["geometry"]["location"]

        map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={center['lat']},{center['lng']}&zoom={self.zoom}&size=800x500&maptype=roadmap"

        # 서울시 구별 병원 위치 마커 추가
        for campsite in self.Mcampsites:
            if campsite["lat"] and campsite["lng"]:
                lat, lng = float(campsite["lat"]), float(campsite["lng"])
                marker_url = f"&markers=color:red%7C{lat},{lng}"
                map_url += marker_url

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
        self.cit_combobox["values"] = []

        # 선택된 도의 시 리스트를 가져와서 시 콤보박스를 업데이트
        cities = Pro_City_Dic.korea_regions.get(selected_do, [])
        self.cit_combobox["values"] = cities
        self.cit_combobox.set(
            self.cit_combobox["values"][0]
        )  # 첫 번째 값으로 초기값 설정
        # 지도 위치 업데이트
        self.update_map()
