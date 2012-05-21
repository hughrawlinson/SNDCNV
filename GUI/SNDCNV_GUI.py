import SNDCNVclassified
from Tkinter import *
import tkFileDialog
import tkMessageBox
import sys

class SNDCNV_GUI:
	
	inputFile = ""
	outputFile = ""
	sndcnv = SNDCNVclassified

	def null():
		pass
		
	def __init__(self, master):
		frame = Frame(height=90, width=140)
		frame.pack_propagate(0)
		frame.pack()
		
		inputFile = ""
		outputFile = ""
		
		SNDCNVLabel = Label(text="|| SNDCNV ||")
		SNDCNVLabel.pack()
		
		goButton = Button(frame, text="Set Input File", command=self.inputFileCallback(1))
		goButton.pack()
		
		goButton = Button(frame, text="Set Output File", command=self.inputFileCallback(2))
		goButton.pack()
		
		goButton = Button(frame, text="Go", command=null)
		goButton.pack()
		
	def inputFileCallback(self,e):
		a = tkFileDialog
		if(e==1):
			fileName = a.askopenfilename()[1]
			if(len(fileName <= 2)):
				self.sndcnv.outputFile(fileName)
			else:
				print("File Not Valid")
		elif(e==2):
			fileName = a.askopenfilename()[1]
			if(len(fileName <= 2)):
				self.sndcnv.outputFile(fileName)
			else:
				print("File Not Valid")

root = Tk()
sndcnv = SNDCNV_GUI(root)
root.mainloop()