import pandas as pd

train_annotations = pd.read_csv("oidv6-train-annotations-bbox.csv")
filtered_annotations = train_annotations[train_annotations['LabelName'].isin(['/m/0jyfg'])]

image_ids = filtered_annotations['ImageID'].unique()

open("IMAGE_LIST.txt", 'w').close()

for id in image_ids[5000:10000]:
    with open("IMAGE_LIST.txt", 'a') as f:
        f.write(f"train/{id}\n")


