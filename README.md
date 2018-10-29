# Computer Vision Preseason Final Project
### Project Guidelines
Create a fully polished and shippable program that utilizes image processing techniques to calculate **distance**, **azimuth**, and **altitude** of a plus shape (+) target. Program must be written in Python 3 and use OpenCV, NumPy, and other relevant libraries for processing.

### Grading Rubric
**Functionality (50%)** and **Style (50%)**

| |Poor|Adequate|Excellent|
|-|-|-|-|
|**Detection<br>(30%)**        |**(10%)**<br>Unable to detect target|**(20%)**<br>Able to detect target sporadically|**(30%)**<br>Able to detect target consistently|
|**Analysis<br>(20%)**         |**(5%)**<br>Calculate with 50% accuracy|**(15%)**<br>Calculate with 20% accuracy|**(20%)**<br>Calculate with 5% accuracy|
|**Structure<br>(20%)**        |**(5%)**<br>No structure|**(15%)**<br>Incorrect structure|**(20%)**<br>Proper structure|
|**Naming Convention<br>(15%)**|**(0%)**<br>No naming convention|**(10%)**<br>Intelligible, but inconsistent, naming convention|**(15%)**<br>Coherent, consistent naming convention|
|**Documentation<br>(15%)**    |**(0%)**<br>Missing documentation|**(10%)**<br>Minimal documentation for all functions, variables, and calculations|**(15%)**<br>Comprehensive documentation for all functions, variables, and calculations|

##### Program Structure
```
Main.py
   Run entire program

Target.py
   Hold attributes of target contour
   Functions:
    → __init__
    → getHeight
    → getWidth
    → getCenter

TargetDetector.py
   Process image for target contour
   Functions:
    → __init__
    → threshold
    → contours
    → filterContours
    → getContour

TargetProcessor.py
   Calculate distance, azimuth, and altitude
   Functions:
    → __init__
    → calculate
    → getDistance
    → getAzimuth
    → getAltitude
```

### Submission Guidelines
Pull request naming convention:
```
<Last>.<First>
```
Remove all extra, unnecessary files before submitting a pull request.
