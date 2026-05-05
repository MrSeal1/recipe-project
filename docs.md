# Technical Documentation

## 1. System Architecture
The project uses a hybrid approach to recipe searching:
- Vision processing: uses a multimodal LLM to extract text from image data
- Semantic search: uses vector embeddings and cosine similarity to find recipes that are semantically similar to the available ingredients
- Exact matching: uses set operations to calculate the status (available or missing) of ingredients for each recipe

## 2. Modules
### `vision.py`
- Responsibility: extract a list of ingredients from an image
- Uses Ollama API using the `qwen3-vl:2b` model
- The function receives raw image bytes, avoiding IO operations. The model uses a strict prompt to return only a list of English ingredient names seperated by commas.

### `vector_db.py`
- Responsibility: semantic ranking of recipes and management of text embeddings
- Uses `nomic-embed-text` model for embeddings and Numpy for calculating cosine similarity.
- Includes an embedding cache that stores pre-calculated recipe vectors to speed up multiple searches

### `app.py`
- Responsibility: serves the web-based UI and coordinates data flow
- User flow:
    - reads uploaded image
    - retrieves ingredients using `vision.py`
    - finds best matches using `vector_db.py`
    - performs set operations to determine available ingredients

### `main.py`
- Used for testing backend functions from the terminal

## 3. Data
Recipes are stored in the `recipes.json` file in the `data` folder. It includes the names, ingredients and instructions of a set number of recipes in a json format.