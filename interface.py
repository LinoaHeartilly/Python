from tkinter import *  # import library


def first():
    window = Tk()

    label = Label(window, text="Calculator", bg='cyan')  # add text
    label.pack()

    button = Button(window, text='close', command=window.quit)  # add button
    button.pack()

    value = StringVar()
    value.set("Default text")
    entry = Entry(window, textvariable=value, width=30)  # add text and entry
    entry.pack()

    button = Checkbutton(window, text='New ?')  # checkbox
    button.pack()

    value = StringVar()
    button1 = Radiobutton(window, text='Oui', variable=value, value=1)  # radio
    button1.pack()

    lis = Listbox(window)  # list
    lis.insert(1, "Python")
    lis.insert(2, "PHP")
    lis.insert(3, "jQuery")
    lis.insert(4, "CSS")
    lis.insert(5, "Javascript")

    lis.pack()

    s = Spinbox(window, from_=0, to=10)
    s.pack()

    value = DoubleVar()
    scale = Scale(window, variable=value)
    scale.pack()

    window.mainloop()


def second():
    window2 = Tk()

    canvas = Canvas(window2, width=150, height=120, background='yellow')
    line1 = canvas.create_line(75, 0, 75, 120)
    line2 = canvas.create_line(0, 60, 150, 60)
    txt = canvas.create_text(75, 60, text="Target", font="Arial 16 italic", fill="blue")
    canvas.pack()

    window2.mainloop()


def frame():
    window_frame = Tk()
    window_frame['bg'] = 'white'

    # frame 1
    frame1 = Frame(window_frame, borderwidth=2, relief=GROOVE)
    frame1.pack(side=LEFT, padx=30, pady=30)

    # frame 2
    frame2 = Frame(window_frame, borderwidth=2, relief=GROOVE)
    frame2.pack(side=LEFT, padx=10, pady=10)

    # frame 3 dans frame 2
    frame3 = Frame(frame2, bg="white", borderwidth=2, relief=GROOVE)
    frame3.pack(side=RIGHT, padx=5, pady=5)

    # Ajout de labels
    Label(frame1, text="Frame 1").pack(padx=10, pady=10)
    Label(frame2, text="Frame 2").pack(padx=10, pady=10)
    Label(frame3, text="Frame 3", bg="white").pack(padx=10, pady=10)
    window_frame.mainloop()


def paned_window():
    paned = Tk()
    p = PanedWindow(paned, orient=HORIZONTAL)
    p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
    p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
    p.add(Label(p, text='Volet 2', background='white', anchor=CENTER))
    p.add(Label(p, text='Volet 3', background='red', anchor=CENTER))
    p.pack()
    paned.mainloop()


def label_frame():
    frame_l = Tk()
    l = LabelFrame(frame_l, text="Titre de la frame", padx=20, pady=20)
    l.pack(fill="both", expand="yes")

    Label(l, text="A l'intérieure de la frame").pack()
    frame_l.mainloop()


again = True
while again:
    choice = input('Which window would you seen ?  : 0 test, 1 lesson, 2 frame, 3 PanedWindow, 4 labelFrame    ')
    if choice == '1':
        first()
    elif choice == '0':
        second()
    elif choice == '2':
        frame()
    elif choice == '3':
        paned_window()
    else:
        label_frame()
    a = input('Would you continue ? 0: No , Other : Yes     ')
    if a == '0':
        again = False
