from tkinter import *

window = Tk()
window.title("Miles To Km Converter")
window.config(padx=20,pady=20)
# window.minsize(width=300,height=100)

#label1
label1 = Label(text="Miles")
label1.grid(column=2,row=0)

#label2
label2 = Label(text="is equal to")
label2.grid(column=0,row=1)

#label3
label3 = Label(text="Km")
label3.grid(column=2,row=1)
#label4
label4 = Label(text="0")
label4.grid(column=1,row=1)
#entry
input = Entry(width=5)
input.insert(END,"0")
input.grid(column=1,row=0)

#button
def button_used():
    inp = int(input.get())
    res = round(inp*1.6)
    label4.config(text=res)
button = Button(text="Calculate",command=button_used)
button.grid(column=1,row=2)




window.mainloop()