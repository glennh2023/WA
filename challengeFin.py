import cv2
import numpy as np

# Calculateds the line of best fit and draws it
def draw_best_fit_line(points, image, color):
    # Get x and y components of coordinates
    x = points[:, 0]
    y = points[:, 1]

    # Perform "linear regression" (still kinda need to learn what that means) to get the slope and intercept for the line
    slope, intercept = np.polyfit(x, y, 1)

    # Calculate points for the best fit line
    start_point = (int(x.min()), int(slope * x.min() + intercept))
    end_point = (int(x.max()), int(slope * x.max() + intercept))

    # Draw best fitting line
    cv2.line(image, start_point, end_point, color, 2)
# For each contour, make sure it large enough to be a traffic cone
def filter_contours(contour):
    # Approximate the shape of the contour
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Use the contour area to filter out small false positives
    area = cv2.contourArea(contour)
    if area < 60:
        return

    # If the contour passes the simple filter, it's likely the red traffic cones (fingers crossed)
    # Draw the (green) contours to see if it worked (for testing)
    cv2.drawContours(result, [approx], 0, (0, 255, 0), 3)
    # compute the center of the contour
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print(str(cX)+","+str(cY))
    # Filter the lines based on if they are on the left or right side of the screen
    if(cX > width/2):
        right.append((cX,cY))
    else:
        left.append((cX, cY))
    # Optionally draw the center on the image
    cv2.circle(result, (cX, cY), 5, (255, 255, 0), -1)  # Draws a blue dot at the center

# Load the image and save its size
image = cv2.imread('red.png')
height,width = image.shape[:2]
# Display the image
cv2.imshow('Original', image)
# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#erode_image = cv2.erode(image, np.ones((5, 5), np.uint8) )
#erode_hsv_image = cv2.cvtColor(erode_image, cv2.COLOR_BGR2HSV)
cv2.imshow('test', hsv_image) #Just so I can see what the hsv looks like

# The range of color to detect in HSV (alot of trial/error)
lower_bound = np.array([0, 200, 180])  # Lower HSV boundary
upper_bound = np.array([255, 255, 255])  # Upper HSV boundary

# Threshold of the HSV image to get only the specified color
mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

# image = erode_hsv_image

# Bitwise-AND mask and original image
result = cv2.bitwise_and(image, image, mask=mask)

# Find the contours that could potentially correlate with the cones
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cone_centers = []
# Create a new image
image2 = cv2.imread('red.png')
# for contour in contours:
#     # Calculate the bounding rectangel of the current contour
#     x, y, w, h = cv2.boundingRect(contour)
    
#     # Calculate the center of the rectangle
#     center = (int(x + w / 2), int(y + h / 2))
#     cone_centers.append(center)
    
#     # Draw the center to see if it working
#     cv2.circle(result, center, 5, (0, 255, 0), -1)  # Drawing a green dot at the center
# Make a left and right array to store the coordinates of the cones on the left and right side of the screen
left = []
right = []
# Loop through all the contours and filter them
for contour in contours:
    filter_contours(contour);

print(left)
print(right)
#convert the arrays into numpy
left = np.array(left)
right = np.array(right)
#Draw the lines
draw_best_fit_line(left, image, (0,0,255))
draw_best_fit_line(right, image, (0,0,255))
#Resize the image so it can actually fit on my screen (so I can see the entire image)
scale_w = 2200 / width
scale_h = 1600 / height
scale = min(scale_w, scale_h)

# Calculate new dimensions
new_width = int(width * scale)
new_height = int(height * scale)

# Resize the image for my screen
image = cv2.resize(image, (new_width, new_height))
result = cv2.resize(result, (new_width, new_height))
# Display the image with center points
cv2.imshow('Centers', image)

# Display the answer image
cv2.imshow('Detected', result)

# Close everything on key press and save the result
cv2.waitKey(0)
cv2.imwrite("answer.png", image)
cv2.destroyAllWindows()
