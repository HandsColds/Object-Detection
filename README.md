# image-recognition

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
  python .\detect.py --source C:\Users\32631\project\datasets\VOCData\images --weights runs\train\exp7\weights\best.pt
