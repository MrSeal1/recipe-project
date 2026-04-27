import os
from vision import get_ingredients
from vector_db import find_best_recipes

def main():
    image_path = '../image2.jpg' 
    
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
    
    found_set = set(ingredients)
    
    print("\n--- BEST RESULTS ---")
    for rank, (score, recipe) in enumerate(best_matches, 1):
        match_percentage = round(score * 100, 1)
        
        recipe_ingredients = [item.strip().lower() for item in recipe['ingredients']]
        recipe_set = set(recipe_ingredients)
        
        missing_ingredients = recipe_set - found_set
        available_ingredients = recipe_set.intersection(found_set)
        
        print(f"\n#{rank} - {recipe['name']} (Match: {match_percentage}%)")
        
        if available_ingredients:
            print(f"Available ingredients: {', '.join(available_ingredients)}")
        
        if missing_ingredients:
            print(f"Missing ingredients: {', '.join(missing_ingredients)}")
        else:
            print("You have all needed ingredients for this recipe!")
            
        print(f"Instructions: {recipe['instructions']}")

if __name__ == '__main__':
    main()