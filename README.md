# apnr
WIP automatic number plate recognition (APNR) software for dashcams, using YOLOv5.
Main target is german / EU number plates, but ideally a lot of the code should work for all kinds of plates (especially the bounding box detection)

## number plate localization

The idea right now is to use the dataset [kaggle/andrewmvd/car-plate-detection](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection) and YOLOv5 to train a custom model. Ideally it should be small enough to run in realtime on a raspberrypi.

## OCR

Once the number plates are located, they need to be converted to text with some optical character recognition software, maybe tesseract.

To get a better reading, [github/goutamgmb/deep-burst-sr](https://github.com/goutamgmb/deep-burst-sr) could be used to upscale the plate from multiple frames of video.
