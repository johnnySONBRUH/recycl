import streamlit as st

def get_about_info():
    return {
        "title": "Recyclify",
        "description": """
This application leverages deep learning to classify various types of waste images. 
By utilizing the YOLOv8 (You Only Look Once) architecture, the model provides fast and accurate real-time classification.

### Features
* **Real-time Inference:** Fast image classification using state-of-the-art computer vision models.
* **Top-5 Confidence Score:** Visualize the top 5 predicted categories along with their confidence levels.
* **Intuitive UI:** A clean, user-friendly interface powered by Streamlit.

### How it Works
1. **Upload:** Upload your waste image (JPG, JPEG, PNG, BMP, or WebP).
2. **Predict:** The model processes the image to identify the waste category.
3. **Analyze:** View the top prediction and explore the top 5 confidence scores.

### Technologies
* **Model:** YOLOv8 (Image Classification)
* **Framework:** Streamlit
* **Language:** Python
""",
        "author": "bruzz-bruzz"
    }

info = get_about_info()

st.title("ℹ️ About")
st.header(info["title"])
st.markdown(info["description"])
st.markdown("---")
st.caption(f"Developed by {info['author']}")
