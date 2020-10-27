import json

def saveRoiData(data, outputPath):
    transformedData = []
    for frame in data:
        transformedData.append(transform(frame, data[frame]))

    with open(outputPath, 'w') as outfile:
        json.dump(transformedData, outfile, indent=2, sort_keys=True)

def transform(frame, rois):
    return {
        "boxes": list(map(transformBox, rois)),
        "labels": [0] * len(rois),
        "image_id": frame,
        "area": list(map(transformArea, rois)),
        "iscrowd": False   
    }

def transformBox(box):
    xs = sorted([box[0], box[2]])
    ys = sorted([box[1], box[3]])
    return [xs[0], ys[0], xs[1], ys[1]]

def transformArea(box):
    return abs((box[0]-box[2])*(box[1]-box[3]))