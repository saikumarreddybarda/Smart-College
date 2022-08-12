import cv2
import dlib
import numpy as np
import pickle
#namesdic={1:"sai",2:"bharath",3:""}
def faceready(path,name):
        face_detect=dlib.get_frontal_face_detector()
        face_feat = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        img = cv2.imread(path, cv2.IMREAD_COLOR)
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
                print(arr)
              #  nameL.append(name)
                namearr=np.array(nameL)
              #  np.save("facedatapred.npy", arr)
              #  np.save("facenamepred.npy", namearr)
                load_face = np.load("facedatapred.npy")
                load_name = np.load("facenamepred.npy")
                new_face = np.vstack([load_face, arr])
                new_pos = np.vstack([load_name, namearr])
                np.save("facedatapred.npy", new_face)
                np.save("facenamepred.npy", new_pos)
faceready("imgg.jpg",1)




