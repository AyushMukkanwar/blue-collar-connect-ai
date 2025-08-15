# 🤖 Blue Collar Connect AI

<div align="center">

![Blue Collar AI](https://img.shields.io/badge/Blue%20Collar-AI%20Assistant-blue?style=for-the-badge&logo=robot)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

**Intelligent RAG Chatbot for Blue-Collar Workers**

*Providing real-time assistance on labor laws, wages, job schemes, and worker rights*

</div>

---

## 🎯 Overview

Blue Collar Connect AI is a **Retrieval-Augmented Generation (RAG)** system designed for blue-collar workers. It provides intelligent, context-aware responses about labor laws, wages, government schemes, workplace rights, and career guidance using Google's Gemini language model with advanced document retrieval.

### 🌟 Key Features

- **Labor Law Expertise** – Worker rights and regulations
- **Wage Intelligence** – Salary data and negotiation guidance
- **Government Schemes** – Support programs and benefits
- **Safety Information** – Workplace safety protocols
- **Multilingual Support** – Multiple regional languages

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **API Framework** | FastAPI | High-performance async API server |
| **LLM Engine** | Google Gemini | Advanced language understanding |
| **RAG Framework** | LangChain | Document processing & retrieval |
| **Workflow Engine** | LangGraph | Complex conversation flows |
| **Vector Database** | ChromaDB | Semantic search & embeddings |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Cloud Project with Vertex AI enabled
- Google Cloud credentials

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create `.env` file:

```env
# Google Cloud
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_API_KEY=your-google-api-key
GOOGLE_MODEL_ID=gemini-1.5-pro

# ChromaDB
CHROMA_DB_PATH=./data/chroma_db
COLLECTION_NAME=blue_collar_knowledge

# API
API_HOST=0.0.0.0
API_PORT=8000
```

### Initialize & Start

```bash
# Initialize knowledge base
python scripts/initialize_db.py

# Start server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

🎉 **Server running at [http://localhost:8000](http://localhost:8000)**

---

## 📡 API Endpoints

### Chat Interface

#### `POST /chat`
```python
# Request
{
    "message": "What are my rights regarding overtime pay?",
    "user_id": "user123",
    "session_id": "session456"
}

# Response
{
    "response": "According to labor law, you are entitled to...",
    "sources": [...],
    "session_id": "session456"
}
```

#### `POST /chat/stream`
Real-time streaming responses using Server-Sent Events.

### Management

- `GET /health` - System health check
- `POST /knowledge/upload` - Upload documents
- `GET /knowledge/stats` - Knowledge base statistics

---

## 📁 Project Structure

```
ai/
├── main.py                    # FastAPI entry point
├── requirements.txt           # Dependencies
├── src/                      # Source code
│   ├── rag_engine.py         # Core RAG implementation
│   ├── models.py             # Data models
│   └── config.py             # Configuration
├── routers/                  # API routes
│   ├── chat.py               # Chat endpoints
│   └── health.py             # Health checks
├── data/                     # Data storage
│   ├── documents/            # Source documents
│   └── chroma_db/            # Vector database
└── tests/                    # Test suite
```

---

## 🚀 Deployment

### Docker
```bash
docker build -t blue-collar-ai .
docker run -p 8000:8000 blue-collar-ai
```

### Google Cloud Run
```bash
gcloud run deploy blue-collar-ai \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 📊 Performance

- **Response Time**: < 2 seconds
- **Throughput**: 100+ requests/minute  
- **Memory Usage**: < 2GB
- **Vector Search**: < 100ms

---

## 🔧 Troubleshooting

### Common Issues

**ChromaDB Connection**
```bash
rm -rf data/chroma_db
python scripts/initialize_db.py
```

**Authentication Errors**
```bash
gcloud auth application-default login
```

**Slow Responses**
```python
# Adjust in config
CHUNK_SIZE=500
MAX_RETRIEVED_DOCS=3
SIMILARITY_THRESHOLD=0.8
```

---

## 🧪 Testing

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest tests/ -v

# With coverage
pytest --cov=src tests/
```

---

## 🆘 Support

<div align="center">

[![Email Support](https://img.shields.io/badge/📧%20Email-AI%20Support-blue?style=for-the-badge)](mailto:bluecollarconnectcompany@gmail.com?subject=AI%20Module%20Support)
[![GitHub Issues](https://img.shields.io/badge/🐛%20Issues-GitHub-red?style=for-the-badge)](https://github.com/AyMk544/blue-collar-connect/issues)

</div>

---

## 📄 License

MIT License - see [LICENSE](../LICENSE) file for details.

---

<div align="center">

**🤖 Empowering workers through intelligent AI assistance 🤖**

</div>
