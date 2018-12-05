import h5py
from keras.models import load_model
import numpy as np

model = load_model('model.h5')

X_test = []

for filename in ["gap_ResNet50.h5", "gap_Xception.h5", "gap_InceptionV3.h5"]:
    with h5py.File(filename, 'r') as h:
        X_test.append(np.array(h['test']))

X_test = np.concatenate(X_test, axis=1)


y_pred = model.predict(X_test, verbose=1)
del model
y_pred = y_pred.clip(min=0.005, max=0.995)


import pandas as pd
from keras.preprocessing.image import *

df = pd.read_csv("sample_submission.csv")

image_size = (224, 224)
gen = ImageDataGenerator()
test_generator = gen.flow_from_directory("test2", image_size, shuffle=False,
                                         batch_size=16, class_mode=None)

for i, fname in enumerate(test_generator.filenames):
    index = int(fname[fname.rfind('/')+1:fname.rfind('.')])
    df.at[index-1,'label']= y_pred[i]

df.to_csv('pred.csv', index=None)
df.head(10)
