import matplotlib.pyplot as plt

def drawRect(ax, x1, y1, x2, y2):
    xs, ys = [x1, x1, x2, x2, x1], [y1, y2, y2, y1, y1]
    ax.plot(xs, ys, 'b--o')

class Canvas:
    def __init__(self, fig, ax):
        self.mouseClicked = False
        self.fig, self.ax = fig, ax
        self.fig.canvas.mpl_connect('button_press_event', self.onPress)
        self.fig.canvas.mpl_connect('motion_notify_event', self.onMove)
        self.fig.canvas.mpl_connect('button_release_event', self.onRelease)

    def open(self, image):
        self.image = image
        self.rois = []
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0

        self.refresh()
        plt.show()

    def close(self):
        plt.close()

    def refresh(self):
        self.ax.clear()
        self.ax.imshow(self.image)
        self.drawRois()
        self.fig.canvas.draw()

    def drawRois(self):
        for roi in self.rois:
            drawRect(self.ax, *roi)
        if (self.mouseClicked):
            drawRect(self.ax, self.x1, self.y1, self.x2, self.y2)

    def onPress(self, event):
        self.mouseClicked = True
        self.x1, self.y1 = round(event.xdata), round(event.ydata)
        self.x2, self.y2 = self.x1, self.y1

    def onMove(self, event):
        if (self.mouseClicked):
            self.x2, self.y2 = round(event.xdata), round(event.ydata)
            self.refresh()

    def onRelease(self, event):
        self.mouseClicked = False
        self.rois.append([self.x1, self.y1, self.x2, self.y2])
        self.refresh()