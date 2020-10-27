# VidLabeller

VidLabeller is a simple UI that allows anyone to turn .mp4 files in to training data for object detection models.

## Setup

### Python

In order run VidLabeller locally you must ensure a python3 environment is set up and active. This can be done using conda or virtualenv. Once this environment is active `python --version` should return `Python 3.6.10`.

### Dependencies

This package is built using matplotlib graphics and OpenCV video processing. In order to ensure these dependencies are installed run the following command in your bash:

    pip install dependencies.txt

## Creating training data

Once dependencies have been istalled its simple, just run:

    python main.py --videoPath <mp4 path> --outputPath <output directory path>

As an example, we consider contamination detection in recycling trucks. In order to explore simply run:

    python main.py

As shown below the UI that is launched allows you to easily transition between frames and label ROIs:

![Alt Text](./documentation/gifs/use-case.gif)

## Using this training data

All ROIs and images are saved and ready for training. The following repo describes this training proces in detail (Coming soon). For inspiration, here is the output of a model trained using transfer learning and data produced by VidLabeller.

![Alt Text](./documentation/gifs/model-in-action.gif)
