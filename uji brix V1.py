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

# Audio Minecraft di menu utama
def play_music():
    if st.session_state.page == "menu":
        st.markdown("""
            <audio autoplay loop>
                <source src="https://vgmsite.com/soundtracks/minecraft-complete-soundtrack/ffdzlrbw/1-01%20Minecraft%20-%20Sweden.mp3" type="audio/mpeg">
            </audio>
            """, unsafe_allow_html=True)

# Fungsi loading ringan
def loading(text="sedang proses sahabat"):
    with st.spinner(text):
        time.sleep(1)

# Tombol kembali
def back_button():
    if st.button("🏠 Kembali ke Menu"):
        st.session_state.page = "menu"

# Fungsi background bergantung halaman
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

# Fungsi Menu Utama
def show_menu():
    st.markdown(f"""
    <style>
    .stApp {{
        animation: fadeIn 2s;
        background: url('{get_background_url()}') no-repeat center center fixed;
        background-size: cover;
    }}
    .block-container {{
        background-color: rgba(0, 0, 0, 0.0);
    }}
    @keyframes fadeIn {{
        0% {{opacity: 0;}}
        100% {{opacity: 1;}}
    }}
    h1 {{
        font-family: 'Press Start 2P', cursive;
        font-size: 70px;
        color: white;
        text-align: center;
        text-shadow: 4px 4px 0px #000000, 8px 8px 0px rgba(0,0,0,0.2);
        margin-top: 50px;
    }}
    .stButton>button {{
        font-family: 'Press Start 2P', cursive;
        background-color: #5a5a5a;
        border: 2px solid #00ff00;
        padding: 15px 20px;
        margin: 10px auto;
        width: 300px;
        font-size: 16px;
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

    play_music()
    st.markdown("<h1>UJI BRIX PADA PANGAN</h1>", unsafe_allow_html=True)

    if st.button("▶️ Memulai Perhitungan"):
        st.session_state.page = "perhitungan"
    if st.button("📜 Rumus-rumus Brix"):
        st.session_state.page = "rumus"
    if st.button("🔬 Alat Hand Refraktometer"):
        st.session_state.page = "alat"
    if st.button("⚙️ Opsi Warna"):
        st.session_state.page = "opsi"

# Fungsi Perhitungan
def show_perhitungan():
    back_button()
    st.header("🔎 Perhitungan Brix")
    with st.sidebar:
        brix_awal = st.number_input("Brix Awal (°Bx)", 0.0, 85.0, step=0.1)
        suhu = st.number_input("Suhu (°C)", 0.0, 100.0, step=0.1)
        st.session_state.dark_mode = st.checkbox("Dark Mode", value=st.session_state.dark_mode)

    if st.session_state.dark_mode:
        st.markdown("""<style>body, .stApp { background-color: #1e1e1e; color: white; }</style>""", unsafe_allow_html=True)

    if st.button("Hitung Koreksi Brix"):
        suhu_referensi = 20.0
        koreksi_per_derajat = 0.03
        selisih = suhu - suhu_referensi
        hasil = brix_awal + (selisih * koreksi_per_derajat)

        st.success(f"Hasil Koreksi: {hasil:.2f} °Bx")

        st.markdown(f"""
        ### 📘 Langkah Perhitungan:
        - Rumus: Brix Terkoreksi = Brix Awal + ((Suhu - 20) × 0.03)
        - Brix Awal = {brix_awal} °Bx
        - Suhu = {suhu} °C
        - Selisih = {selisih} °C
        - Koreksi = {selisih:.2f} × 0.03 = {selisih * koreksi_per_derajat:.2f} °Bx
        - Brix Akhir = {brix_awal:.2f} + {selisih * koreksi_per_derajat:.2f} = {hasil:.2f} °Bx
        """)

        hasil_txt = f"""Hasil Koreksi Brix
Brix Awal: {brix_awal} °Bx
Suhu: {suhu} °C
Brix Akhir: {hasil:.2f} °Bx
"""
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"hasil_brix_{now}.txt"
        st.download_button(label="💾 Simpan Hasil", data=hasil_txt, file_name=filename)

        if hasil < 10:
            st.info("Kategori: Rendah (buah belum matang)")
        elif 10 <= hasil <= 15:
            st.info("Kategori: Sedang (standar buah segar)")
        else:
            st.info("Kategori: Tinggi (madu/sirup)")

# Halaman lainnya
def show_rumus():
    back_button()
    st.header("📜 Rumus Perhitungan Brix")
    st.write("""
    Brix Terkoreksi = Brix Awal + ((Suhu - 20) × 0.03)
    """)

def show_alat():
    back_button()
    st.header("🔬 Alat Hand Refraktometer")
    st.image("/mnt/data/b44f73b2-5a59-42cb-90f6-978d0868e67e.png", caption="Refraktometer Brix", use_column_width=True)

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
