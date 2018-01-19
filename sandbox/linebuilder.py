r"""A simple line segment is created every time a mouse is pressed
"""
from matplotlib import pyplot as plt


class LineBuilder:
    r"""Instances of this class are callable through __call__"""

    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        # The callback registry is an attribute of FigureCanvasBase,
        # thus we need to fetch the canvas to create the connection
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
line, = ax.plot([0], [0])  # initialize the line as an empty line
line_builder = LineBuilder(line)

plt.show()