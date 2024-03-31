######################## IMPORTS
from tkinter import *
import PIL 
from tkinter import messagebox 
from email.mime.text import MIMEText

#media player imports 

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


###music player
import os


####pour l'updater
import updater


#faire attention au chemin d'accès relatif pour les futures mises à jours
os.system('python3 ./updater.py')


#version du logiciel dans un fichier python séparé

######################## VARIABLES

screen = Tk()
screen.title('Application Papy')
screen.geometry("1000x700")
screen.geometry("+500+100")
screen.title('App pour papy')
screen.configure(bg='grey')
screen.resizable(False, False)


######################## FONCTIONS

#/Users/macminithomasconstantin/Downloads/wankil.mp4
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist

def stream_player(stream_url):
    # import youtube_dl

    # url = 'https://www.youtube.com/watch?v=5hheaSDEw18&ab_channel=WankilStudio-LainketTerracid'

    # ydl = youtube_dl.YoutubeDL()
    # info = ydl.extract_info(url, download=False)

    # video_url = info['formats'][0]['url']
        
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
    from PyQt5.QtMultimediaWidgets import QVideoWidget
    from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Video Player')
    window.setGeometry(100, 100, 640, 480)

    video_widget = QVideoWidget(window)
    button = QPushButton('Play', window)

    layout = QVBoxLayout(window)
    layout.addWidget(video_widget)
    layout.addWidget(button)

    player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
    player.setVideoOutput(video_widget)
    button.clicked.connect(lambda: player.play())

    content = QMediaContent(QUrl(stream_url))
    player.setMedia(content)
    player.play()

    window.show()

    sys.exit(app.exec_())


def video_player(file_path):
    from PyQt5.QtCore import QDir, Qt, QUrl
    from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
    from PyQt5.QtMultimediaWidgets import QVideoWidget
    from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
            QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
    from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
    from PyQt5.QtGui import QIcon
    import sys
    
    class VideoPlayer(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("PyQt5 Video Player") 
            self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
    
            videoWidget = QVideoWidget()
    
            self.playButton = QPushButton()
            self.playButton.setEnabled(False)
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.playButton.clicked.connect(self.play)
    
            self.positionSlider = QSlider(Qt.Horizontal)
            self.positionSlider.setRange(0, 0)
            self.positionSlider.sliderMoved.connect(self.setPosition)
    
            self.error = QLabel()
            self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
    
            openButton = QPushButton("Open Video")   
            openButton.setToolTip("Open Video File")
            openButton.setStatusTip("Open Video File")
            openButton.setFixedHeight(24)
            openButton.clicked.connect(self.openFile)
    
            self.openFile(f'{file_path}')

    
            # Create a widget for window contents
            wid = QWidget(self)
            self.setCentralWidget(wid)
    
            # Create layouts to place inside widget
            controlLayout = QHBoxLayout()
            controlLayout.setContentsMargins(0, 0, 0, 0)
            controlLayout.addWidget(self.playButton)
            controlLayout.addWidget(self.positionSlider)
    
            layout = QVBoxLayout()
            layout.addWidget(videoWidget)
            layout.addLayout(controlLayout)
            layout.addWidget(self.error)
    
            # Set widget to contain window contents
            wid.setLayout(layout)
    
            self.mediaPlayer.setVideoOutput(videoWidget)
            self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
            self.mediaPlayer.positionChanged.connect(self.positionChanged)
            self.mediaPlayer.durationChanged.connect(self.durationChanged)
            self.mediaPlayer.error.connect(self.handleError)
    

    
        def openFile(self, file_name=''):
            if file_name:
                fileName = file_name
            else:
                fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                            QDir.homePath())

            if fileName != '':
                self.mediaPlayer.setMedia(
                        QMediaContent(QUrl.fromLocalFile(fileName)))
                self.playButton.setEnabled(True)
                self.mediaPlayer.play()



        def exitCall(self):
            sys.exit(app.exec_())
    
        def play(self):
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                self.mediaPlayer.pause()
            else:
                self.mediaPlayer.play()
    
        def mediaStateChanged(self, state):
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPause))
            else:
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))
    
        def positionChanged(self, position):
            self.positionSlider.setValue(position)
    
        def durationChanged(self, duration):
            self.positionSlider.setRange(0, duration)
    
        def setPosition(self, position):
            self.mediaPlayer.setPosition(position)
    
        def handleError(self):
            self.playButton.setEnabled(False)
            self.error.setText("Error: " + self.mediaPlayer.errorString())
    
    
    app = QApplication(sys.argv)
    videoplayer = VideoPlayer()
    videoplayer.resize(1192, 756)
    videoplayer.geometry()
    videoplayer.show()
    sys.exit(app.exec_())    
    

def header () :
    header_canvas = Canvas(screen,height=80,width=972.5)
    header_canvas.config(bg='yellow',borderwidth=10,relief=FLAT)
    header_canvas.place(x=0,y=0)
    
    mail_image = PhotoImage(file='/Users/macminithomasconstantin/Desktop/local_app_papy/Build1/app_pc_papyV2/GUI_images/acceuil_button.png')
    mail_image_resized = mail_image.subsample(3)
    BUTTON1 = Button(screen,image=mail_image_resized)
    BUTTON1.config(relief="flat",borderwidth=0,highlightthickness=0)
    BUTTON1.place(x=125,y=20)
    
    # send_image =  PhotoImage(file='/Users/macminithomasconstantin/Desktop/codage/paper-plane.png')
    # send_image_resized = send_image.subsample(9)
    # B_SUBMIT = Button(main_menu, command=lambda: envoyer_mail_rapport_bug(sources_erreurs),image=send_image_resized)
    # B_SUBMIT.config(relief="flat",borderwidth=0,highlightthickness=0)
    # B_SUBMIT.place(x=415, y=420)

    # home_logo = PhotoImage(file='/Users/macminithomasconstantin/Desktop/local_app_papy/Build1/app_pc_papyV2/GUI_images/acceuil_button.png')
    # home_logo_resized = home_logo.subsample(3,3)
    # button2 = Button(screen,text='Acceuil')
    # button2.config(image=home_logo_resized)
    # button2.place(x=375,y=45,anchor=CENTER)
    
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
    play_video = Button(screen,text='lire vidéo')
    play_video.config(command=lambda:video_player(r'/Users/macminithomasconstantin/Downloads/LA HONTE IL SAIT PAS CONDUIRE LE GROS NULLOS (Expeditions MudRunner).mp4'))
    play_video.place(x=60,y=100)
    # video_player(r'/Users/macminithomasconstantin/Downloads/wankil.mp4')
    # video_player(r'/Users/macminithomasconstantin/Downloads/QUE SE CACHE-T-IL DANS VOS INTESTINS (Revenge Of The Colon).mp4')
    # video_player(r'/Users/macminithomasconstantin/Downloads/LA HONTE IL SAIT PAS CONDUIRE LE GROS NULLOS (Expeditions MudRunner).mp4')

######################## SCRIPT PRINCIPAL

main_menu()


screen.mainloop()

