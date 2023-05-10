# coding:utf-8

import os
import random
import argparse

parser = argparse.ArgumentParser()
#The address of the xml file, modify it according to your own data. The xml is generally stored under Annotations
parser.add_argument('--xml_path', default='Annotations', type=str, help='input xml label path')
#Data set division, the address selects ImageSets/Main under your own data
parser.add_argument('--txt_path', default='ImageSets/Main', type=str, help='output txt label path')
opt = parser.parse_args()

trainval_percent = 1.0  # The proportion of training set and validation set. There is no test set split here
train_percent = 0.9     # The proportion of the training set can be adjusted by yourself
xmlfilepath = opt.xml_path
txtsavepath = opt.txt_path
total_xml = os.listdir(xmlfilepath)
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

num = len(total_xml)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list_index, tv)
train = random.sample(trainval, tr)

file_trainval = open(txtsavepath + '/trainval.txt', 'w')
file_test = open(txtsavepath + '/test.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')

for i in list_index:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)

file_trainval.close()
file_train.close()
file_val.close()
file_test.close()
