import os

for i in range(160000,220000):
    filename = "/Users/JP25718/00_Aaron/00_github/GPT2-Chinese/data/train-kehuan-utf8_" + str(i) + ".json"
    print("[file name] " + filename)
    if os.path.exists(filename):
      os.remove(filename)
      print("**removed**")
    else:
      print('File does not exists.')
