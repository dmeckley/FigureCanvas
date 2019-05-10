from tkinter import *
from figureCanvas import FigureCanvas


def main():

	# Creates a Tk Widget Object Instance as the main window of the application:
	window = Tk()
	window.title("Display Figures")

	'''Outline Objects'''

	# Line Outline Shape Object Creation:
	xOutline = FigureCanvas(window, "line", 100, 100)
	xOutline.grid(row = 1, column = 1)

	# Rectangle Outline Shape Object Creation:
	squareOutline = FigureCanvas(window, "rectangle", False, 100, 100)
	squareOutline.grid(row = 1, column = 2)

	# Oval Outline Shape Object Creation:
	circleOutline = FigureCanvas(window, "oval", False, 100, 100) 
	circleOutline.grid(row = 1, column = 3)

	# Arc Outline Shape Object Creation:
	arcOutline = FigureCanvas(window, "arc", False, 100, 100)
	arcOutline.grid(row = 1, column = 4)

	'''Shaded Objects'''
	
	# Rectangle Shaded Shape Object Creation:
	squareShaded = FigureCanvas(window, "rectangle", True, 100, 100)
	squareShaded.grid(row = 2, column = 2)

	# Oval Shaded Shape Object Creation:
	circleShaded = FigureCanvas(window, "oval", True, 100, 100) 
	circleShaded.grid(row = 2, column = 3)

	# Arc Shaded Shape Object Creation:
	arcShaded = FigureCanvas(window, "arc", True, 100, 100)
	arcShaded.grid(row = 2, column = 4)

	# Halts Excution of Program:
	window.mainloop()


if __name__ == '__main__':
	main()