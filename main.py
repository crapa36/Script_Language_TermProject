from tkinter import *
from tkinter import ttk  # ttk 모듈 import
from mainTab import MainTab
from detailedTab import DetailedTab
from bookmark import Bookmark
from comparison import Comparison


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
        tab3 = Bookmark(notebook)
        tab4 = Comparison(notebook)

        window.mainloop()


MainGUI()
