
<!-- PROJECT LOGO -->
<br />

  <h3 align="center">Plate-Q</h3>

  <p align="center">
    Bringing Mass Quantification to All
    <br />
  

    
  </p>
</p>

<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/57602146/138389793-1da79ebd-bbf0-4e3d-b512-722a2212f9a3.png" alt="Material Bread logo">
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents


* [Overview](#Overview)
* [Parts List](#PartsList)
* [CAD Files](#CADFiles)
* [Software Pipeline](#SoftwarePipeline)
*  [Code Files](#CodeFiles)
* [Setup and Run](#SetupandRun)
* [Contact](#Contact)





<!-- ABOUT THE PROJECT -->




## Overview

In typical labs, Plate Readers are very helpful in quantifying green fluorescence protein (GFP) and Optical Density (OD) from a 96-well standard plate; however, laboratory grade plate readers can cost up to $15,000 which is cost prohibitive for underfunded labs. To address this issue, we worked with Dr. Bhamla at the Georgia Institute of Technology and his colleague Chinna Devarapu at Tyndall National Institute to create Plate-Q, a frugal microplate reader. At just under $150, Plate-Q is an inexpensive way to quantify both fluorescence and optical density (OD) of samples. Rather than using optical sensors found in laboratory grade plate readers[6], Plate-Q takes advantage of a Raspberry Pi camera to capture images of a well plate and extracts image features using computer vision and machine learning algorithms. A 440 nm wavelength excitation light is used to measure GFP fluorescence using a 510 nm filter for emission, and a 600 nm light source is used for OD without any emission filter. Plate-Q is completely open-source and users can customize the design to scan for other fluorescent proteins by replacing the light source and filter for different wavelengths. Users can retrain the Plate-Q algorithm to take measurements in an affordable and sustainable manner.





### Parts List


<ul>
  <li> Frosted Acrylic Plate </li>
  <li> Raspberry Pi </li>
  <li> Raspberry Pi HQ Camera with 16mm Lens </li>
  <li>440 nm LED Strip Lights</li>
  <li>600 nm LED Strip Lights</li>
  <li>510 nm Glass emission filter</li>
</ul>






<!-- USAGE EXAMPLES -->
### CAD Files

Users are able to retain the CAD files by accesing the <a href="https://github.com/igemsoftware2021/Lambert_GA/tree/main/Stl_Files">STL folder</a> in the github repository.

Folders
<ul>
  <li><a href='https://github.com/igemsoftware2021/Lambert_GA/tree/main/Stl_Files/Camera%20Case'>Camera Case</a>: contains all of the files for the camera case </li>
  <li><a href='https://github.com/igemsoftware2021/Lambert_GA/tree/main/Stl_Files/PlateReaderDesign'>Plate Reader Design</a>: contains all of the files for Plate-Q</li>
  <li><a href='https://github.com/igemsoftware2021/Lambert_GA/tree/main/Stl_Files/Well%20Plate%20Cover'>Well Plate Cover</a>:</a>Contains all of the files for the well plate cover</li>
</ul>

## Software Pipeline
![image](https://user-images.githubusercontent.com/57602146/138385337-2398ea15-545e-4088-b0db-f16b40ccc82e.png)

Plate-Q relies on a standardized Raspberry Pi HQ camera for the quantification of fluorescence and optical density, which is done through a software pipeline (Figure 14-15) that extracts the image features and maps those values to laboratory-grade plate reader values. The pipeline starts by taking pictures in triplicates at 4 different positions across the well plate. Each image is then converted into a grayscale and applied a perspective transformation to analyze the perceived brightness. Then to isolate the wells in the image Otsu's Thresholding (see Image optimization) is used. Then a gamma correction is applied to the image to ecode it into a linear luminescence scale. Finally the brightness values of the triplicates are extracted and averaged to eliminate any outliers. Then the final value is stored in a data frame (CSV file) that is passed through a mathematical regression model to output laboratory-grade plate reader values.

Learn More Here: <a href="https://2021.igem.org/Team:Lambert_GA/Measurement#softwareprocessing">Plate-Q Software Processing (iGEM.org)</a>

## Code Files
Users are able to retain the code files  in the github repository.

Folders
<ul>
  <li><a href='[Lambert_GA/Demonstration_Notebook at main · igemsoftware2021/Lambert_GA (github.com)](https://github.com/igemsoftware2021/Lambert_GA/tree/main/Demonstration_Notebook)'>Demonstration Notebook</a>: contains Jupyter Notebook With Visual </li>
  <li><a href='https://github.com/igemsoftware2021/Lambert_GA/blob/main/Main/takePicture.py'>takePicture.py</a>: Python Script to take picture of sample with proper camera settings </li>
  <li><a href='https://github.com/igemsoftware2021/Lambert_GA/blob/main/Main/Main.py'>Main.py</a>:</a> Main Python File To Calculate Fluorescence or Optical Density</li>
</ul>

<!-- CONTACT -->


## Setup and Run

Plate-Q is run on a Rasperry Pi System. The following steps explain how to download the repository and run the python scripts

### Linux

1. Open Terminal and navigate to folder of intrest
2. Run the Following Command in terminal to download Main Files: 
```
wget https://github.com/igemsoftware2021/Lambert_GA/blob/main/Main/Main.py
wget https://github.com/igemsoftware2021/Lambert_GA/blob/main/Main/takePicture.py
```
3. Now making sure you are in the proper folder run the __takingpitcure.py__ file by running  following command in terminal:
```
python takePicture.py
```
4. Now Taking the output from the python file above run the following command to run the __Main.py__ file:
```
python Main.py
```
5. Follow the propted steps by the command line and emjoy the flourecence/od output

<!-- ACKNOWLEDGEMENTS -->
## Contact
Team: Lambert Highschool


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[firebase]: https://camo.githubusercontent.com/2d891f78cbe8e96dbff64e86fa29ab801c2ebe90/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436c6f75642d46697265626173652d6635626132333f6c6f676f3d4669726562617365
[firebase-url]:https://rnfirebase.io/
[app1]:  https://2020.igem.org/wiki/images/5/58/T--Lambert_GA--Agro1.png
[app2]: https://2020.igem.org/wiki/images/a/a2/T--Lambert_GA--home.png
[app3]: https://2020.igem.org/wiki/images/e/e0/T--Lambert_GA--Agro3.png
[app4]: https://2020.igem.org/wiki/images/3/3e/T--Lambert_GA--Agro5.png
[app5]: https://2020.igem.org/wiki/images/1/15/T--Lambert_GA--Agro6.png
[app6]:https://2020.igem.org/wiki/images/2/22/T--Lambert_GA--ScanAPp.png
[app7]: https://2020.igem.org/wiki/images/e/e0/T--Lambert_GA--Agro7.png
[app8]:https://2020.igem.org/wiki/images/7/7e/T--Lambert_GA--Agro9.png
