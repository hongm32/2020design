import tkinter


window = tkinter.Tk()  # 建立一个窗体的实例并命名为window
window.geometry('300x300')  # 设置窗体的宽度和高度
window.title('窗口标题')  # 设置窗体的标题

# 定义按钮被点击后的执行函数
def click_button():
    text.delete('0.0','end')    # 清空text这个文本框里的所有输入的内容


photo = tkinter.PhotoImage(file="logo.png")  # 加载图片
# 建立一个label标签组件并命名为label,设置文字内容格式
label = tkinter.Label(window, image=photo)  # 把图片整合到标签类中
label.pack()  # pack()作用是把组件的放置在合适的位置

# 建立一个文本框组件并命名为text,并设定文本框的高度
text = tkinter.Text(window, height=4)
text.pack()

# 建立一个按钮组件并命名为button,并设定按钮的属性
button = tkinter.Button(window, text='重写', width=15, height=2, command=click_button)
button.pack()

window.mainloop()  # 窗体的主事件循环
