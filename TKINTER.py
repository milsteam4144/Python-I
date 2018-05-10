import tkinter
import tkinter.messagebox

class SuperBonus:
    def __init__(self):
        #Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Supervisor Bonus")


        #Create 5 frames.
        self.desc_frame = tkinter.Frame(self.main_window)
        self.name_frame = tkinter.Frame(self.main_window)
        self.num_frame = tkinter.Frame(self.main_window)
        self.sal_frame = tkinter.Frame(self.main_window)
        self.output_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #Create and pack the widgets for the frames.

        #Description
        self.desc_label = tkinter.Label(self.desc_frame, \
                                        text = ' This program shows supervisor pay data including a bonus that is 15% of the salary. ')
        self.desc_label.pack(side = 'left')

        #Name
        #This creates the label
        self.name_label = tkinter.Label(self.name_frame, \
                        text = 'Enter the Supervisor\'s name: ')
        
        self.name_entry = tkinter.Entry(self.name_frame, width = 10)

        #This packs the label on the left side of the window.
        self.name_label.pack(side = 'left')
        self.name_entry.pack(side = 'left')

        

        #Number
        self.num_label = tkinter.Label(self.num_frame, \
                        text = 'Enter the Supervisor\'s id number: ')
        
        self.num_entry = tkinter.Entry(self.num_frame, width = 10)

        self.num_label.pack(side = 'left')
        self.num_entry.pack(side = 'left')

        #Salary
        self.sal_label = tkinter.Label(self.sal_frame, \
                        text = 'Enter the Supervisor\'s salary: ')
        
        self.sal_entry = tkinter.Entry(self.sal_frame, width = 10)

        self.sal_label.pack(side = 'left')
        self.sal_entry.pack(side = 'left')


        #Create and pack buttons.
        self.calc_button = tkinter.Button(self.button_frame, \
        text = "Show Bonus", command = self.calc_bonus) #calc_bonus is method
        self.quit_button = tkinter.Button(self.button_frame, \
        text = 'Quit', command = self.main_window.destroy)


        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')


        #Pack the frames into the window.
        self.desc_frame.pack()
        self.name_frame.pack()
        self.num_frame.pack()
        self.sal_frame.pack()
        self.output_frame.pack()
        self.button_frame.pack()
      

        #Start the main loop.
        tkinter.mainloop()

    #The calc_button executes this method when it is clicked.
    def calc_bonus(self):
        #Get the name, idnum and salary.
        self.name = str(self.name_entry.get())
        self.num = str(self.num_entry.get())
        self.sal = float(self.sal_entry.get())

        #Calculate the bonus.
        self.bonus = (self.sal * .15)
        self.total_pay = self.sal + self.bonus
        dataToshow = "Name: "+ self.name + "\n" + \
        "ID Number: " + self.num + "\n" + "Salary: " + str("${:,.2f}".format(self.sal)) + "\n" + \
        "BONUS: " + str("${:,.2f}".format(self.bonus)) + \
                            "\n" + "TOTAL PAY: " + str("${:,.2f}".format(self.total_pay))
        
        tkinter.messagebox.showinfo('Supervisor Pay Data', dataToshow) 
        


def main():
#Create an instance of the SuperBonus class.
    super_bonus = SuperBonus()


main()
        
        

        
        
        
        
