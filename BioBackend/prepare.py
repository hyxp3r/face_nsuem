from imutils import paths
import face_recognition
import pickle
import cv2
import os
import pandas as pd

 
def prepare():
    imagePaths = list(paths.list_images('Images'))
    
    knownEncodings = []
    knownNames = []

    for (i, imagePath) in enumerate(imagePaths):


        name = imagePath.split(os.path.sep)[-2]

        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb,model='hog')

        encodings = face_recognition.face_encodings(rgb, boxes)
        
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)

    data = {"encodings": knownEncodings, "names": knownNames}
    df = pd.DataFrame(data)
    #print(df)
    if len(data['encodings']) == 0:
        pass
    else:
        f = open("face_enc", "wb")
        f.write(pickle.dumps(data))
        f.close()
    return len(data['encodings'])
