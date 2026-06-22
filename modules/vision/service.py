import cv2
import numpy as np
from ultralytics import YOLO
from segment_anything import sam_model_registry, SamPredictor
from sentinel_x.core.config import settings
import torch

class VisionService:
    def __init__(self):
        # Load YOLOv8
        self.yolo_model = YOLO(settings.YOLO_MODEL_PATH)
        
        # Load SAM (placeholder for initialization as it requires model weights)
        self.sam_predictor = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def detect_objects(self, image: np.ndarray):
        """
        Detect objects in an image using YOLOv8.
        """
        results = self.yolo_model(image)
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                    "class": self.yolo_model.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": box.xyxy[0].tolist()
                })
        return detections

    def segment_objects(self, image: np.ndarray, bboxes: list):
        """
        Segment objects in an image using SAM given bounding boxes.
        """
        if self.sam_predictor is None:
            # In a real scenario, weights would be pre-downloaded
            # sam = sam_model_registry["vit_h"](checkpoint="sam_vit_h_4b8939.pth")
            # sam.to(device=self.device)
            # self.sam_predictor = SamPredictor(sam)
            return {"error": "SAM weights not loaded"}
        
        self.sam_predictor.set_image(image)
        segmentations = []
        for bbox in bboxes:
            input_box = np.array(bbox)
            masks, scores, logits = self.sam_predictor.predict(
                box=input_box,
                multimask_output=False,
            )
            segmentations.append(masks[0].tolist())
        return segmentations

vision_service = VisionService()
