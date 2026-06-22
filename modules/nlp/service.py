from faster_whisper import WhisperModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from sentinel_x.core.config import settings
import torch

class NLPService:
    def __init__(self):
        # Initialize faster-whisper (Local OSS)
        self.whisper_model = WhisperModel(settings.WHISPER_MODEL, device="cpu", compute_type="int8")
        
        # Initialize AfroXLMR for multilingual threat detection
        # This model is great for code-switching and Nigerian languages
        self.threat_tokenizer = AutoTokenizer.from_pretrained("Davlan/afro-xlmr-large")
        # Placeholder for a fine-tuned model; using a generic one for now
        self.classifier = pipeline("sentiment-analysis", model="Davlan/afro-xlmr-large")

    def transcribe_audio(self, audio_path: str):
        """
        Transcribe audio using faster-whisper.
        """
        segments, info = self.whisper_model.transcribe(audio_path, beam_size=5)
        text = " ".join([segment.text for segment in segments])
        return {
            "text": text,
            "language": info.language,
            "probability": info.language_probability
        }

    def detect_threats(self, text: str):
        """
        Detect threats/violence in text using AfroXLMR.
        """
        results = self.classifier(text)
        return results

nlp_service = NLPService()
