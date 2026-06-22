from sentinel_x.modules.vision.service import vision_service
from sentinel_x.modules.nlp.service import nlp_service
from sentinel_x.modules.satellite.service import satellite_service
from sentinel_x.db.mongodb import get_database
from datetime import datetime
import numpy as np
import cv2

class FusionService:
    async def process_intelligence(self, image_bytes: bytes = None, audio_path: str = None, location: dict = None):
        """
        Orchestrate multiple AI pillars to produce a fused intelligence report.
        """
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "location": location,
            "findings": {}
        }

        # 1. Vision Processing
        if image_bytes:
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            report["findings"]["vision"] = vision_service.detect_objects(img)

        # 2. NLP Processing
        if audio_path:
            report["findings"]["nlp"] = nlp_service.transcribe_audio(audio_path)

        # 3. Satellite Context (Stub for now based on location)
        if location:
            report["findings"]["satellite"] = satellite_service.search_imagery(
                footprint=str(location), 
                date_range=("NOW-1MONTH", "NOW")
            )

        # 4. Save to MongoDB
        db = get_database()
        if db is not None:
            await db.intelligence.insert_one(report)
            
        return report

fusion_service = FusionService()
