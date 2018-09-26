import cv2
import os
import numpy as np
from PIL import Image
#createEigenFaceRecognizer
#createFisherFaceRecognizer
EigenRecognizer=cv2.createEigenFaceRecognizer(15)
LbphRecognizer = cv2.createLBPHFaceRecognizer(8,8,4,4);

path = "dataSet"

# **************************************Generate faces and Label MultiDimensional Array***************************
try:
        def getImagesWithname(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faces = []
            names = []
            for imagePath in imagePaths:
                faceImg = Image.open(imagePath).convert('L');
                faceImg = faceImg.resize((110, 110))
                faceNp = np.array(faceImg, 'uint8')
                name = int(os.path.split(imagePath)[-1].split('.')[1])
                names.append(name)
                faces.append(faceNp)
                cv2.imshow("Training", faceNp)
                cv2.waitKey(10);
            return np.array(names), faces

        # *********************Training Different Recognizer**************************
        names, faces = getImagesWithname(path)
        print("Training Startted.............\n")
        # -----------------------------------------------------------------------------EigenFaceRecognizerTrain____________
        #EigenRecognizer.train(faces,names)
        #EigenRecognizer.save(path+"/EigentrainnigData.yml")
        #print("EigenFaceTraining Completed.................\n")
        # ------------------------------------------------------------------------------LBPH Recognizer Train_________


        LbphRecognizer.train(faces, names)
        LbphRecognizer.save(path + "/LBPHtrainnigData.yml");
        print("LBPHFaceTraining Completed.................\n")
#Exception handling
except Exception, e:
   print e