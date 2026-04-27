import os
from vision import get_ingredients
from vector_db import find_best_recipes

def main():
    image_path = '../image.jpg' 
    
    if not os.path.exists(image_path):
        print(f"Error: the file ({image_path}) does not exist")
        exit()

    ingredients = get_ingredients(image_path)
    
    if ingredients:
        print(f"\nIngredients list: {ingredients}")
    else:
        print("Could not recognize ingredients.")
        exit()
        
    print("-" * 40)
    print("Analyzing recipebook...")
    
    best_matches = find_best_recipes(ingredients, top_k=2)
    
    print("\n--- BEST RESULTS ---")
    for rank, (score, recipe) in enumerate(best_matches, 1):
        match_percentage = round(score * 100, 1)
        print(f"\n#{rank} - {recipe['name']} (Match: {match_percentage}%)")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Instructions: {recipe['instructions']}")

if __name__ == '__main__':
    main()