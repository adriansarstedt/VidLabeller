# VidLabeller

VidLabeller is a simple UI that allows anyone to turn .mp4 files in to training data for object detection models.

## Setup

### Python Version

In order run VidLabeller locally you must ensure a python3 environment set up and active. This can be done using conda or virtualenv. Once this environment is active `python --version` should return `Python 3.6.10`.

### Dependencies

This package is built using matplotlib graphics and OpenCV video processing. In order to ensure these dependencies are installed run the following command in your bash:

    pip install dependencies.txt

## Creating training data

As an example, we consider contamination detection in recycling trucks. To begin we need a video that showcases the environment we ultimately want our model to detect objects in. Once the video is stored locally it can be opened in VidLabeller. As shown below, our UI allows you to easily transition between frames and label ROIs:

![Alt Text](./documentation/gifs/use-case.gif)

## Using this training data

All ROIs and images are saved and ready for training. The following repo describes this training proces in detail (Coming soon). For inspiration, here is the output of a model trained using transfer learning and data produced by VidLabeller.

![Alt Text](./documentation/gifs/model-in-action.gif)
