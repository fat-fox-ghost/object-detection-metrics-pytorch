import numpy as np


def get_iou(bbox_1: np.ndarray, bbox_2: np.ndarray):
    """ The function calculates the intersection over union (IOU) value
        for 2 bounding boxes.

        Arguments:
        ----------
        box1: list
            The first bounding box (see get_bbox()).
        box2: list
            The second bounding box.

        Returns:
        --------
        float:
            The IOU value.
    """
    xa = max(box1[0], box2[0])
    ya = max(box1[1], box2[1])
    xb = min(box1[2], box2[2])
    yb = min(box1[3], box2[3])

    intersect_area = max(0, xb-xa) * max(0, yb-ya)

    box1_area = (box1[2]-box1[0]) * (box1[3]-box1[1])
    box2_area = (box2[2]-box2[0]) * (box2[3]-box2[1])

    return intersect_area / (box1_area + box2_area - intersect_area)

