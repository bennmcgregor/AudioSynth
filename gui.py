from tkinter import *
import threading
import inputAudio

stream = inputAudio.RecordObject()
quitClicked = False

def recording():
    def run():
        while quitClicked is False:
            stream.record()
            if quitClicked is True:
                break
    thread = threading.Thread(target = run)
    thread.start()

def start_record():
    global quitClicked
    quitClicked = False
    print("Recording...")
    recording()

def end_record():
    print("Stopped")
    global quitClicked
    quitClicked = True
    global stream
    stream.isRecording = False

def kill():
    root.destroy()

root = Tk()
root.geometry("500x500") 
root.title("")


topFrame = Frame(root)
topFrame.pack()


bottomFrame = Frame(root, bg="#e3e4e6")
bottomFrame.pack(side=BOTTOM)

start_rec_button = Button(bottomFrame, text="Click to record", command=start_record, font="Helvetica", bg="#f7d0cb", fg="#313131")
start_rec_button.pack()

stop_rec_button = Button(bottomFrame, text="Stop recording", command=end_record, fg="#313131", font="Helvetica", bg="#f7d0cb")
stop_rec_button.pack()

quit_button = Button(bottomFrame, text="Exit", command=kill, font="Helvetica", bg="#f7d0cb", fg="#313131")
quit_button.pack()

root.mainloop()
