<!-- PROJECT LOGO -->
<br />

  <h3 align="center">Plate-Q</h3>

  <p align="center">
    Bringing Mass Quantification to All
    <br />
    
  </p>
</p>





<!-- TABLE OF CONTENTS -->
## Table of Contents


* [Overview](#Overview)
* [Parts List](#PartsList)
* [CAD Files](#CADFiles)
* [Software Pipeline](#SoftwarePipeline)
* [Setup and Run](#SetupandRun)
* [Contanct](#Contact)





<!-- ABOUT THE PROJECT -->



  <a href="#">
    <img src="https://cdn.discordapp.com/attachments/769754881414004741/769755050637262848/agroLogo.png" alt="Logo" width="80" height="80">
  </a>


## Overview

In typical labs, Plate Readers are very helpful in quantifying green fluorescence protein (GFP) and Optical Density (OD) from a 96-well standard plate; however, laboratory grade plate readers can cost up to $15,000 which is cost prohibitive for underfunded labs. To address this issue, we worked with Dr. Bhamla at the Georgia Institute of Technology and his colleague Chinna Devarapu at Tyndall National Institute to create Plate-Q, a frugal microplate reader. At just under $150, Plate-Q is an inexpensive way to quantify both fluorescence and optical density (OD) of samples. Rather than using optical sensors found in laboratory grade plate readers[6], Plate-Q takes advantage of a Raspberry Pi camera to capture images of a well plate and extracts image features using computer vision and machine learning algorithms. A 440 nm wavelength excitation light is used to measure GFP fluorescence using a 510 nm filter for emission, and a 600 nm light source is used for OD without any emission filter. Plate-Q is completely open-source and users can customize the design to scan for other fluorescent proteins by replacing the light source and filter for different wavelengths. Users can retrain the Plate-Q algorithm to take measurements in an affordable and sustainable manner.





### Parts List


#screenshots

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
  <li><a href='https://github.com/igemsoftware2021/Lambert_GA/tree/main/Stl_Files/Camera%20Case'>__Camera Case__</a>: contains all of the files for the camera case </li>
  <li><a href='https://github.com/igemsoftware2021/Lambert_GA/tree/main/Stl_Files/PlateReaderDesign'>__Plate Reader Design__</a>: contains all of the files for Plate-Q</li>
  <li><a href='https://github.com/igemsoftware2021/Lambert_GA/tree/main/Stl_Files/Well%20Plate%20Cover'>__Well Plate Cover__</a>:</a>Contains all of the files for the well plate cover</li>
</ul>

## Software Pipeline
![image](https://user-images.githubusercontent.com/57602146/138385337-2398ea15-545e-4088-b0db-f16b40ccc82e.png)

Plate-Q relies on a standardized Raspberry Pi HQ camera for the quantification of fluorescence and optical density, which is done through a software pipeline (Figure 14-15) that extracts the image features and maps those values to laboratory-grade plate reader values. The pipeline starts by taking pictures in triplicates at 4 different positions across the well plate. Each image is then converted into a grayscale and applied a perspective transformation to analyze the perceived brightness. Then to isolate the wells in the image Otsu's Thresholding (see Image optimization) is used. Then a gamma correction is applied to the image to ecode it into a linear luminescence scale. Finally the brightness values of the triplicates are extracted and averaged to eliminate any outliers. Then the final value is stored in a data frame (CSV file) that is passed through a mathematical regression model to output laboratory-grade plate reader values.

Learn More Here: <a href="https://2021.igem.org/Team:Lambert_GA/Measurement#softwareprocessing">Plate-Q Software Processing (iGEM.org)</a>



<!-- CONTACT -->


## Setup and Run

Agro-Q uses React Native . First, install the React Native CLI using the instructions at https://reactnative.dev/docs/environment-setup. 
Select the “React Native CLI Quickstart” option and your desired platforms and complete the installation with the instructions provided.


Download the project files to your computer

### Mac - Android or iOS
1. Open Terminal and navigate to the project folder
1. To run the app on the iOS Simulator, Xcode must be installed with a valid signing profile. Enter the following command in the terminal: 
```
npx react-native run-ios
```

Run the app on the iOS Simulator by opening the .xcworkspace file and clicking the play button at the top of the screen. To run on a physical iOS device, plug the device into the Mac and choose the device from the dropdown menu at the top of the screen.


To run on an Android simulator, simply use the following command or open Android Studio and run the app manually.
```
npx react-native run-android
```

### Windows - Android
1. To run the app on the Android simulator, open a command prompt window and navigate to the project folder
2. Run the following command: 
```
npx react-native run-android
```
To run on a physical Android device, plug in the device into the computer and use Android Studio to manually run the app onto the device.


Note to user: 
- app currently optimized for android
- Data uploads to the app between 5sec -1min 
- Sometimes data may not update properly so restart the app and run again

Login info for test account: (create user will be created in future version)
- Username : lamberttest@gamil.com
- Password : lambert123


## Testing
Download the code from this repository to run a node js server to update values on the app:
https://github.com/VarunSendilraj/testingagro-q/tree/main 

### Run
1. Open Terminal and navigate to the project folder
1. To run the server, enter the following command in the terminal: 
```
npm install
```
To start the server run the following command in the terminal:
```
npm start
```

To update the data values type the values in the following link 
```
http://localhost:3000/sendData/temp,Ph,light,co2,waterTemp,humidity

```



<!-- ACKNOWLEDGEMENTS -->
## Contact
Lambert Highschool


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
