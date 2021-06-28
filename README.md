# License-Plate-Recognition-Yolo
License plate recognition from video and photo

In this project, I trained my module with Google Colab, and then I added this trained file in python by using Yolov3.

1-Creating Dataset

First of all, we need to create a dataset of our model about what it is. We will download images and then mark the license plates on each image. To do this I used the app which name is 'LabelImg'
                                                                                                      
![image](https://user-images.githubusercontent.com/62347094/123666237-b2d96e80-d841-11eb-91df-cc9530678f23.png)

You can use this extension to download images
 
![image](https://user-images.githubusercontent.com/62347094/123666557-ffbd4500-d841-11eb-90ce-fd988a202c91.png)

And this is the app that I use

![image](https://user-images.githubusercontent.com/62347094/123666704-1fed0400-d842-11eb-9ccb-ad9517efc932.png)

![image](https://user-images.githubusercontent.com/62347094/123668086-6f7fff80-d843-11eb-865c-eb5164ec82de.png)


We mark each image that includes the license plates and we determine our class which name is License Plate.

2-Upload Files On Google Drive

After creating the dataset we are gonna create a file on google drive and upload it and then thanks to google colab we'll train our model

![image](https://user-images.githubusercontent.com/62347094/123668276-9fc79e00-d843-11eb-89a7-0e5213bc39c3.png)

3-Training Model With Google Colab

We completed our dataset and uploaded it on drive. Now, we'll train the model thanks to colab and 'Train_YoloV3_Multiple.ipynb'

![image](https://user-images.githubusercontent.com/62347094/123668903-3eec9580-d844-11eb-9697-124f510f529a.png)

![image](https://user-images.githubusercontent.com/62347094/123668969-4ca21b00-d844-11eb-9ec1-7a51d6e20800.png)

![image](https://user-images.githubusercontent.com/62347094/123668978-4f9d0b80-d844-11eb-850a-79f17479dc52.png)

Make sure select the GPU during the training

![image](https://user-images.githubusercontent.com/62347094/123669091-6a6f8000-d844-11eb-834c-6cbf58efdce6.png)

We opened .ipynb files and started to train our model by following the steps. Here we should arrange some changes like class name, class numbers, and configuration settings.

![image](https://user-images.githubusercontent.com/62347094/123669446-c20deb80-d844-11eb-90ae-e9e45d1f5b5d.png)

After complete all of the steps finally, we reached the files that we need. We are going to download the files ‘yolov3_training_last.weights’, ‘yolov3_testing.cfg’, 'classes.txt'.

4-Coding

We completed the hardest part now we will add these files in our .py files then we'll start coding to get the results.
You can access the codes from my directory.

5- Result

-VIDEO OR CAMERA-

![image](https://user-images.githubusercontent.com/62347094/123673076-b7555580-d848-11eb-996e-4114c2546ea3.png)

-IMAGE-

![image](https://user-images.githubusercontent.com/62347094/123673242-ebc91180-d848-11eb-8197-5160cd3aeccb.png)

![image](https://user-images.githubusercontent.com/62347094/123673298-f97e9700-d848-11eb-90e0-12b621672cc3.png)

![image](https://user-images.githubusercontent.com/62347094/123673338-04392c00-d849-11eb-9332-a1ef3959a843.png)

![image](https://user-images.githubusercontent.com/62347094/123673369-0ef3c100-d849-11eb-9b66-a402090c38b4.png)

![image](https://user-images.githubusercontent.com/62347094/123673428-20d56400-d849-11eb-9c90-696ce70f9bec.png)

I've tried to tell as far as I can
That's all for now
Have a nice day




