
import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# CSS untuk background dan font tebal
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                    url('https://images.unsplash.com/photo-1577436932028-2d18814ef666?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&dl=emrecan-arik-h1_R9-o9an0-unsplash.jpg');
        background-size: cover;
        background-position: center;
        color: white;
        font-weight: bold;
    }
    @keyframes flicker {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    .title-anim {
        font-size: 2.5em;
        text-align: center;
        animation: flicker 2s infinite;
        color: #FFDD57;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Judul animasi
st.markdown('<div class="title-anim">🍓 Uji Brix pada Bahan Pangan 🍍</div>', unsafe_allow_html=True)

st.write("""
Aplikasi ini menghitung kadar Brix yang telah dikoreksi suhu, estimasi densitas larutan, dan kandungan gula (gram/L).
""")

# Input kolom
col1, col2 = st.columns(2)
with col1:
    brix_awal = st.number_input("Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
with col2:
    suhu = st.number_input("Suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

# Tombol hitung
if st.button("🔍 Hitung"):

    # --- Koreksi Suhu ---
    suhu_referensi = 20.0
    faktor_koreksi = 0.03
    selisih_suhu = suhu - suhu_referensi
    koreksi = selisih_suhu * faktor_koreksi
    brix_terkoreksi = brix_awal + koreksi

    # --- Estimasi Densitas ---
    densitas = 0.998 + (0.00385 * (brix_terkoreksi / 10))

    # --- Estimasi Gula (gram/L) ---
    gula_per_liter = brix_terkoreksi * densitas * 10

    # Tampilkan hasil di bawah kolom
    with col1:
        st.success(f"Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Perhitungan: {brix_awal:.2f} + ({suhu:.2f} - 20) × 0.03 = {brix_terkoreksi:.2f}")
    with col2:
        st.info(f"Densitas: {densitas:.4f} kg/L")
        st.info(f"Gula: {gula_per_liter:.2f} g/L")

    # Kategori kualitas
    if brix_terkoreksi < 10:
        kualitas = "Rendah (buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (standar buah segar)"
    else:
        kualitas = "Tinggi (madu, sirup, buah manis)"
    st.warning(f"Kategori Kadar Gula: {kualitas}")

# Penjelasan
with st.expander("📘 Penjelasan Rumus dan Alat"):
    st.markdown("""
**Rumus Perhitungan:**

1. Koreksi Suhu:  
   `Brix_terkoreksi = Brix_awal + (Suhu - 20) × 0.03`

2. Estimasi Densitas:  
   `Densitas ≈ 0.998 + (Brix / 10 × 0.00385)`

3. Estimasi Gula (g/L):  
   `Gula = Brix × Densitas × 10`

**Alat yang Digunakan:**
- Refraktometer
- Termometer
- Hidrometer / Piknometer
""")

st.caption("📗 Dibuat dengan Streamlit | Edukasi uji Brix, densitas, dan kandungan gula dalam pangan cair.")
