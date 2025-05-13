import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Gaya latar belakang dengan wallpaper buah-buahan
st.markdown("""
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1576402187875-4b6a8b0f15f7?auto=format&fit=crop&w=1500&q=80");
        background-size: cover;
        background-position: center;
        color: #ffffff;
    }
    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Container agar konten mudah dibaca di atas background
with st.container():
    st.markdown('<div class="block-container">', unsafe_allow_html=True)

    st.title("🍎 Uji Brix pada Bahan Pangan 🍓")

    st.write("""
    Aplikasi ini membantu menghitung kadar Brix dari larutan gula pada bahan pangan, dengan koreksi suhu.
    Termasuk perhitungan densitas dan estimasi kandungan gula dalam g/L.
    """)

    with st.sidebar:
        st.header("Input Parameter")
        brix_awal = st.number_input("Masukkan nilai Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
        suhu = st.number_input("Masukkan suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

    # Tombol perhitungan
    if st.button("🔍 Hitung Koreksi Brix & Estimasi Gula"):
        suhu_referensi = 20.0
        faktor_koreksi = 0.03

        selisih_suhu = suhu - suhu_referensi
        koreksi = selisih_suhu * faktor_koreksi
        brix_terkoreksi = brix_awal + koreksi

        # Estimasi densitas (kg/L) dan kandungan gula
        densitas = 0.998 + (0.00385 * brix_terkoreksi / 10)  # pendekatan sederhana
        gula_gram_per_liter = brix_terkoreksi * densitas * 10  # g/L

        st.success(f"✅ Nilai Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
        st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} × {faktor_koreksi}) = {brix_terkoreksi:.2f} °Bx")

        st.info(f"Densitas (perkiraan): {densitas:.4f} kg/L")
        st.info(f"Estimasi Kandungan Gula: {gula_gram_per_liter:.2f} gram/L")

        # Kategori kualitas
        if brix_terkoreksi < 10:
            kualitas = "Rendah (buah belum matang)"
        elif 10 <= brix_terkoreksi <= 15:
            kualitas = "Sedang (standar buah segar)"
        else:
            kualitas = "Tinggi (madu, sirup, dll)"

        st.warning(f"Kategori Gula: {kualitas}")

    # Penutup kontainer
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.caption("📘 Dibuat dengan Streamlit untuk edukasi uji Brix pada pangan.")



   
    

