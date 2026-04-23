import os
from vision import get_ingredients

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

if __name__ == '__main__':
    main()