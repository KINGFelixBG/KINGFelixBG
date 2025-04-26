import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Model 3D Refraktometer", layout="centered")

st.title("🔬 Model 3D Refraktometer dengan Animasi")

st.write("Berikut adalah tampilan interaktif model 3D Refraktometer:")

components.html(
    """
    <model-viewer src="URL_FILE_GLB_KAMU.glb" 
      alt="Refraktometer 3D" 
      auto-rotate 
      camera-controls 
      ar 
      autoplay
      style="width: 100%; height: 500px;">
    </model-viewer>

    <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    """,
    height=550,
)
