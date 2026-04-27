import json
import numpy as np
import ollama

def get_embedding(text):
    response = ollama.embeddings(model='nomic-embed-text', prompt=text)
    return response['embedding']

def cosine_similarity(vec1, vec2):
    norm_a, norm_b = np.linalg.norm(vec1), np.linalg.norm(vec2)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return np.dot(vec1, vec2) / (norm_a * norm_b)

def find_best_recipes(found_ingredients, top_k=2):
    json_path = '../data/recipes.json'
    
    with open(json_path, 'r', encoding='utf-8') as f:
        recipes = json.load(f)
        
    query_vector = np.array(get_embedding(", ".join(found_ingredients)))
    scored_recipes = []
    
    for recipe in recipes:
        recipe_text = f"{recipe['name']} {', '.join(recipe['ingredients'])}"
        recipe_vector = np.array(get_embedding(recipe_text))
        
        score = cosine_similarity(query_vector, recipe_vector)
        scored_recipes.append((score, recipe))
        
    scored_recipes.sort(key=lambda x: x[0], reverse=True)
    return scored_recipes[:top_k]