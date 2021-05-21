from tkinter import *
import random

top = Tk()
playlist = []
myRolls = []
dieType = 0
rollTimes = 0
myList = []
Unique_list = 0

   
def printList():
    print(playlist)

def exportList():
    with open('test.txt', 'w') as f:
        for item in playlist:
            f.write("%s\n" % item)


def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def printLists():
    if len(unique_list) == 0:
        print(myList)

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "Week 1", bg = "cyan", command = week1)
    B1Main.grid(column = 0, row = 2)
    B2Main = Button(text = "Week 2", bg = "cyan", command = week2)
    B2Main.grid(column = 0, row = 3)
    B3Main = Button(text = "Week 3", bg = "cyan")
    B3Main.grid(column = 0, row = 4)
    
def week1():
    clearWindow()
    def results():
        result = E1.get()
        playlist.append(result)
        E1.delete(0, END)
        
    # This is a Label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row = 1)

    # This is an Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row = 2)

    #This is a Button widget
    B1 = Button(text= " +  ", bg = "green", command = results)
    B1.grid(column = 1, row = 2)

    B2 = Button(text = " Print ", bg = "light blue", command = printList)
    B2.grid(column = 2, row = 2) 

    B3 = Button(text = "Export List", bg = "grey", command = exportList)
    B3.grid(column = 0, row = 3)

    Bexit = Button(text = "Clear Window", bg = "red", command = mainMenu)
    Bexit.grid(column = 1, row = 3)

def week2():
    def rollDice():
        #update variable data
        dieType =E2Week2.get()
        rollTimes = E1Week2.get()
        #clear window AFTER updating variables
        clearWindow()
        #roll thee dice
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        #build the results window
        L4Week2 = Label(top, text = "Here's your rolls!")
        L4Week2.grid(column = 0, row = 1)
        
        L5Week2 = Label(top, text = "{}".format(myRolls))
        L5Week2.grid(column = 0, row = 2)
        
        B2Week2 = Button(text = "Main Menu", bg = "orange", command = mainMenu)
        B2Week2.grid(column = 0, row = 3)





    clearWindow()
    B1Week2 = Button(text = "Roll em!", bg = "green", command = rollDice)
    B1Week2.grid(column = 2, row = 4)
    
    L1Week2 = Label(top, text = "Dice Roller App")
    L1Week2.grid(column = 2, row = 1)
    
    L2Week2 = Label(top, text = "# of Rolls")
    L2Week2.grid(column = 0, row = 2)
    
    L3Week2 = Label(top, text = "# of Sides")
    L3Week2.grid(column = 3, row = 2)
    
    E1Week2 = Entry(top, bd = 5)
    E1Week2.grid(column = 0, row = 3)
    
    E2Week2 = Entry(top, bd = 5)
    E2Week2.grid(column = 3, row = 3)


def week3():
    def printLists():
        unique_list = E3Week3.get()
        myList = E3Week3.get()
        clearWindow()
        whichOne = input("Which list do you want to see? Sorted or un-Sorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        
       

    L1Week3 = Label(top, text = "Printed List")
    L1Week3.grid(column = 0, row = 1)
        
    L2Week3 = Label(top, text = "{}".format(myList))
    L2Week3.grid(column = 0, row = 2)
        
    B1Week3 = Button(text = "Main Menu", bg = "green", command = mainMenu)
    B1Week3.grid(column = 0, row = 3)

    clearWindow()
    B1Week3 = Button(text = "print em!", bg = "blue", command = printLists)
    B1Week3.grid(column = 2, row = 4)
    
    L1Week3 = Label(top, text = "Printed Lists")
    L1Week3.grid(column = 2, row = 1)
    
    L2Week3 = Label(top, text = "Sorted Lists")
    L2Week3.grid(column = 0, row = 2)
    
    L3Week3 = Label(top, text = "Un-Sorted Lists")
    L3Week3.grid(column = 3, row = 2)
    
    E1Week3 = Entry(top, bd = 5)
    E1Week3.grid(column = 0, row = 3)
    
    E2Week3 = Entry(top, bd = 5)
    E2Week3.grid(column = 3, row = 3)


   



if __name__ == "__main__":
    mainMenu()
    top.mainloop()
