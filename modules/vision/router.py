from fastapi import APIRouter, UploadFile, File
from sentinel_x.modules.vision.service import vision_service
import cv2
import numpy as np
import io

router = APIRouter()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    detections = vision_service.detect_objects(img)
    return {"detections": detections}

@router.post("/analyze-stream")
async def analyze_stream(url: str):
    # This would typically trigger an async task to process an RTSP stream
    return {"message": f"Analysis started for stream: {url}", "task_id": "placeholder-task-id"}
