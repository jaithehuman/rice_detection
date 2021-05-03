# rice_detection
This project is use for detections of rice in an image or video capture using open-cv python

## Features
This program will determine ...
- Number of rice
- Size of each rice
- Categorized different types of rice

## Installation
First, clone this repository
```sh
git clone https://github.com/jaithehuman/rice_detection/

```
then install the requirements
```sh
cd rice_detection
pip install -r requirements.txt
```

## Usage
Run **image.py** to detect from dataset.

To use **webcam.py** you need a webcam and proper background to detect rice accurately. The webcam needs to be installed in a topview manner.

## Important
One measured object need to be placed at the top left position of an image. In from the dataset, I used a 20 mm coin. 
If you want to use different size objects, you have to change the following value...

```sh
pixelsPerMetric = dB / 0.787402  ## change 0.787 to the object size in inch unit
```
