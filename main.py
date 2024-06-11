from tkinter import *
from tkinter import ttk  # ttk 모듈 import
from mainTab import MainTab

from bookmark import Bookmark
from comparison import Comparison
import requests
import xml.etree.ElementTree as ET


# 공공데이터 API 키
api_key = "KZPiFTl7RsdgCF1Qz9UqM6hKAIib9ELWN7w9OIm3LiuHvM9VW269DvJoLJ5Luvxs3keNZqLAlzRi88mpophJBg%3D%3D"

# 캠핑장 정보 데이터
url = "http://apis.data.go.kr/B551011/GoCamping/basedList?serviceKey=" + api_key
queryParams = {
    "numOfRows": 100,
    "pageNo": 1,
    "MobileOS": "ETC",
    "MobileApp": "AppTest",
}

response = requests.get(url, params=queryParams)
root = ET.fromstring(response.content)
items = root.findall(".//item")

campsites = []
for item in items:
    campsite = {
        "name": item.findtext("facltNm"),  # 이름
        "address": item.findtext("addr1"),  # 주소
        "lat": item.findtext("mapY"),  # 위도
        "lng": item.findtext("mapX"),  # 경도
        "homepage": item.findtext("homepage"),  # 홈페이지 주소
        "intro": item.findtext("intro"),  # 캠핑장 소개
        "induty": item.findtext("induty"),  # 업종(카라반, 글램핑, 일반야영)
        "siteView": item.findtext("lctCl"),  # 입지 구분 (호수, 산)
        "telNum": item.findtext("tel"),  # 전화번호
        "reserve": item.findtext("resveCl"),  # 예약 방법(전화)
        "openSeason": item.findtext("operPdCl"),  # 운영계절
        "openDate": item.findtext("operDeCl"),  # 운영일(평일+주말)
        "animalAllow": item.findtext("animalCmgCl"),  # 동물 허용
        "amenities": item.findtext("sbrsCl"),  # 부대시설
        "brazier": item.findtext("brazierCl"),  # 화로대
    }
    campsites.append(campsite)


class MainGUI:
    def __init__(self, campsites):
        window = Tk()
        window.title("캠핑가자")

        # Notebook 위젯 생성 (ttk 사용)
        notebook = ttk.Notebook(window)
        notebook.pack(expand=True, fill="both")

        self.campsites = campsites

        # 찜하기
        self.bookmarks = []

        # 탭 객체 생성 및 추가
        tab1 = MainTab(notebook, campsites)

        tab2 = tab1.DetailedTab

        tab3 = Bookmark(notebook, self.bookmarks)
        tab4 = Comparison(notebook, self.bookmarks)

        window.mainloop()

    def get_campsite_by_name(self, name):
        for campsite in self.campsites:
            if campsite["name"] == name:
                return campsite
        return None


MainGUI(campsites)
