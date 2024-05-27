from tkinter import *
import Pro_City_Dic
class MainTab:
    def __init__(self):
        window = Tk()
        window.title("캠핑가자")
        self.canvas = Canvas(window, width=1600, height=900, bg='white')
        self.canvas.pack()
        #좌측 체크박스
        self.canvas.create_rectangle(20, 20, 400-20, 900-20, tags='CheckList')
        frameC = Frame(window)
        frameC.place(x=30, y=30)
        self.CheckBox1 = IntVar()
        Checkbutton(frameC, text='항목1', variable=self.CheckBox1).pack(side=TOP)
        self.CheckBox2 = IntVar()
        Checkbutton(frameC, text='항목2', variable=self.CheckBox2).pack(side=TOP)
        #항목 숫자별로 추가

        #상세항목
        self.canvas.create_rectangle(400 + 20, 20, 1600 - 20, 400 - 20, tags='Details')

        #지도탭
        self.canvas.create_rectangle(400 + 20, 400 + 20, 1600 - 20, 900 - 20, tags='Details')
        frameL = Frame(window)
        frameL.place(x=400+20, y=400 + 20)

        ProListBox = Listbox(frameL, selectmode='extended')
        ProListBox.pack(side=LEFT)

        Proscroll = Scrollbar(frameL, orient="vertical")
        Proscroll.config(command=ProListBox.yview)
        Proscroll.pack(side=RIGHT, fill="y")
        ProListBox.config(yscrollcommand=Proscroll.set)

        

        window.mainloop()

MainTab()