# 🛡️ SENTINEL-X — Multimodal AI Intelligence Platform

SENTINEL-X is a unified, production-grade AI platform designed for national security, climate monitoring, and sustainability in Nigeria and across Africa. It fuses real-time computer vision, NLP, satellite intelligence, and explainable AI into a single actionable intelligence core.

## 🚀 Key Pillars

- **👁️ Multimodal Computer Vision**: YOLOv8 + SAM for real-time person tracking, crowd density, and threat detection.
- **📡 Remote Sensing**: Direct ESA Sentinel-2 ingestion for NDVI analysis and land-use change detection.
- **🎙️ Multilingual NLP**: Faster-Whisper + AfroXLMR for transcribing and scoring sentiment across Hausa, Yoruba, Igbo, and English.
- **🤝 Unified Fusion**: A "Single Brain" ingestion engine that correlates vision, audio, and satellite data.
- **🔍 Explainable AI (XAI)**: SHAP-based attribution to explain *why* the AI flags specific events.
- **🔒 Federated Learning**: Privacy-preserving model training across distributed nodes (Coming Soon).

---

## 🛠️ Tech Stack (100% Free & Open Source)

- **Backend**: FastAPI, Uvicorn
- **Intelligence**: PyTorch, Ultralytics, Transformers, Faster-Whisper, SHAP
- **Data**: MongoDB (NoSQL), Redis (Task Queue)
- **GIS**: Rasterio, GDAL, Sentinelsat
- **Deployment**: Local Virtualenv / Manual (Optimized for Bare Metal)

---

## 📂 Project Structure

```text
sentinel_x/
├── api/                # FastAPI routes and versioning
├── core/               # App configuration and global security
├── db/                 # MongoDB/NoSQL connection logic
├── modules/            # The 6 core technical pillars
│   ├── vision/         # Computer Vision Service
│   ├── nlp/            # Speech & NLP Service
│   ├── satellite/      # Remote Sensing Service
│   ├── xai/            # Explainable AI Service
│   └── fusion/         # Intel Orchestration Service
├── tests/              # Pytest suite
└── main.py             # Application entry point
```

---

## 🛠️ Getting Started for Contributors

### 1. Prerequisites
- Python 3.10+
- MongoDB installed and running locally
- Redis installed and running locally

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Uszkido/sentinel-x.git
cd sentinel-x

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

### 4. Running the Platform
```bash
python main.py
```
Access the API docs at `http://localhost:8000/docs`.

---

## 🤝 Contributing

We welcome contributions from the African AI community! 
1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---
**Developed with ❤️ for Nigeria by [Uszkido](https://github.com/Uszkido)**
