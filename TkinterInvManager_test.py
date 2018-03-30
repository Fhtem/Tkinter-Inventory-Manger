# python 3 tkinter based player experience tracker
from tkinter import *
from tkinter import Radiobutton

inventory_a = { 'Kade' : {}, 'Nate' : {}, 'Neo' : {'pants' : 1,}, 'Will' : {'tesseract' : 1,}}


def add_item(inventory, player, item):
	inventory[player] += item
	
def button_appear(button, rw, col):
	button.grid(row=rw, column=col)


# defining tk window
invmng = Tk()
invmng.geometry('250x250')
invmng.title('Inventory Manager')

players = []
for char in inventory_a:
	players.append(char)

playerv = IntVar()
v_addItem = StringVar()

for count, player in enumerate(players):
	num = count + 1
	playerb = Radiobutton(invmng, text = player, variable = playerv, value = num, 
	command= lambda: button_appear(button_addItem, 0, 1))
	playerb.grid(row=count, column=0)
	
	button_addItem = Button(invmng, text='Add', command= lambda: add_item(inventory_a, player, v_addItem))
	entry_addItem = Entry(invmng, textvariable= v_addItem)


# run the thing	
invmng.mainloop()
