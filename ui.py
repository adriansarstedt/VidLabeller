import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import cv2

from canvas import Canvas
from transform import saveRoiData

class VidUI:
    def __init__(self, videoPath, outputPath):
        self.outputPath = outputPath
        self.vidcap = cv2.VideoCapture(videoPath)

        self.frame = 0
        self.speed = 100
        self.rois = {}

        self.fig = plt.figure(figsize=(10, 6))
        self.imageAx = self.fig.add_subplot(111)
        self.canvas = Canvas(self.fig, self.imageAx)

        plt.subplots_adjust(bottom=0.2)

        self.axs = []
        self.btns = []

        btnTemplates = {
            "Speed x1": self.setSpeed(1),
            "x2": self.setSpeed(2),
            "x4": self.setSpeed(4),
            'x10': self.setSpeed(10),
            'x100': self.setSpeed(100),
            "x1000": self.setSpeed(1000),
            "Save & Next": self.nextFrame,
            "Skip": self.skip,
            "Quit": self.quit,
        }
        buttonOffset = 0.5 - len(btnTemplates) * 0.05

        for i, (label, callback) in enumerate(btnTemplates.items()):
            self.axs.append(plt.axes([buttonOffset+i*0.1, 0.05, 0.09, 0.075]))
            self.btns.append(Button(self.axs[i], label))
            self.btns[i].on_clicked(callback)

        self.SET_FRAME_CONSTANT = 1
        self.setTitle()

    def setTitle(self):
        totalFrames = int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fig.suptitle(
            f'Frame {self.frame}/{totalFrames} : Speed = {self.speed} : Labbeled frames = {len(self.rois)}', 
            fontsize=16
        )

    def setSpeed(self, speed):
        def setSpeed(event):
            self.speed = speed
            self.setTitle()
        return setSpeed


    def nextFrame(self, event):
        self.rois[self.frame] = self.canvas.rois
        self.frame += self.speed
        self.setTitle()
        self.save()
        self.open()

    def skip(self, event):
        self.frame += self.speed
        self.setTitle()
        self.open()

    def save(self):
        saveRoiData(self.rois, self.outputPath+"ROIs.json")
        cv2.imwrite(self.outputPath+"frame%d.jpg" % self.frame, self.image)
        self.setTitle()
        print(self.rois)

    def quit(self, event):
        plt.close()

    def open(self):
        self.vidcap.set(self.SET_FRAME_CONSTANT, self.frame)
        success, self.image = self.vidcap.read()
        self.canvas.open(self.image)

