from roboflow import Roboflow
from ultralytics import YOLO

# rf = Roboflow(api_key="")
# project = rf.workspace("patst").project("gta-fishing")
# dataset = project.version(2).download("yolov8")

# rf = Roboflow(api_key="")
# project = rf.workspace("manfred-schaut-zu-y6xxp").project("fischengta")
# dataset = project.version(1).download("yolov8")

# rf = Roboflow(api_key="")
# project = rf.workspace("manfred-schaut-zu-y6xxp").project("fischengta")
# dataset = project.version(2).download("yolov8")

# rf = Roboflow(api_key="")
# project = rf.workspace("patst").project("gta-fishing")
# dataset = project.version(3).download("yolov8")

preModel = [
    "yolov8s.pt",
    "./runs/detect/train/weights/best.pt",
    "./runs/detect/train2/weights/best.pt"
]

datasets = [
    "datasets/fischengta-1/data.yaml",
    "datasets/fischengta-2/data.yaml",
    "datasets/gta-fishing-3/data.yaml"
]

for (modelName, dataset) in zip(preModel, datasets):
    print(modelName, dataset)
    model = YOLO(modelName)
    results = model.train(
        data=dataset,
        epochs=30,
        device="cpu",
        cache="ram",
        pretrained=True)
