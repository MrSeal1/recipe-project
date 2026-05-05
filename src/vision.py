import ollama

def get_ingredients(image_data):
    try:
        response = ollama.chat(
            model='qwen3-vl:2b',
            messages=[
                {
                    'role': 'user',
                    'content': """List out the foods or ingredients on the given image. Do not guess. Respond only with the english names of the items separated by commas. 
                                If there are no ingredients on the image, reply only with the following phrase: NO_FOOD_FOUND.
                                Make sure to not include any other things in the response other than the ingredient names, or the NO_FOOD_FOUND phrase if there are none. No explanations or flavor text.""",
                    'images': [image_data]
                }
            ]
        )
        
        content = response['message']['content']
        
        # feldarabolás, trimmelés és listává alakítás
        ingredients_list = [item.strip().lower() for item in content.split(',') if item.strip()]
        return ingredients_list
    
    except Exception as e:
        print(f"Exception when calling Ollama: {e}")
        return []