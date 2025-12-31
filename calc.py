import tkinter as tk
'''Imports Tkinter module
tk is an alias for easy access'''

#Button click handler
def press(v):
    entry.insert(tk.END,v)
    '''Called when a number or operator button is clicked
    Inserts the pressed value at the end of the Entry widget'''

#clear Function
def clear():
    entry.delete(0, tk.END)
    '''Clears the calculator screen
    Delets all characters from index 0 to End'''

#Backspace Function
def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)


#Calculation Function
def calc():
    try:
        result = eval(entry.get())
        '''entry.get() retrives the expression e.g.(2+6)
        eval() evaluates the string as a Python expression'''

        entry.delete(0, tk.END)#Clears the old expression
        entry.insert(0, result)#Displays exception instead of crashing

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")
        '''Handles invalid expression (e.g. 5++)
        Displays "exception" instead of crashing'''
#Main window creation
root = tk.Tk() #creates the main application window

root.title("Calculator")# Sets window title

root.configure(bg="#1e1e1e")#Sets background colour

root.resizable(False, False) #Disable resizing the windows

#Entry Widget(Display Screen)
entry = tk.Entry(
    root,
    font=("Times new roman",20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
'''Text input field
Acts as calculator display
Right-aligned for better calculator look'''
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

#Button Lables
button = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
    ]

'''Represent calculator buttons
   Stored in list to reduce repetitive code'''

#Dynamic Button Creation
r=1
c=0
'''Rows and column counter for grid layout'''

for b in button:
    cmd = calc if b=="=" else lambda x=b: press(x)
    '''if button is "=",call calc()
    else, call press() with the button value
    lambda x=b prevents late binding issues'''

    tk.Button(
        root,
        text=b,
        command=cmd,# these three lines creates a button widget
        font=("Calibri", 14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/" else "#3a3a3a",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)
    c+=1
    if c==4:
        r+=1
        c=0
        '''moves to next row after 4 buttons'''

#Clear Button
tk.Button(
    root,
    text="Clear",
    command=clear,
    font=("Calibri", 14),
    width=15,
    height=2,
    bg="#ff3b3b",
    fg="white",
    bd=0
).grid(row=r, column=0, columnspan=3, pady=4, padx=4)

'''Clears the calculator display screen
Spans across all columns'''

#Backspace Button
tk.Button(
    root,
    text="⌫",
    command=backspace,
    font=("Calibri", 14),
    width=5,
    height=2,
    bg="#555555",
    fg="white",
    bd=0
).grid(row=r, column=3, pady=4, padx=4)




#Event Loop
root.mainloop()
'''keeps the window running
Listens for user interactions'''
