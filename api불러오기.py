import tkinter as tk
import tkinter.ttk as ttk
import requests
import xml.etree.ElementTree as ET
from PIL import Image, ImageTk
import io
from googlemaps import Client

zoom = 13

# 공공데이터 API 키
api_key = "KZPiFTl7RsdgCF1Qz9UqM6hKAIib9ELWN7w9OIm3LiuHvM9VW269DvJoLJ5Luvxs3keNZqLAlzRi88mpophJBg%3D%3D"

# 서울시 캠핑장 정보 데이터
url = "http://apis.data.go.kr/B551011/GoCamping/basedList"
queryParams = {
    "serviceKey": api_key,
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

for campsite in campsites:
    print(f"이름: {campsite['name']}")
    print(f"주소: {campsite['address']}")
    print(f"위도: {campsite['lat']}")
    print(f"경도: {campsite['lng']}")
    print(f"홈페이지: {campsite['homepage']}")
    print(f"소개: {campsite['intro']}")
    print(f"업종: {campsite['induty']}")
    print(f"입지 구분: {campsite['siteView']}")
    print(f"전화번호: {campsite['telNum']}")
    print(f"예약 방법: {campsite['reserve']}")
    print(f"운영계절: {campsite['openSeason']}")
    print(f"운영일: {campsite['openDate']}")
    print(f"동물 허용: {campsite['animalAllow']}")
    print(f"부대시설: {campsite['amenities']}")
    print(f"화로대: {campsite['brazier']}")
    print("-" * 50)
