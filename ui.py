from re import L
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
BACKGROUND_COLOR = "#ffffff"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas= Canvas(width=300, height=250)
        self.question_text= self.canvas.create_text(150, 
                                         125, 
                                         width=280,
                                         text="Some text here.", 
                                         font=(FONT_NAME, 20, "italic"), 
                                         fill=THEME_COLOR)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self. canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        #Labels
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        #Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0, highlightbackground=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
    
        self.get_next_question()
       
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        
        
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        
    
    