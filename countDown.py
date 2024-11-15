

import time

from tkinter import *

from tkinter import messagebox

 

root = Tk()

root.geometry("1080x2130+0+0")

root.overrideredirect(True)

root.config(bg="black")



hour=StringVar()

minute=StringVar()

second=StringVar()



hour.set("00")

minute.set("00")

second.set("00")



hourEntry= Entry(root,bd=0, fg="red",bg="black",width=3, font=("Arial",45,"bold"),textvariable=hour)

hourEntry.place(x=50,y=300,width=300,height=300)



minuteEntry= Entry(root,bd=0, fg="red",bg="black", width=3, font=("Arial",45,"bold"),textvariable=minute)

minuteEntry.place(x=400,y=300,width=300,height=300)



secondEntry= Entry(root,bd=0, fg="red",bg="black", width=3, font=("Arial",45,"bold"),textvariable=second)

secondEntry.place(x=750,y=300,width=300,height=300)



def submit():

	try:

		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())

		

	except:

		print("Please input the right value")

		

	while temp >-1:

	    mins,secs = divmod(temp,60) 

	    hours=0

	    

	    if mins >60:

	    	hours, mins = divmod(mins, 60)

	    	

	    hour.set("{0:2d}".format(hours))

	    minute.set("{0:2d}".format(mins))

	    second.set("{0:2d}".format(secs))

	    

	    root.update()

	    time.sleep(1)

	    

	    if (temp == 0):

	    	messagebox.showinfo("Time Countdown", "Time\'s Up Stop")

	    temp -= 1

	    

btn = Button(root,font=("Arial",8,"bold"),bg="black" ,fg="yellow",text='Start Countdown', bd='5',command= submit)

btn.place(x = 320,y = 800)




root.mainloop()