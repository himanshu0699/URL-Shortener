from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root = Tk()
root.title("Alarm Clock")
root.geometry("550x350")
root.configure(bg="#000000")  # Set the root window background to black

mixer.init()

# Create a variable to track the alarm status (on/off)
alarm_on = False

def toggle_alarm():
    global alarm_on
    if not alarm_on:
        alarm_on = True
        indicator.config(text="Alarm On", bg="green", fg="white")  # Update text and color
        th = threading.Thread(target=a, args=())
        th.start()
    else:
        alarm_on = False
        indicator.config(text="Alarm Off", bg="red", fg="white")  # Update text and color

def a():
    a = hr.get()
    if a == "":
        msg = messagebox.showerror('Invalid data', 'Please enter valid time')
    else:
        Alarmtime = a
        CurrentTime = time.strftime("%H:%M")

        while Alarmtime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")

        if Alarmtime == CurrentTime:
            mixer.music.load(
                r'C:\Users\Himanshu\Desktop\Internship\ALARM CLOCK\code\tone.mp3')
            mixer.music.play()
            msg = messagebox.showinfo('It is time', f'{amsg.get()}')
            if msg == 'ok':  # Use lowercase 'ok'
                mixer.music.stop()
                alarm_on = False
                indicator.config(text="Alarm Off", bg="red", fg="white")

header = Frame(root, bg="#000000")  # Set the header background to black
header.place(x=5, y=5)

head = Label(root, text="ALARM CLOCK", font=('comic sans', 20), bg="#000000", fg="white")  # Set text and foreground color
head.pack(fill=X)

panel = Frame(root, bg="#000000")  # Set the panel background to black
panel.place(x=5, y=70)

alpp = PhotoImage(
    file=r'C:\Users\Himanshu\Desktop\Internship\ALARM CLOCK\code\al.png')

alp = Label(panel, image=alpp, bg="#000000")  # Set the label background to black
alp.grid(rowspan=4, column=0)

atime = Label(panel, text="   Alarm Time \n   HH:MM \n24 Hour Format", font=('comic sans', 18), bg="#000000", fg="white")  # Set text and foreground color
atime.grid(row=0, column=1, padx=10, pady=5)

hr = Entry(panel, font=('comic sans', 20), width=5)
hr.grid(row=0, column=2, padx=10, pady=5)

amessage = Label(panel, text=" Alarm Message", font=('comic sans', 20), bg="#000000", fg="white")  # Set text and foreground color
amessage.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

amsg = Entry(panel, font=('comic sans', 15), width=25)
amsg.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

start = Button(panel, text="Start alarm", font=('comic sans', 20), command=toggle_alarm)
start.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

# Create an indicator Label
indicator = Label(root, text="Alarm Off", font=('comic sans', 14), bg="red", fg="white")
indicator.pack(side=BOTTOM, padx=10, pady=10, anchor="sw")  # Position the indicator at the bottom left

# Quit button to close the application
quit_button = Button(root, text="Quit", font=('comic sans', 16), command=root.quit,bg="red", fg="white")
quit_button.place(relx=1.0, rely=1.0, anchor="se")  # Position the button at the bottom right

root.mainloop()
