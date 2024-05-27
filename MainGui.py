from tkinter import *

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title("캠핑가자")
        self.canvas = Canvas(window, width=1600, height=900, bg='white')
        self.canvas.pack()
        self.canvas.create_rectangle(20, 20, 400-20, 900-20, tags='CheckList')
        frame = Frame(window)
        frame.place(x=30, y=30)
        self.CheckBox1 = IntVar()
        Checkbutton(frame, text='항목1', variable=self.CheckBox1).pack(side=TOP)
        self.CheckBox2 = IntVar()
        Checkbutton(frame, text='항목2', variable=self.CheckBox2).pack(side=TOP)
        #항목 숫자별로 추기
        window.mainloop()



MainGUI()