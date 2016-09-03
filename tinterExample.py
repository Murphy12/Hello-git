import tkinter
import turtle
import sys

def main():
    root = tkinter.Tk()

    cv = tkinter.Canvas(root, width=600, height=600)# create wigit for drawing

    #control layout through packing
    cv.pack(side =tkinter.LEFT)
    #change title
    root.title('Drawing Board')

    #creating a turtle

    t = turtle.RawTurtle(cv)# make turtle use this drawing board
    screen = t.getscreen()
    screen.setworldcoordinates(0,0,600,600)
    # creating another wigit for buttons
    frame = tkinter.Frame(root)
    # packing like above
    frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)# fills left and right
    screen.tracer(0)#prevents stack overflow
    #create quit button

    def quitHandler(): #event handler function
        print('GoodBye')
        sys.exit(0)
    quitButton = tkinter.Button(frame, text='Quit',command=quitHandler)#event handler function
    quitButton.pack()

    textLable = tkinter.Label(frame,text='Text to write!')
    textVar = tkinter.StringVar()
    textVar.set('Hello World!')
    textEntry = tkinter.Entry(frame,textvariable=textVar)
    textEntry.pack()

    def writeHandler(): #event handler function

        t.write(textVar.get())
    writeButton = tkinter.Button(frame, text='Write',command=writeHandler)#event handler function
    writeButton.pack()


      #event handler which will respond to mouse clicks on screen
    def clickHander(x,y):
         t.goto(x,y)
         screen.update() # helps to up date so no stack overflow

    screen.onclick(clickHander)

    #free hand drawing

    def dragHandndler(x,y):
        t.goto(x,y)
        screen.update()
    t.ondrag(dragHandndler)





    tkinter.mainloop()


if __name__ == "__main__" :
    main()