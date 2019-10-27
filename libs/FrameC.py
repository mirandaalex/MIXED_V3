from tkinter import Frame,sys, RIGHT, Label
class FrameC(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		self.master = master
		self.__list_label=[]
		self.__list_listbox=[]
		self.__list_scrollbar=[]
		self.__list_button=[]
		self.__texture=[]
		self.configure(height=524,width=1088,background="#f0f0f0",borderwidth=0)
		self.place(x=7,y=116)


