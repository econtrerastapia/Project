from tkinter import *
from logic import *


class GUI:
    def grade(self):
        '''
        Function that calculates and displays the final grades based on
        the entered scores
        '''
        self.frame_three = Frame(self.window)
        self.scores_inputted = self.scores_inputted[0:self.num_of_students]

        text_widget = Text(self.frame_three, width=50, height=20)
        for student in self.scores_inputted:
            final_result = self.logic.student_score(self.scores_inputted, self.num_of_students, student)
            text_widget.insert('end', f'{final_result}\n')

            text_widget.pack(anchor='w', padx=10, pady=10)
            self.frame_three.pack(anchor='w', padx=10, pady=10)
        text_widget.config(state='disabled')

    def retrieve_scores(self):
        '''
        Function that retrieves input scores from the user
        '''
        self.scores_inputted = []
        for j in self.all_scores:
            self.score_entered = j.get()
            self.score_entered = self.score_entered.strip()
            self.scores_inputted.append(self.score_entered)
            j.config(state='disabled')

        self.grade()

    def the_scores(self):
        '''
        Function that displays the fields for entering the students scores
        '''
        self.num_of_students = int(self.entered)  # number of students
        num = int(0)

        for i in range(self.num_of_students):
            num += 1

            self.frame_two = Frame(self.window)

            self.enter_scores = Label(self.frame_two, text=f'Enter student {num} score:')
            self.input_scores = Entry(self.frame_two, width=20)

            self.enter_scores.pack(side='left')
            self.input_scores.pack(side='right')
            self.input_scores.pack(padx=55)
            self.input_scores.focus_set()

            self.frame_two.pack(anchor='w', padx=10, pady=10)

            self.all_scores.append(self.input_scores)

            self.button_enter.config(command=self.retrieve_scores)

    def enter_button(self):
        '''
        Funtion that handles what happens when the 'ENTER' button is first clicked
        '''
        self.entered = self.input_students.get()
        self.entered = self.entered.strip()

        try:
            self.entered = int(self.entered)
            if self.entered <= 0:
                self.frame_error_message.config(text='Must be positive')
            else:
                self.frame_error_message.pack_forget()
                self.input_students.config(state='disabled')
                self.the_scores()

        except ValueError:
            self.frame_error_message.config(text='Please input a number')
            self.enter_students.config(text='Total number of students:')
            self.input_students.delete(0, END)

    def __init__(self, window):
        '''
        :param window: The main Tkinter window
        '''

        self.window = window
        self.all_scores = []
        self.logic = Logic()

        # Frame for entering the number of students
        self.frame_one = Frame(self.window)
        self.enter_students = Label(self.frame_one, text='Total number of students:')
        self.input_students = Entry(self.frame_one, width=20)

        self.enter_students.pack(side='left')
        self.input_students.pack(side='right')
        self.input_students.focus_set()

        self.frame_one.pack(anchor='w', padx=10, pady=10)

        # Frame for displaying error messages
        self.frame_error = Frame(self.window)
        self.frame_error_message = Label(self.frame_error, text='')

        self.frame_error_message.pack(side='bottom')
        self.frame_error.pack(anchor='s')

        # Frame for enter button
        self.frame_two = Frame(self.window)
        self.button_enter = Button(self.window, text='ENTER', command=self.enter_button)

        self.button_enter.pack(side='bottom')
