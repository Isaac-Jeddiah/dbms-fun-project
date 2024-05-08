import pymongo
import matplotlib.pyplot as plt 
import matplotlib.image as img
import os
import glob
import natsort
import pandas as pd
import numpy as np
myclient = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = myclient["mydb"]

mycol = mydb["pokemon"]
import csv


dir1 = r"pokemon_images"  

path1 = os.path.join(dir1,'*g')

files = glob.glob(path1)
files1= natsort.natsorted(files,reverse=False)
imag = []
for x in files1:
    img = plt.imread(x)
    imag.append(img)
print("Welcome to pokemon database")
print("1.Search" )
print("Enter your choice")
ch=int(input())
if ch==1:
    print("1.Search by pokemon number")
    print("2.Search by pokemon name")
    c=int(input())
    if c==1:
        print("Enter pokemon number")
        n=int(input())
        for o in mycol.find({"pokemon_number":n}):
            print(o)
        

        from PIL import Image
        img = Image.open("1.png")
        img.show()
        #testImage = img.imread('C:\Users\ISAAC JEDDIAH\Desktop\test poke\pokemon_images\1.png') 
        #plt.imshow(testImage) 
    if c==2:
        print("Enter pokemon name")
        n=input()
        for o in mycol.find({"name":n}):
            print(o)

