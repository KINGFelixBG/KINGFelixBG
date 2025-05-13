import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Uji Brix pada Bahan Pangan", layout="centered")

# Judul aplikasi
st.title("🍓 Uji Brix pada Bahan Pangan 🍍")

# Deskripsi aplikasi
st.write("""
Aplikasi ini membantu menghitung nilai Brix dari larutan gula dengan koreksi suhu, serta menghitung estimasi densitas dan kandungan gula dalam gram per liter (g/L).
""")

# Sidebar input
with st.sidebar:
    st.header("Input Parameter")
    brix_awal = st.number_input("Nilai Brix dari refraktometer (°Bx):", min_value=0.0, max_value=85.0, step=0.1)
    suhu = st.number_input("Suhu larutan saat pengukuran (°C):", min_value=0.0, max_value=100.0, step=0.1)

# Tombol perhitungan
if st.button("🔍 Hitung Koreksi & Gula"):
    suhu_referensi = 20.0  # suhu acuan
    faktor_koreksi = 0.03  # koreksi °Bx per °C

    # Koreksi suhu
    selisih_suhu = suhu - suhu_referensi
    koreksi = selisih_suhu * faktor_koreksi
    brix_terkoreksi = brix_awal + koreksi

    # Estimasi densitas (kg/L) dan gula (g/L)
    densitas = 0.998 + (0.00385 * brix_terkoreksi / 10)  # pendekatan sederhana
    gula_gram_per_liter = brix_terkoreksi * densitas * 10

    # Tampilkan hasil
    st.success(f"✅ Nilai Brix Terkoreksi: {brix_terkoreksi:.2f} °Bx")
    st.caption(f"Perhitungan: {brix_awal:.2f} + ({selisih_suhu:.2f} × {faktor_koreksi}) = {brix_terkoreksi:.2f} °Bx")

    st.info(f"📏 Densitas larutan (perkiraan): {densitas:.4f} kg/L")
    st.info(f"🍬 Estimasi Kandungan Gula: {gula_gram_per_liter:.2f} gram/L")

    # Penilaian kualitas
    if brix_terkoreksi < 10:
        kualitas = "Rendah (buah belum matang)"
    elif 10 <= brix_terkoreksi <= 15:
        kualitas = "Sedang (standar buah segar)"
    else:
        kualitas = "Tinggi (madu, sirup, buah sangat manis)"
    
    st.warning(f"Kategori Gula: {kualitas}")

# Informasi tambahan
with st.expander("📘 Tentang Uji Brix"):
    st.markdown("""
**Apa itu Derajat Brix?**
- Derajat Brix (°Bx) menunjukkan jumlah padatan terlarut (biasanya sukrosa) dalam larutan.
- Contoh: 10 °Bx berarti terdapat 10 gram gula per 100 gram larutan.

**Alat yang Digunakan:**
1. **Refraktometer**: Untuk membaca °Bx.
2. **Termometer**: Untuk mengukur suhu larutan.
3. **Hidrometer / Piknometer**: Untuk mengukur densitas secara lebih presisi.

**Koreksi Suhu:**
- Refraktometer manual perlu koreksi karena indeks bias dipengaruhi suhu.
- Rumus koreksi sederhana:  
  `Brix_terkoreksi = Brix_awal + (Suhu - 20) * 0.03`
""")

# F


   
    
   
    

