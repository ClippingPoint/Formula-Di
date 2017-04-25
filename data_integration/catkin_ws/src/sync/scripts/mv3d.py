##---------------------------------------------------------------------------------------
## Data preparation
##---------------------------------------------------------------------------------------

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
##---------------------------------------------------------------------------------------
## Hyper parameters
## As in 04/25/2017, Dumpy variables for now, subject to change
##---------------------------------------------------------------------------------------
batch_size = 128
num_classes = 10
epochs = 12

##---------------------------------------------------------------------------------------
## Shuffling?
##---------------------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
##---------------------------------------------------------------------------------------
## Convolutional layers for views
## bv: bird_eye_view
## fv: front_view Cylindrical projection
## rgb: (mono?) camera_image
## Use Keras?
## GPU compatibility?
##---------------------------------------------------------------------------------------
# input layer

model = Sequential()
crop_shape = ((), ())


