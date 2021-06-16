import os
import time

def create_dir():
    path=os.path.dirname("D:/Documents/Rice_detection/exp/")

    latest = max(os.listdir(path))

    latest_dir = "exp/test"+str(int(latest[-1])+1)
    os.mkdir(latest_dir)
    # print(latest_dir)
    return latest_dir

dir = create_dir()
print(dir)