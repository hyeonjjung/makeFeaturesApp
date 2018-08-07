'''
Magnetometer, Accel, Gyro sensor들의 x, y, z 데이터에서
자동으로 features를 뽑아주는 application

<Feature list>
- Mean (x), (y), (z), (x, y, z)
- Magnitude of Mean : sqrt(x^2+y^2+z^2)
- ...

2018-08-07 HyeonJung Park
'''

import os
import glob
import csv
import arff
from numpy import *


# Sensor's delay (Window time is 3 seconds)
# M is 10000 msec
M_window = 300
# A is 5000 msec
A_window = 600
# G is 5000 msec
G_window = 600

directory = "log"
allFiles = glob.glob(directory+"/*.csv")

features = {
    u'attributes': [
        (u'A mean (x)', u'REAL')],
    u'data': [
        [12],
        [34]
    ],
    u'description': u'',
    u'relation': u'sensor data'
}

def readFileData(file):
    f = open(file, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    x = []
    y = []
    z = []
    for line in rdr:
        if len(line) >= 4:
            x.append(float(line[1]))
            y.append(float(line[2]))
            z.append(float(line[3]))
    f.close()
    return [x, y, z]

def writeARFF(data):
    arff.dumps(data)

def getFeatures(frames):
    print('hello')

for file in allFiles:
    fileName = os.path.basename(file)
    (name, ext) = os.path.splitext(fileName) # split fileName and .csv
    parts = name.split("_")
    sensorType = parts[0]
    testCase = parts[1]
    fileData = readFileData(file)

    windowSize = 0
    if sensorType == 'M':
        windowSize = M_window
    elif sensorType == 'A':
        windowSize = A_window
    elif sensorType == 'G':
        windowSize = G_window

    count = 0
    frames = []
    tmp = []

    # 각각의 x, y, z 데이터들을 window_size에 맞게 잘라서 frames에 넣음
    for i in range(len(fileData)):
        for j in range(len(fileData[i])):
            count = count + 1
            tmp.append(fileData[i][j])
            if count == windowSize:
                count = 0
                frames.append(tmp)
                tmp = []

    getFeatures(frames)
    #writeARFF(features)
