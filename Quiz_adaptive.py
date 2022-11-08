# Import the required libraries
from tkinter import *
import pyttsx3
import codecs
import time

# Text to speech engine
engine = pyttsx3.init()

first_time = True
questions = []
answers = []
correct_answers = []
language = 'en'
q_no = 0
max_q = 20
question_frames = []
user_answers = []
output = ""

with codecs.open('questions_part2.txt', encoding='utf-8') as f:
    for line in f:
        words = line.split(",")
        questions.append(words[0])
        answers.append(words[1:5])
        correct_answers.append(int(words[5].removesuffix('\n')))


# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window to fullscreen
win.attributes("-fullscreen", True)

# Create all frames
greet = Frame(win)
end = Frame(win)
for i in range(max_q):
    question_frames.append(Frame(win))

# Pack first frame to start
greet.pack(fill='both', expand=1)


# Define a function for switching the frames
def change_frames(button_no=10):
    global q_no
    global user_answers
    global first_time
    global output

    if first_time is not True:
        q_no += 1
    first_time = False

    if button_no != 10:
        user_answers.append(button_no)

    if q_no != max_q:
        question_frames[q_no].pack(fill='both', expand=1)
    else:
        end.pack(fill='both', expand=1)

    if q_no == 0:
        greet.pack_forget()
    elif q_no == max_q:
        question_frames[q_no - 1].pack_forget()
    else:
        question_frames[q_no - 1].pack_forget()
    
    if q_no != max_q:
        question_text = Label(question_frames[q_no], text=questions[q_no], font=("Arial", 25))
        button0 = Button(question_frames[q_no], text=answers[q_no][0], command=lambda m=1: change_frames(m), width=25, height=5, font=("Arial", 12))
        button1 = Button(question_frames[q_no], text=answers[q_no][1], command=lambda m=2: change_frames(m), width=25, height=5, font=("Arial", 12))
        button2 = Button(question_frames[q_no], text=answers[q_no][2], command=lambda m=3: change_frames(m), width=25, height=5, font=("Arial", 12))
        button3 = Button(question_frames[q_no], text=answers[q_no][3], command=lambda m=4: change_frames(m), width=25, height=5, font=("Arial", 12))
        question_text.pack(pady=100)
        button0.pack(pady=50, padx=70, side=LEFT)
        button1.pack(pady=50, padx=70, side=LEFT)
        button2.pack(pady=50, padx=70, side=LEFT)
        button3.pack(pady=50, padx=70, side=LEFT)

    if q_no == max_q:
        result = 0
        for i in range(len(user_answers)):
            if user_answers[i] != correct_answers[i]:
                output += "wrong "
                result += 1
            else:
                output += "correct "
        end_text = Label(end, text=f"Thank you for participating! \n \n You got {result} wrong answers and {max_q-result} correct answers!", font=("Arial", 35))
        end_text.pack(pady=200)
        button_end = Button(end, text="Quit", command=win.destroy, width=25, height=5, font=("Arial", 12))
        button_end.pack(pady=50, padx = 650, side=LEFT)

        with open('C:\\Users\\lasse\\Desktop\\results_adaptive.txt', 'w') as f:
            f.write(output)

    #engine.say(questions[q_no])
    #engine.runAndWait()


# Add a heading logo in the frames
label1 = Label(greet, text="Hello, and welcome to this experiment. When you are ready, press OK to begin.", font=('Arial', 25))
btn1 = Button(greet, text="OK", command=change_frames, font=('Arial', 25))
label1.pack(pady=100)
btn1.pack(pady=100)

win.mainloop()
