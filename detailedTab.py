from tkinter import *

from PIL import Image, ImageTk
import io
import requests
from googlemaps import Client
import telepot
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

TOKEN = "7481744351:AAE3Po9SQfY-HfkDk4hIoIYQ3s36X3eke-Q"  # 텔레그램 봇의 API 토큰
bot = telepot.Bot(TOKEN)


class DetailedTab:
    def __init__(self, notebook, selected_campsite, main_gui):
        self.notebook = notebook
        self.selected_campsite = selected_campsite
        self.frame = Frame(notebook)
        notebook.add(self.frame, text="세부정보")
        self.main_gui = main_gui
        self.canvas = Canvas(
            self.frame, width=1600, height=900, bg="white"
        )  # frame을 부모로 가지는 Canvas 생성
        self.canvas.pack(expand=True, fill="both")  # Canvas를 확장하여 채우도록 설정
        # 지도탭
        
        frameL = Frame(self.frame)
        frameL.place(x=60, y=30)
        # Google Maps API 클라이언트 생성
        self.Google_API_Key = "AIzaSyCzFgc9OGnXckq1-JNhSCVGo9zIq1kSWcE"
        self.gmaps = Client(key=self.Google_API_Key)

        self.zoom = 10
        # 지도 이미지 라벨 생성
        self.map_label = Label(frameL)

        # 지도 업데이트
        self.update_map()

        # 지도 이미지 라벨 배치
        self.map_label.pack()

        # 주소 정보
        self.canvas.create_rectangle(20, 900 - 200, 800 - 20, 900 - 20, tags="Address")
        address_frame = Frame(self.frame, bg="white")
        address_frame.place(x=40, y=900 - 180)

        self.address_label = Label(
            address_frame, text=selected_campsite["address"], bg="white"
        )
        self.address_label.pack(side=TOP, anchor="w")

        self.homepage_label = Label(
            address_frame, text=selected_campsite["homepage"], bg="white"
        )
        self.homepage_label.pack(side=TOP, anchor="w")

        self.telNum_label = Label(
            address_frame, text=selected_campsite["telNum"], bg="white"
        )
        self.telNum_label.pack(side=TOP, anchor="w")

        self.reserve_label = Label(
            address_frame, text=selected_campsite["reserve"], bg="white"
        )

        # 캠핑장 이름
        self.canvas.create_rectangle(800 + 20, 20, 1600 - 20, 200 - 20, tags="Name")

        name_frame = Frame(self.frame, bg="white")
        name_frame.place(x=800 + 40, y=20 + 20)

        self.name_label = Label(
            name_frame, text="이름: " + selected_campsite["name"], font=30, bg="white"
        )
        self.name_label.pack(side=TOP, anchor="w")

        self.intro_label = Label(
            name_frame,
            text=selected_campsite["intro"],
            wraplength=720,
            justify=LEFT,
            bg="white",
        )
        self.intro_label.pack(side=TOP)

        # 캠핑장 특성
        self.canvas.create_rectangle(
            800 + 20, 200 + 20, 1600 - 20, 900 - 20, tags="Trait"
        )
        trait_frame = Frame(self.frame, bg="white")
        trait_frame.place(x=800 + 40, y=200 + 40)

        # 업종, 입지 구분, 운영계절, 운영일, 동물 허용, 부대시설, 화로대
        self.induty_label = Label(
            trait_frame,
            text="업종: " + selected_campsite["induty"],
            font=30,
            bg="white",
        )
        self.induty_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(trait_frame, bg="white").pack(side=TOP)

        self.siteView_label = Label(
            trait_frame,
            text="입지: " + selected_campsite["siteView"],
            font=30,
            bg="white",
        )
        self.siteView_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(trait_frame, bg="white").pack(side=TOP)

        self.openSeason_lable = Label(
            trait_frame,
            text="운영 계절: " + selected_campsite["openSeason"],
            font=30,
            bg="white",
        )
        self.openSeason_lable.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(trait_frame, bg="white").pack(side=TOP)

        self.openDate_label = Label(
            trait_frame,
            text="운영일: " + selected_campsite["openDate"],
            font=30,
            bg="white",
        )
        self.openDate_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(trait_frame, bg="white").pack(side=TOP)

        self.animalAllow_lable = Label(
            trait_frame,
            text="동물 동반 여부: " + selected_campsite["animalAllow"],
            font=30,
            bg="white",
        )
        self.animalAllow_lable.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(trait_frame, bg="white").pack(side=TOP)

        self.amenities_label = Label(
            trait_frame,
            text="부대시설: " + selected_campsite["amenities"],
            font=30,
            bg="white",
        )
        self.amenities_label.pack(side=TOP, anchor="w")
        # 띄어쓰기
        Label(trait_frame, bg="white").pack(side=TOP)

        self.brazier_label = Label(
            trait_frame,
            text="화로대: " + selected_campsite["brazier"],
            font=30,
            bg="white",
        )
        self.brazier_label.pack(side=TOP, anchor="w")

        # 찜하기 버튼
        self.button_frame = Frame(self.frame)
        self.button_frame.place(x=1520, y=220)
        self.bookmark_button = Button(
            self.button_frame, text="찜하기", command=self.add_to_bookmarks
        )
        self.bookmark_button.pack(side=TOP)

        # 텔레그램 버튼
        self.bookmark_button = Button(
            self.button_frame, text="텔레그램", command=self.send_telegram_message
        )
        self.bookmark_button.pack(side=TOP)

        # 이메일 버튼
        self.bookmark_button = Button(
            self.button_frame, text="이메일", command=self.send_email
        )
        self.bookmark_button.pack(side=TOP)

    def update_map(self):

        map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={float(self.selected_campsite['lat'])},{float(self.selected_campsite['lng'])}&zoom={self.zoom}&size=1200x1200&maptype=roadmap"
        lat, lng = float(self.selected_campsite["lat"]), float(
            self.selected_campsite["lng"]
        )
        marker_url = f"&markers=color:red%7C{lat},{lng}"
        map_url += marker_url

        # 지도 이미지 다운로드
        response = requests.get(map_url + "&key=" + self.Google_API_Key)
        image = Image.open(io.BytesIO(response.content))
        photo = ImageTk.PhotoImage(image)

        # 지도 이미지 라벨 업데이트
        self.map_label.configure(image=photo)
        self.map_label.image = photo

    def update_labels(self):
        self.address_label.config(text=self.selected_campsite["address"])
        self.homepage_label.config(text=self.selected_campsite["homepage"])
        self.telNum_label.config(text=self.selected_campsite["telNum"])
        self.reserve_label.config(text=self.selected_campsite["reserve"])
        self.name_label.config(text="이름: " + self.selected_campsite["name"])
        self.intro_label.config(text=self.selected_campsite["intro"])
        self.induty_label.config(text="업종: " + self.selected_campsite["induty"])
        self.siteView_label.config(text="입지: " + self.selected_campsite["siteView"])
        self.openSeason_lable.config(
            text="운영 계절: " + self.selected_campsite["openSeason"]
        )
        self.openDate_label.config(text="운영일: " + self.selected_campsite["openDate"])
        self.animalAllow_lable.config(
            text="동물 동반 여부: " + str(self.selected_campsite["animalAllow"])
        )
        self.amenities_label.config(
            text="부대시설: " + self.selected_campsite["amenities"]
        )
        self.brazier_label.config(
            text="화로대: " + str(self.selected_campsite["brazier"])
        )

    def update(self, selected_campsite):
        self.selected_campsite = selected_campsite
        self.update_map()
        self.update_labels()

    # 이 아래로 버튼 추가 필요
    def zoom_in(self):
        self.zoom += 1
        self.update_map()

    def zoom_out(self):
        if self.zoom > 2:
            self.zoom -= 1
            self.update_map()

    def send_telegram_message(self):
        msg = f"""
        이름: {self.selected_campsite['name']}
        주소: {self.selected_campsite['address']}
        홈페이지: {self.selected_campsite['homepage']}
        소개: {self.selected_campsite['intro']}
        업종: {self.selected_campsite['induty']}
        입지 구분: {self.selected_campsite['siteView']}
        전화번호: {self.selected_campsite['telNum']}
        예약 방법: {self.selected_campsite['reserve']}
        운영 계절: {self.selected_campsite['openSeason']}
        운영일: {self.selected_campsite['openDate']}
        동물 동반 여부: {self.selected_campsite['animalAllow']}
        부대시설: {self.selected_campsite['amenities']}
        화로대: {self.selected_campsite['brazier']}
        """
        if msg:
            try:
                bot.sendMessage(5845654861, msg)
            except Exception as e:
                print(f"Error occurred while sending message: {e}")

    def add_to_bookmarks(self):
        self.main_gui.add_to_bookmarks(self.selected_campsite)

    def send_email(self):
        host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "logo.html"

        senderAddr = "crapa36@gmail.com"  # 보내는 사람 email 주소.
        recipientAddr = "minsoolee123@naver.com"  # 받는 사람 email 주소.

        msg = MIMEBase("multipart", "alternative")

        msg = MIMEText(
            f"""주소: {self.selected_campsite['address']}
        홈페이지: {self.selected_campsite['homepage']}
        소개: {self.selected_campsite['intro']}
        업종: {self.selected_campsite['induty']}
        입지 구분: {self.selected_campsite['siteView']}
        전화번호: {self.selected_campsite['telNum']}
        예약 방법: {self.selected_campsite['reserve']}
        운영 계절: {self.selected_campsite['openSeason']}
        운영일: {self.selected_campsite['openDate']}
        동물 동반 여부: {self.selected_campsite['animalAllow']}
        부대시설: {self.selected_campsite['amenities']}
        화로대: {self.selected_campsite['brazier']}
        """
        )
        msg[
            "Subject"
        ] = f"""
        이름: {self.selected_campsite['name']}
        """
        msg["From"] = senderAddr
        msg["To"] = recipientAddr
        # MIME 문서를 생성합니다.

        # 메일을 발송한다.
        s = smtplib.SMTP(host, port)
        # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("crapa36@gmail.com", "tfwp hcgq xucg ekhc")
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()
