from ui import VidUI
import os

vidPath = 'data/sample-vids/side-loader.mp4'
outputName = 'side-loader-labels.json'

if os.path.exists(vidPath):
    path = vidPath.split("/")
    outputPath = "/".join(path[:-1]+[outputName])

    v = VidUI(vidPath, outputPath)
    v.open()
else:

    print(f'Cannot find file with path: {vidPath}')