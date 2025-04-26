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

# Fungsi musik
def play_music():
    if st.session_state.page == "menu":
        st.markdown("""
            <audio autoplay loop>
                <source src="https://vgmsite.com/soundtracks/minecraft-complete-soundtrack/ffdzlrbw/1-01%20Minecraft%20-%20Sweden.mp3" type="audio/mpeg">
            </audio>
            """, unsafe_allow_html=True)

# Fungsi loading dengan overlay ala Minecraft
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

# Background dinamis per halaman
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

# Menu utama

def show_menu():
    play_music()
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

# Halaman perhitungan

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

        📖 **Penjelasan Ilmiah:**
        Koreksi suhu pada pengukuran Brix penting karena indeks bias larutan dipengaruhi oleh suhu. Menurut *Jurnal Kimia Terapan Indonesia*, setiap kenaikan suhu 1°C dapat menurunkan indeks bias, sehingga hasil pengukuran perlu dikoreksi untuk mendapat nilai aktual. Koreksi ini umum digunakan dalam industri pangan seperti jus buah, madu, dan sirup.
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
    Brix Terkoreksi = Brix Awal + ((Suhu - Suhu Referensi) × Faktor Koreksi)
    Suhu Referensi = 20°C, Faktor Koreksi = 0.03 °Bx/°C
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

# Routing halaman
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
