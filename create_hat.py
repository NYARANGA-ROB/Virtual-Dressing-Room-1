import numpy as np
import cv2

# Create a transparent image
img = np.zeros((200, 300, 4), dtype=np.uint8)

# Draw a black hat
cv2.ellipse(img, (150, 80), (100, 50), 0, 0, 360, (0, 0, 0, 255), -1)
cv2.rectangle(img, (50, 80), (250, 120), (0, 0, 0, 255), -1)

# Save the image
cv2.imwrite('data/data/Hat1.png', img)
print("Created Hat1.png in data/data/")
