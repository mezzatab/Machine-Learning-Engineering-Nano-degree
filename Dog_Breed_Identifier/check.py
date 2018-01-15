from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense, Input
from keras.models import Sequential
import numpy as np
import pandas as pd 

model = Sequential()

### TODO: Define your architecture.
num_classes=133
# this is our input placeholder
input = Input(shape=(224,224,3)) ## Input size of each image ## 
print(input.shape[:])

model.add(Conv2D(16, kernel_size=(5, 5), strides=(1, 1), activation='relu', input_shape=(224,224,3)))

#iothing added to commit but untracked files present
print(model.summary())
