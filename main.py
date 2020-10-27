import os
import argparse

from src.ui import VidUI

parser = argparse.ArgumentParser(description='VidLabeller: Quick and easy training data from videos.')
parser.add_argument(
    '--videoPath', '-v', type=str, default='data/sample-vids/side-loader.mp4', help='Path of mp4 file you would like to label')
parser.add_argument(
    '--outputPath', '-o', type=str, default='data/outputs/', help='Path of directory you would like outputs to be stored in')

args = parser.parse_args()

if os.path.exists(args.videoPath):
    if not os.path.exists(args.outputPath):
        os.mkdir(args.outputPath)
    v = VidUI(args.videoPath, args.outputPath)
    v.open()
else:
    print(f'Cannot find file with path: {args.videoPath}')