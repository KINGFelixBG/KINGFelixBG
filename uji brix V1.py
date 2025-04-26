import streamlit as st
import time

# Set halaman
st.set_page_config(page_title="Uji Brix Minecraft", layout="centered")

# Session state
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "background_color" not in st.session_state:
    st.session_state.background_color = "#1e1e1e"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# CSS Minecraft-style + background
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    html, body, [class*="css"] {{
        font-family: 'Press Start 2P', cursive;
        background-image: url('https://static.wikia.nocookie.net/minecraft_gamepedia/images/8/8d/Grass_Block_JE4_BE3.png');
        background-size: cover;
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
    .back-button {{
        position: absolute;
        top: 10px;
        left: 10px;
        z-index: 999;
    }}
    </style>
""", unsafe_allow_html=True)

# Suara klik
st.markdown("""
<audio id="clickSound" src="https://freesound.org/data/previews/146/146725_2511580-lq.mp3"></audio>
<script>
function playClick() {
    document.getElementById("clickSound").play();
}
</script>
""", unsafe_allow_html=True)

# Fungsi loading
def loading(text="Loading..."):
    with st.spinner(text):
        time.sleep(2)

# Fungsi tombol kembali global
def back_button():
    with st
