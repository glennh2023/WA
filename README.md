# WA PERCEPTIONS Coding Challenge Introduction
After an EMBARRASSINGLY long time googling and geeksforgeeking what I need to know to complete the challenge, I came to the following solution: 
<ol>
  <li>Read in the image and convert it to HSV Color space</li>
  <li>Fiddled with the lower bound and upper bound of the color range for the mask to filter</li>
  <li>Got the contours of the image and filtered it so that only cones remain</li>
  <li>Got the center of these contours and sorted if they were on the left side of the screen, or right</li>
  <li>Drew a line of best fit for each side of the screen</li>
</ol>

Anyway, here is what my before/after looks like:
Original Image            |  sample answer.png
:-------------------------:|:-------------------------:
![](https://github.com/WisconsinAutonomous/CodingChallenges/blob/master/perception/red.png)  |  ![](https://github.com/glennh2023/WA/blob/main/answer.png)

*\*Ignore the difference in image size, I rescaled it so that it can fit on my laptop screen (so I can see the results)*

## Libraries Used
OpenCV
Numpy

## What I've Tried
I've tried isolating the cones using simple HSV transformations, erosions, etc. in order to try and isolate the cones. After asking Pravin for a hint, he mentioned looking into contours and I came up with my current solution from there

## Solution I wish I had time to implement
When I was learning how to detect the cones, I came across the concept of "Haar-like Features". If I had more time, I would've implemented this solution as it seems cooler (and less crude) than just manually fiddling with HSV values and basic contours to detect the bright red cones.
