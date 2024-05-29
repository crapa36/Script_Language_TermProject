from tkinter import *
from tkinter import ttk
import requests
import xml.etree.ElementTree as ET
from PIL import Image, ImageTk
import io

# 공공데이터 API 키
api_key = "KZPiFTl7RsdgCF1Qz9UqM6hKAIib9ELWN7w9OIm3LiuHvM9VW269DvJoLJ5Luvxs3keNZqLAlzRi88mpophJBg%3D%3D"

# 서울시 캠핑장 정보 데이터
url = "http://apis.data.go.kr/B551011/GoCamping/basedList?serviceKey=" + api_key
queryParams = {
    "numOfRows": 10,
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


def search_campsites():
    search_term = search_var.get().lower()
    results = [
        campsite for campsite in campsites if search_term in campsite["name"].lower()
    ]
    display_results(results)


def display_results(results):
    for widget in results_frame.winfo_children():
        widget.destroy()

    for campsite in results:
        frame = Frame(results_frame)
        frame.pack(fill="x", padx=5, pady=5)

        name_label = Label(frame, text=f"이름: {campsite['name']}")
        name_label.pack(anchor="w")

        address_label = Label(frame, text=f"주소: {campsite['address']}")
        address_label.pack(anchor="w")

        lat_label = Label(frame, text=f"위도: {campsite['lat']}")
        lat_label.pack(anchor="w")

        lng_label = Label(frame, text=f"경도: {campsite['lng']}")
        lng_label.pack(anchor="w")

        homepage_label = Label(frame, text=f"홈페이지: {campsite['homepage']}")
        homepage_label.pack(anchor="w")

        intro_label = Label(frame, text=f"소개: {campsite['intro']}")
        intro_label.pack(anchor="w")

        induty_label = Label(frame, text=f"업종: {campsite['induty']}")
        induty_label.pack(anchor="w")

        siteView_label = Label(frame, text=f"입지 구분: {campsite['siteView']}")
        siteView_label.pack(anchor="w")

        telNum_label = Label(frame, text=f"전화번호: {campsite['telNum']}")
        telNum_label.pack(anchor="w")

        reserve_label = Label(frame, text=f"예약 방법: {campsite['reserve']}")
        reserve_label.pack(anchor="w")

        openSeason_label = Label(frame, text=f"운영계절: {campsite['openSeason']}")
        openSeason_label.pack(anchor="w")

        openDate_label = Label(frame, text=f"운영일: {campsite['openDate']}")
        openDate_label.pack(anchor="w")

        animalAllow_label = Label(frame, text=f"동물 허용: {campsite['animalAllow']}")
        animalAllow_label.pack(anchor="w")

        amenities_label = Label(frame, text=f"부대시설: {campsite['amenities']}")
        amenities_label.pack(anchor="w")

        brazier_label = Label(frame, text=f"화로대: {campsite['brazier']}")
        brazier_label.pack(anchor="w")

        separator = Label(frame, text="-" * 50)
        separator.pack(anchor="w")


# GUI Setup
root = Tk()
root.title("캠핑장 검색")

# 검색 창과 버튼
search_var = StringVar()
search_entry = Entry(root, textvariable=search_var)
search_entry.pack(padx=10, pady=10)

search_button = Button(root, text="검색", command=search_campsites)
search_button.pack(padx=10, pady=10)

# 결과 표시 프레임
results_frame = Frame(root)
results_frame.pack(fill="both", expand=True, padx=10, pady=10)

# 초기 데이터 표시
display_results(campsites)

root.mainloop()
