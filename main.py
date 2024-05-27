from tkinter import *
from tkinter import ttk  # ttk 모듈 import
from mainTab import MainTab
from detailedTab import DetailedTab


class MainGUI:
    def __init__(self):
        window = Tk()
        window.title("캠핑가자")

        # Notebook 위젯 생성 (ttk 사용)
        notebook = ttk.Notebook(window)
        notebook.pack(expand=True, fill="both")

        # 탭 객체 생성 및 추가
        tab1 = MainTab(notebook)
        tab2 = DetailedTab(notebook)

        window.mainloop()


ProvinceList = [
    "강원도",
    "경기도",
    "경상북도",
    "경상남도",
    "전라북도",
    "전라남도",
    "충청북도",
    "충청남도",
]
ProvinceList.sort()
MainGUI()
