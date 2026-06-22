from sklearn.ensemble import IsolationForest
import numpy as np
import pandas as pd

class AnomalyDetector:
    def __init__(self):
        # Isolation Forest is excellent for outlier detection in high-dimensional data
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.is_trained = False

    def train(self, historical_data: list):
        """
        Train the model on historical threat features.
        """
        if not historical_data:
            return
        
        df = pd.DataFrame(historical_data)
        # Assuming features are pre-extracted numerical values (e.g. counts, scores)
        self.model.fit(df)
        self.is_trained = True

    def detect(self, current_features: list):
        """
        Detect if the current intelligence report is an anomaly.
        Returns: 1 for normal, -1 for anomaly.
        """
        if not self.is_trained:
            # Fallback for small initial datasets: simple thresholding
            return 1 if np.mean(current_features) < 0.8 else -1
            
        prediction = self.model.predict([current_features])
        return int(prediction[0])

anomaly_detector = AnomalyDetector()
