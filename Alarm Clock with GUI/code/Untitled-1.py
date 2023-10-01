from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root = Tk()
root.title("Alarm Clock")
root.geometry("550x400")  # Increased the height to accommodate changes
root.configure(bg="#F0F0F0")  # Set a light gray background

mixer.init()

# Create a variable to track the alarm status (on/off)
alarm_on = False

def toggle_alarm():
    global alarm_on
    if not alarm_on:
        alarm_on = True
        start.config(text="Stop Alarm", bg="#FF5555")  # Change button text and color
        indicator.config(text="Alarm On", bg="#55FF55")  # Update text and color
        th = threading.Thread(target=a, args=())
        th.start()
    else:
        alarm_on = False
        start.config(text="Start Alarm", bg="#55FF55")  # Change button text and color
        indicator.config(text="Alarm Off", bg="#FF5555")  # Update text and color

def a():
    a = hr.get()
    if a == "":
        msg = messagebox.showerror('Invalid data', 'Please enter a valid time')
    else:
        Alarmtime = a
        CurrentTime = time.strftime("%H:%M")

        while Alarmtime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")

        if Alarmtime == CurrentTime:
            mixer.music.load(
                r'C:\Users\Himanshu\Downloads\AlarmClock-in-python-master\AlarmClock-in-python-master\tone.mp3')
            mixer.music.play()
            msg = messagebox.showinfo('Alarm', f'{amsg.get()}')
            if msg == 'ok':
                mixer.music.stop()

# Label at the top
head = Label(root, text="Professional Alarm Clock", font=('Arial', 24), bg="#F0F0F0")
head.pack(pady=10)

# Create a frame for the input elements
input_frame = Frame(root, bg="#F0F0F0")
input_frame.pack(pady=20)

# Alarm Time Input
atime_label = Label(input_frame, text="Alarm Time (HH:MM)", font=('Arial', 14), bg="#F0F0F0")
atime_label.grid(row=0, column=0, padx=10, pady=5)

hr = Entry(input_frame, font=('Arial', 14), width=5)
hr.grid(row=0, column=1, padx=10, pady=5)

# Alarm Message Input
amessage_label = Label(input_frame, text="Alarm Message", font=('Arial', 14), bg="#F0F0F0")
amessage_label.grid(row=1, column=0, padx=10, pady=5)

amsg = Entry(input_frame, font=('Arial', 14), width=25)
amsg.grid(row=1, column=1, padx=10, pady=5)

# Start/Stop Button
start = Button(root, text="Start Alarm", font=('Arial', 16), command=toggle_alarm, bg="#55FF55")
start.pack(pady=20)

# Create an indicator Label
indicator = Label(root, text="Alarm Off", font=('Arial', 16), bg="#FF5555", fg="white")
indicator.pack(pady=10)

# Quit button to close the application
quit_button = Button(root, text="Quit", font=('Arial', 16), command=root.quit, bg="#FF5555")
quit_button.pack(pady=10)

root.mainloop()
