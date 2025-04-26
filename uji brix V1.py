import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Uji Brix Minecraft", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "menu"
if "background_color" not in st.session_state:
    st.session_state.background_color = "#1e1e1e"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "play_music" not in st.session_state:
    st.session_state.play_music = True

# Fungsi loading dengan overlay Minecraft-style
def loading(text="sedang proses sahabat"):
    loading_html = f"""
    <div style="position:fixed; top:0; left:0; width:100%; height:100%; background-color:black; z-index:9999; display:flex; justify-content:center; align-items:center;">
        <h1 style='color:lime; font-family:monospace; font-size:40px;'>{text}</h1>
    </div>
    <script>
    setTimeout(() => document.querySelector('div[style*="z-index:9999"]').remove(), 2000);
    </script>
    """
    st.markdown(loading_html, unsafe_allow_html=True)
    time.sleep(1.5)

# Fungsi tombol kembali
def back_button():
    if st.button("🏠 Kembali ke Menu"):
        st.session_state.page = "menu"

# Fungsi musik
def embed_music():
    if st.session_state.play_music and st.session_state.page in ["menu", "perhitungan"]:
        st.markdown("""
        <iframe width="0" height="0" scrolling="no" frameborder="no" allow="autoplay"
        src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/36529168&color=%23333333&inverse=false&auto_play=true&show_user=false">
        </iframe>
        """, unsafe_allow_html=True)

# Fungsi logo musik toggle
def music_toggle_icon():
    icon = "🔊" if st.session_state.play_music else "🔇"
    col = st.columns([0.9, 0.1])[1]
    with col:
        if st.button(icon, key="music_toggle"):
            st.session_state.play_music = not st.session_state.play_music

# Background dinamis
def get_background_url():
    if st.session_state.page == "perhitungan":
        return "https://e0.pxfuel.com/wallpapers/891/197/desktop-wallpaper-minecraft-backround-minecraft-scenery.jpg"
    elif st.session_state.page == "rumus":
        return "https://img.freepik.com/free-photo/open-book-library-with-copy-space_1150-8687.jpg"
    elif st.session_state.page == "alat":
        return "https://img.freepik.com/free-photo/close-up-scientific-equipment-laboratory_23-2148916225.jpg"
    elif st.session_state.page == "opsi":
        return "https://wallpaperaccess.com/full/2682775.png"
    else:
        return "https://i.pinimg.com/736x/f7/4c/e6/f74ce6007b53858d32503641f6dd88ba.jpg"

# CSS global
bg_url = get_background_url()
st.markdown(f"""
    <style>
    .stApp {{
        animation: fadeIn 1s;
        background: url('{bg_url}') no-repeat center center fixed;
        background-size: cover;
    }}
    .block-container {{ background-color: rgba(0, 0, 0, 0.0); }}
    @keyframes fadeIn {{ 0% {{opacity: 0;}} 100% {{opacity: 1;}} }}
    h1 {{ font-family: 'Press Start 2P', cursive; color: white; text-shadow: 3px 3px 0 black; }}
    </style>
""", unsafe_allow_html=True)

# MENU
def show_menu():
    embed_music()
    music_toggle_icon()
    st.markdown("""
    <h1 style="
        font-family: 'Press Start 2P', cursive;
        font-size: 70px;
        color: white;
        text-align: center;
        text-shadow: 4px 4px 0px #000000, 8px 8px 0px rgba(0,0,0,0.2);
        margin-top: 50px;">
    UJI BRIX PADA PANGAN
    </h1>
    """, unsafe_allow_html=True)

    if st.button("▶️ Memulai Perhitungan"):
        st.session_state.page = "perhitungan"
    if st.button("📜 Rumus-rumus Brix"):
        st.session_state.page = "rumus"
    if st.button("🔬 Alat Hand Refraktometer"):
        st.session_state.page = "alat"
    if st.button("⚙️ Opsi Warna"):
        st.session_state.page = "opsi"

# PERHITUNGAN
def show_perhitungan():
    embed_music()
    music_toggle_icon()
    back_button()
    st.header("🔎 Perhitungan Brix")
    with st.sidebar:
        brix_awal = st.number_input("Brix Awal (°Bx)", 0.0, 85.0, step=0.1)
        suhu = st.number_input("Suhu (°C)", 0.0, 100.0, step=0.1)
        st.session_state.dark_mode = st.checkbox("Dark Mode", value=st.session_state.dark_mode)

    if st.session_state.dark_mode:
        st.markdown("""<style>body, .stApp { background-color: #1e1e1e; color: white; }</style>""", unsafe_allow_html=True)

    if st.button("Hitung Koreksi Brix"):
        suhu_ref = 20.0
        koreksi = 0.03
        selisih = suhu - suhu_ref
        hasil = brix_awal + (selisih * koreksi)

        st.success(f"Hasil Koreksi: {hasil:.2f} °Bx")
        st.markdown(f"""
        ### 📘 Langkah Perhitungan:
        - Rumus: Brix Terkoreksi = Brix Awal + ((Suhu - 20) × 0.03)
        - Brix Awal = {brix_awal} °Bx
        - Suhu = {suhu} °C
        - Koreksi = {selisih:.2f} × 0.03 = {selisih * koreksi:.2f} °Bx
        - Hasil = {brix_awal:.2f} + {selisih * koreksi:.2f} = {hasil:.2f} °Bx

        📖 **Penjelasan Ilmiah:**
        Menurut *Jurnal Kimia Terapan Indonesia*, koreksi suhu pada pengukuran Brix penting karena indeks bias larutan dipengaruhi oleh suhu. Koreksi digunakan untuk hasil akurat pada jus, madu, dll.
        """)

# RUMUS
def show_rumus():
    back_button()
    st.header("📜 Rumus Perhitungan Brix")
    st.write("""Brix Terkoreksi = Brix Awal + ((Suhu - Suhu Referensi) × Faktor Koreksi)
Suhu Referensi = 20°C, Faktor Koreksi = 0.03 °Bx/°C""")

# ALAT
def show_alat():
    back_button()
    st.header("🔬 Alat Hand Refraktometer")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Refractometer.png/640px-Refractometer.png", caption="Refraktometer Brix", use_column_width=True)

# OPSI
def show_opsi():
    back_button()
    st.header("⚙️ Ganti Warna Background")
    pilihan = st.radio("Pilih warna:", ["Merah", "Kuning", "Hijau", "Biru"], horizontal=False)
    warna = {"Merah": "#ff4c4c", "Kuning": "#ffeb3b", "Hijau": "#4caf50", "Biru": "#2196f3"}
    st.session_state.background_color = warna[pilihan]
    st.success(f"Warna latar diganti menjadi: {pilihan}")

# Routing
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
