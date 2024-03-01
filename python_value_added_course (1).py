# -*- coding: utf-8 -*-
"""PYTHON VALUE ADDED COURSE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Q6-OJ-IFXSAwrBcfQMCg2t3U-UFV1rD
"""

#import tensorflow as ts
#from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPool2D,Dropout
#from tensorflow.keras import layers
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import cifar10

(xtrain,ytrain),(xtest,ytest)=cifar10.load_data()

#to check the type of the train and test
type(xtrain)

#to check shape of the train and test
xtrain.shape

#look the first image in the array
xtrain[10]

img0=plt.imshow(xtrain[10])

#get image label
lab1=ytrain[10]
print(lab1)

classification=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

print('image class is ',classification[ytrain[10][0]])

ytrain_one_hot=to_categorical(ytrain)
ytest_one_hot=to_categorical(ytest)

xtrain[10]

xtrain=xtrain/255
xtest=xtest/255

#create the architecture
model=Sequential()
#first conv layer
model.add(Conv2D(32,(5,5),activation='relu',input_shape=(32,32,3)))
#Pooling Layer
model.add(MaxPool2D(pool_size=(2,2)))
#second conv
model.add(Conv2D(32,(5,5),activation='relu'))
#Pooling Layer two
model.add(MaxPool2D(pool_size=(2,2)))

#flattening layer
model.add(Flatten())

#add a layer
model.add(Dense(1000,activation='relu'))
#add Dropout layer
model.add(Dropout(0.5))

#add a layer
model.add(Dense(500,activation='relu'))
#add Drop
model.add(Dropout(0.5))


#add a layer
model.add(Dense(250,activation='relu'))


#add a layer
model.add(Dense(10,activation='softmax'))

#create the architecture
model=Sequential()
#first conv layer
model.add(Conv2D(32,(5,5),activation='relu',input_shape=(32,32,3)))
#Pooling Layer
model.add(MaxPool2D(pool_size=(2,2)))
#second conv
model.add(Conv2D(32,(5,5),activation='relu'))
#Pooling Layer two
model.add(MaxPool2D(pool_size=(2,2)))

#flattening layer
model.add(Flatten())

#add a layer
model.add(Dense(1000,activation='relu'))
#add Dropout layer
model.add(Dropout(0.5))

#add a layer
model.add(Dense(500,activation='relu'))
model.add(Dropout(0.5))


#add a layer
model.add(Dense(250,activation='relu'))


#add a layer
model.add(Dense(10,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

tr=model.fit(xtrain,ytrain_one_hot,batch_size=256,epochs=20,validation_split=0.2)

deer=plt.imread('/content/index.jpg')

from skimage import transform

img=plt.imshow(deer)

resize=transform.resize(deer,(32,32,3))

img=plt.imshow(resize)

prediction=model.predict(np.array([resize]))
print(prediction)

list_index=[0,1,2,3,4,5,6,7,8,9]
x=prediction
for i in range(10):
    for j in range(10):
        if x[0][list_index[i]]>=x[0][list_index[j]]:
            temp=list_index[i]
            list_index[i]=list_index[j]
            list_index[j]=temp
print(list_index)

for i in range(5):
   print(classification[list_index[i]])