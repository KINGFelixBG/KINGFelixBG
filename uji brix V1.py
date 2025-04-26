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
        background-color: {st.session_state['background_color']};
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
        time.sleep(1)

# Fungsi tombol kembali

def back_button():
    if st.button("🏠 Kembali ke Menu"):
        st.session_state.page = "menu"

# Fungsi menu utama

def show_menu():
    st.title("🧪 Uji Brix Minecraft Style")

    if st.button("▶️ Memulai Perhitungan"):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)
        st.session_state.page = "perhitungan"

    if st.button("📜 Rumus-rumus Brix"):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)
        st.session_state.page = "rumus"

    if st.button("🔬 Alat Hand Refraktometer"):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)
        st.session_state.page = "alat"

    if st.button("⚙️ Opsi Warna"):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)
        st.session_state.page = "opsi"

# Halaman Perhitungan

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
        if hasil < 10:
            kualitas = "Rendah (buah belum matang)"
        elif 10 <= hasil <= 15:
            kualitas = "Sedang (standar buah segar)"
        else:
            kualitas = "Tinggi (madu, sirup, dll)"
        st.info(f"Kategori Kadar Gula: {kualitas}")

# Halaman Rumus

def show_rumus():
    back_button()
    st.header("📜 Rumus Perhitungan Brix")
    st.write("""
    Rumus koreksi suhu:

    **Brix Terkoreksi = Brix Awal + ((Suhu Pengukuran - Suhu Referensi) × Faktor Koreksi)**

    - Suhu Referensi: 20°C
    - Faktor Koreksi: 0.03 °Bx/°C
    """)

# Halaman Alat

def show_alat():
    back_button()
    st.header("🔬 Alat Hand Refraktometer")
    st.image("/mnt/data/b44f73b2-5a59-42cb-90f6-978d0868e67e.png", caption="Refraktometer Brix", use_column_width=True)

# Halaman Opsi Warna

def show_opsi():
    back_button()
    st.header("⚙️ Ganti Warna Background")
    pilihan = st.radio("Pilih warna:", ["Merah", "Kuning", "Hijau", "Biru"], horizontal=True)
    warna = {"Merah": "#ff4c4c", "Kuning": "#ffeb3b", "Hijau": "#4caf50", "Biru": "#2196f3"}
    st.session_state.background_color = warna[pilihan]
    st.success(f"Warna latar diganti menjadi: {pilihan}")

# Navigasi halaman
if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "perhitungan":
    loading("Memuat Perhitungan...")
    show_perhitungan()
elif st.session_state.page == "rumus":
    loading("Memuat Rumus...")
    show_rumus()
elif st.session_state.page == "alat":
    loading("Memuat Alat...")
    show_alat()
elif st.session_state.page == "opsi":
    loading("Memuat Opsi...")
    show_opsi()
