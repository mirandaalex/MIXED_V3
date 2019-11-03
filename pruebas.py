from json import load
from os import scandir, getcwd,listdir
import importlib
y=[]


module=[]
#SE IMPORTAN MODULOS DENTRO DE LIBS
import importlib




#ENCONTRAR JSON
def ls(ruta = getcwd()):
	   return [arch.name for arch in scandir() if arch.is_file()]

def buscaHerramientas():
	temp=ls()
	for x in temp:
		
		if x[len(x)-4:]=="json":
			y.append(x)
			print(x,"Es igual y funciona")
buscaHerramientas()


data_file=open(y[0],"r") 
data=load(data_file)



tree = listdir(".\\libs\\")
print(tree)
for i in tree:
	if i != "__init__.py" and i !="__pycache__" and i !="FrameBackGround.py" and i !="FrameButton.py" and i !="FrameC.py":
		name = i.replace(".py", "")
		print(name)
		name="libs."+name
		module=importlib.import_module(name)
		try:
			class_ = getattr(module, data["Clase"])
			instance = class_()
			method_to_call = getattr(instance, data["Metodo"])
			method_to_call()
		except Exception as e:
			print(e)
		
		