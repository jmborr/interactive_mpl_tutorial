r"""Connecting a mouse event to a callback function
"""

from __future__ import print_function, absolute_import


# This may be required if you are on a Mac and default to using OSX as
# your backend
# import matplotlib
# matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
import numpy as np

last_ev = None


def event_printer(event):
    """Helper function for exploring events.

    Prints all public attributes +
    """
    # capture the last event
    global last_ev
    last_ev = event
    for k, v in sorted(vars(event).items()):
        print('{}: {!r}'.format(k, v))
    print('-'*25)


th = np.linspace(0, 2*np.pi, 64)
fig, ax = plt.subplots()

# the `picker=5` kwarg turns on pick-events for this artist
# if clicked at a distance < 5 points from the artist
ax.plot(th, np.sin(th), 'o-', picker=5)

# - The callback registry is an attribute of FigureCanvasBase,
#   thus we need to fetch the canvas to create the connection
# - pick_event is one of the built-in event names
#   https://matplotlib.org/users/event_handling.html
# - cid : Connection ID, uniquely defines an event:callback pair
cid = fig.canvas.mpl_connect('pick_event', event_printer)

plt.show()
fig.canvas.mpl_disconnect(cid)


"""EXERCISE
Add additional connections to the canvas by connecting all 'active' events
to event_printer.
Active events: ['button_press_event', 'button_release_event', 'scroll_event',
                'key_press_event', 'key_release_event', 'pick_event']
"""

