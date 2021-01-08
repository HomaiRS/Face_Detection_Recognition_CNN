# MIT face recognition project dataset
The “MIT face recognition project” (http://courses.media.mit.edu/2004fall/mas622j/04.projects/faces/) dataset was used for classifying face images using different machine learning algorithms. 

# Face detection
 There are different face detection methods; here, we used histogram of oriented gradients (HOG) algorithm for the face detection task in a given image. In the following figure, faces in the twenty-five randomly selected images from MIT dataset have been detected using HOG.
 
 ![detectPics](https://user-images.githubusercontent.com/43753085/103984151-36948700-514c-11eb-94b2-66bdc418aa46.png)
 
Then we using the built-in Python functions, we estimated the face landmarks that are key facial features of the image. In the following figure, facial features are marked in blue.

![landmarkPic](https://user-images.githubusercontent.com/43753085/103985001-c4bd3d00-514d-11eb-89cb-008dcd4bcf86.png)
