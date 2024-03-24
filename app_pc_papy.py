######################## IMPORTS
from tkinter import *
import webbrowser
import time
from tkinter import messagebox 
import smtplib
from email.mime.text import MIMEText

###music player
import pygame
import os


####pour l'updater
import updater


os.system('python3 ./updater.py')

VERSION_LOGICIEL = "1.0"

######################## VARIABLES

screen = Tk()
screen.title('Application Papy')
screen.geometry("1000x700")
screen.geometry("+500+100")
screen.title('App pour papy')
screen.configure(bg='grey')
screen.resizable(False, False)



#### INFO BULLES // TOOLTIP : 
class ToolTip:
   def __init__(self, widget, bg_color="lightblue"):
      self.widget = widget
      self.tipwindow = None
      self.id = None
      self.x = self.y = 0
      self.bg_color = bg_color

   def showtip(self, text):
      """Affiche le texte dans la fenêtre contextuelle (tooltip)"""
      self.text = text
      if self.tipwindow or not self.text:
         return
      x, y, cx, cy = self.widget.bbox("insert")
      x = x + self.widget.winfo_rootx() + 57
      y = y + cy + self.widget.winfo_rooty() + 27
      self.tipwindow = tw = Toplevel(self.widget)
      tw.wm_overrideredirect(1)
      tw.wm_geometry(f"+{x}+{y}")
      label = Label(tw, text=self.text, justify=LEFT, background=self.bg_color, relief=SOLID, borderwidth=1, font=("tahoma", 8, "normal"))
      label.pack(ipadx=1)

   def hidetip(self):
      tw = self.tipwindow
      self.tipwindow = None
      if tw:
         tw.destroy()
   
def CreateToolTip(widget, text, bg_color):
   toolTip = ToolTip(widget, bg_color)

   def enter(event):
      toolTip.showtip(text)
      # Change the button's background color to blue when hovered
      widget.configure(bg=bg_color)

   def leave(event):
      toolTip.hidetip()
      # Change the button's background color back to its original color
      widget.configure(bg="SystemButtonFace")

   widget.bind("<Enter>", enter)
   widget.bind("<Leave>", leave)

def on_enter(event):
    button.config(bg="lightblue")

def on_leave(event):
    button.config(bg="SystemButtonFace")


button = Button(screen, text="Survolez-moi !")

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

############## BOUTON QUI CHANGE DE COULEUR AU SURVOL : 
# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

######################## FONCTIONS

def header () :
    header_canvas = Canvas(screen,height=80,width=972.5)
    header_canvas.config(bg='yellow',borderwidth=10,relief=FLAT)
    header_canvas.place(x=0,y=0)
    
    
    button1 = Button(screen,text='Acceuil')
    button1.config(padx=2,pady=2,border=0,borderwidth=0,font=('Avenir', 20))
    button1.place(x=175,y=45,anchor=CENTER)
    
    button2 = Button(screen,text='Acceuil')
    button2.config(padx=2,pady=2,border=0,borderwidth=0,font=('Avenir', 20))
    button2.place(x=375,y=45,anchor=CENTER)
    
    button3 = Button(screen,text='Acceuil')
    button3.config(padx=2,pady=2,border=0,borderwidth=0,font=('Avenir', 20))
    button3.place(x=575,y=45,anchor=CENTER)
    
    button3 = Button(screen,text='Acceuil')
    button3.config(padx=2,pady=2,border=0,borderwidth=0,font=('Avenir', 20))
    button3.place(x=775,y=45,anchor=CENTER)
        

def navbar () : 
    navbar_canvas = Canvas(screen,height=570,width=150)
    navbar_canvas.config(bg='lightgreen',borderwidth=10,relief=FLAT)
    navbar_canvas.place(x=0,y=102.5)
    
def music_player ():
   pass
def main_menu () : 
    header()
    navbar()
    music_player()

######################## SCRIPT PRINCIPAL

main_menu()
screen.mainloop()
