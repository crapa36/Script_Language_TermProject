#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
import requests
from datetime import date, datetime
import traceback
import xml.etree.ElementTree as ET

import noti  # Assuming noti.py contains necessary functions and constants

# 공공데이터 API 키
api_key = ""
MAX_MSG_LENGTH = 300
baseurl = "http://apis.data.go.kr/B551011/GoCamping/basedList?serviceKey=" + api_key


def getCampsiteData():
    queryParams = {
        "numOfRows": 10,
        "pageNo": 1,
        "MobileOS": "ETC",
        "MobileApp": "AppTest",
    }
    response = requests.get(baseurl, params=queryParams)
    root = ET.fromstring(response.content)
    items = root.findall(".//item")

    res_list = []
    for item in items:
        campsite = {
            "name": item.findtext("facltNm"),
            "address": item.findtext("addr1"),
            "lat": item.findtext("mapY"),
            "lng": item.findtext("mapX"),
            "homepage": item.findtext("homepage"),
            "intro": item.findtext("intro"),
            "induty": item.findtext("induty"),
            "siteView": item.findtext("lctCl"),
            "telNum": item.findtext("tel"),
            "reserve": item.findtext("resveCl"),
            "openSeason": item.findtext("operPdCl"),
            "openDate": item.findtext("operDeCl"),
            "animalAllow": item.findtext("animalCmgCl"),
            "amenities": item.findtext("sbrsCl"),
            "brazier": item.findtext("brazierCl"),
        }
        row = f"""
        이름: {campsite['name']}
        주소: {campsite['address']}
        위도: {campsite['lat']}
        경도: {campsite['lng']}
        홈페이지: {campsite['homepage']}
        소개: {campsite['intro']}
        업종: {campsite['induty']}
        입지 구분: {campsite['siteView']}
        전화번호: {campsite['telNum']}
        예약 방법: {campsite['reserve']}
        운영계절: {campsite['openSeason']}
        운영일: {campsite['openDate']}
        동물 허용: {campsite['animalAllow']}
        부대시설: {campsite['amenities']}
        화로대: {campsite['brazier']}
        """
        res_list.append(row.strip())
    return res_list


def replyCampsiteData(user):
    print(user)
    res_list = getCampsiteData()
    msg = ""
    for r in res_list:
        print(str(datetime.now()).split(".")[0], r)
        if len(r + msg) + 1 > MAX_MSG_LENGTH:
            noti.sendMessage(user, msg)
            msg = r + "\n"
        else:
            msg += r + "\n"
    if msg:
        noti.sendMessage(user, msg)
    else:
        noti.sendMessage(user, "해당 기간에 해당하는 데이터가 없습니다.")


def save(user):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users( user TEXT, PRIMARY KEY(user) )")
    try:
        cursor.execute("INSERT INTO users(user) VALUES (?)", (user,))
    except sqlite3.IntegrityError:
        noti.sendMessage(user, "이미 해당 정보가 저장되어 있습니다.")
        return
    else:
        noti.sendMessage(user, "저장되었습니다.")
        conn.commit()


def check(user):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users( user TEXT, PRIMARY KEY(user) )")
    cursor.execute("SELECT * from users WHERE user=?", (user,))
    for data in cursor.fetchall():
        row = "id:" + str(data[0])
        noti.sendMessage(user, row)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != "text":
        noti.sendMessage(chat_id, "난 텍스트 이외의 메시지는 처리하지 못해요.")
        return

    text = msg["text"]
    args = text.split(" ")

    if text.startswith("캠핑장"):
        print("try to 캠핑장")
        replyCampsiteData(chat_id)
    elif text.startswith("저장"):
        print("try to 저장")
        save(chat_id)
    elif text.startswith("확인"):
        print("try to 확인")
        check(chat_id)
    else:
        noti.sendMessage(
            chat_id,
            """모르는 명령어입니다.\n캠핑장\n저장\n확인 중 하나의 명령을 입력하세요.""",
        )


today = date.today()
print("[", today, "] received token :", noti.TOKEN)

bot = telepot.Bot(noti.TOKEN)
pprint(bot.getMe())

bot.message_loop(handle)

print("Listening...")

while 1:
    time.sleep(10)
