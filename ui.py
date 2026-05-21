from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#FAE7CB"

class UI:

  def __init__(self, quiz_brain:QuizBrain):

    self.quiz=quiz_brain

    self.score=0
    self.window=Tk()

    self.window.title("Quizzler")
    self.window.geometry("500x600")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)

    self.score_label=Label(text="Score:0",bg=THEME_COLOR,font=("Brass Mono Regular", 17, "bold"),pady=20)
    self.score_label.grid(row=0, column=2, sticky="ne")

    self.canvas=Canvas(self.window, width=400, height=250, bg=THEME_COLOR, highlightthickness=0)
    self.canvas.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
    self.question_text=self.canvas.create_text(200, 125, width=290, fill="black")

    self.correct_img=PhotoImage(file="images/correct.png")
    self.wrong_img=PhotoImage(file="images/wrong.png")

    self.correct_button=Button(image=self.correct_img, highlightthickness=0, bg=THEME_COLOR, bd=0, command=self.correct_button_func)
    self.correct_button.grid(row=2, column=0, padx=10, pady=20)

    self.wrong_button=Button(image=self.wrong_img, highlightthickness=0, bg=THEME_COLOR, bd=0, command=self.wrong_button_func)
    self.wrong_button.grid(row=2, column=2, padx=10, pady=20)

    self.questions()

    self.window.mainloop()

  def questions(self):

    question_test=self.quiz.next_question()
    self.canvas.itemconfig(self.question_text, text=question_test, font=("Brass Mono Regular", 17,"bold"))

  def reset_bg(self):

    self.correct_button.config(bg=THEME_COLOR)
    self.wrong_button.config(bg=THEME_COLOR)
    self.score_label.config(bg=THEME_COLOR)
    self.window.config(bg=THEME_COLOR)
    self.canvas.config(bg=THEME_COLOR)
    self.questions()

  def correct_button_func(self):

    is_corrent=self.quiz.check_answer("True")

    if is_corrent:
      self.score+=1
      self.score_label.config(text=f"Score:{self.score}",)

      self.correct_button.config(bg="#59B292")
      self.wrong_button.config(bg="#59B292")
      self.score_label.config(bg="#59B292")
      self.window.config(bg="#59B292")
      self.canvas.config(bg="#59B292")

    else:
      self.correct_button.config(bg="#FA6781")
      self.wrong_button.config(bg="#FA6781")
      self.score_label.config(bg="#FA6781")
      self.window.config(bg="#FA6781")
      self.canvas.config(bg="#FA6781")

    self.window.after(1000, self.reset_bg)

  def wrong_button_func(self):

    is_wrong=self.quiz.check_answer("False")

    if is_wrong:
      self.score+=1
      self.score_label.config(text=f"Score:{self.score}",)

      self.correct_button.config(bg="#59B292")
      self.wrong_button.config(bg="#59B292")
      self.score_label.config(bg="#59B292")
      self.window.config(bg="#59B292")
      self.canvas.config(bg="#59B292")

    else:
      self.correct_button.config(bg="#FA6781")
      self.wrong_button.config(bg="#FA6781")
      self.score_label.config(bg="#FA6781")
      self.window.config(bg="#FA6781")
      self.canvas.config(bg="#FA6781")

    self.window.after(1000, self.reset_bg)
