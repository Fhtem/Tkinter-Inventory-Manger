# python 3 tkinter based player experience tracker
from tkinter import *
from tkinter import Radiobutton

inventory_a = { 'Kade' : {}, 'Nate' : {}, 'Neo' : {'pants' : 1,}, 'Will' : {'tesseract' : 1,}}


def add_item(inventory, player, item):
	inventory[player] = item
	
def button_appear(button, rw, col):
	button.grid(row=rw, column=col)


# defining tk window
invmng = Tk()
invmng.geometry('250x250')
invmng.title('Inventory Manager')

# create list of players from inventory dictionary
players = []
for char in inventory_a:
	players.append(char)

# creates list of radiobuttons for players
playerv = IntVar()
playerv.set(1)
for count, player in enumerate(players):
	num = count + 1
	playerb = Radiobutton(invmng, text = player, variable = playerv, value = num, 
	command= lambda: button_appear(button_addItem, 0, 1))
	playerb.grid(row=count, column=0)

char = players[playerv.get()]

# entry box to put item name into
item_to_add = StringVar()
entry_addItem = Entry(invmng, textvariable= item_to_add)
entry_addItem.grid(row=0, column=2)

# button that adds item from entry box to inventory[player]
button_addItem = Button(invmng, text='Add Item', command= lambda: add_item(inventory_a, char, item_to_add.get()))
button_addItem.grid(row=0, column=1)







# run the thing	
invmng.mainloop()
