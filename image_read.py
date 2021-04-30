from darkflow.net.build import TFNet
from os import listdir
from os.path import isfile, join
import numpy as np
import cv2
import os 

total = 0
ukuran_font = 0
tebal_font = 0
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
        
        images[n] = cv2.rectangle(images[n], tl, br, (255, 0, 0), 2)
        #print(obj['confidence'])
    
    get_the_x.sort()
    
    baca = ""
    for y in range(0, len(get_the_x)):
        baca += get_the_x[y][1]
    
    tinggi = images[n].shape[0]
    lebar = images[n].shape[1]
    
    if tinggi < 200:
        ukuran_font = 0.5
        tebal_font = 1
    elif tinggi > 200 and tinggi < 300:
        ukuran_font = 1
        tebal_font = 1
    elif tinggi > 300 and tinggi < 400:
        ukuran_font = 1.5
        tebal_font = 1
    elif tinggi > 400 and tinggi < 500:
        ukuran_font = 2
        tebal_font = 2
    elif tinggi > 500 and tinggi < 600:
        ukuran_font = 2.5
        tebal_font = 2
    elif tinggi > 600 and tinggi < 700:
        ukuran_font = 3
        tebal_font = 3
    elif tinggi > 700 and tinggi < 800:
        ukuran_font = 3.5
        tebal_font = 3
    elif tinggi > 800 and tinggi < 900:
        ukuran_font = 4
        tebal_font = 4
    elif tinggi > 900 and tinggi < 1000:
        ukuran_font = 4.5
        tebal_font = 4
    elif tinggi > 1000 and tinggi < 1100:
        ukuran_font = 5
        tebal_font = 5
    elif tinggi > 1100 and tinggi < 1200:
        ukuran_font = 5.5
        tebal_font = 5
    elif tinggi > 1200 and tinggi < 1300:
        ukuran_font = 6
        tebal_font = 6
    elif tinggi > 1300 and tinggi < 1400:
        ukuran_font = 6.5
        tebal_font = 6
    elif tinggi > 1400 and tinggi < 1500:
        ukuran_font = 7
        tebal_font = 7
    elif tinggi > 1500 and tinggi < 1600:
        ukuran_font = 7.5
        tebal_font = 7
    
    #ukuran_font = 0.3 * tinggi
    ukuran_huruf = cv2.getTextSize(baca, cv2.FONT_HERSHEY_SIMPLEX, ukuran_font, tebal_font)
    #print(baca)
    
    x1 = 10
    y1 = 10
    x2 = x1 + ukuran_huruf[0][0]
    y2 = y1 + ukuran_huruf[0][1]
    
    images[n] = cv2.rectangle(images[n], (x1,y1), (x2+10,y2+10), (0, 0, 0), cv2.FILLED)
    cv2.putText(images[n], str(baca), (x1+5,y2+5), cv2.FONT_HERSHEY_SIMPLEX, ukuran_font, (255,255,255), tebal_font)
    cv2.imwrite(os.path.join(savepath, onlyfiles[n]), images[n])
 
