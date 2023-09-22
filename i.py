import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('best.pt')

# Open the video file
results=model('giphy1.gif',save=True)