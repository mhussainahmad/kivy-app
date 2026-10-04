# kivy-app

A Kivy desktop app that does face verification from a webcam using a Siamese neural network. It shows a live camera feed and, when you press **Verify**, compares the current frame against a set of stored reference images.

The model is trained in [mhussainahmad/face_detection](https://github.com/mhussainahmad/face_detection). This repository contains the app and a copy of the training notebook.

## How it works

- `faceid.py` builds a Kivy layout with three parts: a webcam image widget, a **Verify** button and a status label. It updates the camera image about 33 times a second, using a 250x250 crop of each OpenCV frame.
- On **Verify**:
  - The current crop is saved to `application_data/input_image/input_image.jpg`.
  - The crop is resized to 100x100 and scaled to [0, 1].
  - The model scores it against every image in `application_data/verification_images/`.
- A comparison counts as a match when its score is above `detection_threshold = 0.99`.
- The label shows **Verified** when the share of matches is above `verification_threshold = 0.8`.
- `layers.py` defines the custom `L1Dist` layer (absolute difference of the two embeddings), which is needed to load the saved Keras model.

## Repository layout

```
faceid.py                 Kivy app (camera feed, preprocessing, verification)
layers.py                 Custom L1Dist Keras layer
face_recognition.ipynb    Data collection and Siamese model training (local version of the face_detection notebook)
TODO.md                   Build checklist used while writing the app
```

## Getting started

These files are gitignored, so you need to provide them before running:

```
siamesemodel.h5                         # trained model, from the face_detection notebook
application_data/
  input_image/                          # the app writes the captured frame here
  verification_images/                  # reference photos of the person to verify
```

Then:

```bash
pip install kivy opencv-python tensorflow numpy
python faceid.py      # run from the repository root
```

No requirements file is included. The training notebook was run with TensorFlow 2.4.1.

`faceid.py` opens camera index 4 (`cv2.VideoCapture(4)`). On most machines the built-in webcam is index 0, so change that line if the feed is blank.

## Tech stack

Python, Kivy, OpenCV, TensorFlow/Keras.

## License

MIT. See [LICENSE](LICENSE).
