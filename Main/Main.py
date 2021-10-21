#import dependencies
import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu
from skimage import data, filters, measure, morphology
import numpy as np 
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from skimage.io import imread, imshow
from skimage.measure import label, regionprops, regionprops_table



#Load image to code
def imgLoad(file):
    originalImg = cv2.imread(file)
    originalImg = cv2.cvtColor(originalImg, cv2.COLOR_BGR2RGB)
    greyImg = cv2.cvtColor(originalImg, cv2.COLOR_RGB2GRAY)
    return(greyImg)

#Perspective Transform 
def perspectiveTransform(image,tl,tr,bl,br,width,height):
    pts1 = np.float32(
        [[tl[0], tl[1]], # top left
         [tr[0], tr[1]], # top right
         [bl[0], bl[1]], # bottom left
         [br[0], br[1]]] # bottom right
    )

    pts2 = np.float32(
            [[0,0], # top left
             [width,0], # top right
             [0,height], # bottom left
             [width,height]] # bottom right
             )


    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    pResult = cv2.warpPerspective(greyImg, matrix, (width,height)) 
    
    return(presult)


  
#gamma correction
def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

#otsus Method with plot 
def otsuMethod(sample):
    image = sample
    thresh = threshold_otsu(image)
    binary = image > thresh
    binary = morphology.remove_small_objects(binary, 400)
    binary = morphology.remove_small_holes(binary, 400)
    labels = measure.label(binary)
    fig, axes = plt.subplots(ncols=3, figsize=(16, 4.5))
    ax = axes.ravel()
    ax[0] = plt.subplot(1, 3, 1)
    ax[1] = plt.subplot(1, 3, 2)
    ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title('Original')
    ax[0].axis('off')

    ax[1].hist(image.ravel(), bins=256)
    ax[1].set_title('Histogram')
    ax[1].axvline(thresh, color='r')

    ax[2].imshow(binary, cmap=plt.cm.gray)
    ax[2].set_title('Thresholded')
    ax[2].axis('off')
    

    plt.show()
    return(labels)

def maskFExtractor(mask):
    props = regionprops_table(labels, properties=('centroid','area', 'eccentricity', 'perimeter','label'))
    maskFeatures = pd.DataFrame(props)
    maskFeatures.drop(maskFeatures.index[maskFeatures['area'] < 50000], inplace=True)
    return(maskFeatures)

#individual Mask Creator
def maskCreator(im,df):
    maskList= []
    coords = []
    x= df['centroid-0'].tolist()
    y =df['centroid-1'].tolist()
    area = df['area'].tolist()
    for i in range(0, len(x)):
        image = np.zeros((im.shape[0], im.shape[1]))
        radius = math.sqrt((area[i]/math.pi))
        rr, cc = ellipse(x[i], y[i],radius, radius)
        image[rr, cc] = 1
        maskList.append(image)
        masked = cv2.bitwise_and(im, im, mask=image.astype(np.uint8))
        mean = cv2.mean(masked, mask=masked)
        coords.append([(x[i], y[i]), mean[0]])
        coords.sort
    return(coords,maskList)

#Combined Well Plate Code
def wellplateCode(item):
    gammaIMG = adjust_gamma(item, gamma=0.7)
    imshow(gammaIMG)
    labels = otsuMethod(item)
    props = regionprops_table(labels, properties=('centroid','area', 'eccentricity', 'perimeter','label'))
    maskFeatures = pd.DataFrame(props)
    maskFeatures.drop(maskFeatures.index[maskFeatures['area'] < 50000], inplace=True)
    
    print(len(x))
    print(len(y))
    coords=maskCreator(gammaIMG,maskFeatures)

    return(coords)
#Flourecence Calc
def flourenceValues(sampleCoords,clearCoords):
    slope = 19.5
    yIntercept = 36.6
    flourenceVals = [(slope*(sampleCoords[i][1]-clearCoords[i][1]))+yIntercept for i in range(len(postitions))]
    return(flourenceVals)

#OD Calc
def odValues(sampleCoords,clearCoords):
    slope = 1.5
    yIntercept = .03635
    flourenceVals = [(slope(math.log10(clearCoords[i][1]/sampleCoords[i][1])))+yIntercept for i in range(len(postitions))]
    return(flourenceVals)



#Main Run
if __name__ == "__main__":
    img1 = print(input('File Path 1 of Sample: '))
    img2 = print(input('File Path 2 of Blank: '))
    question = print(input('fluorescence or optical density? '))
    masterCoords= []
    for img in [img1,img2]:
        sample = imgLoad(img)
        topLeft = print(input('Top Left Coord: '))
        topRight = print(input('Top Right Coord: '))
        bottomLeft = print(input('Bottom Left Coord: '))
        bottomRight = print(input('Bottom Right Coord: ' ))
        width = print(input('Width of Transform: '))
        height = print(input('hieght of transform: '))
        pSample = perspectiveTransform(sample,topLeft,topRight,bottomLeft,bottomRight,width,height)
        masterCoords.append(wellplateCode(psample))
    if (question == "optical density"):
        outputDict = {'position': postitions,'values':odValues(masterCoords[0],masterCoords[1]) } 
    else if (question =='fluorescence'):
        outputDict = {'position': postitions,'values':flourenceValues(masterCoords[0],masterCoords[1])
    outputDf = pd.DataFrame(outputDict)
    outputDf.to_csv('Sample.csv')

    
        
    
        
        
        
    