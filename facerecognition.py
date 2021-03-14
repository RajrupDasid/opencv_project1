#DeepLearning model
import os
import cv2 as cv
import numpy as np
people = ['Bear Grylls','Taylor Swift']
DIR = r'C:\Users\Rajrup Das\source\repos\opencv1\Photos'

haar_cascade = cv.CascadeClassifier('haarcascade.xml')

features = []
lables = []
def create_train():
    for person in people:
        path= os.path.join(DIR, person)
        lable= people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                lables.append(lable)


create_train()
print ("Training complete---------------")
#print(f'Length of the features = {len(features)}')
#print(f'Length of the lables = {len(lables)}')
features = np.array(features, dtype= 'object')
lables = np.array(lables)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train recognizer

face_recognizer.train(features,lables)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', lables)

cv.waitKey(0)