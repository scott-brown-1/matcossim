path = "./data/alma.txt"

with open(path, "r+") as f:
    text = f.read()
    text_clean = text.replace("\n\n","\n$")
    f.seek(0)
    f.write(text_clean)
    f.truncate()
    f.close()