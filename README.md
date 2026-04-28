# AI Vision Based Recipe Recommender

This project is an AI powered recipe search app. It can recognize food ingredients from a photo and use semantic search to find suitable recipes from a recipe book based on the available ingredients.

## Prerequisites
- Python
- Ollama: download from https://ollama.com/
- Models: you can download the needed models using Ollama in your terminal:
    ```
    ollama pull qwen3-vl:2b
    ollama pull nomic-embed-text
    ```

## Installation
1. Clone repository
2. Create and activate a virtual environment
3. Install Python dependencies (with  `pip install` or `uv add`):
    - opencv-python
    - ollama

## Usage
1. Place an image in the projects root folder
2. Check `main.py` and input the correct file path (default is `../image.jpg`)
3. Run `main.py`

