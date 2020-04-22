#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Importing the necessary required libraries
import numpy as np
import pandas as pd
import cv2
import os


# In[13]:


#Reading our test and train data csv files
train_data = pd.read_csv("D:/Q1/question_1_dataset/train.csv")
test_data = pd.read_csv("D:/Q1/question_1_dataset/test.csv")


# In[14]:


#Checking the type of the variables involved
type(train_data["name"][0])


# In[15]:


#For the sake of viewing and analysing and deducing the total number of categories.
l = []
for i in range(4465):
    l.append({train_data["name"][i] + ":" +str(train_data["category"][i])})
l


# In[ ]:


#Creating folder with names of the categories of classification
folder = "D:/Q1/question_1_dataset/train/train" 
for i in range(1,17): 
         output_folder = folder + "/" + str(i)
         if not os._exists(output_folder):
            os.makedirs(output_folder)


# In[ ]:


#Saving images of LEGO according to their category number.
for j in range(1,17):
    for k in range(4465):
        if train_data["category"][k] == j:
            img = cv2.imread(folder + "/" + train_data["name"][k]  , 1)
            path = folder + "/" + str(j)
            cv2.imwrite(os.path.join(path ,train_data["name"][k]), img)
            cv2.waitKey(0)


# In[ ]:


#Deleting the image files from the training folder to prepare out dataset to be implemented in the training model pipeline.
for filename in range(1,4466):
        os.remove(os.path.join(folder + "/" + str(filename) + ".png"))

