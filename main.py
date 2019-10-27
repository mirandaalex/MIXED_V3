from tkinter import Tk
from threading import Thread
from libs.FrameA import *
from libs.FrameB import *
from libs.FrameC import *
root = Tk()
F=BackGround(root)
FB=FrameB(root)
FB.buscaHerramientas()
FC=FrameC(root)
root.mainloop()