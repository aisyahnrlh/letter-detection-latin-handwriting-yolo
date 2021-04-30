from darkflow.net.build import TFNet
from os import listdir
from os.path import isfile, join
import numpy as np
import cv2
import os 

total = 0
mypath ='pengujian5'
savepath = 'D:/darkflow-master/pengujian5/out'

options = {"pbLoad": "built_graph/yolopt1.pb", 
           "metaLoad": "built_graph/yolopt1.meta", 
           "threshold": 0.3, "gpu": 0.7}

tfnet = TFNet(options)

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)

#check if dir out is available
if (os.path.exists(savepath)):
   print("Directory Available")
else:
    os.makedirs(savepath)

for n in range(0, len(onlyfiles)):
    
    images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
    
    result = tfnet.return_predict(images[n])
    #print(result)
    
    #a1 = len(range(0, len(onlyfiles))) #jumlah files dalam folder sample_img
    #a2 = len(result) #jumlah bounding box pada gambar
    get_the_x = []
    total += len(result)
    for obj in result:
        tl = (obj['topleft']['x'], obj['topleft']['y'])
        br = (obj['bottomright']['x'], obj['bottomright']['y'])
        label = obj['label']
        get_the_x.append((obj['topleft']['x'], label))
        
        #print (obj['confidence'])
        images[n] = cv2.rectangle(images[n], tl, br, (255, 0, 0), 2)
        images[n] = cv2.putText(images[n], label, (obj['topleft']['x'], obj['topleft']['y']-5), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 1)
    
    cv2.imwrite(os.path.join(savepath, onlyfiles[n]), images[n])