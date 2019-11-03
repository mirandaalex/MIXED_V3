from tkinter import Tk
from threading import Thread
from libs.FrameBackGround import *
from libs.FrameButton import *
from libs.FrameC import *
root = Tk()
F=BackGround(root)
FB=FrameB(root)
FB.buscaHerramientas()
FB.crearBotones()
FC=FrameC(root)
root.mainloop()