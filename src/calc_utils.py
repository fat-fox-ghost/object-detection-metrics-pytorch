""" Calculation utilities.

This module contains helper functions.

List of function names
----------------------
    - calculate_iou
"""
import numpy as np


def calculate_iou(bbox_1: np.ndarray, bbox_2: np.ndarray) -> float:
    """ Calculates the Intersection over Union value for 2 bounding boxes.

        Parameters
        ----------
        box1: np.ndarray
            The first bounding box.
        box2: np.ndarray
            The second bounding box.

        Returns
        -------
        float:
            The IOU value.
    """
    xa = np.maximum(bbox_1[0], bbox_2[0])
    ya = np.maximum(bbox_1[1], bbox_2[1])
    xb = np.minimum(bbox_1[2], bbox_2[2])
    yb = np.minimum(bbox_1[3], bbox_2[3])

    intersect_area = max(0, xb-xa) * max(0, yb-ya)

    bbox_1_area = (bbox_1[2] - bbox_1[0]) * (bbox_1[3] - bbox_1[1])
    bbox_2_area = (bbox_2[2] - bbox_2[0]) * (bbox_2[3] - bbox_2[1])

    return intersect_area / (bbox_1_area + bbox_2_area - intersect_area)
