# Digital Image Processing 

### Watch any YouTube series for image processing to revise. 

Ex: https://www.youtube.com/watch?v=4mGLtMWyx_4&list=PL3uLubnzL2TkQ5ZpBIpX34t0cpggGMuIF&index=17 


Starting from Noise: 

## Noise in Image:  

![!](/resources/Screenshot%202022-11-27%20at%209.56.20%20AM.png)

- Photon noise is also called as Poisson noise or shot noise [source light and capturing issue / photon]
- Thermal noise is also called as johnson-nyquist noise
- Thermal noise is termed White noise. [source is random motion of charge]
- Thermal noise can be reduced with reduction in temperature. 


### Impulse Noise: 

Spike noise or independent noise.

Source: 

- miss transmission of signal 
- malfunctioning of pixel in sensors of camera 
- memort location faults in storage 


Types: 

1. Salt [pixel gray level - 255]
2. Pepper [gray level - 0]

Solution: 

1. Median filter 
2. Mean filter 
3. Dark fram subtraction 



### Structured Noise 



## Edge Detection: 


![!](/resources/Screenshot%202022-11-27%20at%2010.14.27%20AM.png)


![!](/resources/Screenshot%202022-11-27%20at%2010.16.51%20AM.png)


### Sobel Edge detection: 

1.  gradient of image intensity at each pixel 

3x3 filters with gradient in X and Y.
![!](/resources/Screenshot%202022-11-27%20at%2010.19.49%20AM.png)


2. gradient of each pixel in X and Y with above filters 
3. overall gradient $ G = \sqrt{G_x^2 + G_y^2}$ 
4. compare with thresold and decide if part of edge or not. eg. threshold 10.


### Prewitt edge detection:

1. it is symmetric around center. 

![!](/resources/Screenshot%202022-11-27%20at%2010.26.05%20AM.png)


### Robinson and KRISCH Masks: 

1. rotate the mask in all 8 directions. 


 - robinson - mask values are fixed
![!](/resources/Screenshot%202022-11-27%20at%2010.28.14%20AM.png)

- Krisch -mask values can be changed



## Canny: 

1. Apply gaussian blur [removes noise]
2. Intensity gradient calcultion [use sobel]
3. Non-maximum supression 
    To adjust the thick edges and get thin edges for final edges. 

        3.1 Edge direction from sobel $inv tan (Gx/Gy)$
        3.2 relate direction with image 
        3.3 supress the non-max edges - push edge to zero if they can't be considered as edges.
4. Thresholding and Smoothing 

        4.1 0.8 and 0.2 or any other value

        values in-between this range may or may not be an edge. termed weak edges.

5. Edge tracking and final cleansing 

        - weak edges connected to strong are strong; thus retain such weak.


### Laplacian operator: 

1. sensitive to noise 
2. produce two pixel thick edges

![!](/resources/Screenshot%202022-11-27%20at%2010.45.17%20AM.png)


## Image smoothing: 

Can be done with spatial and frequency filters. 


![!](/resources/Screenshot%202022-11-27%20at%2010.49.54%20AM.png)


## Erosion and Dilation: 

- Erosion makes image blacker 
- Dilation makes image whiter 

opencv: 

- kernel  = 5x5 with 1's

- cv2.erode/dialte(img,kernel,iteration = 5)

![!](/resources/Screenshot%202022-11-27%20at%2010.58.07%20AM.png)


## Frequency Domain: 

1. tranformation of coefficients 

2. Low pass filter for smoothing 
3. High pass filter for sharpening 

### Ideal low pass filter: 

anything above $D_o$ cutoff and below $D_o$ to pass

- sharper transition 
- ringing effects 

### Butterworth low pass filter:

- smnooth transition
- value of n will define the closeness to ILPF 
- $D(u,v)$ is euclidean distance from point (u,v) to origin in frequency plane.

- still gives ringing effect with higher orders of value n.


![!](/resources/Screenshot%202022-11-27%20at%2011.14.16%20AM.png)


### Gaussian low pass filter: 

- no ringing effect 
- no concept of order of filter 


![!](/resources/Screenshot%202022-11-27%20at%2011.19.32%20AM.png)


### High pass filters:

have similar concepts.

- sharpens the image



# Image Segmentation: 


![!](/resources/Screenshot%202022-11-27%20at%2011.23.52%20AM.png)


## Thresholding Method: 

1. used for clear distict object image. 
2. divide the imagte in foreground and background based on intensity.

Three types: 
1. Global 
2. Variable 
3. Multiple 


## Histogram Based: 

simple valley in historgram can give threshold values for get foreground and background. 

## Region Based: 

segment based on similar characteristics 

Types:
1. Region growing
2. Region split and merge


## Edge Based: 

simply close edge as object 


## Clusterin Based: 

clusters image pixel similarity


## Morphological Tranforms Based: 

- study of shapes 
- operations based on shapes to get segmentation

example: dilation and erosion, openin and closing etc.


![!](/resources/Screenshot%202022-11-27%20at%2011.48.33%20AM.png)

![!](/resources/Screenshot%202022-11-27%20at%2011.48.59%20AM.png)

![!](/resources/Screenshot%202022-11-27%20at%2011.49.12%20AM.png)

### Opening and closing:

1. Opening 

-  erosion followed by dialtion (removes narrow connections/lines)

1. Closing

-  Dilation followed by erosion (fills hole)


## Texture Based: 

- divide image based on similar texture features 