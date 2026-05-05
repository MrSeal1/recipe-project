import streamlit as st
from vision import get_ingredients
from vector_db import find_best_recipes
from PIL import Image

st.set_page_config(page_title="AI Recipe Recommender", layout="wide")

st.title("AI Recipe Recommender")
st.write("Upload a photo of your ingredients to discover matching recipes.")

with st.sidebar:
    st.header("How it works")
    st.write("1. Upload an image of your ingredients.")
    st.write("2. The AI identifies the items.")
    st.write("3. Semantic search finds the best matching recipes.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)
    
    image_bytes = uploaded_file.getvalue()

    with st.spinner('Identifying ingredients...'):
        try:
            ingredients = get_ingredients(image_bytes)
            
            if 'no_food_found' in ingredients:
                st.error('Please upload an image containing ingredients.')            
            elif ingredients:
                with col2:
                    st.success("### Identified Ingredients")
                    st.write(", ".join([f"**{i}**" for i in ingredients]))
                    
                    st.divider()
                    
                    best_matches = find_best_recipes(ingredients, top_k=3)
                    found_set = set(ingredients)
                    
                    st.write("### Recommended Recipes")
                    
                    for score, recipe in best_matches:
                        match_pct = int(score * 100)
                        
                        with st.expander(f"{recipe['name']} ({match_pct}% match)"):
                            
                            r_ingredients = [item.strip().lower() for item in recipe['ingredients']]
                            recipe_set = set(r_ingredients)
                            
                            missing = recipe_set - found_set
                            available = recipe_set.intersection(found_set)
                            
                            c1, c2 = st.columns(2)
                            with c1:
                                st.write("**Available:**")
                                for item in available:
                                    st.write(f"- {item}")
                            with c2:
                                if missing:
                                    st.write("**Missing:**")
                                    for item in missing:
                                        st.write(f"- {item}")
                                else:
                                    st.write("Done! **You have all the ingredients.**")
                            
                            st.write("**Instructions:**")
                            st.info(recipe['instructions'])
            else:
                st.error("Could not recognize any ingredients in the image.")
                
        except Exception as e:
            st.error(f"An error occurred during processing: {e}")
        