from tkinter import Frame,sys, RIGHT, Label
from PIL import Image, ImageTk
class BackGround(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		self.master = master
		self.__list_label=[]
		self.__list_listbox=[]
		self.__list_scrollbar=[]
		self.__list_button=[]
		self.__texture=[]
		self.init_window(master)

	def init_window(self,master):
		self.master.title("MOTVIAL")
		if sys.platform.startswith('win32'):
			self.master.iconbitmap("cod.ico")
		elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
			#self.master.iconbitmap("image/cod.ico")
			pass
		
		self.master.geometry("1106x649")
		self.master.configure(bg="#343838")
		self.master.resizable(1,1)

		self.__loadIMG()

	def __loadIMG(self):
		render=ImageTk.PhotoImage(Image.open("BACK.png"))
		self.img = Label(self.master, image=render,borderwidth=0)
		self.img.image = render
		self.img.place(x=0,y=0)
