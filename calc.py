from tkinter import Tk, Label, Button, IntVar
from math import sqrt

class Calculator:
	def __init__(self, master):
		self.master = master

		self.total = 0
		self.op = False
		self.operator = ""
		self.entry1 = ""
		self.entry2 = ""
		self.num1 = 0
		self.num2 = 0

		self.total_label_text = IntVar()
		self.total_label_text.set(self.total)
		self.total_label = Label(master, textvariable=self.total_label_text)

		self.num0_button = Button(master, text="0", command=lambda: self.calc_loop("0"))
		self.num1_button = Button(master, text="1", command=lambda: self.calc_loop("1"))
		self.num2_button = Button(master, text="2", command=lambda: self.calc_loop("2"))
		self.num3_button = Button(master, text="3", command=lambda: self.calc_loop("3"))
		self.num4_button = Button(master, text="4", command=lambda: self.calc_loop("4"))
		self.num5_button = Button(master, text="5", command=lambda: self.calc_loop("5"))
		self.num6_button = Button(master, text="6", command=lambda: self.calc_loop("6"))
		self.num7_button = Button(master, text="7", command=lambda: self.calc_loop("7"))
		self.num8_button = Button(master, text="8", command=lambda: self.calc_loop("8"))
		self.num9_button = Button(master, text="9", command=lambda: self.calc_loop("9"))

		self.div_button = Button(master, text="÷", command=lambda: self.calc_loop("d"))
		self.mult_button = Button(master, text="x", command=lambda: self.calc_loop("m"))
		self.sub_button = Button(master, text="-", command=lambda: self.calc_loop("s"))
		self.add_button = Button(master, text="+", command=lambda: self.calc_loop("a"))
		self.equ_button = Button(master, text="=", command=lambda: self.calc_loop("eq"))
		self.sqrt_button = Button(master, text="sqrt", command=lambda: self.calc_loop("sqrt"))
		self.clr_button = Button(master, text="c", command=lambda: self.calc_loop("cl"))

		# LAYOUT
		self.total_label.grid(row=0, column=0)

		self.clr_button.grid(row=1, column=3)

		self.num0_button.grid(row=5, column=0)
		self.num1_button.grid(row=4, column=0)
		self.num2_button.grid(row=4, column=1)
		self.num3_button.grid(row=4, column=2)
		self.num4_button.grid(row=3, column=0)
		self.num5_button.grid(row=3, column=1)
		self.num6_button.grid(row=3, column=2)
		self.num7_button.grid(row=2, column=0)
		self.num8_button.grid(row=2, column=1)
		self.num9_button.grid(row=2, column=2)

		self.div_button.grid(row=2, column=3)
		self.mult_button.grid(row=3, column=3)
		self.sub_button.grid(row=4, column=3)
		self.add_button.grid(row=5, column=3)
		self.equ_button.grid(row=5, column=2)

		self.sqrt_button.grid(row=1, column=2)

	# Clean up, reset
	def clearScreen(self):
		self.total = 0
		self.op = False
		self.operator = ""
		self.entry1 = ""
		self.entry2 = ""
		self.num1 = 0
		self.num2 = 0
		self.total_label_text.set(self.total)

	# Main algorithm for calculations
	def calc_loop(self, arg):
		# If clear button is pressed
		if arg == "cl":
			self.clearScreen()
			return True
		# If still entering the first number
		if not self.op:
			if arg == "s" and self.num1 == 0:
				self.operator = arg
				self.op = True
				return True
			if arg not in ["a","s","m","d","eq","sqrt"]:
				self.entry1 += arg
				self.num1 = int(self.entry1)
				self.total_label_text.set(self.num1)
			else:
				# Section for special math functions on single numbers
				if arg == "sqrt":
					self.total = self.sqroot()
					self.num1 = self.total
					self.total_label_text.set(self.total)
					return True
				else:
					self.operator = arg
					self.op = True
					return True
		# After the operator is entered
		else:
			# If still entering the second number
			if arg not in ["a","s","m","d","eq"]:
				self.entry2 += arg
				self.num2 = int(self.entry2)
				self.total_label_text.set(self.num2)
				return True
			# Do the calculation
			else:
				if self.operator == "a":
					self.total = self.add()
				if self.operator == "s":
					self.total = self.sub()
				if self.operator == "m":
					self.total = self.mul()
				if self.operator == "d":
					self.total = self.div()
				# Allow continual calculations
				self.num1 = self.total
				self.entry2 = ""
				self.num2 = 0
				if arg == "eq":
					self.op = False
				else:
					self.operator = arg
				self.total_label_text.set(float(self.total))

	# Basic arithmetic functions
	def add(self):
		return self.num1 + self.num2
	def sub(self):
		return self.num1 - self.num2
	def mul(self):
		return self.num1 * self.num2
	def div(self):
		return self.num1 / self.num2
	# Special math functions
	def sqroot(self):
		return sqrt(self.num1)
    def exponent(self):
        return pow(self.num1, self.num2)

# Main Tkinter object/window
root = Tk()
# Creating the calculator object and passing in root object
my_calc = Calculator(root)
# Running the main loop...
root.mainloop()
