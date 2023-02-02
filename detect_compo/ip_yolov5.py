import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./detect_compo/weights/yolov5.pt')

path_img = './data/input/1.jpg'

result = model(path_img)

result.show()