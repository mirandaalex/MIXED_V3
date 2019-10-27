from tkinter import Frame,sys, RIGHT, Label
from os import scandir, getcwd

class FrameB(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		self.master = master
		self.__list_label=[]
		self.__list_listbox=[]
		self.__list_scrollbar=[]
		self.__list_button=[]
		self.__texture=[]
		self.configure(height=91,width=1088,background="#f0f0f0",borderwidth=0)
		self.place(x=7,y=18)
	
	def __ls(ruta = getcwd()):
 	   return [arch.name for arch in scandir() if arch.is_file()]
	
	def buscaHerramientas(self):
		temp=self.__ls()
		for x in temp:
			print(x)
			if x=="LICENSE":
				print("Es igual y funciona")

	def cargaHerramientas(self):
		pass
##Buscar un document que se encuetre dentro de  una carpeta el cual empieze por algun digitito o caracter en especial
