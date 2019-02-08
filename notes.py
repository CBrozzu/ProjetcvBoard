from tkinter import *


class Animation:

    notes = []

    def __init__(self, notes):
        self.width = keys * 30
        self.height = 800

        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.checkered(30)
        self.rectList = []
        self.notes = notes

        self.start_anim
        self.init()
        self.root.mainloop()

    def start_anim(self):
        self.update()

    def checkered(self, line_distance):
        # vertical lines at an interval of "line_distance" pixel
        for x in range(line_distance, self.width, line_distance):
            self.canvas.create_line(x, 0, x, self.height, fill="#476042")
        # horizontal lines at an interval of "line_distance" pixel
        for y in range(line_distance, self.height, line_distance):
            self.canvas.create_line(0, y, self.width, y, fill="#476042")

    def init(self):

        for note in self.notes:
            self.rectList.append(note)

    def update(self):

        t = 20

        for i in range(len(self.notes)):
            xlist = self.particlelist[i]
            for note in notes:
                note.move()

        self.canvas.after(t, self.update)


class Note:

    channel = 0
    note = 0
    velocity = 0
    time = 0

    def __init__(self, channel, note, velocity, time, canvas):
        self.channel = channel
        self.note = note
        self.velocity = velocity
        self.time = time
        self.canvas = canvas
        self.shape = (self.canvas.create_rectangle(int(self.note), 50, int(self.note) + 30, 50 + int(self.time), fill="#476042"))

    def move(self):
        """
        Function for moving the shape.

            * "pos" gives a vector of position [x0, y0, x1, y1] where 0 is the left upper corner
              and 1 is the right down corner of the shape
        """

        self.canvas.move(self.shape, self.xspeed, 0)
        pos = self.canvas.coords(self.shape)

        if pos[0] >= screenwidth:     # returning the shape to the left side of the screen
            overlap = (pos[0] - screenwidth)
            self.canvas.coords(self.shape, gap-size+overlap, pos[1], gap+overlap, pos[3])


    def delete(self):
        """Function for deleting the shape"""

        self.canvas.delete(self.shape)


keys = 25  # later this will be guessed from the video

notes = [Note(0, 40, 100, 5), Note(0, 80, 100, 10), Note(0, 150, 100, 20)]
Animation(notes)
