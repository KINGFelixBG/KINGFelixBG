import streamlit as st
import time

# Setup Page
st.set_page_config(page_title="Uji Brix Minecraft Style", layout="centered")

# Inisialisasi session_state
if 'page' not in st.session_state:
    st.session_state['page'] = 'menu'
if 'background_color' not in st.session_state:
    st.session_state['background_color'] = '#1e1e1e'  # Default warna gelap

# Inject CSS untuk Minecraft Style
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    html, body, [class*="css"] {{
        font-family: 'Press Start 2P', cursive;
        background-color: {st.session_state['background_color']};
        color: white;
    }}
    .stButton>button {{
        background-color: #5a5a5a;
        color: white;
        border: 2px solid #00ff00;
        border-radius: 4px;
        padding: 10px 15px;
        font-size: 12px;
        transition: 0.2s;
    }}
    .stButton>button:hover {{
        background-color: #3e3e3e;
        border-color: #00cc00;
    }}
    .stApp {{
        text-align: center;
        margin-top: 50px;
    }}
    </style>
""", unsafe_allow_html=True)

# Tambahkan Sound Click
st.markdown("""
    <audio id="clickSound" src="https://freesound.org/data/previews/146/146725_2511580-lq.mp3"></audio>
    <script>
    function playClick() {
        var audio = do

