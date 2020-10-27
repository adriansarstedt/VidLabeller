from ui import VidUI
import os

vidPath = 'data/sample-vids/side-loader.mp4'
outputPath = 'data/outputs/'

if os.path.exists(vidPath):
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)
    v = VidUI(vidPath, outputPath)
    v.open()
else:
    print(f'Cannot find file with path: {vidPath}')