import os, socket, sys
from tkinter import *
#from tkinter import ttk
from PIL import Image, ImageTk

class meuIp():
    
      def __init__(self):
         
        self.hostName = socket.gethostname()
        self.loginUser = os.getlogin()
        self.hostIp = socket.gethostbyname(self.hostName)
        
        self.Window()

      def Window(self):
        home = Tk()
        home.title("MEU IP")
        home.geometry("250x200")
        home['bg']='#778899'
        home.iconbitmap("img/icon.ico")
        
        Host = StringVar()
        Host.set(self.hostName)
        User = StringVar()
        User.set(self.loginUser)
        Ip = StringVar()
        Ip.set(self.hostIp)
        
        
        frameLogo = Frame(home, width= 250,height= 100)
        frameLogo.pack()
        frameLogo.place(anchor='center', relx= 0.5 ,rely= 0.3)
        Logo = ImageTk.PhotoImage(Image.open("img/Logo.jpg"))
        showLogo = Label(frameLogo, image = Logo, borderwidth=0)
        #showLogo.grid(row=1, column=1)
        showLogo.pack()
       
        # stylesLabel = ttk.Style()
        # stylesLabel.configure("TLabel", borderwidth =0,background ='#015ffc', font ="Calibri, 14", foreground ='white')
        # I tried several ways but for some reason I couldn't make "ttk styles" work.
        
        
        showUser = Label(home, textvariable = (User),borderwidth=0,background= '#778899',font="Calibri, 16",foreground = '#363636')   
        showUser.pack()
        showUser.place(anchor='center',relx=0.5, rely= 0.6) 
        
        showHost = Label(home, textvariable = (Host),borderwidth =0,background ='#778899', font ="Calibri, 14", foreground ='#363636')
        showHost.pack()
        showHost.place(anchor='center',relx=0.5 , rely= 0.7)
        
        
        showIP = Label(home, textvariable = (Ip),borderwidth=0,background= '#778899',font="Calibri, 14",foreground = '#363636')
        showIP.pack()
        showIP.place(anchor='center',relx=0.5 , rely= 0.9)
       
        
      
        home.mainloop()



meuIp()



