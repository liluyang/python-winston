from Tkinter import *

class Application(Frame):
  def say_hi(self):
    print "hi there, everyone!"

  def createWidgets(self):
    frame = Frame(self)
    frame.pack()

    bottomframe = Frame(self)
    bottomframe.pack(side=BOTTOM)

    self.TEXTAREA = Text(frame, height=2, width=30)
    self.TEXTAREA.pack()
    self.TEXTAREA.insert(END, "Hello! Winston & Sophia\nHow's your summer time?\n")
        
    self.TEXTAREA.pack(side=TOP)
      
    self.QUIT = Button(bottomframe)
    self.QUIT["text"] = "QUIT"
    self.QUIT["fg"] = "red"
    self.QUIT["command"] = self.quit

    self.QUIT.pack(side=LEFT)

    self.hi_there = Button(bottomframe)
    self.hi_there["text"] = "Hello",
    self.hi_there["command"] = self.say_hi

    self.hi_there.pack(side=LEFT)

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
