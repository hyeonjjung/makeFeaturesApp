import os
import glob
import pandas as pd

directory = "log"
allFiles = glob.glob(directory+"/*.csv")

def readFileData(file):
    columnNames = ['timeStamp', 'x-axis', 'y-axis', 'z-axis']
    data = pd.read_csv(file, header = None, names = columnNames)
    x = data['x-axis']
    y = data['y-axis']
    z = data['z-axis']
    return [x, y, z]

for file in allFiles:
    fileName = os.path.basename(file)
    (name, ext) = os.path.splitext(fileName) # split fileName and .csv
    parts = name.split("_")
    sensorType = parts[0]
    testCase = parts[1]
    fileData = readFileData(file)
