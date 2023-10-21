'''
    The game does not need this file to run. This is simply to display the highscore board.
'''
import csv
from tkinter import *
from tkinter import ttk

def scores():
    global root
    try:
        root.destroy()
    except:
        pass
    f = open("Highscores.csv" , 'r')
    r = list(csv.reader(f))
    f.close()
    root = Tk()
    root.geometry("800x400+400+200")
    root['bg'] = 'black'

    style = ttk.Style()
    style.configure("Treeview")
    style.theme_use("clam")
    if len(r) %2:
        color = "grey"
    else:
        color = 'silver'
    style.configure("Treeview" , font = "Consolas" , background = "silver" ,foreground = "red" , rowheight = '35', fieldbackground = color )
    style.map("Treeview" , background = [('selected' , 'black')])
    style.configure("Horizontal.TScrollbar" , background = "grey" , foreground = "black")

    frame = Frame(root , background = "black")
    

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side = RIGHT , fill = Y)

    tree = ttk.Treeview(frame , height = 5 , yscrollcommand = scrollbar.set , selectmode = 'browse')
    tree['columns'] = ("Name" , "Email ID" , "Highscore1" , "Highscore2" , "Highscore3")

    scrollbar.config(command = tree.yview)

    tree.column("#0" , width = 0 , minwidth = 0)
    tree.column("Name" , anchor = CENTER , width = 120 , minwidth = 120)
    tree.column("Email ID" , anchor = CENTER , width = 300 , minwidth = 300)
    tree.column("Highscore1" , anchor = CENTER , width = 120 , minwidth = 120)
    tree.column("Highscore2" , anchor = CENTER , width = 120 , minwidth = 120)
    tree.column("Highscore3" , anchor = CENTER , width = 120 , minwidth = 120)

    tree.heading("Name" , text = "Username" , anchor = CENTER)
    tree.heading("Email ID" , text = "Email ID" , anchor = CENTER)
    tree.heading("Highscore1" , text = "Journey of Curiosity" , anchor = CENTER)
    tree.heading("Highscore2" , text = "Path to Eternity" , anchor = CENTER)
    tree.heading("Highscore3" , text = "Test of Destiny" , anchor = CENTER)

    tree.tag_configure("oddrow" ,background =  'grey')
    tree.tag_configure("evenrow" ,background =  'silver')


    
    for i in r[1:]:
        if i[2] == '':
            _2 = '-'
        else:
            _2 = str(i[2])+' s' 
        if i[3] == '':
            _3 = '-'
        else:
            _3 = str(i[3])+' s' 
        if i[4] == '':
            _4 = '-'
        else:
            _4 = str(i[4])+' s' 
        if r.index(i) % 2:
            color = 'oddrow'
        else:
            color = 'evenrow'

        tree.insert(parent = '' ,index = 'end' , iid = r.index(i) , text = '', values = (i[0],i[1] ,_2 , _3,_4 ) , tags = (color,))

    lab = Label(root, text="HIGHSCORES", bg="black", fg="red", font=("Comic Sans MS", 20 , "bold"))
    lab.pack()
    tree.pack()
    frame.pack(pady = 10 )
    quitb = Button(root, text="EXIT", font=("Comic Sans MS", 20 , 'bold'), bg="black", fg="red", command=root.destroy)
    quitb.pack(pady = 20)

    root.mainloop()

if __name__ == "__main__":
    scores()
