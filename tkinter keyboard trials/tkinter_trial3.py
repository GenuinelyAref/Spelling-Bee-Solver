from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = Tk()
root.title('Keyboard')
root.configure(background='black')


class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, corner_radius, padding, color, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
                           relief="flat", highlightthickness=0)
        self.command = command

        """
        if corner_radius > 0.5 * width:
            print("Error: corner_radius is greater than width.")
            return None

        if corner_radius > 0.5 * height:
            print("Error: corner_radius is greater than height.")
            return None
        """

        rad = 2 * corner_radius

        def shape():
            self.create_polygon((padding, height - corner_radius - padding, padding, corner_radius + padding,
                                 padding + corner_radius, padding, width - padding - corner_radius, padding,
                                 width - padding, corner_radius + padding, width - padding,
                                 height - corner_radius - padding, width - padding - corner_radius, height - padding,
                                 padding + corner_radius, height - padding), fill=color, outline=color)
            self.create_arc((padding, padding + rad, padding + rad, padding), start=90, extent=90, fill=color,
                            outline=color)
            self.create_arc((width - padding - rad, padding, width - padding, padding + rad), start=0, extent=90,
                            fill=color, outline=color)
            self.create_arc((width - padding, height - rad - padding, width - padding - rad, height - padding),
                            start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding, height - padding - rad, padding + rad, height - padding), start=180, extent=90,
                            fill=color, outline=color)

        id = shape()
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1 - x0)
        height = (y1 - y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()


def test():
    print("Hello")


canvas = Canvas(root, height=280, width=910)
canvas.pack()

# mytext = canvas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",text="Click the bubbles that are multiples of two.")
button = RoundedButton(root, 80, 80, 10, 0, 'red', command=test)
button.place(x=10, y=10)

button_two = RoundedButton(root, 80, 80, 10, 0, 'green', command=test)
button_two.place(x=100, y=10)

button_three = RoundedButton(root, 80, 80, 10, 0, 'blue', command=test)
button_three.place(x=190, y=10)

button_four = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_four.place(x=280, y=10)

button_five = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_five.place(x=370, y=10)

button_six = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_six.place(x=460, y=10)

button_seven = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_seven.place(x=550, y=10)

button_eight = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_eight.place(x=640, y=10)

button_nine = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_nine.place(x=730, y=10)

button_ten = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_ten.place(x=820, y=10)

# 2nd row

button_eleven = RoundedButton(root, 80, 80, 10, 0, 'green', command=test)
button_eleven.place(x=55, y=100)

button_twelve = RoundedButton(root, 80, 80, 10, 0, 'blue', command=test)
button_twelve.place(x=145, y=100)

button_thirteen = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_thirteen.place(x=235, y=100)

button_fourteen = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_fourteen.place(x=325, y=100)

button_fifteen = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_fifteen.place(x=415, y=100)

button_sixteen = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_sixteen.place(x=505, y=100)

button_seventeen = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_seventeen.place(x=595, y=100)

button_eighteen = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_eighteen.place(x=685, y=100)

button_nineteen = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_nineteen.place(x=775, y=100)

# 3rd row


button_twenty = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_twenty.place(x=145, y=190)

button_twenty_one = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_twenty_one.place(x=235, y=190)

button_twenty_two = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_twenty_two.place(x=325, y=190)

button_twenty_three = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_twenty_three.place(x=415, y=190)

button_twenty_four = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_twenty_four.place(x=505, y=190)

button_twenty_five = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_twenty_five.place(x=595, y=190)

button_twenty_six = RoundedButton(root, 80, 80, 10, 0, 'yellow', command=test)
button_twenty_six.place(x=685, y=190)

# mylabel = canvas.create_text((400, 190), text="Label text")
# mylabel.lift()
"""
canvas.tag_raise(canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold')))


# img = PhotoImage(file="try_two.png")
# canvas.tkraise(canvas.create_image(20,20, anchor=NW, image=img))
line = canvas.create_line(10, 10, 200, 50, 90, 150, 50, 80)
canvas.tag_raise(line)
"""

"""img = ImageTk.PhotoImage(Image.open('try_two.png'))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")"""

root.mainloop()
