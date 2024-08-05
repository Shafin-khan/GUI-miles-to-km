from tkinter import *
windw = Tk()
windw.title('Mile to Kilometer')
windw.minsize(width=500, height=400)
#Entry

mile_input = Entry(width=10)

mile_input.place(x=200, y=50)

#Label
miles = Label(text='Miles')
miles.place(x=250, y=50)

equal = Label(text='is equal to')
equal.place(x=140, y=80)

mile_output = Label(text="0")
mile_output.place(x=200, y=80)

km = Label(text='km')
km.place(x=250, y=80)

def mile_to_Km():
    mile = float(mile_input.get())
    km = (mile*1.60934)
    mile_output.config(text=f"{round(km,2)}")

calculate = Button(text='Calculate', command= mile_to_Km)
calculate.place(x=200, y=120)

windw.mainloop()