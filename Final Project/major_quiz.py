import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox as mb
import json


class Quiz:
    """A class that comprises the functionality of a quiz
    
    Attributes:
    
    q_no (int): A counter that represents the question number of the quiz
    
    opt_selected (int): An integer value used for the selected option in a 
    question
    
    self.opts (list): List of radio button objects to display selection buttons
    
    data_size (int): The number of questions
    
    correct (int): A counter for the number of c
    
    """
    def __init__(self):
         
        self.q_no=0
        
        self.display_title()
        self.display_question()
         
        self.opt_selected=IntVar()
         
        self.opts=self.radio_buttons()
         
        self.display_options()
         
        self.buttons()
         
        self.data_size=len(question)
         
    
    def dict_to_series_bar(self):
        results_series = pd.Series(class_dict)
        new_plot = results_series.plot.bar()
        return (new_plot)

    def display_result(self):
        """Method that creates the result popup at the end of the GUI
        
        Returns:
        Result (String): Highest and lowest matched majors are returned as a 
        message
        
        """
        mb.showinfo("Result", f"You should go into {max(class_dict, key=class_dict.get)}")
        self.dict_to_series_bar()
        plt.show()
    
        #https://www.python-graph-gallery.com/390-basic-radar-chart 
        df  = pd.DataFrame(class_dict,index=[0])

        categories=list(df)[0:]
        N = len(categories)
        

        values=df.loc[0].tolist()
        values += values[:1]
        values

        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]

        ax = plt.subplot(111, polar=True)

        plt.xticks(angles[:-1], categories, color='grey', size=8)

        ax.set_rlabel_position(0)
        plt.yticks([2,4,6,8,10], ["2","4","6","8","10"], color="grey", size=7)
        plt.ylim(0,10)

        ax.plot(angles, values, linewidth=1, linestyle='solid')

        ax.fill(angles, values, 'b', alpha=0.1)

        plt.show()


    def check_ans(self):
        """A method that checks the answer given after user hits "next" and
        updates class_dict to formulate final result
        
        
        """


        
        if self.q_no == 0:
            
            if self.opt_selected.get() == 1:
                class_dict['Communication'] +=1
                class_dict['Humanities'] +=1
                class_dict['Business'] +=1
                class_dict['Health'] +=1
            
            elif self.opt_selected.get() == 2:
                class_dict['Engineering'] +=2
                class_dict['Computer Science'] +=2
                class_dict['Science'] +=1

                
            elif self.opt_selected.get() == 3:
                class_dict['Art'] +=2
                class_dict['Health'] +=2
                class_dict['Science'] +=1
                      
            else:

                class_dict['Law and Public Policy'] +=2


        else:
            pass
            
        
        if self.q_no == 1:
            if self.opt_selected.get() == 1:
                class_dict['Computer Science'] +=3
                class_dict['Engineering'] +=2
                class_dict['Business'] +=2
                class_dict['Science'] +=1
            

            elif self.opt_selected.get() == 2:
                class_dict['Communication'] +=2
                class_dict['Humanities'] +=2
                class_dict['Health'] +=1
                class_dict['Art'] +=1

            elif self.opt_selected.get() == 3:
                class_dict['Science'] +=2
                class_dict['Math'] +=2
            
            else:
                class_dict['Health'] +=2
                class_dict['Law and Public Policy'] +=1   


        else:
            pass

        if self.q_no == 2:
            if self.opt_selected.get() == 1:
                class_dict['Engineering'] +=1
                class_dict['Computer Science'] +=2
                class_dict['Law and Public Policy'] +=1
                class_dict['Business'] +=1 
                class_dict['Health'] +=1  
                    
            elif self.opt_selected.get() == 2:
                class_dict['Math'] +=1
                class_dict['Science'] +=1
                
            elif self.opt_selected.get() == 3:
                class_dict['Communication'] +=1
                class_dict['Humanities'] +=1
                class_dict['Art'] +=1
            
            else:
                class_dict['Business'] +=3
                class_dict['Computer Science'] +=2 
            
        else:
            pass

        if self.q_no == 3:
            if self.opt_selected.get() == 1:
                class_dict['Engineering'] +=1
                class_dict['Business'] +=2
                class_dict['Health'] +=1
                class_dict['Communication'] +=1   
                
            elif self.opt_selected.get() == 2:
                class_dict['Computer Science'] +=1
                class_dict['Law and Public Policy'] +=1
                class_dict['Humanities'] +=1
                class_dict['Art'] +=1
                class_dict['Science'] +=1
                
            elif self.opt_selected.get() == 2:
                class_dict['Communication'] +=1
                class_dict['Art'] +=1
                class_dict['Humanities'] +=1
            else:
                class_dict['Business'] +=2
                
        else:
            pass

        if self.q_no == 4:
            if self.opt_selected.get() == 1:
                class_dict['Computer Science'] +=1
                class_dict['Business'] +=1
                class_dict['Law and Public Policy'] +=1
                
            elif self.opt_selected.get() == 2:
                class_dict['Health'] +=1
                class_dict['Science'] +=1
                class_dict['Art'] +=1
                
            elif self.opt_selected.get() == 3:
                class_dict['Business'] +=2
                class_dict['Communication'] +=1
                class_dict['Humanities'] +=1
            else:
                class_dict['Math'] +=1
                class_dict['English'] +=1
                
        else:
            pass
        
        if self.q_no == 5:
            if self.opt_selected.get() == 1:
                class_dict['Art'] +=1
                class_dict['Humanities'] +=1
                
            elif self.opt_selected.get() == 2:
                class_dict['Communication'] +=1
                class_dict['Humanities'] +=1
                               
            elif self.opt_selected.get() == 3:
                class_dict['Engineering'] +=1
                class_dict['Computer Science'] +=1
                class_dict['Health'] +=1
            else:
                class_dict['Business'] +=1
                class_dict['Law and Public Policy'] +=2
                class_dict['Health'] +=1      
        else:
            pass

        if self.q_no == 6:
            if self.opt_selected.get() == 1:
                class_dict['Art'] +=2
                
            elif self.opt_selected.get() == 2:
                class_dict['Business'] +=2
                
            elif self.opt_selected.get() == 3:
                class_dict['Communication'] +=1
                class_dict['Humanities'] +=1
                
            else:
                class_dict['Science'] +=1
                class_dict['Engineering'] +=1
        else:
            pass


        
        if self.q_no == 7:
            if self.opt_selected.get() == 1:
                class_dict['Science'] +=2
                
            elif self.opt_selected.get() == 2:
                class_dict['Computer Science'] +=2
                
            elif self.opt_selected.get() == 3:
                class_dict['Art'] +=1
                class_dict['Communication'] +=1
                class_dict['Humanities'] +=1

            else:
                class_dict['Engineering'] +=1
        else:
            pass

        if self.q_no == 8:
            
            if self.opt_selected.get() == 1:
                class_dict['Communication'] +=1
                class_dict['Humanities'] +=1
                class_dict['Law and Public Policy'] +=1
                
                
            elif self.opt_selected.get() == 2:
                class_dict['Math'] +=2
                class_dict['Computer Science'] +=1
                class_dict['Engineering'] +=1
                
            elif self.opt_selected.get() == 3:
                class_dict['Health'] +=2
                class_dict['Science'] +=1
                class_dict['Engineering'] +=1  
                
            elif self.opt_selected.get() == 4:
                class_dict['Art'] +=2

        else:
            pass

 

    def next_btn(self):
        """Method used to check the answer and perform the calculations towards
        the final result, as well as update counters and end the GUI once the
        quiz is over, else, goes to next question.
        
        """

        self.check_ans()

        self.q_no += 1

        if self.q_no==self.data_size:

            self.display_result()

            gui.destroy()
            
        else:
            self.display_question()
            self.display_options()

 
    def buttons(self):
        """Interface method used to show two buttons on the screen. This method
        sets the button properties and the physical coordinates.
        
        """

        next_button = Button(gui, text="Next",command=self.next_btn,
        width=10,bg="white",fg="black",font=("ariel",16,"bold"))
         

        next_button.place(x=350,y=380)
         

        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="white", fg="black",font=("ariel",16," bold"))
         

        quit_button.place(x=700,y=50)
 

    def display_options(self):
        """This method displays the options available for the current question.
        it updates the question each time.
        """
        
        val=0
        

        self.opt_selected.set(0)
        

        for option in options[self.q_no]:
            self.opts[val]["text"] = option
            val+=1
            
 

    def display_question(self):
        """GUI method that literally displays the question header.
        """

        q_no = Label(gui, text=question[self.q_no], width=60,
        font=('ariel',16,'bold'), anchor= 'w' )

        q_no.place(x=70, y=100)
 

    def display_title(self):
        """Displays title of the quiz.
        """

        title = Label(gui, text="THE MAJOR QUIZ",
        width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
         

        title.place(x=0, y=2)
 

    def radio_buttons(self):
        """Shows the radio buttons to select the question, determines how many
        radio buttons needed.

        Returns:
            list: radio button objects
        """
         

        q_list = []

        y_pos = 150
        

        while len(q_list) < len(options[self.q_no]):
            

            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",15))
            

            q_list.append(radio_btn)
            

            radio_btn.place(x = 90, y = y_pos)

             

            y_pos += 40

        return q_list

class_dict = {'Math' : 0,
        "English" : 0,
        'Computer Science' : 0,
        'Engineering' : 0,
        'Art' : 0,
        'Business' : 0,
        'Communication' : 0,
        'Science' : 0,
        'Law and Public Policy' : 0,
        'Health' : 0,
        'Humanities' : 0}


gui = Tk()

gui.geometry("800x450")

gui.title("INST326 Final Project Team SES")

with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])

quiz = Quiz()

gui.mainloop()
 
# GUI code involved use of TKINTER, which I couldn't have done without
# https://www.geeksforgeeks.org/python-mcq-quiz-game-using-tkinter/
# Used for JSON file idea for data retrieval, and instructions for quiz creation