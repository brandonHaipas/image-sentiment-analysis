import requests
import pandas as pd
import os
import pathlib
from os import path
from utils import save_img, create_dict
from colorthief import ColorThief

# first download the dataset from data.world, then use it afterwards here
old_data = pd.read_csv("image-Sentiment-polarity-DFE.csv")

# then create the folder for images
newpath = pathlib.Path().absolute()
folder_path = path.join(newpath, '/images/')
if not path.exists(folder_path):
    os.makedirs(folder_path)

# variables de iniciacion del dataframe
num = 6
id_num = 0

data_dict = create_dict(num)
img_names = []

for index, row in old_data.iterrows():
    label = "no_label"
    img_name = ""
    try:
        img_name = f"{str(folder_path)}img_{id_num}"
        save_img(row["imageurl"], img_name)
    except Exception as e:
        print({str(e)})
        continue
    label = row["which_of_these_sentiment_scores_does_the_above_image_fit_into_best"]
    data_dict["label"].append(label)
    img_names.append(img_name)
    id_num+=1
    
for i in img_names:
    color_thief = ColorThief(i)
    palette = color_thief.get_palette(color_count= num, quality = 1)
    
    for i in range(0, num):
        color = palette[i]
        data_dict[f"red_{str(i)}"].append(color[0])
        data_dict[f"green_{str(i)}"].append(color[1])
        data_dict[f"blue_{str(i)}"].append(color[2])
        
data_pd_df = pd.DataFrame.from_dict(data_dict)
pd.DataFrame.to_csv(data_pd_df)