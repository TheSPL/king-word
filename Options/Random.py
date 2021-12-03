from tkinter import *
from tkinter import messagebox
import time
import random

RANDOMS_WORD = ["C/C/y/a/a/h/u", "ẳ/n/g/ơ/L/L", "T/ổ/ô/g/n/C/h", "c/Đ/C/á/ố", "n/ệ/n/Ả/h/Đ/i",
                "í/t/ị/R/K/t/h", "n/ệ/ứ/h/S/M", "o/ã/H/H/à/o/n", "C/c/h/ị/h/T/ủ", "H/à/ư/i/H/ớ/c"]

RANDOMS_ANSWER = ["Chua Cay", "Lẳng Lơ", "Thổ Công", "Cốc Đá", "Điện Ảnh",
                  "Khít Rịt", "Sứ Mệnh", "Hoà Hoãn", "Chủ Tịch", "Hài Hước"]

bg_color = '#99ffd6'
var = 0
ran_num_array = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
ran_num_array.append(10)
ran_num = ran_num_array[var]
points = 0

f = open("../king-word/Max_Point/MP_Random.txt", 'r', encoding='utf-8')
maxP = str(f.read())
f.close()


def main():
    def back():
        global var, ran_num_array, points, ran_num
        var = 0
        ran_num_array = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
        ran_num = ran_num_array[var]
        points = 0
        my_window.destroy()
        import index
        index.start_main_page()

    def change():
        global ran_num
        global var,  ran_num_array, bg_color, points, ran_num
        var += 1
        if var == 10 and points >= 30:
            var = 0
            ran_num_array = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
            ran_num = ran_num_array[var]
            bg_color = '#888844'
            my_window.destroy()
            messagebox.showinfo('You win!', "Bạn là nhất!!!")
            points = 0
            import index
            index.start_main_page()
        elif var == 10 and points < 30:
            var = 0
            ran_num_array = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
            ran_num = ran_num_array[var]
            bg_color = '#ff3300'
            my_window.destroy()
            messagebox.showinfo('You loss!', "Bạn như lốp xe vậy, hơi non!!!")
            import index
            index.start_main_page()
        ran_num = ran_num_array[var]
        word.configure(text=RANDOMS_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak(event=None):
        global points, ran_num, var, ran_num_array, bg_color, maxP, points
        user_word = get_input.get().title().strip()
        if user_word == RANDOMS_ANSWER[ran_num]:
            points += 5
            if points > int(maxP):
                f = open("../king-word/Max_Point/MP_Random.txt",
                         'w', encoding='utf-8')
                f.write(str(points))
                f.close()
                f = open("../king-word/Max_Point/MP_Random.txt",
                         'r', encoding='utf-8')
                maxP = str(f.read())
                f.close()

            var += 1
            if var == 10 and points >= 30:
                var = 0
                ran_num_array = random.sample(
                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
                ran_num = ran_num_array[var]
                bg_color = '#888844'

                my_window.destroy()
                messagebox.showinfo('You win!', "Bạn là nhất!!!")
                points = 0
                import index
                index.start_main_page()
            elif var == 10 and points < 30:
                var = 0
                ran_num_array = random.sample(
                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
                ran_num = ran_num_array[var]
                bg_color = '#ff3300'
                my_window.destroy()
                messagebox.showinfo(
                    'You loss!', "Bạn như lốp xe vậy, hơi non!!!")
                import index
                index.start_main_page()
            score.configure(text="Point: " + str(points))
            messagebox.showinfo('Good', "Được của ló, tiếp thôi bro!")
            ran_num = ran_num_array[var]
            word.configure(text=RANDOMS_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            var += 1
            score.configure(text="Point: " + str(points))
            messagebox.showerror("Error", "Xai dồi!")
            ran_num = ran_num_array[var]
            word.configure(text=RANDOMS_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")

    def show_answer():
        global points
        if points > 9:
            points -= 10
            score.configure(text="Điểm: " + str(points))
            ans_lab.configure(text=RANDOMS_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Kiếm 10 điểm rồi quay lại nha :v')

    my_window = Tk()
    my_window.geometry("450x600+500+150")
    my_window.resizable(0, 0)
    my_window.title("Vua Tiếng Việt")
    my_window.configure(background="#e6fff5")
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw')

    max_point = Label(
        my_window,
        text="Max Point: " + maxP,
        bg="#e6fff5",
        fg="#660000",
        font="Titillium 15 bold",
    )
    max_point.pack(anchor="n")

    score = Label(
        text="Point: 0",
        pady=10,
        bg="#e6fff5",
        fg="#00004d",
        font="Titillium 14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=RANDOMS_WORD[ran_num],
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium 30 bold"
    )
    word.pack()

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#660066",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    get_input = Entry(
        font="Titillium 26",
        borderwidth=10,
        justify='center',
    )
    get_input.bind('<Return>', cheak)
    get_input.focus_set()
    get_input.pack()

    submit = Button(
        text="Submit",
        width=15,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(40, 20))

    change = Button(
        text="Chane Word",
        width=15,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 18),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=15,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 18),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    my_window.mainloop()
