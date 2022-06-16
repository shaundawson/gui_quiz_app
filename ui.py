from tkinter import *

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
BACKGROUND_COLOR = "#ffffff"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas= Canvas(width=300, height=250)
        self.question_text= self.canvas.create_text(150, 
                                         125, 
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
        self.true_button = Button(image=true_image,highlightthickness=0, highlightbackground=THEME_COLOR)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0, highlightbackground=THEME_COLOR)
        self.false_button.grid(row=2, column=1)
        
        
        self.window.mainloop()