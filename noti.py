#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
import xml.etree.ElementTree as ET

# 공공데이터 API 키
api_key = ""
TOKEN = ""
MAX_MSG_LENGTH = 300
baseurl = "http://apis.data.go.kr/B551011/GoCamping/basedList?serviceKey=" + api_key
bot = telepot.Bot(TOKEN)


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


def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)


def run():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )"
    )
    conn.commit()

    user_cursor = sqlite3.connect("users.db").cursor()
    user_cursor.execute(
        "CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )"
    )
    user_cursor.execute("SELECT * from users")

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, param)
        res_list = getCampsiteData()
        msg = ""
        for r in res_list:
            try:
                cursor.execute("INSERT INTO logs (user,log) VALUES (?, ?)", (user, r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print(str(datetime.now()).split(".")[0], r)
                if len(r + msg) + 1 > MAX_MSG_LENGTH:
                    sendMessage(user, msg)
                    msg = r + "\n"
                else:
                    msg += r + "\n"
        if msg:
            sendMessage(user, msg)
    conn.commit()


if __name__ == "__main__":
    today = date.today()
    print("[", today, "] received token :", TOKEN)
    pprint(bot.getMe())
    run()
