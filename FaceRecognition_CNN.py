import PIL.Image
import PIL.ImageDraw
import face_recognition
import numpy as np


# ------------> Face detection <------------ #
# Load the clear file into a numpy array
image = face_recognition.load_image_file("/Users/homai/Desktop/myFaceRecognition/Exercise Files/myImgs/ma1.jpg") #/Users/homai/Desktop/myFaceRecognition/Exercise Files/Ch03/

N = 3 # number of faces in the loaded image
print(image[1:N])
print(np.shape(image))
# Find all the faces in the image
fLocations = face_recognition.face_locations(image)


number_of_faces = len(fLocations)
print("I found {} face(s) in this photograph.".format(number_of_faces))

# Load the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)

for fLocation in fLocations:

    # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
    top, right, bottom, left = fLocation
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # Let's draw a box around the face
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="red",width=4)

# Display the image on screen
pil_image.show()


# ------------> Facial feature extraction <------------ #
# Load the jpg file into a numpy array

image = face_recognition.load_image_file("ma1.jpg")

# Find all facial features in all the faces in the image
ListOf_faceLandmarks = face_recognition.face_landmarks(image)

number_of_faces = len(ListOf_faceLandmarks)
print("I found {} face(s) in this photograph.".format(number_of_faces))

# Load the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)

# Create a PIL drawing object to be able to draw lines later
draw = PIL.ImageDraw.Draw(pil_image)

# Loop over each face
for ListOf_faceLandmark in ListOf_faceLandmarks:

    # Loop over each facial feature (eye, nose, mouth, lips, etc)
    for name, list_of_points in ListOf_faceLandmark.items():

        # Print the location of each facial feature in this image
        print("The {} in this face has the following points: {}".format(name, list_of_points))

        # Let's trace out each facial feature in the image with a line!
        draw.line(list_of_points, fill="blue", width=3)

pil_image.show()


# ------------> Face recognition <------------ #
# Load the known images

image_of_person_1 = face_recognition.load_image_file("Myperson_1.png")
image_of_person_2 = face_recognition.load_image_file("Myperson_2.png")

# Get the face encoding of each person. This can fail if no one is found in the photo.
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]

# Create a list of all known face encodings
known_face_encodings = [
    person_1_face_encoding,
    person_2_face_encoding,
]

# Load the image we want to check
unknown_image = face_recognition.load_image_file("Myunknown_4.png")

# Get face encodings for any people in the picture
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_face_encoding in unknown_face_encodings:
    # Test if this unknown face encoding matches any of the three people we know
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.6)
    name = "Unknown"
    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"

    print(f"Found {name} in the photo!")












