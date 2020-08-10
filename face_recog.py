import cv2
import time
import async

variable = 0

# Load the cascade
face_cascade = cv2.CascadeClassifier('stuff.xml')
# Read the input image
img = cv2.imread('test2.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    variable += 1

print(str(variable) + " People detected")

cv2.imshow('img', img)
cv2.waitKey()

