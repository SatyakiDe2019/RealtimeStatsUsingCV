# Restore old video with Python

## About this app

This computer-vision app will visually read the number of stacked-up coins & based on that it will show the numbers in real-time. Anyone, can add or remove coins to reflect the true number. This is especially very useful for real-time stocks tracking purposes. This application developed using Open-CV. This project is for the intermediate Python developer & Data Science Newbi's.


## How to run this app

(The following instructions apply to Posix/bash. Windows users should check
[here](https://docs.python.org/3/library/venv.html).)

First, clone this repository and open a terminal inside the root folder.

Create and activate a new virtual environment (recommended) by running
the following:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the model Visual Reading-App:

```bash
python visualDataRead.py
```

Make sure that you are properly connected with a functional WebCam (Preferably a separate external WebCam) & mount that at a pre-defined distance from the subjects.

## Screenshots

![demo.GIF](demo.GIF)

## Resources

- To learn more about Open-CV, check out our [documentation](https://opencv.org/opencv-free-course/).
