This is a readme file regarding the Deep Learning model to classify the lego images.
About the directories/files:

Python Scripts-Contains both python scripts involved in building up this model.
Notebooks-Conatins notebooks(.ipynb) of the above mentioned scripts.
Train-Folder containing the Training dataset images.
Test-Folder containing the test dataset images.
Train_Original-The folder/dataset created after treating the "train" folder with the "Q1_Dataprep_and_Processing" script.
Final Submission-This folder contains the final submission file in the required format.
train.csv-.csv files of training images.
test.csv-.csv files of test images.
sample submission.csv- Provided sample doc showing how to submit results.
RAR/ZIP Files of Train and Test.

About the dataset:


The dataset provided consisted of two separate folders of Test and Train dataset both collectively comprising of 6379 images.
The task was to classify these images into 16 categories which can be understood by seeing the train.csv(4465 images) file
A tensorflow.keras based Sequential Model with ResNet50(https://keras.io/getting-started/sequential-model-guide/) was implemented to train the dataset.
Input in such a model requires all train files to be separated into their classes and saved in the folder naming their classes.
Hence the data was tweaked to be ready to be imported in the model pipeline. 
The Notebook and Py script named "Q1_Dataprep_and_Processing" shows the same.

Performance of the model:

The model was runtaking the validation dataset same as the training one and with 35 epochs and 187 steps_per_epoch.
It resulted in a fairly good model with an accuracy of 95.74% and Validation_Score of 94.66%.
This can be ensured ny the notebook amd Py script named "Q1_Training_model_and_Classification".

Google Colab IDE + GPU Support was used to run the training model.
