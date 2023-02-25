from tkinter import *

root = Tk()

enter_1 = Entry(root, width=25, borderwidth=5,)
enter_2 = Entry(root, width=25, borderwidth=5)


def my_click():
	my_label_1 = Label(root, text=enter_1.get())
	my_label_2 = Label(root, text=enter_2.get())
	my_label_1.pack()
	my_label_2.pack()


myButton = Button(root, text="Submit", command=my_click, padx=10)

enter_1.pack()
enter_2.pack()
myButton.pack()

root.mainloop()
