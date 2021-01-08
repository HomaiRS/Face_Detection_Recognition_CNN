# MIT face recognition project 
The “MIT face recognition project” (http://courses.media.mit.edu/2004fall/mas622j/04.projects/faces/) dataset was used for classifying face images using different machine learning algorithms. 

## Face detection
 There are different face detection methods; here, we used histogram of oriented gradients (HOG) algorithm for the face detection task in a given image. In the following figure, faces in the twenty-five randomly selected images from MIT dataset were detected using HOG.
 
 ![detectPics](https://user-images.githubusercontent.com/43753085/103984151-36948700-514c-11eb-94b2-66bdc418aa46.png)
 
 ## Facial features extraction
 
Then we used the built-in Python functions to estimate the key facial features of images. In the following figure, facial features (n=128) are marked in blue.

![landmarkPic](https://user-images.githubusercontent.com/43753085/103985001-c4bd3d00-514d-11eb-89cb-008dcd4bcf86.png)

 ## Face recognition
 
Now that the facial features are extracted, the 128-dimensional vector of features is like a point in R^128 that uniquely represents an image. Therefore, we compute the pairwise distance (e.g., Euclidean distance) between the feature vectors of different images to determine whether the two images are similar or not. As this distance is lower, the more similar the images are. Then, we set a face maximum distance (e.g., D = 0.6) as a threshold on the distances. If the distance between images *a* and *b* is less than or equal to 0.6, then the two images match. Otherwise, they do not match. Using pairwise distances CNN could recognize faces with 100% accuracy. Images shown in the red box are used as test images and images in the blue box are used as train images. Some of the test images (e.g., the first and third test images from left) contain more than one face in them with the different facial gestures seen in the train set. Also, CNN has done a good job in recognizing faces in the second and third test images even though one has bears and one has a sunglass.

![FaceEncodepic](https://user-images.githubusercontent.com/43753085/104043950-32935400-51a2-11eb-8509-6ecbada77db5.png)

