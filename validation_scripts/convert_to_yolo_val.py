import csv, pathlib, tqdm

annotations_file = pathlib.Path("/workspace/fine-tune/glasses-val-annotations-bbox.csv")
images_directory = pathlib.Path("/workspace/fine-tune/images")
labels_directory = images_directory.parent / "labels/val"

labels_directory.mkdir(parents=True, exist_ok=True)

with annotations_file.open() as f:
    reader = csv.DictReader(f)
    for row in tqdm.tqdm(reader, desc="writing YOLO .txt"):
        img_id  = row["ImageID"]
        txt_out = labels_directory / f"{img_id}.txt"

        xmin, xmax = float(row["XMin"]), float(row["XMax"])
        ymin, ymax = float(row["YMin"]), float(row["YMax"])

        xc = (xmin + xmax) / 2
        yc = (ymin + ymax) / 2
        bw =  xmax - xmin
        bh =  ymax - ymin

        with txt_out.open("a") as t:                 
            t.write(f"80 {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}\n")

print(f"YOLO format salvat in {labels_directory}")
