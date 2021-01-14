import tkinter as tk
import os
from gtts import gTTS 
from playsound import playsound

window=tk.Tk()

language = 'en'

window.title('Hello Python')
window.geometry("300x200+10+10")

lbl=tk.Label(window, text="Enter the input text", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)

txtfld=tk.Entry(window, text="", bd=5)
txtfld.place(x=70, y=100)

def on_change():
    message=txtfld.get()
    print(message)
    if os.path.exists("output_audio.mp3"):
        os.remove("output_audio.mp3")
    obj = gTTS(text=message,lang=language,slow=False)
    obj.save("output_audio.mp3")
    playsound("output_audio.mp3")
    
    
Btn=tk.Button(window, text="convert to speech", fg='blue', command=on_change)
Btn.place(x=80, y=150)



window.mainloop()
