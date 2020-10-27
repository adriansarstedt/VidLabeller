from ui import VidUI
import os

vidPath = 'data/sample-vids/side-loader.mp4'

if os.path.exists(vidPath):
    v = VidUI(vidPath)
    v.open()
else:
    print(f'Cannot find file with path: {vidPath}')