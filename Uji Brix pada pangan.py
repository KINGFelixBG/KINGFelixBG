import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Tambahkan CSS untuk background gelap, font tebal, dan kotak hasil yang menyala
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                    url("https://images.unsplash.com/photo-1577436932028-2d18814ef666?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb");
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
    .highlight-box {
        background-color: rgba(255, 255, 255, 0.15);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 0 10px rgba(255,255,255,0.2);
    }
    @keyframes fadein {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.markdown('<div class="animated-title">🍓 Uji Brix pada Bahan Pangan 🍍</div>', unsafe_allow_html=True)
st.write("Aplikasi ini menghitung kadar Brix yang telah dikoreksi suhu, estimasi densitas larutan, dan kandungan gula (gram/L).")

# Sidebar Input
with st.sidebar:
    st.header("Input Data")
    brix_awal = st.number_input("Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

# Tombol Hitung
if st.button("🔍 Hitung"):

    # Koreksi Suhu
    suhu_referensi = 20.0
    faktor_koreksi = 0.03
    selisih_suhu = suhu - suhu_referensi
    koreksi = selisih_suhu * faktor_koreksi
    brix_terkoreksi = brix_awal + koreksi

    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.subheader("📌 Koreksi Suhu")
    st.write(f"**Brix Terkoreksi:** {brix_terkoreksi:.2f} °Bx")
    st.caption(f"Perhitungan: {brix_awal:.2f} + ({suhu:.2f} - {suhu_referensi}) × {faktor_koreksi} = {brix_terkoreksi:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Estimasi Densitas
    densitas = 0.998 + (0.00385 * (brix_terkoreksi / 10))

    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.subheader("📌 Estimasi Densitas")
    st.write(f"**Densitas larutan (perkiraan):** {densitas:.4f} kg/L")
    st.caption(f"Perhitungan: 0.998 + 0.00385 × ({brix_terkoreksi:.2f} ÷ 10) = {densitas:.4f}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Estimasi Gula
    gula_per_liter = brix_terkoreksi * densitas * 10

    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.subheader("📌 Estimasi Kandungan Gula")
    st.write(f"**Kandungan gula:** {gula_per_liter:.2f} gram/L")
    st.caption(f"Perhitungan: {brix_terkoreksi:.2f} × {densitas:.4f} × 10 = {gula_per_liter:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Kategori Gula
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.subheader("📌 Kategori Kadar Gula")
    if brix_terkoreksi < 10:
        kualitas = "Rendah (buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (standar buah segar)"
    else:
        kualitas = "Tinggi (madu, sirup, buah sangat manis)"
    st.warning(f"Kategori: {kualitas}")
    st.markdown('</div>', unsafe_allow_html=True)

# Penjelasan
with st.expander("📘 Penjelasan Rumus dan Alat"):
    st.markdown("""
### 📌 Rumus Perhitungan

1. **Koreksi Suhu:**  
   Brix_terkoreksi = Brix_awal + (Suhu - 20) × 0.03

2. **Estimasi Densitas (kg/L):**  
   Densitas ≈ 0.998 + (Brix ÷ 10 × 0.00385)

3. **Estimasi Kandungan Gula (g/L):**  
   Gula = Brix × Densitas × 10

### 🧪 Alat yang Digunakan

- **Refraktometer**: Mengukur Brix.
- **Termometer**: Mengukur suhu larutan.
- **Hidrometer / Piknometer**: Validasi densitas larutan.

### ⚠️ Catatan:
Rumus ini adalah pendekatan praktis yang digunakan untuk estimasi cepat.
""")

# Footer
st.caption("📗 Dibuat dengan Streamlit | Edukasi uji Brix, densitas, dan kadar gula dalam pangan cair.")
