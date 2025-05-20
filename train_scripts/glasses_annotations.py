import pandas as pd

annotations = pd.read_csv("oidv6-train-annotations-bbox.csv")
glasses_annotations = annotations[annotations['LabelName'].isin(['/m/0jyfg'])]
glasses_annotations = glasses_annotations.drop_duplicates(subset=['ImageID'])

glasses_annotations[5000:10000].to_csv("glasses-train-annotations-bbox.csv")



