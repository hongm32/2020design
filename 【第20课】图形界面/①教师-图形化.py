from tkinter import *       # 导入tkinter模块
kaisa = Tk()                 # 建立一个窗口
kaisa.title("凯撒密码")      # 设置窗口标题
kaisa.geometry('300x200')    # 设置窗口大小

Label(kaisa, text='请输入明文', font=('Arial', 10)).pack()
mingwen=Text(kaisa,width=300,height=4)
mingwen.pack()
mingwen.focus_set()    # 获得焦点
Button(kaisa, text="加密",relief="solid",width=10).pack()

kaisa.mainloop()
