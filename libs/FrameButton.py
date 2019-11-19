from tkinter import Frame,sys, RIGHT,LEFT, Label, Button
from json import load
from os import scandir, getcwd,listdir
import importlib
from PIL import Image, ImageTk

class FrameB(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		self.master = master
		self.__tool_list=[]
		self.__list_listbox=[]
		self.__list_scrollbar=[]
		self.__list_button=[]
		self.__texture=[]
		self.configure(height=91,width=1088,background="#F0F0F0",borderwidth=0)
		self.place(x=7,y=18)

	

##Buscar un document que se encuetre dentro de  una carpeta el cual empieze por algun digitito o caracter en especial
	def __ls(self,ruta = getcwd()):
		if sys.platform.startswith('win32'):
			return [ruta+"\\libs\\"+arch.name for arch in scandir(ruta+"\\libs\\") if arch.is_file()]
		elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
			return [ruta+"/libs/"+arch.name for arch in scandir(ruta+"/libs/") if arch.is_file()]

	def buscaHerramientas(self):
		
		temp=self.__ls()
		for x in temp:
			if x[len(x)-4:]=="json":
				self.__tool_list.append(x)
				#print(x,"Es igual y funciona")

	def cargarHerramientas(self,data,ruta0 = getcwd()):
		if sys.platform.startswith('win32'):
			tree = listdir(ruta0+"\\libs\\")
		elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
			tree = listdir(ruta0+"/libs/")

		for i in tree:
			if i == data["Nombre_Archivo"]:
				name = i.replace(".py", "")
				#print(name)
				name="libs."+name
				module=importlib.import_module(name)
				try:
					class_ = getattr(module, data["Clase"])
					instance = class_(self.master)
					method_to_call = getattr(instance, data["Metodo"])
					#method_to_call()
					if data["Imagen"]==1:
						ruta=data["Nombre"]+"."+data["Tipo"]	
						load=Image.open(ruta)
						render=ImageTk.PhotoImage(load)
						nbutton=Button(	self, 	
										image=render,
										bg=data["Fondo"],
										borderwidth=data["BorderWidth"],
										activebackground=data["FondoActivo"],
										highlightthickness = 0,
										cursor="hand2"
										)
						nbutton.configure(command=lambda:method_to_call(self.master))
						nbutton.image=render
						nbutton.place(x=data["x"],y=data["y"])
						self.__list_button.append(nbutton)
					
					elif data["Etiqueta"]==1:
						nbutton=Button(	self,
										text=data["Texto"],
										bg=data["Fondo"],
										fg=data["Color"],
										borderwidth=data["BorderWidth"],
										activebackground=data["FondoActivo"],
										cursor="hand2"
										)	
						nbutton.configure(command=lambda:method_to_call(self.master))
						nbutton.config(font=(data["Tipografia"],data["Size"]))
						nbutton.place(x=data["x"],y=data["y"])
						self.__list_button.append(nbutton)
				
					else:
						nbutton=Button(	self,
										text=data["Texto"],
										bg=data["Fondo"],
										fg=data["Color"],
										borderwidth=data["BorderWidth"],
										activebackground=data["FondoActivo"],
										cursor="hand2"
										)	
						nbutton.configure(command=lambda:method_to_call(self.master))

						nbutton.config(font=(data["Tipografia"],data["Size"]))
						nbutton.place(x=data["x"],y=data["y"])
						self.__list_button.append(nbutton)
				except Exception as e:
					print(e)

	
	def crearBotones(self):
		for x in self.__tool_list:
			data_file=open(x,"r") 
			data=load(data_file)
			self.cargarHerramientas(data)