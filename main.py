from tkinter import *
from tkinter import messagebox
import tkinter as tk

root = Tk()
root.configure(bg="#FFE080")

root.title("Викторина")
root.geometry("600x253+800+200")


def nachalo():
    privetstvie = Label(root, text="Приветсвтую тебя, дорогой друг! Это викторина по английскому языку! Желаю удачи!",
                        font="Times 12")
    start = Button(text="Перейти к викторине", font="Times 20", command=lambda: vopros_1())

    privetstvie.pack(expand=1)
    start.pack(expand=1)

    def vopros_1():
        question_1 = Label(root, text="Какая вторая форма глагола make?", font='Times 20')
        btn1_1 = Button(root, text="make", font='Times 20', background="#1585FF", activebackground="red",
                        foreground="white", width="30", command=lambda: nepravilno())
        btn2_1 = Button(root, text="made", font='Times 20', background="#1585FF", activebackground="green",
                        foreground="white", width="30", command=lambda: pravilno())
        btn3_1 = Button(root, text="maked", font='Times 20', background="#1585FF", activebackground="red",
                        foreground="white", width="30", command=lambda: nepravilno())
        btn4_1 = Button(root, text="mace", font='Times 20', background="#1585FF", activebackground="red",
                        foreground="white", width="30", command=lambda: nepravilno())

        privetstvie.pack_forget()
        start.pack_forget()

        def pravilno():
            messagebox.showinfo("Правильно!", "Вы ответили верно!")
            vopros_2()
            question_1.pack_forget()
            btn1_1.pack_forget()
            btn2_1.pack_forget()
            btn3_1.pack_forget()
            btn4_1.pack_forget()

        def nepravilno():
            messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

        question_1.pack()
        btn1_1.pack()
        btn2_1.pack()
        btn3_1.pack()
        btn4_1.pack()


