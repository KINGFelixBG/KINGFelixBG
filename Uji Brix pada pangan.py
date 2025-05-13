import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Judul aplikasi
st.markdown("<h1 style='text-align: center;'>🍓 Uji Brix pada Bahan Pangan 🍍</h1>", unsafe_allow_html=True)

# Deskripsi aplikasi
st.write("Aplikasi ini membantu menghitung kadar Brix dari larutan gula pada bahan pangan, dengan koreksi suhu, estimasi densitas, dan kadar gula (gram/L).")

st.markdown("---")

# Sidebar untuk input
with st.sidebar:
    st.header("Input Parameter")
    brix_awal = st.number_input("Masukkan nilai Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Masukkan suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

# Tombol untuk menghitung hasil
if st.button("Hitung Koreksi Brix"):
    # Koreksi Brix berdasarkan suhu
    suhu_referensi = 20.0
    faktor_koreksi = 0.03
    selisih_suhu = suhu - suhu_referensi
    koreksi = selisih_suhu * faktor_koreksi
    brix_terkoreksi = brix_awal + koreksi

    # Menampilkan hasil perhitungan Brix Terkoreksi
    st.subheader("📏 Hasil Koreksi Brix:")
    st.write(f"**Brix Terkoreksi:** {brix_terkoreksi:.2f} °Bx")
    st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} × {faktor_koreksi}) = {brix_terkoreksi:.2f} °Bx")

    # Penilaian kualitas gula berdasarkan Brix Terkoreksi
    if brix_terkoreksi < 10:
        kualitas = "Rendah (buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (buah segar industri)"
    else:
        kualitas = "Tinggi (madu, sirup, atau buah manis)"
    st.info(f"Kategori Kadar Gula: {kualitas}")

    # Estimasi densitas berdasarkan Brix Terkoreksi
    # Rumus pendekatan densitas air-gula (g/mL) berdasarkan literatur
    densitas = 0.9982 + 0.00385 * brix_terkoreksi  # g/mL
    st.subheader("🧪 Estimasi Densitas Larutan:")
    st.write(f"**Densitas (ρ):** {densitas:.4f} g/mL")

    # Estimasi kadar gula dalam gram per liter
    # Rumus: (Brix/100) × densitas × 1000
    kadar_gula = (brix_terkoreksi / 100) * densitas * 1000  # gram/L
    st.subheader("🍬 Estimasi Kadar Gula:")
    st.write(f"**Kadar Gula:** {kadar_gula:.2f} gram/L")

    st.markdown("---")
    st.caption("📘 Dibuat dengan Streamlit untuk edukasi uji Brix pada pangan.")





