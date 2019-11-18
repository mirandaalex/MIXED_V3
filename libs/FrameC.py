from tkinter import Frame,sys, RIGHT, Label,Scrollbar,VERTICAL,Listbox,NONE,END,LEFT

class FrameC(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		self.master = master
		self.__list_label={}
		self.__list_listbox=[]
		self.__list_scrollbar=[]
		self.__list_button=[]
		self.__texture=[]
		self.__actualErrors={"Todos":0,"Graves":0}
		self.__Inicializa()
		

		
	def __Inicializa(self):
		#Se configura el Frame en tamaño y color
		self.configure(height=524,width=1088,background="#343838",borderwidth=0)
		self.place(x=7,y=116)
		#Se añade Texto encima del TextBox
		temp=self.addLabel("  Serial Number            Status                         Date",
							x=27,
							y=47,
							ax=74,
							ay=1,
							bg="#069696")
		temp.configure(cursor="arrow",anchor="w",font=(None, 10))
		temp=self.addLabel("  Serial Number                         Date                Banda",
							x=665,
							y=267,
							ax=48,
							ay=1,
							bg="#069696")
		temp.configure(cursor="arrow",anchor="w",font=(None, 10))
		#Se añade Textbox
		self.__addTextbox()
		for q in range(0,100):
			self.addText(0,"   Serial Number            Status                         Date","Todos")
		
		#Se añaden Etiquetas para abrir otros
		self.addLabel("GENERAL",30,26,8,1,"#343838")
		self.__cargaBandas(
			self.__buscaBandas())

		#Se carga Segunda Textbox y Label
		temp=self.addLabel("ESTADO DE LA BANDA",
							x=665,
							y=45,
							ax=18,
							ay=1,
							bg="#343838",
							fontcolor="#00b4cc")
		temp.configure(cursor="arrow",anchor="w",font=("Ebrima", 17,"bold"))
		temp=self.addLabel("Daños graves en la banda",
							x=665,
							y=227,
							ax=25,
							ay=1,
							bg="#343838",
							fontcolor="#00b4cc")
		temp.configure(cursor="arrow",anchor="w",font=("Ebrima", 17,"bold"))
		self.__addTextbox(dx=55,dy=11,x1=665,y=267,x2=1052,sdy=210)
		for q in range(0,100):
			self.addText(1,"   Serial Number                         Date                Banda","Graves")



	def __addTextbox(self,dx=85,dy=24,x1=27,y=47,x2=624,sdy=430):
		scrolly=Scrollbar(self,activebackground="#171212",bg="#343838",orient=VERTICAL,troughcolor="#171212")
		listbox=Listbox(self,
						height=dy, 
						width=dx ,
						background="#343838",
						borderwidth=0,
						highlightcolor="#4d86a1",
						selectbackground="#4d86a1",
						activestyle=NONE,
						highlightbackground="#4a4a4a",
						yscrollcommand=scrolly.set)

		listbox.config(font=("", 10),fg="#FFFFFF")
		listbox.place(x=x1,y=y+21)
		scrolly.place(x=x2,y=y,height=sdy)	
		self.__list_listbox.append(listbox)
		self.__list_scrollbar.append(scrolly)
		
		listbox.configure(yscrollcommand=scrolly.set)
		scrolly.configure(command=listbox.yview)

	def addText(self,x,text,typee):
		n=self.__actualErrors[typee]
		self.__list_listbox[x].insert(END,text)
		self.__actualErrors[typee]+=1
		if (n+3)%2==0:
			self.__list_listbox[x].itemconfigure(n,bg="#696969")

	def addLabel(self,textvar="NONE",x=0,y=0,ax=2,ay=1,bg="#343838",fontcolor="#FFFFFF"):
		label=Label(self,
					activeforeground="#4d86a1",
					cursor="hand2",
					height=ay,
					width=ax,
					background=bg,
					text=textvar,
					fg=fontcolor,
					takefocus=0)
		label.place(x=x,y=y)
		self.__list_label[textvar]={"Apuntador":label,"x":x,"y":y}
		return label

	def __buscaBandas(self):
		return ["Banda1","Banda2"]

	def __cargaBandas(self,bandas):
		dx=65
		for x in bandas:
			self.addLabel(x,30+dx,26,8,1,"#343838")
			dx=dx+65