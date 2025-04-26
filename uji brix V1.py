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
    st.markdown("""
    <div style="position: fixed; top: 20px; left: 20px; z-index: 1000;">
        <form action="" method="post">
            <button onclick="playClick()" name="back" style="background-color:#5a5a5a; border:2px solid #00ff00; padding:10px; font-family:'Press Start 2P'; color:white;">🏠</button>
        </form>
    </div>
    """, unsafe_allow_html=True)
    if st.session_state.get("back"):
        st.session_state.page = "menu"

# Fungsi menu utama

def show_menu():
    st.title("🧪 Uji Brix Minecraft Style")

    if st.button("▶️ Memulai Perhitungan"):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)
        switch_page("perhitungan")

    if st.button("📜 Rumus-rumus Brix"):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)
        switch_page("rumus")

    if st.button("🔬 Alat Hand Refraktometer"):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)
        switch_page("alat")

    if st.button("⚙️ Opsi Warna"):
        st.markdown("<script>playClick()</script>", unsafe_allow_html=True)
        switch_page("opsi")

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
        selisih = suhu - 20
        hasil = brix_awal + (selisih * 0.03)
        st.success(f"Brix Terkoreksi: {hasil:.2f} °Bx")

# Halaman Rumus

def show_rumus():
    back_button()
    st.header("📜 Rumus Perhitungan Brix")
    st.write("**Brix Terkoreksi = Brix Awal + ((Suhu Pengukuran - 20) × 0.03)**  \n"
             "- Suhu Referensi: 20°C  \n"
             "- Faktor Koreksi: 0.03 °Bx per °C")

# Halaman Alat

def show_alat():
    back_button()
    st.header("🔬 Alat Hand Refraktometer")
    st.image("/mnt/data/b44f73b2-5a59-42cb-90f6-978d0868e67e.png", caption="Refraktometer Brix", use_column_width=True)

# Halaman Opsi Warna

def show_opsi():
    back_button()
    st.header("⚙️ Ganti Warna Background")
    pilihan = st.radio("Pilih warna:", ["Merah", "Kuning", "Hijau", "Biru"])
    warna = {"Merah": "#ff4c4c", "Kuning": "#ffeb3b", "Hijau": "#4caf50", "Biru": "#2196f3"}
    st.session_state.background_color = warna[pilihan]

# Fungsi untuk switch halaman

def switch_page(next_page):
    st.session_state.page = "loading"
    st.session_state.next_page = next_page

# Kontrol navigasi halaman
if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "loading":
    loading("Memuat...")
    st.session_state.page = st.session_state.next_page
elif st.session_state.page == "perhitungan":
    show_perhitungan()
elif st.session_state.page == "rumus":
    show_rumus()
elif st.session_state.page == "alat":
    show_alat()
elif st.session_state.page == "opsi":
    show_opsi()
```
}
