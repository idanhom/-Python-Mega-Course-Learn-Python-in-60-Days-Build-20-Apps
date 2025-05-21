contents = ["All carrots are sliced lonitudinally", "All carrots were reportedly sliced"]

filenames = ["doc.txt", "report.txt"]

for content, filename in zip(contents, filenames):
    txt_file = open(f"files/{filename}", "w")
    txt_file.write()