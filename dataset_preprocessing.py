#!encoding=utf-8

import os
import shutil

train_filenames = os.listdir('train')
train_cat = filter(lambda x:x[:3] == 'cat', train_filenames)
train_dog = filter(lambda x:x[:3] == 'dog', train_filenames)

# train_cat = [x for x in train_filenames if x[0:3]=='cat']
# train_dog = [x for x in train_filenames if lambda x:x[0:3]=='dog']

def rmrf_mkdir(dirname):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)

# rmrf_mkdir('train2')
# os.mkdir('train2/cat')
# os.mkdir('train2/dog')
#
# rmrf_mkdir('test2')
# os.symlink('../test/', 'test2/test')
#
# for filename in train_cat:
#     os.symlink('../../train/'+filename, 'train2/cat/'+filename)
#
# for filename in train_dog:
#     os.symlink('../../train/'+filename, 'train2/dog/'+filename)

rmrf_mkdir('train3')
os.mkdir('train3/cat')
os.mkdir('train3/dog')

rmrf_mkdir('test3')
os.symlink('../test/', 'test3/test')

i = 0
for filename in train_cat:
    os.symlink('../../train/'+filename, 'train3/cat/'+filename)
    i=i+1
    if i>10:
        break
i = 0
for filename in train_dog:
    os.symlink('../../train/'+filename, 'train3/dog/'+filename)
    i=i+1
    if i>10:
        break

