# VidLabeller

VidLabeller is a simple UI that allows anyone to turn .mp4 files in to training data for object detection models.

## Creating training data

As an example, we consider contamination detection in recycling trucks. To begin we need a video that showcases the environment we ultimately want our model to detect objects in. Once the video is stored locally it can be opened in VidLabeller. As shown below, our UI allows you to easily transition between frames and label ROIs:

![Alt Text](./documentation/assets/use-case.gif)

## Using this training data

All ROIs and images are saved and ready for training. The following repo describes this training proces in detail (Coming soon). For inspiration, here is the output of a model trained using transfer learning and data produced by VidLabeller.

![Alt Text](./documentation/assets/model-in-action.gif)
