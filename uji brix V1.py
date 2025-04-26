import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Uji Brix Minecraft", layout="centered")

# Initialize session states
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "play_music" not in st.session_state:
    st.session_state.play_music = True
if "volume" not in st.session_state:
    st.session_state.volume = 0.5  # default volume 50%
if "font_choice" not in st.session_state:
    st.session_state.font_choice = "Times New Roman"

# Function for loading spinner
def loading(text="sedang proses sahabat"):
    with st.spinner(text):
        time.sleep(1.2)

# Function for background
def get_background_url():
    if st.session_state.page == "perhitungan":
        return "https://e0.pxfuel.com/wallpapers/891/197/desktop-wallpaper-minecraft-backround-minecraft-scenery.jpg"
    elif st.session_state.page == "rumus":
        return "https://c4.wallpaperflare.com/wallpaper/446/712/946/minecraft-bookshelves-hd-wallpaper-preview.jpg"
    elif st.session_state.page == "alat":
        return "https://img.freepik.com/free-photo/close-up-scientific-equipment-laboratory_23-2148916225.jpg"
    elif st.session_state.page == "opsi":
        return "https://wallpaperaccess.com/full/2682775.png"
    else:
        return "https://i.pinimg.com/736x/f7/4c/e6/f74ce6007b53858d32503641f6dd88ba.jpg"

# Apply CSS
bg_url = get_background_url()
st.markdown(f"""
    <style>
    html, body, [class*="css"] {{
        font-family: {st.session_state.font_choice}, sans-serif;
        background: url('{bg_url}') no-repeat center center fixed;
        background-size: cover;
    }}
    .stApp {{
        animation: fadeIn 1s;
    }}
    @keyframes fadeIn {{ 0% {{opacity: 0;}} 100% {{opacity: 1;}} }}
    .stButton>button {{
        font-family: 'Press Start 2P', cursive;
        background-color: #5a5a5a;
        border: 3px solid #00ff00;
        border-radius: 8px;
        padding: 12px 18px;
        margin: 10px auto;
        width: 300px;
        font-size: 14px;
        color: white;
        text-align: center;
        display: block;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #3e3e3e;
        border-color: #00cc00;
    }}
    </style>
""", unsafe_allow_html=True)

# Music player
def embed_music():
    if st.session_state.play_music and st.session_state.page in ["menu", "perhitungan"]:
        volume = st.session_state.volume
        st.markdown(f"""
        <audio id="audioPlayer" autoplay loop>
            <source src="https://vgmsite.com/soundtracks/minecraft-volume-beta/hbceziht/12%20-%20Wet%20Hands.mp3" type="audio/mpeg">
        </audio>
        <script>
        var audio = document.getElementById('audioPlayer');
        audio.volume = {volume};
        </script>
        """, unsafe_allow_html=True)

# Tiny music toggle button
def music_toggle_icon():
    icon = "🔊" if st.session_state.play_music else "🔇"
    col = st.columns([0.95, 0.05])[1]
    with col:
        if st.button(icon, key="music_toggle"):
            st.session_state.play_music = not st.session_state.play_music

# Navigation back to menu
def back_button():
    if st.button("🏠 Kembali ke Menu"):
        st.session_state.page = "menu"

# Pages
def show_menu():
    embed_music()
    music_toggle_icon()
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>UJI BRIX PADA PANGAN</h1>", unsafe_allow_html=True)

    if st.button("▶️ Memulai Perhitungan"):
        st.session_state.page = "perhitungan"
    if st.button("📜 Rumus-rumus Brix"):
        st.session_state.page = "rumus"
    if st.button("🔬 Alat Hand Refraktometer"):
        st.session_state.page = "alat"
    if st.button("⚙️ Opsi Aplikasi"):
        st.session_state.page = "opsi"

def show_perhitungan():
    embed_music()
    music_toggle_icon()
    back_button()
    st.header("🔎 Perhitungan Brix")
    with st.sidebar:
        brix_awal = st.number_input("Brix Awal (°Bx)", 0.0, 85.0, step=0.1)
        suhu = st.number_input("Suhu (°C)", 0.0, 100.0, step=0.1)

    if st.button("Hitung Koreksi Brix"):
        suhu_ref = 20.0
        koreksi = 0.03
        selisih = suhu - suhu_ref
        hasil = brix_awal + (selisih * koreksi)

        st.success(f"Hasil Koreksi: {hasil:.2f} °Bx")

        if hasil < 8:
            keterangan = "Buah belum matang (sangat rendah)"
        elif 8 <= hasil < 12:
            keterangan = "Buah setengah matang (cukup)"
        elif 12 <= hasil < 16:
            keterangan = "Buah matang sempurna (standar industri)"
        elif 16 <= hasil < 22:
            keterangan = "Sangat manis (sirup alami)"
        else:
            keterangan = "Kadar gula tinggi (madu atau konsentrat)"

        st.info(f"Keterangan: {keterangan}")

        st.markdown(f"""
        **Langkah Perhitungan:**
        - Brix Terkoreksi = Brix Awal + ((Suhu - 20) × 0.03)
        - {brix_awal} + (({suhu} - 20) × 0.03) = {hasil:.2f} °Bx
        """)

def show_rumus():
    back_button()
    st.header("📜 Rumus Uji Brix")
    st.write("""
    **Rumus:**
    Brix Terkoreksi = Brix Awal + ((Suhu - 20) × 0.03)

    Penyesuaian ini mengoreksi perubahan indeks bias akibat suhu. Biasanya suhu referensi adalah 20°C.
    """)

def show_alat():
    back_button()
    st.header("🔬 Alat Hand Refraktometer")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6d/Refractometer.png", caption="Gambar Alat Hand Refraktometer", use_column_width=True)

def show_opsi():
    back_button()
    st.header("⚙️ Opsi Aplikasi")
    pilihan_font = st.radio("Pilih Font Tampilan:", ["Times New Roman", "Arial"], horizontal=True)
    st.session_state.font_choice = pilihan_font

    volume = st.slider("Volume Musik", 0.0, 1.0, st.session_state.volume, step=0.05)
    st.session_state.volume = volume
    st.success(f"Volume diatur: {int(volume*100)}%")

# Page Controller
if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "perhitungan":
    loading()
    show_perhitungan()
elif st.session_state.page == "rumus":
    loading()
    show_rumus()
elif st.session_state.page == "alat":
    loading()
    show_alat()
elif st.session_state.page == "opsi":
    loading()
    show_opsi()
