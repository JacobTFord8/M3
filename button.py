import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
	print "Hello!"
	tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
