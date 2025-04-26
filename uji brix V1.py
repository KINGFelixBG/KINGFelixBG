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
        var audio = document.getElementById("clickSound");
        audio.play();
    }
    </script>
""", unsafe_allow_html=True)

# Function untuk Loading Screen
def loading_screen(text="Loading..."):
    with st.spinner(text):
        time.sleep(2)

# Fungsi masing-masing halaman
def show_menu():
    st.title("🧪 Uji Brix")

    if st.button("▶️ Memulai Perhitungan", on_click=lambda: switch_page('perhitungan')):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)

    if st.button("📜 Rumus-rumus Brix", on_click=lambda: switch_page('rumus')):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)

    if st.button("🔬 Alat Hand Refraktometer", on_click=lambda: switch_page('alat')):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)

    if st.button("⚙️ Opsi Ganti Warna", on_click=lambda: switch_page('opsi')):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)

def switch_page(page_name):
    st.session_state.page = 'loading'
    st.session_state.next_page = page_name

def show_perhitungan():
    st.header("🔎 Memulai Perhitungan Brix")
    brix_awal = st.number_input("Masukkan nilai Brix:", 0.0, 85.0, step=0.1)
    suhu = st.number_input("Masukkan suhu (°C):", 0.0, 100.0, step=0.1)

    if st.button("Hitung!"):
        suhu_referensi = 20.0
        koreksi_per_derajat = 0.03
        selisih = suhu - suhu_referensi
        hasil = brix_awal + (selisih * koreksi_per_derajat)
        st.success(f"Hasil Koreksi: {hasil:.2f} °Bx")

    if st.button("🔙 Kembali ke Menu"):
        st.session_state.page = 'menu'

def show_rumus():
    st.header("📜 Rumus-rumus Brix")
    st.write("""
    Rumus koreksi suhu:
    
    **Brix Terkoreksi = Brix Awal + (Suhu Pengukuran - Suhu Referensi) × 0.03**

    Dimana:
    - Suhu Referensi: 20°C
    - Faktor Koreksi: 0.03 °Bx/°C
    """)
    if st.button("🔙 Kembali ke Menu"):
        st.session_state.page = 'menu'

def show_alat():
    st.header("🔬 Alat Hand Refraktometer")
    st.image("/mnt/data/b44f73b2-5a59-42cb-90f6-978d0868e67e.png", caption="Hand Refraktometer Brix", use_column_width=True)

    if st.button("🔙 Kembali ke Menu"):
        st.session_state.page = 'menu'

def show_opsi():
    st.header("⚙️ Ganti Warna Background")
    warna = st.radio("Pilih warna latar:", ["Merah", "Kuning", "Hijau", "Biru"], index=2)
    
    if warna == "Merah":
        st.session_state.background_color = "#ff4c4c"
    elif warna == "Kuning":
        st.session_state.background_color = "#ffeb3b"
    elif warna == "Hijau":
        st.session_state.background_color = "#4caf50"
    elif warna == "Biru":
        st.session_state.background_color = "#2196f3"

    if st.button("🔙 Kembali ke Menu"):
        st.session_state.page = 'menu'

# Kontrol tampilan halaman
if st.session_state.page == 'menu':
    show_menu()
elif st.session_state.page == 'loading':
    loading_screen("Memuat...")
    st.session_state.page = st.session_state.next_page
elif st.session_state.page == 'perhitungan':
    show_perhitungan()
elif st.session_state.page == 'rumus':
    show_rumus()
elif st.session_state.page == 'alat':
    show_alat()
elif st.session_state.page == 'opsi':
    show_opsi()
