import random
import time
import tkinter as tk

def start_game():
    global lst,goal_list,replay_list,m
    m = 0
    lst, goal_list = creat_lst()
    replay_list.append(lst.copy())
    # root.bind("<Left>", left)
    # root.bind("<Right>", right)
    # root.bind("<Up>", north)
    # root.bind("<Down>", south)
    output_lst()

def game_clear():
    global lst
    global goal_list
    if lst == goal_list:
        result = tk.Toplevel()
        label_result = tk.Label(result, text='game clear\ncongratulation!!',
                                bg='white', font=('Arial', 14),
                                width=18, height=6)
        label_result.grid()
        button_replay = tk.Button(result, text = 'review',
                                  bg='white', font = ('Arial', 14),
                                  width=18, height=2,command = replay_function)
        button_replay.grid()

def replay_function():
    replay_window = tk.Toplevel()
    replay_window.geometry("450x420")
    replay_window.resizable(False, False)
    frm_1 = tk.Frame(replay_window, width=450, height=420, bg='#87CEEB').grid(rowspan=6, columnspan=3)
    for a in range(m):
        replay_window.after(500,output_replay_lst(a,replay_window))
        replay_window.update()


def label_result():
    label_result = tk.Label(root_result, text='game clear', bg='white', font=('Arial', 14),
                            width=12, height=5)
    label_result.grid()

def label_move_num():
    move = tk.Label(root,text='步数:',font=('宋体', 24),bg ='white')
    move.place(x = 455,y = 16)
    move_num = tk.Label(root,text=m,font=('宋体', 24),bg ='white',width = 5)
    move_num.place(x = 540,y =16)

def button_start():
    button_start = tk.Button(root, text='开始游戏',
                             bg='white', font=('宋体', 18),
                             width=12, height=5, command=start_game)
    button_start.place(x = 455,y = 285, width=190, height=60)

def button_goal_list():
    button_goal_list = tk.Button(root, text='目标位置',
                             bg='white', font=('宋体', 18),
                             width=12, height=5, command=output_goal_list)
    button_goal_list.place(x=455, y=355, width=190, height=60)

def button_left():
    button_left = tk.Button(root, text='move_left',
                            bg='white', font=('Arial', 11),
                            width=12, height=5, command=lambda: left(lst))
    button_left.grid(row=4, column=0)

def button_right():
    button_left = tk.Button(root, text='move_right',
                            bg='white', font=('Arial', 11),
                            width=12, height=5, command=lambda: right(lst))
    button_left.grid(row=4, column=2)

def button_up():
    button_left = tk.Button(root, text='move_up',
                            bg='white', font=('Arial', 11),
                            width=12, height=5, command=lambda: north(lst))
    button_left.grid(row=3, column=1)

def button_down():
    button_left = tk.Button(root, text='move_down',
                            bg='white', font=('Arial', 11),
                            width=12, height=5, command=lambda: south(lst))
    button_left.grid(row=4, column=1)

def replay_up(replay_window):
    global m
    if m == 0:
        output_replay_lst(replay_window)
    else:
        m -=1
        output_replay_lst(replay_window)

def replay_down(replay_window):
    global m
    if m == len(replay_list)-1:
        output_replay_lst(replay_window)
    else:
        m +=1
        output_replay_lst(replay_window)

def replay_m(input,replay_window):
    global m
    m = int(input)
    output_replay_lst(replay_window)

def output_replay_lst(a,replay_window):
    j = -2
    for i in range(9):
        if (i % 3 == 0):
            j += 2
        label1 = tk.Label(replay_window, text=replay_list[a][i],
                          bg='#F8F8FF', font=('Arial', 20),
                          width=6, height=3)
        label1.grid(row=j, column=(i % 3), rowspan=2, padx=4, pady=4, sticky='n,e,w,s')

def output_lst():
    j = -2
    for i in range(9):
        if (i % 3 == 0):
            j += 2
        label1 = tk.Label(root, text=lst[i],
                          bg='#F8F8FF', font=('Arial', 20),
                          width=6, height=3)
        label1.grid(row=j, column=(i % 3), rowspan=2, padx=4, pady=4, sticky='n,e,w,s')
    root.update()

