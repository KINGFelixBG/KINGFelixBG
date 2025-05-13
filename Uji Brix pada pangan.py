import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# CSS untuk latar belakang dan font menyala
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1577436932028-2d18814ef666?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&dl=emrecan-arik-h1_R9-o9an0-unsplash.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        color: #000000;
    }}
    .stApp > * {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 1rem;
        border-radius: 10px;
    }}
    h1, h2, h3, .stMarkdown, .stTextInput label, .stNumberInput label, .stSidebar, .stCaption {{
        color: #111111 !important;
        font-weight: 700;
        text-shadow: 0px 0px 2px #ffffff;
    }}
    .stButton>button {{
        font-weight: bold;
        color: white;
        background-color: #e63946;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Judul dengan animasi berjalan
st.markdown("""
    <marquee behavior="scroll" direction="left" scrollamount="10" style="color:red; font-size:30px; font-weight:bold;">
        🍇 UJI BRIX PADA BAHAN PANGAN - CEK GULA, DENSITAS, DAN KUALITAS 🍎
    </marquee>
""", unsafe_allow_html=True)

st.write("""
Aplikasi ini menghitung kadar Brix yang telah dikoreksi suhu, estimasi densitas larutan, dan kandungan gula (gram/L).
""")

# Sidebar untuk input
with st.sidebar:
    st.header("Input Data")
    brix_awal = st.number_input("Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

# Tombol untuk menghitung
if st.button("🔍 Hitung"):

    # --- Koreksi Suhu ---
    suhu_referensi = 20.0
    faktor_koreksi = 0.03
    selisih_suhu = suhu - suhu_referensi
    koreksi = selisih_suhu * faktor_koreksi
    brix_terkoreksi = brix_awal + koreksi

    # --- Estimasi Densitas (kg/L) ---
    densitas = 0.998 + (0.00385 * (brix_terkoreksi / 10))

    # --- Estimasi Kandungan Gula (g/L) ---
    gula_per_liter = brix_terkoreksi * densitas * 10

    # --- Tampilkan Hasil ---
    st.subheader("📊 Hasil Perhitungan")

    st.write(f"### 1. **Nilai Brix Terkoreksi:** {brix_terkoreksi:.2f} °Bx")
    st.caption(f"Perhitungan: {brix_awal:.2f} + ({suhu:.2f} - 20) × 0.03 = {brix_terkoreksi:.2f} °Bx")

    st.write(f"### 2. **Estimasi Densitas Larutan:** {densitas:.4f} kg/L")
    st.caption(f"Perhitungan: Densitas ≈ 0.998 + ({brix_terkoreksi:.2f} / 10) × 0.00385 = {densitas:.4f} kg/L")

    st.write(f"### 3. **Estimasi Kandungan Gula:** {gula_per_liter:.2f} gram/L")
    st.caption(f"Perhitungan: Gula (g/L) = Brix × Densitas × 10 = {brix_terkoreksi:.2f} × {densitas:.4f} × 10 = {gula_per_liter:.2f} gram/L")

    # --- Kategori Kadar Gula ---
    if brix_terkoreksi < 10:
        kualitas = "Rendah (buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (standar buah segar)"
    else:
        kualitas = "Tinggi (madu, sirup, buah sangat manis)"
    st.warning(f"Kategori Kadar Gula: {kualitas}")

# Penjelasan tambahan
with st.expander("📘 Penjelasan Rumus dan Alat"):
    st.markdown("""
### 📌 Rumus Perhitungan

1. **Koreksi Suhu:**
   \nBrix_terkoreksi = Brix_awal + (Suhu - 20) × 0.03

2. **Estimasi Densitas (kg/L):**
   \nDensitas ≈ 0.998 + (Brix / 10 × 0.00385)

3. **Estimasi Kandungan Gula (g/L):**
   \nGula (g/L) = Brix × Densitas × 10

### 🧪 Alat yang Digunakan

- **Refraktometer**: Mengukur Brix secara langsung.
- **Termometer**: Untuk mengetahui suhu larutan.
- **Hidrometer / Piknometer**: Untuk validasi densitas larutan.

### ⚠️ Catatan:
- Rumus yang digunakan adalah pendekatan praktis dan dapat memiliki deviasi dari hasil laboratorium tergantung komposisi larutan.
""")

# Footer
st.caption("📗 Dibuat dengan Streamlit | Edukasi uji Brix, densitas, dan kandungan gula dalam pangan cair.")
