import cv2
import dlib
import numpy as np
import pickle
from SmartCollegeApp.database import WorkspaceData

loaded_model = pickle.load(open("facemodel.pickle", 'rb'))
namesdic={3:"1602-19-737-089",2:"1602-19-737-069",1:"1602-19-737-094"}

def facepred(path):
        face_detect=dlib.get_frontal_face_detector()
        face_feat = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        print("entered in face pred")
        list1=[]
        nameL=[]
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=face_detect(gray)
        for i in face:
                features = face_feat(gray, i)
                for points in features.parts()[1:68]:
                    list1.append((points.x,points.y))
                arr=np.array(list1)
                arr=arr.flatten()
               # print("about to print")
                print(arr)
                res=loaded_model.predict([arr])
                temp=namesdic[res[0]]
                print(temp)
                db = WorkspaceData()
                db.add('attendence', [(temp,'present')])
                file1=open("namefile.txt","w")
                file1.write(temp)
                file1.close()

#facepred("imgg.jpg")
