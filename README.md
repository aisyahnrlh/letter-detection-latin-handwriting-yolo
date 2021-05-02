# Letter Detection in Latin Handwriting using You Only Look Once (YOLO) Network

## 🎯Table of contents
* [Overview](#overview)
* [Demo](#demo)
* [Technologies](#technologies)
* [Steps](#steps)

## 🎯Overview
This project made to detect each letter in one-word Latin handwriting using the You Only Look Once (YOLO) network, one of the Convolutional Neural Networks’ algorithms. The experimental result shows processing time per one word is 0.0776 seconds with an accuracy of 81.93%. 

## 🎯Demo


## 🎯Technologies
* [labelImg](https://github.com/tzutalin/labelImg) ➡️ to label each letter in image and produce its annotation.
* [Darkflow](https://github.com/thtrieu/darkflow) ➡️ to train your weight, it translate darknet to tensorflow.
* [mAP](https://github.com/Cartucho/mAP) ➡️ to evaluates the performance of your network detection.

## 🎯Steps
Here's steps to make network for detect each letter in Latin Handwriting:

### **1. Data Acquisition**

The picture is taken using the camera. It would be better if you use a professional camera for better lighting and image quality.

![1](https://user-images.githubusercontent.com/68186227/116775015-f78b9800-aa92-11eb-90e0-bb9fc04cef3a.gif)

### **2. Grayscaling**

The purpose of the grayscaling process is to equate the color of the ink used on the paper so that the features and backgrounds can be distinguished. 

![3](https://user-images.githubusercontent.com/68186227/116775321-0b37fe00-aa95-11eb-9172-c5f19a1f3f8b.gif)

### **3. Image Upscaling**

Because the image quality I took was poor, I upscaled the image. I use [Smart Upscaler](https://icons8.com/upscaler) to upscale my image. Images can be upscaled up to 3000x3000px.

![2](https://user-images.githubusercontent.com/68186227/116775217-7503d800-aa94-11eb-9f34-8475dfefa2f7.gif)

### **4. Image Cropping**

The image is cropped into pieces so one image contains only one word. Also the size of cropped image is in square ratio.

![4](https://user-images.githubusercontent.com/68186227/116775618-8f3eb580-aa96-11eb-99c5-b97650c704e1.gif)

### **5. Change Predefined Class on labelImg**

Change **predefined_class.txt** file with your custom class. For this case, I wrote alphabet from A to Z.

![5](https://user-images.githubusercontent.com/68186227/116775825-c06bb580-aa97-11eb-9db7-a44801330f91.gif)

### **6. Image Labeling**

Use [labelImg](https://github.com/tzutalin/labelImg) to label every object within the image. Run command 

```
python labelimg.py
```

to run the code then you can label your own dataset. The result of this process is annotation that contain object's position within the image.

![6](https://user-images.githubusercontent.com/68186227/116775880-1cced500-aa98-11eb-951f-bb13e1273eea.gif)

### **7. Change Parameters on cfg File**

In Darkflow folder, you need to change cfg file before training the weight. The parameters I changed are:
```
Width = 416
Height = 416
Batch = 64
Subdivision = 32
Epoch = 1000
Learning Rate = 0.001
Class = 26
Filter in last two convolutional layer = num ∗ (classes + 5) where num = 5
```

![7](https://user-images.githubusercontent.com/68186227/116776084-65d35900-aa99-11eb-8d54-16dbb6bbe6bd.gif)

### **8. Change Class on Darkflow**

Change class on **labels.txt** file with with your custom class. Like the step 5, I wrote alphabet from A to Z.

![8](https://user-images.githubusercontent.com/68186227/116815960-a06cec80-ab92-11eb-9794-30370e0df6c3.gif)

### **9. Training Process**

Before start training, make sure your annotations & images dataset for training saved in **test/training/** directory. For testing dataset, make sure it's in the **sample_img/** directory. After that, run this command in the Darkflow directory.

```
!phyton3 flow --model cfg/[your cfg file's name] --load bin/[your weight's file name] --train --annotation [your annotations' foldername] --dataset [your images foldername]
```

After the training process is done, you run the command below to save your new weight. It will saved in **built_graph/** folder.

```
!python3 flow --model cfg/[your cfg file's name] --load -1 --savepb
```

### **10. Try New Weights on Testing Dataset**

After you made your new weight, try the weight using **image_detect.py** or **image_read.py** with command

```
python image_detect.py or python image_read.py
```

the result saved in **[your directory]/out/** folder

![9](https://user-images.githubusercontent.com/68186227/116817423-d6ad6a80-ab98-11eb-97a8-684c6c3f27bc.gif)

### **11. See the Results and Evaluate by Measure mAP**

You can measure your weight's accuracy using [mAP](https://github.com/Cartucho/mAP). Checkout the repos for more.

## 🎯Notes
1. This step can be used for all types of datasets. You just adjust the parameters in order to produce the desired weight.
2. Based on my experiments result, YOLO is optimal for large objects so far. That's why I decided to crop the image so the letter in image is bigger.
3. Training process involved Google Colaboratory. It is okay to use your own computer.
4. Please give me feedbacks in order to improve my skills.

**Made with ❤️ by Aisyah Nurul Hidayah**
