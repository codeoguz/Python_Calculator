from tkinter import *
from tkinter import ttk

# Create window and make configurations
root = Tk()
root.resizable(0, 0)
root.title("Calculator")

# This class is for creating buttons and their functions can be accessed from the class
# Type1 = number, Type2 = operation, Type3 = equals, Type4 = C
class cButton:
    def __init__(self, text, width = 10, isDouble = False, type = 1):
        self.text = text
        self.type = type
        
        self.button = Button(root, text=text, width=22 if isDouble else width, height=5, 
                             command= self.enter_number if self.type == 1
                             else self.set_operation if self.type == 2 else self.calculate if self.type == 3 else self.clear if self.type == 4 else self.decimal
                             )
    
    # This will run when a number button gets clicked
    def enter_number(self):
        number = self.text
        if expression[0] == '':
            expression[1] += number
        else:
            expression[2] += number
        display.config(text= returnDisplay())
        
        
    # This will run when a number operation gets clicked
    def set_operation(self):
        # If first parameter is empty affect first parameter
        # If first parameter is NOT empty set operator
        # If first parameter and operator are NOT empty set operator
        
        if (expression[0] == '' and expression[1] != '') or (self.text != '-' and expression[0] != '' and expression[1] != ''):
            expression[0] = self.text
            display.config(text= returnDisplay())
        else:
            if self.text == '-' or '+':
                if expression[0] != '' and expression[2] == '':
                    expression[2] = self.text
                    
                if expression[0]  == '' and expression[1] == '':
                    expression[1] = self.text
        display.config(text= returnDisplay())

    # This will run when the equal button gets clicked
    def calculate(self):
        try:
            result = float()
            parameter1 = float(expression[1])
            parameter2 = float(expression[2])
            if expression[0] == '÷':
                result = float(parameter1 / parameter2)
            elif expression[0] == 'x':
                result = float(parameter1 * parameter2)
            elif expression[0] == '-':
                result = float(parameter1 - parameter2)
            elif expression[0] == '+':
                result = float(parameter1 + parameter2)
            
            expression[0], expression [2] = '', ''
            expression[1] = str(result)
            display.config(text= returnDisplay())
        except Exception as err:
            display.config(text= err)
            self.clear
        
    # This will run when the clear button gets clicked
    def clear(self):
        expression[0], expression[1], expression[2] = '','',''
        display.config(text=returnDisplay())
    
    # This will run when the decimal button gets clicked
    def decimal(self):
        if expression[0] == '':
            if '.' not in expression[1]:
                expression[1] += '.'
        else:
            if '.' not in expression[2]:
                expression[2] += '.'
        display.config(text=returnDisplay())

# This will hold the values of operations and numbers
# First element represet operation operator, and the second is for the first number and third one is for the secind number  
expression = ['', '', '']

# This will evaluate expression[] and output something like '5 + 4'
# First element represents operation, second is the first number and the last one is the second number
def returnDisplay():
    print(expression)
    if expression[0] + expression[1] + expression[2] == '':
        return 'Do calculations!'
    elif expression[1] is '' and expression[0] == '':
        return expression[1]
    else:
        return f'{expression[1]} {expression[0]} {expression[2]}'
    
# Sign text for displaying operations, information and results
display = Label(root, text= returnDisplay(), justify='right', font= 'size=20', pady=30)
display.grid(column=0, row=0, columnspan=4)

# Input buttons
    # Buttons created using tkinter library
zero = cButton('0')
zero.button.grid(row=5, column=1)

one = cButton('1')
one.button.grid(row=4, column=0)

two = cButton('2')
two.button.grid(row=4, column=1)

thre = cButton('3')
thre.button.grid(row=4, column=2)

four = cButton('4')
four.button.grid(row=3, column=0)

five = cButton('5')
five.button.grid(row=3, column=1)

six = cButton('6')
six.button.grid(row=3, column=2)

seve = cButton('7')
seve.button.grid(row=2, column=0)

eigh = cButton('8')
eigh.button.grid(row=2, column=1)

nine = cButton('9')
nine.button.grid(row=2, column=2)



# Operations

sum = cButton('+', type = 2)
sum.button.grid(row=1, column=3)
subt = cButton('-', type = 2)
subt.button.grid(row=2, column=3)
divi = cButton('÷', type = 2)
divi.button.grid(row=3, column=3)
mult = cButton('x', type = 2)
mult.button.grid(row=4, column=3)


# Other operation buttons

resu = cButton('=', type = 3)
resu.button.grid(row=5, column=3)

clea = cButton('C', type = 4, isDouble=True)
clea.button.grid(row=1, column=0, columnspan=2)

dot = cButton('.', type = 5)
dot.button.grid(row=5, column=2)

root.mainloop() 