def vopros_2():
    question_2 = Label(root, text="Какая третья форма глагола choose?", font='Times 20')
    btn1_2 = Button(root, text="choose", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn2_2 = Button(root, text="chose", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn3_2 = Button(root, text="cheese", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn4_2 = Button(root, text="chosen", font='Times 20', background="#1585FF", activebackground="green",
                    foreground="white", width="30", command=lambda: pravilno())

    def pravilno():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        vopros_3()
        question_2.pack_forget()
        btn1_2.pack_forget()
        btn2_2.pack_forget()
        btn3_2.pack_forget()
        btn4_2.pack_forget()

    def nepravilno():
        messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

    question_2.pack()
    btn1_2.pack()
    btn2_2.pack()
    btn3_2.pack()
    btn4_2.pack()


def vopros_3():
    question_3 = Label(root, text="Какая инфинитивная форма глагола went?", font='Times 20')
    btn1_3 = Button(root, text="warn", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn2_3 = Button(root, text="do", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn3_3 = Button(root, text="go", font='Times 20', background="#1585FF", activebackground="green",
                    foreground="white", width="30", command=lambda: pravilno())
    btn4_3 = Button(root, text="wear", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())

    def pravilno():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        vopros_4()
        question_3.pack_forget()
        btn1_3.pack_forget()
        btn2_3.pack_forget()
        btn3_3.pack_forget()
        btn4_3.pack_forget()

    def nepravilno():
        messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

    question_3.pack()
    btn1_3.pack()
    btn2_3.pack()
    btn3_3.pack()
    btn4_3.pack()


def vopros_4():
    question_4 = Label(root, text="Какая третья форма глагола catch?", font='Times 20')
    btn1_4 = Button(root, text="caught", font='Times 20', background="#1585FF", activebackground="green",
                    foreground="white", width="30", command=lambda: pravilno())
    btn2_4 = Button(root, text="cought", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn3_4 = Button(root, text="catch", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn4_4 = Button(root, text="kchau", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())

    def pravilno():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        vopros_5()
        question_4.pack_forget()
        btn1_4.pack_forget()
        btn2_4.pack_forget()
        btn3_4.pack_forget()
        btn4_4.pack_forget()

    def nepravilno():
        messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

    question_4.pack()
    btn1_4.pack()
    btn2_4.pack()
    btn3_4.pack()
    btn4_4.pack()


def vopros_5():
    question_5 = Label(root, text="Какая третья форма глагола know?", font='Times 20')
    btn1_5 = Button(root, text="know", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn2_5 = Button(root, text="known", font='Times 20', background="#1585FF", activebackground="green",
                    foreground="white", width="30", command=lambda: pravilno())
    btn3_5 = Button(root, text="klown", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn4_5 = Button(root, text="knew", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())

    def pravilno():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        chast2()
        question_5.pack_forget()
        btn1_5.pack_forget()
        btn2_5.pack_forget()
        btn3_5.pack_forget()
        btn4_5.pack_forget()

    def nepravilno():
        messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

    question_5.pack()
    btn1_5.pack()
    btn2_5.pack()
    btn3_5.pack()
    btn4_5.pack()


def chast2():
    message1 = Label(root, text="Поздравляю! Первая часть пройдена! Давай приступим ко второй части - артикли.",
                     font="Times 12")
    message2 = Label(root, text="Задание: выберите артикль - a/an/the/-?", font="Times 15")
    perexod = Button(text="Перейти ко второй части", font="Times 20", command=lambda: vopros_6())

    message1.pack(expand=1)
    message2.pack(expand=1)
    perexod.pack(expand=1)

    def vopros_6():
        question_6 = Label(root, text="I put ___ ball to the table.", font='Times 20')
        btn1_6 = Button(root, text="a", font='Times 20', background="#1585FF", activebackground="red",
                        foreground="white", width="30", command=lambda: nepravilno())
        btn2_6 = Button(root, text="an", font='Times 20', background="#1585FF", activebackground="red",
                        foreground="white", width="30", command=lambda: nepravilno())
        btn3_6 = Button(root, text="the", font='Times 20', background="#1585FF", activebackground="green",
                        foreground="white", width="30", command=lambda: pravilno())
        btn4_6 = Button(root, text="-", font='Times 20', background="#1585FF", activebackground="red",
                        foreground="white", width="30", command=lambda: nepravilno())

        message1.pack_forget()
        message2.pack_forget()
        perexod.pack_forget()

        def pravilno():
            messagebox.showinfo("Правильно!", "Вы ответили верно!")
            vopros_7()
            question_6.pack_forget()
            btn1_6.pack_forget()
            btn2_6.pack_forget()
            btn3_6.pack_forget()
            btn4_6.pack_forget()

        def nepravilno():
            messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

        question_6.pack()
        btn1_6.pack()
        btn2_6.pack()
        btn3_6.pack()
        btn4_6.pack()


def vopros_7():
    question_7 = Label(root, text="I want to visit ___ Russia.", font='Times 20')
    btn1_7 = Button(root, text="a", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn2_7 = Button(root, text="an", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn3_7 = Button(root, text="the", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn4_7 = Button(root, text="-", font='Times 20', background="#1585FF", activebackground="green",
                    foreground="white", width="30", command=lambda: pravilno())

    def pravilno():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        vopros_8()
        question_7.pack_forget()
        btn1_7.pack_forget()
        btn2_7.pack_forget()
        btn3_7.pack_forget()
        btn4_7.pack_forget()

    def nepravilno():
        messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

    question_7.pack()
    btn1_7.pack()
    btn2_7.pack()
    btn3_7.pack()
    btn4_7.pack()


def vopros_8():
    question_8 = Label(root, text="Alex hit ___ ball through ___ window.", font='Times 20')
    btn1_8 = Button(root, text="a/the", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn2_8 = Button(root, text="a/a", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn3_8 = Button(root, text="the/the", font='Times 20', background="#1585FF", activebackground="green",
                    foreground="white", width="30", command=lambda: pravilno())
    btn4_8 = Button(root, text="the/-", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())

    def pravilno():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        vopros_9()
        question_8.pack_forget()
        btn1_8.pack_forget()
        btn2_8.pack_forget()
        btn3_8.pack_forget()
        btn4_8.pack_forget()

    def nepravilno():
        messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

    question_8.pack()
    btn1_8.pack()
    btn2_8.pack()
    btn3_8.pack()
    btn4_8.pack()


def vopros_9():
    question_9 = Label(root, text="In ___ summer we swam in ___ river.", font='Times 20')
    btn1_9 = Button(root, text="the/-", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())
    btn2_9 = Button(root, text="-/the", font='Times 20', background="#1585FF", activebackground="green",
                    foreground="white", width="30", command=lambda: pravilno())
    btn3_9 = Button(root, text="the/the", font='Times 20', background="#1585FF", activebackground="green",
                    foreground="white", width="30", command=lambda: pravilno())
    btn4_9 = Button(root, text="the/a", font='Times 20', background="#1585FF", activebackground="red",
                    foreground="white", width="30", command=lambda: nepravilno())

    def pravilno():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        vopros_10()
        question_9.pack_forget()
        btn1_9.pack_forget()
        btn2_9.pack_forget()
        btn3_9.pack_forget()
        btn4_9.pack_forget()

    def nepravilno():
        messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

    question_9.pack()
    btn1_9.pack()
    btn2_9.pack()
    btn3_9.pack()
    btn4_9.pack()


def vopros_10():
    question_10 = Label(root, text="___ apple fell on Newton's head.", font='Times 20')
    btn1_10 = Button(root, text="a", font='Times 20', background="#1585FF", activebackground="red",
                     foreground="white", width="30", command=lambda: nepravilno())
    btn2_10 = Button(root, text="an", font='Times 20', background="#1585FF", activebackground="green",
                     foreground="white", width="30", command=lambda: pravilno())
    btn3_10 = Button(root, text="the", font='Times 20', background="#1585FF", activebackground="red",
                     foreground="white", width="30", command=lambda: nepravilno())
    btn4_10 = Button(root, text="-", font='Times 20', background="#1585FF", activebackground="red",
                     foreground="white", width="30", command=lambda: nepravilno())

    def pravilno():
        messagebox.showinfo("Правильно!", "Вы ответили верно!")
        the_end()
        question_10.pack_forget()
        btn1_10.pack_forget()
        btn2_10.pack_forget()
        btn3_10.pack_forget()
        btn4_10.pack_forget()

    def nepravilno():
        messagebox.showinfo("Неправильно!", "Дайте другой ответ!")

    question_10.pack()
    btn1_10.pack()
    btn2_10.pack()
    btn3_10.pack()
    btn4_10.pack()


def the_end():
    final_message = Label(root, text="Поздравляю! Вы успешно прошли тест!", font="Times 20", backgroun="#8080FF")
    end_btn = Button(root, text="Завершить тест", font="Times 20", background="#80FFE0",
                     activebackground="#80FFE0", command=root.destroy)
    restart_btn = Button(root, text="Пройти тест еще раз", font="Times 20", background="#80FFE0",
                         activebackground="#80FFE0", command=lambda: restart())

    final_message.pack()
    end_btn.pack(expand=1)
    restart_btn.pack(expand=1)

    def restart():
        end_btn.pack_forget()
        restart_btn.pack_forget()
        final_message.pack_forget()
        nachalo()


nachalo()
root.mainloop()