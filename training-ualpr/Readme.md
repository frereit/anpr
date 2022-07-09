# Training: UALPR

This directory is meant to contain scripts for training from [UALPR](https://github.com/DoubangoTelecom/ultimateALPR-SDK)

The setup should be:

- `/app/input` should be volume mounted to folders full of videos and images. It will recursively go through all the folders. For videos it will take a frame every 5 seconds.
- `/app/tmp` will contain the frames from the current video. Pictures will be analysed directly.
- `/app/output/positive` will contain positive samples. numbered jpgs and the matching json file with the output from the ualpr recognizer.
- `/app/output/negative` will contain negative samples. Also numbered jpgs, but no accomodating json file.

```
docker build -t ghcr.io/jm-lemmi/anpr-training-ualpr .
docker run -v C:\Users\julian.lemmerich\Github\anpr\example-videos:/app/input --rm -it ghcr.io/jm-lemmi/anpr-training-ualpr
```