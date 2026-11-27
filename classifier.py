from pathlib import Path
from PIL import Image
import streamlit as st
from ultralytics import YOLO

DEFAULT_MODEL_PATH = "saved_models/yolo26l-cls-best.pt"
IMG_SIZE = 320

st.set_page_config(page_title="Recyclify", layout="wide")


st.markdown("<h1 style='text-align: center;'>♻️ Recyclify</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload an image to identify the waste type.</p>", unsafe_allow_html=True)
st.divider()

@st.cache_resource
def load_classifier(weights_path: str) -> YOLO:
    return YOLO(weights_path)

model_path = DEFAULT_MODEL_PATH
if not Path(model_path).exists():
    st.error(f"Model file not found: `{model_path}`")
    st.stop()

model = load_classifier(model_path)


col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📸 Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png", "bmp", "webp"],
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Input Image", use_container_width=True)

with col2:
    if uploaded_file is not None:
        st.subheader("🔍 Prediction Results")
        with st.spinner("Running inference..."):
            results = model.predict(source=image, imgsz=IMG_SIZE, verbose=False)

        probs = results[0].probs
        names = results[0].names

        top1_idx = probs.top1
        top1_label = names[top1_idx]
        top1_conf = probs.top1conf.item()

        
        st.metric(label="Top Prediction", value=top1_label.capitalize(), delta=f"{top1_conf:.2%}")
        
        st.markdown("---")
        
        
        top_indices = probs.top5
        top_confs = probs.top5conf.tolist()
        
        st.subheader("Top-5 Predictions")
        
        
        data = [{"Class": names[idx].capitalize(), "Confidence": conf} for idx, conf in zip(top_indices, top_confs)]
        
        st.bar_chart(
            {names[idx].capitalize(): conf for idx, conf in zip(top_indices, top_confs)},
            horizontal=True
        )
        
        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Please upload an image to see results.")
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; padding: 20px;">
    <p>Made by bruzz-bruzz</p>
    <div style="display: flex; justify-content: center; gap: 20px;">
        <a href="https://github.com/bruzz-bruzz" target="_blank">GitHub Profile</a>
        <a href="https://github.com/bruzz-bruzz/waste-image-classifier" target="_blank">GitHub Repository</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)
