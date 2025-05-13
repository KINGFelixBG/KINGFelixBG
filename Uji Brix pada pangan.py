import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Tambahkan CSS untuk background gelap dan font tebal
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                    url("https://images.unsplash.com/photo-1577436932028-2d18814ef666?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&dl=emrecan-arik-h1_R9-o9an0-unsplash.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
        font-weight: bold;
    }
    .animated-title {
        font-size: 32px;
        font-weight: bold;
        color: #fff;
        animation: fadein 2s ease-in-out;
        text-align: center;
        margin-bottom: 20px;
    }
    @keyframes fadein {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi dengan animasi
st.markdown('<div class="animated-title">🍓 Uji Brix pada Bahan Pangan 🍍</div>', unsafe_allow_html=True)

# Deskripsi aplikasi
st.write("Aplikasi ini menghitung kadar Brix yang telah dikoreksi suhu, estimasi densitas larutan, dan kandungan gula (gram/L).")

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

    st.subheader("📌 Koreksi Suhu")
    st.success(f"Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
    st.caption(f"Perhitungan: {brix_awal:.2f} + ({suhu:.2f} - {suhu_referensi}) × {faktor_koreksi} = {brix_terkoreksi:.2f} °Bx")

    # --- Estimasi Densitas (kg/L) ---
    densitas = 0.998 + (0.00385 * (brix_terkoreksi / 10))

    st.subheader("📌 Estimasi Densitas")
    st.info(f"Densitas larutan (perkiraan): {densitas:.4f} kg/L")
    st.caption(f"Perhitungan: 0.998 + (0.00385 × ({brix_terkoreksi:.2f} ÷ 10)) = {densitas:.4f} kg/L")

    # --- Estimasi Kandungan Gula (g/L) ---
    gula_per_liter = brix_terkoreksi * densitas * 10

    st.subheader("📌 Estimasi Kandungan Gula")
    st.info(f"Kandungan gula: {gula_per_liter:.2f} gram/L")
    st.caption(f"Perhitungan: {brix_terkoreksi:.2f} × {densitas:.4f} × 10 = {gula_per_liter:.2f} g/L")

    # --- Kategori Kadar Gula ---
    st.subheader("📌 Kategori Kadar Gula")
    if brix_terkoreksi < 10:
        kualitas = "Rendah (buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (standar buah segar)"
    else:
        kualitas = "Tinggi (madu, sirup, buah sangat manis)"
    st.warning(f"Kategori: {kualitas}")

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
- Rumus ini merupakan pendekatan umum dan dapat bervariasi tergantung jenis larutan.
""")

# Footer
st.caption("📗 Dibuat dengan Streamlit | Uji Brix, densitas, dan kadar gula larutan pangan.")
