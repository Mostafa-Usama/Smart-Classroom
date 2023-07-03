from roboflow import Roboflow
rf = Roboflow(api_key="GN6rbgSIiaObyAPShVga")
project = rf.workspace("assiut-university").project("head-detection-t4zes")
dataset = project.version(2).download("yolov8")