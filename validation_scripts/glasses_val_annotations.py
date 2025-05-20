import pandas as pd

annotations = pd.read_csv("validation-annotations-bbox.csv")
glasses_annotations = annotations[annotations['LabelName'].isin(['/m/0jyfg'])]
glasses_annotations = glasses_annotations.drop_duplicates(subset=['ImageID'])

glasses_annotations.to_csv("glasses-val-annotations-bbox.csv")



