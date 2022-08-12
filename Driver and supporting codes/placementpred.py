import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
from sklearn import svm,metrics
import pickle
df1=pd.read_csv(r'C:\Users\user\Documents\collegePlace.csv')
print(df1.info())
#print(df1)
#y=pd.get_dummies(df1['Stream'])
z=pd.get_dummies(df1['Gender'])
final_df=pd.concat([df1,z],axis=1)
#print(final_df['Civil'])
#print(final_df.head(10))
#print(final_df.info())
#print(final_df.isnull().sum())
df_fi=final_df.drop(['Gender','Stream','Hostel'],axis=1)
print("print df_fi")
#print(df_fi.info())
#print(df_fi.head())
df_fi=df_fi.drop(['PlacedOrNot'],axis=1)
#print("print df_fi 123")
#print(df_fi.info())

X_train,X_test,Y_train,Y_test=train_test_split(df_fi,final_df['PlacedOrNot'],test_size=0.3,random_state=109)
#print(X_test)

model=svm.SVC(kernel='linear')
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)

pickle.dump(model, open("placements.pickle", 'wb'))
print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))

print(X_test.info())
print(model.predict([[20,0,6,4,50,87,0,1]]))
print(df1.head())





