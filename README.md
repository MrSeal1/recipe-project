# AI Vision Based Recipe Recommender

This project is an AI powered recipe search app. It can recognize food ingredients from a photo and use semantic search to find suitable recipes from a recipe book based on the available ingredients.

## Prerequisites
- Python
- Ollama: download from https://ollama.com/
- Local AI models: you can download the needed models using Ollama in your terminal:
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

### 1. Web Application (Recommended)
To launch the interactive graphical user interface:
1. Open your terminal in the project's `src` folder.
2. Run the following command:
    ```bash
    streamlit run app.py
    ```
3. Open the provided local URL in your web browser, upload an image, and explore the recommendations.

### 2. Command Line Interface (Testing)
To test the core logic via the terminal:
1. Ensure you have an image file available (e.g., `image2.jpg`).
2. Verify the file path in the `main.py` file.
3. Run the script:
    ```bash
    python main.py
    ```

## Architecture & Technical Details
The application is built on a hybrid architecture combining modern AI techniques with classic programmatic logic:
1. **Vision Processing:** Uses the `qwen3-vl:2b` multimodal model. The prompt is strictly instructed to return only a comma-separated list of English names to prevent hallucinations. The image data is passed directly from memory as bytes.
2. **Vector Embeddings:** Uses the `nomic-embed-text` model to convert both the found ingredients and the recipe text into vectors.
3. **Similarity Scoring:** Calculates the **cosine similarity** between the query vector and recipe vectors to rank the best matching recipes.
4. **Exact Matching:** The app uses set operations to calculate the list of available and missing ingredients.