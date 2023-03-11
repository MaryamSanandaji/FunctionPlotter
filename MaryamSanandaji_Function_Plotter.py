# All plot imports
from tkinter import messagebox
from tkinter import *
import tkinter.font as font
from matplotlib import pyplot as plot
from sympy import symbols, parse_expr
import numpy as np


# Function to remove every x in function and substitute by the value
def subs_function(value_to_subs, function_of_x):
    x_symbol = symbols('x')
    cast_pol_exp = parse_expr(function_of_x)
    cur_expression = cast_pol_exp.subs(x_symbol, value_to_subs)
    return cur_expression


# Function to check about valid case -> max should be greater than min (e.g.)
# also subs by max and min value then plot the function
def plot_function():
    min_value = float(min_value_entry.get())#int
    max_value = float(max_value_entry.get())#int
    function_to_plot = function_entry.get()
    if min_value < max_value:
        subs_function(min_value, function_to_plot)
        subs_function(max_value, function_to_plot)
        plot_it()
        window.mainloop()
    else:
        messagebox.showerror('Limited Error', 'Max value should be greater than min value')


# Function to create scale for (x, y) axis and show the final graph
def plot_it():
    min_value = float(min_value_entry.get())#int
    max_value = float(max_value_entry.get())
    x_axis = []
    y_axis = []
    '''
    for values in range(min_value, max_value ):#+ 100
        x_axis.append(values)
    '''
    x_axis = np.linspace(min_value, max_value, int(sample_number_value_entry.get()))
    for values in x_axis:
        y_axis.append(subs_function(values, function_entry.get()))

    x_axis_values = x_axis
    y_axis_values = y_axis
    plot.plot(x_axis_values, y_axis_values)
    plot.xlabel('x-axis')
    plot.ylabel('y-axis')
    plot.show()


window = Tk()

window.title("Function Plotter")
window.geometry("600x400")
frame_tool = Frame(window, bg='white')
frame_tool.pack(fill='x')
#myFont = font.Font(family="Calibre", size=15)
myFont = font.Font(family="Tahoma", size=12)

window.minsize(300, 300)



# Welcome Message
welcome_msg = Label(window, text='نرم افزار ترسيم توابع **طراحي توسط مريم سنندجي**', font=('Helvetica', 16), height=5)
welcome_msg.pack(side=TOP)


####### ####### #######
sample_number_value_label = Label(text="تعداد نقاط", font=myFont)
sample_number_value_label.pack()
sample_number_value_label.place(x=250, y=100, height=90, width=100)

# Textbox for min value
sample_number_value_entry = Entry()
sample_number_value_entry.pack()
sample_number_value_entry.place(x=250, y=170, height=35, width=100)
####### ####### #######

min_value_label = Label(text="شروع بازه زماني", font=myFont)
min_value_label.pack()
min_value_label.place(x=100, y=100, height=90, width=120)

# Textbox for min value
min_value_entry = Entry()
min_value_entry.pack()
min_value_entry.place(x=100, y=170, height=35, width=100)

max_value_label = Label(text="پايان بازه زماني", font=myFont)
max_value_label.pack()
max_value_label.place(x=400, y=100, height=90, width=120)

# Textbox for max value
max_value_entry = Entry()
max_value_entry.pack()
max_value_entry.place(x=400, y=170, height=35, width=100)

# Textbox for function to plot
function_entry = Entry()
function_entry.pack()
function_entry.place(x=200, y=230, height=45, width=200)

# Button for add plot action
btn_plot = Button(text="ترسيم", command=plot_function, font=myFont)
btn_plot.place(x=180, y=300, height=40, width=85)

# Button to exit the program
btn_exit = Button(window, text="خروج!", font=myFont, fg='red', command=window.destroy)
btn_exit.place(x=330, y=300, height=40, width=85)

# show GUI
window.mainloop()
