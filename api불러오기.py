from tkinter import *
from tkinter import ttk
import requests
import xml.etree.ElementTree as ET
from PIL import Image, ImageTk
import io

# 공공데이터 API 키
api_key = ""

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


def search_campsites():
    search_term = search_var.get().lower()
    results = [
        campsite for campsite in campsites if search_term in campsite["name"].lower()
    ]
    display_results(results)


def get_campsite_info_by_name(name):
    """
    캠핑장 이름을 입력받아 해당 캠핑장의 정보를 리턴하는 함수
    :param name: 캠핑장 이름
    :return: 캠핑장 정보 딕셔너리 (없으면 None)
    """
    for campsite in campsites:
        if campsite["name"].lower() == name.lower():
            return campsite
    return None


def update_results():
    results = campsites
    if weekday_var.get():
        results = [campsite for campsite in results if "평일" in campsite["openDate"]]
    if weekend_var.get():
        results = [campsite for campsite in results if "주말" in campsite["openDate"]]
    display_results(results)


def display_campsite_info(campsite):
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


def display_results(results):
    for widget in results_frame_inner.winfo_children():
        widget.destroy()
    for campsite in results:
        frame = Frame(results_frame_inner)
        frame.pack(fill="x", padx=5, pady=5)

        # 결과를 클릭할 수 있는 버튼 생성
        result_button = Button(
            frame,
            text=f"이름: {campsite['name']}",
            command=lambda campsite=campsite: display_campsite_info(campsite),
        )
        result_button.pack(anchor="w")


# GUI 설정
root = Tk()
root.title("캠핑장 검색")
root.geometry("1200x900")  # 창 크기 설정

# 검색 창과 버튼
search_var = StringVar()
search_entry = Entry(root, textvariable=search_var)
search_entry.pack(padx=10, pady=10)

search_button = Button(root, text="검색", command=search_campsites)
search_button.pack(padx=10, pady=10)

# 체크박스를 담을 프레임 생성
checkbox_frame = Frame(root)
checkbox_frame.pack(padx=10, pady=10)

weekday_var = BooleanVar()
weekday_checkbox = Checkbutton(
    checkbox_frame, text="평일 운영", variable=weekday_var, command=update_results
)
weekday_checkbox.grid(row=0, column=0)

weekend_var = BooleanVar()
weekend_checkbox = Checkbutton(
    checkbox_frame, text="주말 운영", variable=weekend_var, command=update_results
)
weekend_checkbox.grid(row=0, column=1)

# 결과 표시 프레임
results_frame = Frame(root)
results_frame.pack(fill="both", expand=True, padx=10, pady=10)

canvas = Canvas(results_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(results_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

results_frame_inner = Frame(canvas)
canvas.create_window((0, 0), window=results_frame_inner, anchor="nw")

display_results(campsites)

root.mainloop()
