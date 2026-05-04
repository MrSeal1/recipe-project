import ollama

def get_ingredients(image_data):
    try:
        response = ollama.chat(
            model='qwen3-vl:2b',
            messages=[
                {
                    'role': 'user',
                    'content': 'What food ingredients do you see on the image? Do not guess. Respond only with the english names of the items separated by commas.',
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