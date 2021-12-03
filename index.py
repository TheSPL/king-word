from tkinter import *
from Options import Province, Job, Nation, FolkGame, Random


def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            Province.main()
        elif args == 2:
            Job.main()
        elif args == 3:
            Nation.main()
        elif args == 4:
            FolkGame.main()
        elif args == 5:
            Random.main()

    def option():

        lab_img1 = Button(
            main_window,
            text="Topic:",
            bg='#e6fff5',
            border=0,
            justify='center',
            font=("Courier", 28)
        )

        sel_btn1 = Button(
            text="Địa danh",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg=Province.bg_color,
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Nghề Nghiệp",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg=Job.bg_color,
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Dân Tộc",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg=Nation.bg_color,
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Trò Chơi Dân Gian",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg=FolkGame.bg_color,
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Chơi Tự Do",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg=Random.bg_color,
            cursor="hand2",
            command=lambda: start_game(5),
        )

        lab_img1.pack(pady=(40, 0),)
        sel_btn1.pack(pady=(40, 0), )
        sel_btn2.pack(pady=(20, 0), )
        sel_btn3.pack(pady=(20, 0), )
        sel_btn4.pack(pady=(20, 0), )
        sel_btn5.pack(pady=(20, 0), )

    def show_option():
        start_btn.destroy()
        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("450x600+500+150")
    main_window.resizable(0, 0)
    main_window.title("Vua Tiếng Việt")
    main_window.configure(background="#e6fff5")

    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        text="King of Word",
        bg='#e6fff5',
        font=("Courier", 28)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=22,
        height=11,
        fg="#000000",
        bg="#99ffd6",
        font=("", 18),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

    main_window.mainloop()


start_main_page()
