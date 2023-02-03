import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./detect_compo/weights/yolov5.pt')

jpg = '11'
path_img = f'D:\\_proj_dev\\UIED\\data\\local\\input\\{jpg}.jpg'

result = model(path_img)

result.show()