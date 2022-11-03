from flask import Flask, render_template, request, Response, jsonify
from com_convert_image.utils import decodeImage
from flask import request
import torch
from pathlib import Path
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        image = request.json['image']
        # decodeImage(image, clApp.filename)
        # result = clApp.objectDetection.inference('file.jpg')

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"
    return jsonify(result)

if __name__ == '__main__':
    # device = torch.device('cpu')
    # model = TheModelClass(*args, **kwargs)
    # model.load_state_dict(torch.load(PATH, map_location=device))
    # model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True) 
    #dirs = os.path.dirname()
    pa = Path("yolov5/runs/train/yolov5s_results/weights/best.pt")
    # print("soem", os.getcwd())
    model = torch.load(pa)
    app.run()
