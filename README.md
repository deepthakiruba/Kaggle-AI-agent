# Kaggle-AI-agent
InstaWise — Multi-Agent Instagram Captioning &amp; Posting Assistant

# InstaWise — Multi-Agent Instagram Captioning Assistant

## Overview
InstaWise is a multi-agent AI system that:
- Analyzes images using CLIP
- Generates 3 caption styles using an LLM
- Produces optimized hashtags
- Suggests best posting times
- (Optional) Posts to Instagram via Meta API

Built using:
- FastAPI backend
- Streamlit UI
- CLIP (HuggingFace)
- LLM-based Text Generation (OpenAI or local)
- Custom Hashtag + Time Agents

## Features
✔ Upload image/video  
✔ Auto vision analysis  
✔ Auto caption generation  
✔ Auto hashtag optimization  
✔ Posting time recommendation  
✔ Modular agent architecture  
✔ Extendable for real Instagram API posting  

## Directory Structure
```
starter_code/
starter_clip/
docs/
README.md
```

## How to Run
1. Create environment:
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

2. Install dependencies:
```
pip install -r starter_code/requirements.txt
```

3. Start backend:
```
uvicorn starter_code.app:app --reload --port 8000
```

4. Start UI:
```
streamlit run starter_code/streamlit_app.py
```

5. Upload an image → Get captions → Get hashtags → Get posting times.

## Agents
- Vision Agent → CLIP labels & structured summary  
- Caption Agent → LLM prompt, 3 variants  
- Hashtag Agent → keyword extraction + scores  
- Time Agent → category-based scheduling  
- Poster Agent → optional, Meta API  

## License
MIT License

