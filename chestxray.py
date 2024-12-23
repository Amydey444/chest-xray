import numpy as np
import pandas as pd
from PIL import Image
import cv2
import os
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
dir="/Users/user/Desktop/anacondaJupyter/archive"
print("files in directory:")
os.listdir(dir)
import pandas as pd

file_age = os.path.join(dir, "train_age.csv")
file_gender = os.path.join(dir, "train_gender.csv")

if os.path.exists(file_age) and os.path.exists(file_gender):
    df_age = pd.read_csv(file_age)
    df_gen = pd.read_csv(file_gender)
    print(df_age.head())
    print(df_gen.head())
else:
    print("One or both files do not exist.")
dir="/Users/user/Desktop/anacondaJupyter/archive"
file_age = os.path.join(dir, "train_age.csv")
file_gender = os.path.join(dir, "train_gender.csv")

df_age=pd.read_csv(file_age)
df_gen=pd.read_csv(file_gender)
print(df_age.head())
print(df_gen.head())