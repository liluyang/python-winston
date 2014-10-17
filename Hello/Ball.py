from Tkinter import *

import random
import time

class Ball:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
    self.canvas.move(self.id, 245, 100)
    starts = [-3, -2, -1, 1, 2, 3]
    random.shuffle(starts)
    self.x = starts[0]
    self.y = -3
    self.canvas.height = self.canvas.winfo_height()
    self.canvas.width = self.canvas.winfo_width()

  def draw(self):
    self.canvas.move(self.id, 0, -1)
    pos = self.canvas.coords(self.id)
    if pos[1] <= 0:
      self.y = 1
    if pos[3] >= self.canvas.height:
      self.y = -1
    if pos[0] <= 0:
      self.y = -3
    if pos[2] >= self.canvas_width:
      self.x = -3

tk = Tk()
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
tk.update()
ball = Ball(canvas, 'red')

while 1:
  ball.draw()
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)