def output_goal_list():
    goal_list_tk = tk.Toplevel()
    goal_list_tk.title('目标位置')
    goal_list_tk.geometry("450x420")
    frm_1 = tk.Frame(goal_list_tk, width=450, height=420, bg='#87CEEB').grid(rowspan=6, columnspan=3)
    j = -2
    for i in range(9):
        if (i % 3 == 0):
            j += 2
        label2 = tk.Label(goal_list_tk, text=goal_list[i],
                          bg='#F8F8FF', font=('Arial', 20),
                          width=6, height=3)
        label2.grid(row=j, column=(i % 3), rowspan=2, padx=4, pady=4, sticky='n,e,w,s')

def inversion_number(lst):
    n = 0
    for i in range(1,9):
        if lst[i] == 0:
            continue
        for j in range(i):
            if lst[j] > lst[i]:
                n += 1
    return n

def can_start(lst, goal_list):
    return inversion_number(lst) % 2 == inversion_number(goal_list) % 2

def creat_lst():
    lst = [i for i in range(0, 9)]
    goal_list = [i for i in range(0, 9)]
    random.shuffle(lst)
    random.shuffle(goal_list)
    while (can_start(lst, goal_list) != 1):
        random.shuffle(goal_list)
    return lst,goal_list

def move_bind():
    root.bind("<Left>", left)
    root.bind("<Right>", right)
    root.bind("<Up>", north)
    root.bind("<Down>", south)

def move_none():
    root.bind("<Left>", None)
    root.bind("<Right>", None)
    root.bind("<Up>", None)
    root.bind("<Down>", None)

def north(event):
    global m
    n = lst.index(0)
    if (n <3):
        output_lst()
    else:
        lst[n] = lst[n - 3]
        lst[n - 3] = 0
        m += 1
        replay_list.append(lst.copy())
    label_move_num()
    output_lst()
    game_clear()

def south(event):
    global m
    n = lst.index(0)
    if (n >5):
        output_lst()
    else:
        lst[n] = lst[n + 3]
        lst[n + 3] = 0
        m += 1
        replay_list.append(lst.copy())
    label_move_num()
    output_lst()
    game_clear()

def left(event):
    global m
    n = lst.index(0)
    if(n in [0, 3, 6]):
        output_lst()
    else:
        lst[n] = lst[n - 1]
        lst[n - 1] = 0
        m +=1
        replay_list.append(lst.copy())
    label_move_num()
    output_lst()
    game_clear()

def right(event):
    global m
    n = lst.index(0)
    if(n in [2, 5, 8]):
        output_lst()
    else:
        lst[n] = lst[n + 1]
        lst[n + 1] = 0
        m += 1
        replay_list.append(lst.copy())
    label_move_num()
    output_lst()
    game_clear()

def move():
    move_none()
    while(lst != goal_list and v.get() == 2):
        ch = random.randint(1,4)
        if ch == 1:
            north(lst)
        elif ch == 2:
            south(lst)
        elif ch == 3:
            left(lst)
        elif ch == 4:
            right(lst)
        time.sleep(0.3)

if __name__ == '__main__':

    root = tk.Tk()
    root.title('八数码游戏')

    root.geometry("650x420")
    root.resizable(False, False)

    frm_1 = tk.Frame(root, width=450, height=420, bg='#87CEEB').grid(rowspan=6, columnspan=3)
    frm_2 = tk.Frame(root, width=200, height=70, bg='#F8F8FF').grid(row=0, column=3)
    frm_3 = tk.LabelFrame(root, width=200, height=210, bg='#E0FFFF', text='游戏模式',font = 18).grid(row=1, column=3, rowspan=3)
    frm_4 = tk.Frame(root, width=200, height=140, bg='#7FFFD4').grid(row=4, column=3, rowspan=2)

    m = 0
    replay_list = []


    lst = [i for i in range(9)]
    lst[1] = 0
    lst[0] = 1
    goal_list = [i for i in range(9)]
    output_lst()

    button_start()
    button_goal_list()

    label_move_num()

    move_way = [('人工移动',1),
                ('随机移动',2),
                ('智能移动',3)]
    v = tk.IntVar()
    v .set(1)
    tk.Radiobutton(root, text = '人工移动', variable = v, value = 1,
                   bg='#E0FFFF', width=18, height=2, font=35, anchor='w', command = move_bind()).place(x = 460 ,y = 90)
    tk.Radiobutton(root, text = '随机移动', variable = v, value = 2,
                   bg='#E0FFFF', width=18, height=2, font=35, anchor='w', command = move).place(x = 460 ,y = 155)
    tk.Radiobutton(root, text = '智能移动', variable = v, value = 3,
                   bg='#E0FFFF', width=18, height=2, font=35, anchor='w').place(x = 460 ,y = 220)
    root.mainloop()
