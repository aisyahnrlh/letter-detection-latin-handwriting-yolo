# Letter Detection in Latin Handwriting using You Only Look Once (YOLO) Network

## 🎯Table of contents
* [Overview](#overview)
* [Demo](#demo)
* [Technologies](#technologies)
* [Setup](#setup)

## 🎯Overview
This project made to detect each letter in one-word Latin handwriting using the You Only Look Once (YOLO) network, one of the Convolutional Neural Networks’ algorithms. The experimental result shows processing time per one word is 0.0776 seconds with an accuracy of 81.93%. 

## 🎯Demo


## 🎯Technologies
Labeling
Darkflow
mAP

## 🎯Setup
1. data acquisition
2. image upscaling for better quailty
3. grayscaling
4. crop the image so one image contains only one word (size is in square ratio)
5. change predefined_class on labelimg
6. image labeling
7. change parameter on cfg file
8. change class on darkflow
9. start training with command phyton3 flow --model cfg/name --load bin/weights --train --annotation test/training/foldername --dataset test/training/foldername
10. try your new weights on testing dataset using image_detection.py or image_reading.py
11. see the results

## 🎯Notes
step ini bisa digunakan untuk semua jenis dataset tinggal menyesuaikan paramaternya agar dapat menghasilkan weight yang diinginkan
yolo optimal untuk obyek yang besar saja, maka dari itu saya memutuskan untuk crop gambar
please give me feedbacks in order to improve my skills

**Made with ❤️ by Aisyah Nurul Hidayah**
