import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# distance function to calculate the distance between two points in euclidean space having n dimensions(784 in this case)
def distance(p1, p2):
    return np.sum((p2 - p1)**2)**.5


# knn function to find the k nearest points to the input point
# first we will calc distance from input to each training data point then sort(obv in increasing order) them and take 
# first k and make predictions based upon them

def knn(X , Y, test , k = 50):
    # it will have the distance( from the input point ) and label of each point as tuple ie : (distance, label)
    d = []
    r = X.shape[0]
    for i in range(r):
        d.append((distance(test, X[i]), Y[i]))
        
    # l is the list of sorted distance label
    l = np.array(sorted(d))[:, 1]
    l = l[:k]
    u = np.unique(l, return_counts = True)
    
    # convert the unique labels with their frequency into key value pair
    freq_dict = dict()
    for i in range(len(u[0])):
        freq_dict[u[0][i]] = u[1][i]
    
    # get the key whose value is maxmimum in the dictionary
    pred = int(max(freq_dict, key = freq_dict.get))
    
    accuracy = int(freq_dict[pred])
    
    percentage_accuracy = int((accuracy/k)*100)
    
    print("I can say with %d%% of accurancy that test input is %d" %(percentage_accuracy, pred))
    
    return freq_dict




cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

dataset_path = ".facedata"


# cv2.puttext("anything you want")