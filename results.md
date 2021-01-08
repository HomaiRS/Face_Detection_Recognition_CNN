# MIT face recognition project 
The “MIT face recognition project” (http://courses.media.mit.edu/2004fall/mas622j/04.projects/faces/) dataset was used for classifying face images using different machine learning algorithms. 

## Face detection
 There are different face detection methods; here, we used histogram of oriented gradients (HOG) algorithm for the face detection task in a given image. In the following figure, faces in the twenty-five randomly selected images from MIT dataset have been detected using HOG.
 
 ![detectPics](https://user-images.githubusercontent.com/43753085/103984151-36948700-514c-11eb-94b2-66bdc418aa46.png)
 
 ## Facial features extraction
 
Then we using the built-in Python functions to estimate the key facial features of images. In the following figure, facial features (n=128) are marked in blue.

![landmarkPic](https://user-images.githubusercontent.com/43753085/103985001-c4bd3d00-514d-11eb-89cb-008dcd4bcf86.png)

 ## Face recognition
 
Now that the facial features are extracted, the 128 dimensional vector of features is like a point in R^128 that uniquely represents an image. Therefore, we compute the pairwise distance (e.g., Euclidean distance) between the feature vectors of different images to determine whether the two images are similar or not. As this distance is lower, the more similar the images are. Then, we set a face maximum distance (e.g., D = 0.6) as a threshold on the distances. If the distance between an image *a* and *b* is less than or equal to 0.6, then the two images match. Otherwise, they do not match. 

![FaceEncodepic](https://user-images.githubusercontent.com/43753085/103986274-11a21300-5150-11eb-815b-92a0aaf83a70.png)
