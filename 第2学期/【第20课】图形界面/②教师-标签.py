import tkinter


window = tkinter.Tk()  # 建立一个窗体的实例并命名为window
window.geometry('300x300')  # 设置窗体的宽度和高度
window.title('窗口标题')  # 设置窗体的标题

# 建立一个label标签组件并命名为label,设置文字内容格式
label = tkinter.Label(window, text='吴江盛泽中学', font=('黑体', 10))
label.pack()  # pack()作用是把组件的放置在合适的位置

window.mainloop()  # 窗体的主事件循环
