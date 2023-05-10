# Yolov5 for somking image-recognition
In many places, people are violating the regulations or smoking secretly. This detection is to identify whether there are people violating the regulations in the image
# Install
Clone this repo and use the following script to install YOLOv5.
# Train code
  --IMG Set Image Size  
  --Batch sets the amount of data sent into the model for each batch, commonly known as batch size  
  --Epochs sets the number of training rounds  
  --Set the path of the yaml file that was just configured with data  
  --Weights setting models (pre trained model on Coco dataset)  
  
  python train.py --img 640 --batch 16 --epochs 10 --data myvoc.yaml --weights yolov5s.pt
  
# run 
  --Source is the directory of the target dataset, which contains all image files that need to be inferred  
  --Weights is the selection of previously trained models  
  fold---yolov5
       |--datasets
  python .\detect.py --source ...\datasets\VOCData\images --weights runs\train\exp\weights\best.pt

# Results
The following charts were produced after training YOLOv5s with input size 640x640 on the fire dataset for 10 epochs.

P_curve   PR_curve  R_curve
<img src="/results/P_curve.png" width="200" height="100"> <img src="/results/PR_curve.png" width="200" height="100"> <img src="/results/R_curve.png" width="200" height="100">


