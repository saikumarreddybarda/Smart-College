import numpy as np
from sklearn import svm
import pickle
def train():
    load_face = np.load("facedatapred.npy")
    load_name = np.load("facenamepred.npy")

  #  print(load_face.shape)

    load_name=load_name.flatten()
   # print(load_name)
    model=svm.SVC(kernel='linear')
    model.fit(load_face,load_name)
    #print(model.predict([load_face[4]]))

    pickle.dump(model, open("facemodel.pickle", 'wb'))



