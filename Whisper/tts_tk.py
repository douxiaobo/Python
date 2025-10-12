import sounddevice as sd
from tkinter import *

class VoiceRecorder:
    def __init__(self):
        self.recording=False
        self.audio_data=None
        self.fs=44100

        self.root=Tk()
        self.root.title("Text-to-Speech")
        self.root.geometry("400x300")

        self.TextL=Label(self.root,text="Enter Text Here:",font='arial 15 bold')
        self.TextL.grid(row=0,column=0)

        self.EntryL=Entry(self.root,width=50,font='arial 15 bold')





TextL=Label(root,text="Enter Text Here:",font='arial 15 bold')
TextL.grid(row=0,column=0)

TextE=Entry(root,width=50,font='arial 15 bold')
TextE.grid(row=0,column=1)

ButtonL=Button(root,text="Speak",font='arial 15 bold',command=lambda:speak(TextE.get()))
ButtonL.grid(row=1,column=0)

ButtonL=Button(root,text="Exit",font='arial 15 bold',command=lambda:exit())
ButtonL.grid(row=1,column=1)

root.mainloop()
def speak(text):
    # from gtts import gTTS
    # from playsound import playsound
    # tts=gTTS(text=text,lang='en')
    # filename='voice.mp3'
    # tts.save(filename)
    # playsound(filename)
    return text

if __name__=='__main__':
    app=VoiceRecorder()
    app.run()